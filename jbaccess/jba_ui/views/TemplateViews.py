from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'static/home.html'


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = 'ui:home'

    def get_success_url(self):
        return reverse('ui:home')


class LogoutConfirmView(TemplateView):
    template_name = 'registration/logout-confirm.html'


class CustomLogoutView(LogoutView):
    pass