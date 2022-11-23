from django.shortcuts import redirect
from django.views.generic import CreateView

from vacancies.forms import VacancyForm
from vacancies.models.vacancies import Vacancy


class VacancyCreateView(CreateView):
    template_name = 'resume_create.html'
    form_class = VacancyForm
    model = Vacancy

    def get(self, request, *args, **kwargs):
        # vacancy = Vacancy.objects.create(author=request.user)
        return redirect('index.html')
