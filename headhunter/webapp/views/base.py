from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView

from accounts.forms import CustomUserCreationForm, LoginForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = CustomUserCreationForm
        context['form_log'] = LoginForm
        return context
