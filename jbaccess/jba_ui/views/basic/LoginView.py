from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import TemplateView


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = 'ui:home'

    def get_success_url(self):
        return reverse('ui:home')


class LogoutConfirmView(TemplateView):
    template_name = 'registration/logout-confirm.html'


class CustomLogoutView(LogoutView):
    success_url_allowed_hosts = 'ui:home'
