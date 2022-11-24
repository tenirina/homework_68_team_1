from django.urls import path

from vacancies.views import VacancyCreateView, VacancyListView, VacancyEditView, VacancyDetailView

urlpatterns = [
    path('', VacancyListView.as_view(), name='vacancies'),
    path('create/', VacancyCreateView.as_view(), name='vacancy_create'),
    path('<int:pk>/edit/', VacancyEditView.as_view(), name='vacancy_edit'),
    path('<int:pk>/detail/', VacancyDetailView.as_view(), name='vacancy_detail')
]
