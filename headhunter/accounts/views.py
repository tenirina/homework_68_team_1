from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
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


class LoginView(TemplateView):
    template_name = 'index.html'
    form_log = LoginForm

    def get(self, request, *args, **kwargs):
        next = request.GET.get('next')
        form_data = {} if not next else {'next': next}
        form = self.form_log(form_data)
        context = {'form_log': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form_log(request.POST)
        if not form.is_valid():
            return redirect('index')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        next = form.cleaned_data.get('next')
        user = authenticate(request, email=email, password=password)
        if not user:
            form.add_error(None, 'Пользователь или пароль неправильно введены!')
            return redirect('index')
        login(request, user)
        if next:
            return redirect(next)
        user = Account.objects.filter(email=form.cleaned_data.get('email'))[0]
        return redirect('user_detail', pk=user.pk)


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
