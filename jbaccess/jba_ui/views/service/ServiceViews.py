from typing import List

from django.contrib.auth import views
from django.db.models import QuerySet
from django.urls import reverse
from django.views.generic import TemplateView
from django_tables2 import Table

from jba_core.service import PersonService, RoleService, KeyService, PlaceService, DoorService, ControllerService
from jba_ui.common.mixins import TitleMixin, ReturnUrlMixin, FormContextMixin
from jba_ui.forms.service import LoginForm
from jba_ui.tables import PersonTable, KeyTable, RoleTable, PlaceTable, DoorTable, ControllerTable, PersonHomePageTable


class Home(TemplateView, TitleMixin):
    title = 'Home'
    template_name = 'static/home.html'

    @staticmethod
    def get_table() -> Table:
        persons = PersonService.get_all()
        data = []
        for person in persons:
            data.append({
                'person': person,
                'keys': PersonService.get_keys(id=person.id),
                'roles': PersonService.get_roles(id=person.id)
            })
        return PersonHomePageTable(data=data)

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['table'] = self.get_table()
        context['person_count'] = PersonService.get_all().count()
        context['keys_count'] = KeyService.get_all().count()
        context['roles_count'] = RoleService.get_all().count()
        context['places_count'] = PlaceService.get_all().count()
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
