from django.urls import path, include
from .views import RegistrationView, LoginView

urlpatterns = [
    path("auth/register/", RegistrationView.as_view()),
    path("auth/login/", LoginView.as_view()),
]