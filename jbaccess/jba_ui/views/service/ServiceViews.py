from django.contrib.auth import views
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.urls import reverse
from django.views.generic import TemplateView

from jba_ui.common.mixins import TitleMixin


class Home(TemplateView, TitleMixin):
    title = 'Home'
    template_name = 'static/home.html'


class Login(views.LoginView, TitleMixin):
    template_name = 'registration/login.html'
    title = 'Login'

    def get_success_url(self):
        return reverse('ui:home')


class LogoutConfirm(TemplateView, TitleMixin):
    template_name = 'registration/logout-confirm.html'
    title = 'Logout confirmation'


class Logout(views.LogoutView):
    pass


def page_not_found(request):
    response = render(request, '404.html', {'status': 400})
    response.status_code = 404
    return response
