from django.urls import path
from resumes.views import ResumeCreateView

urlpatterns = [
    path('create/', ResumeCreateView.as_view())
]