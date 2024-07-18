from django.contrib.auth import views as auth_views

from .forms import AuthenticationForm
from .mixins import AnonymousRequiredMixin


class LoginView(
    AnonymousRequiredMixin,
    auth_views.LoginView,
):
    next_page = 'chats:chat'
    form_class = AuthenticationForm
