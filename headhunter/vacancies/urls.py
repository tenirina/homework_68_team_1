from django.urls import path

from vacancies.views import VacancyCreateView

urlpatterns = [
    path('create/', VacancyCreateView.as_view(), name='resume_create'),
]
