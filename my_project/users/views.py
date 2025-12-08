from django.urls import reverse_lazy
from django.views.generic import CreateView
from djoser.webauthn.views import LoginView

from users.forms import RegisterForm, LoginForm


# Create your views here.

class RegisterUserView(CreateView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')


class LoginUserView(LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('welcome')