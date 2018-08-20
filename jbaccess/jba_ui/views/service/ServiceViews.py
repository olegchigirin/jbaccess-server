from typing import List

from django.contrib.auth import views
from django.db.models import QuerySet
from django.urls import reverse
from django.views.generic import TemplateView
from django_tables2 import Table

from jba_core.service import PersonService, RoleService, KeyService, PlaceService, DoorService, ControllerService
from jba_ui.common.mixins import TitleMixin, ReturnUrlMixin, FormContextMixin
from jba_ui.forms.service import LoginForm
from jba_ui.tables import PersonTable, KeyTable, RoleTable, PlaceTable, DoorTable, ControllerTable


class Home(TemplateView, TitleMixin):
    title = 'Home'
    template_name = 'static/home.html'
    services = [PersonService, KeyService, RoleService, PlaceService, DoorService, ControllerService]
    table_classes = [PersonTable, KeyTable, RoleTable, PlaceTable, DoorTable, ControllerTable]

    def get_data_tables(self) -> List[Table]:
        tables = []
        for service, table in zip(self.services, self.table_classes):
            queryset: QuerySet = service.get_all()[:5]
            tables.append(table(queryset))
        return tables

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['tables'] = self.get_data_tables()
        return context


class Login(views.LoginView, TitleMixin):
    template_name = 'registration/login.html'
    title = 'Login'
    form_class = LoginForm

    def get_success_url(self):
        return reverse('ui:home')


class LogoutConfirm(TemplateView, TitleMixin, FormContextMixin):
    template_name = 'registration/logout-confirm.html'
    title = 'Logout confirmation'
    form_type = 'Logout confirm'
    form_model = ' '


class Logout(views.LogoutView):
    pass
