from django.urls import path
from resumes.views import ResumeCreateView, ResumeEditView, ResumeDetailView, EducationCreateView, ExperienceCreateView

urlpatterns = [
    path('create/', ResumeCreateView.as_view(), name='resume_create'),
    path('<int:pk>/edit/', ResumeEditView.as_view(), name='resume_edit'),
    path('<int:pk>/detail/', ResumeDetailView.as_view(), name='resume_detail'),
    path('<int:pk>/create/experience', ExperienceCreateView.as_view(), name='resume_experience_create'),
    path('<int:pk>/create/education', EducationCreateView.as_view(), name='resume_education_create')
]