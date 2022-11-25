import imp
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView

from accounts.forms import CustomUserCreationForm, LoginForm
from resume.models import Resume


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = CustomUserCreationForm
        context['form_log'] = LoginForm
        context['vacancies'] = ''
        context['yeap'] = False
        context['resumes'] = ''
        if self.request.user.is_authenticated:
            user = self.request.user
            if user.is_worker:
                context['vacancies'] = 'Help'
            else:
                context['resumes'] = 'Help'
                resumes = Resume.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        cont = super().get(request, *args, **kwargs)
        return cont
