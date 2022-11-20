from django.urls import path

from accounts.views import RegisterView, login_view, logout_view, ProfileView, UserChangeView

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/<int:pk>', ProfileView.as_view(), name='user_detail'),
    path('profile/<int:pk>/update', UserChangeView.as_view(), name='user_update'),
]
