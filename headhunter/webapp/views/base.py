from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
