from django.urls import path

from accounts.views import RegisterView, LoginView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('', RegisterView.as_view(), name='register'),
]