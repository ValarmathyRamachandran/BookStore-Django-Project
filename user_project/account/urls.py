from django.urls import path
from user_project.account.views import RegistrationAPIView

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
]

