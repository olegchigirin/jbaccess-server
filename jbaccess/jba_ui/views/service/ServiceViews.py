from django.contrib.auth import views
from django.urls import reverse
from django.views.generic import TemplateView

from jba_ui.common.mixins import TitleMixin
from jba_ui.forms import ACLForm


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


class TestFormView(views.FormView):
    form_class = ACLForm
    template_name = 'test.html'
