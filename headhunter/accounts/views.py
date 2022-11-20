import json
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView

from accounts.forms import LoginForm, CustomUserCreationForm, UserUpdateForm
from accounts.models import Account


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
        return self.render_to_response(context)


@csrf_exempt
def login_view(request):
    data = json.loads(request.body)
    email = data['email']
    password = data['password']
    if email and password:
        user_auth = authenticate(request, email=email, password=password)
        if user_auth:
            login(request, user_auth)
            user = Account.objects.filter(email=email)[0]
            print(user)
            # response_data = {'user': user}
            # print(response_data)
            response = JsonResponse({'answer': user.pk, 'status': 200})
            print(response)
            return response
        print('NOT CORRECT')
        response_data = {'error': 'Пользователь или пароль не валидны!', 'status': 400}
        response = JsonResponse(response_data)
        return response
    print('NOT DATA')
    response_data = {'error': 'Введите логин и пароль!', 'status': 400}
    response = JsonResponse(response_data)
    return response

        # if not form.is_valid():
        #     response_data = {'error': 'Пользователь и пароль обязательные поля!', 'status': 400}
        #     response = JsonResponse(response_data)
        #     response.status_code = 200
        #     return response
        # email = form.cleaned_data.get('email')
        # password = form.cleaned_data.get('password')
        # next = form.cleaned_data.get('next')
        # user = authenticate(request, email=email, password=password)
        # if not user:
        #     response_data = {'error': 'Пользователь или пароль не валидны!', 'status': 400}
        #     response = JsonResponse(response_data)
        #     response.status_code = 200
        #     return response
        # login(request, user)
        # if next:
        #     return redirect(next)
        # user = Account.objects.filter(email=form.cleaned_data.get('email'))[0]
        # return redirect('user_detail', pk=user.pk)


def logout_view(request):
    logout(request)
    return redirect('index')


class ProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'


class UserChangeView(UpdateView):
    model = get_user_model()
    form_class = UserUpdateForm
    template_name = 'user_update.html'
    context_object_name = 'user_obj'

    def has_permission(self):
        return super().has_permission() or self.get_object() == self.request.user

    def get_success_url(self):
        return reverse('user_detail', kwargs={'pk': self.object.pk})
