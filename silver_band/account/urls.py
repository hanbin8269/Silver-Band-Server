from django.urls import path, include
from .views import RegistrationView, LoginView, WearerViewSet

urlpatterns = [
    path("auth/register/", RegistrationView.as_view()),
    path("auth/login/", LoginView.as_view()),
    path("<user_id>/wearer/", WearerViewSet.as_view()),
]