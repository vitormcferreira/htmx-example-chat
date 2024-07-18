from django.contrib.auth.views import logout_then_login
from django.urls import path

from .views import LoginView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path("logout/", logout_then_login, name='logout'),
]
