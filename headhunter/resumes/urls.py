from django.urls import path
from resumes.views import ResumeCreateView

urlpatterns = [
    path('create/', ResumeCreateView.as_view(), name='resume_create'),
    path('<int:pk>/edit/', ResumeCreateView.as_view(), name='resume_edit')
]