from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import RegisterForm


# Create your views here.

class RegisterUserView(CreateView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')


class LoginUserView(LoginView):
    template_name = 'users/login.html'
    form_class = AuthenticationForm

    def get_success_url(self):
        return reverse_lazy('welcome')


class LogoutUserView(LoginRequiredMixin,LogoutView):
    def get_success_url(self):
        return reverse_lazy('login')
