import imp
import json
from multiprocessing import context
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView

from accounts.forms import LoginForm, CustomUserCreationForm, UserUpdateForm
from resume.forms import ResumeForm
from accounts.models import Account
from resume.models import Resume


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_detail', pk=user.pk)
        context = {}
        context['form'] = form
        return redirect('index')


class LoginView(View):

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        email = data['email']
        password = data['password']
        if email and password:
            user_auth = authenticate(request, email=email, password=password)
            if user_auth:
                login(request, user_auth)
                user = Account.objects.filter(email=email)[0]
                response = JsonResponse({'answer': user.pk})
                response.status_code = 200
                return response
            response_data = {'error': 'Пользователь или пароль не валидны!'}
            response = JsonResponse(response_data)
            response.status_code = 400
            return response
        response_data = {'error': 'Введите логин и пароль!'}
        response = JsonResponse(response_data)
        response.status_code = 400
        return response


def logout_view(request):
    logout(request)
    return redirect('index')


class ProfileView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
    form_class = UserUpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_res_create'] = ResumeForm
        context['form_edu'] = ResumeForm
        context['form_exp'] = ResumeForm
        context['resumes'] = Resume.objects.filter(author=context['user_obj'].id)
        return context


class UserChangeView(UpdateView):
    model = get_user_model()
    form_class = UserUpdateForm
    template_name = 'user_update.html'
    context_object_name = 'user_obj'

    def has_permission(self):
        return super().has_permission() or self.get_object() == self.request.user

    def get_success_url(self):
        return reverse('user_detail', kwargs={'pk': self.object.pk})
