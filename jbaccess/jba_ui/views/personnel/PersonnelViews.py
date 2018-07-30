from django.urls import reverse
from django.views.generic import CreateView

from jba_core.models import Person
from jba_core.service import PersonService
from jba_ui.views.common import CustomListView, CustomDetailView
from jba_ui.forms import PersonCreateForm


class PersonListView(CustomListView):
    template_name = 'personnel/person-list.html'
    model = Person
    displayed_headers = ['id', 'name']

    def get_queryset(self):
        return PersonService.get_all()


class PersonDetailView(CustomDetailView):
    template_name = 'personnel/person-detail.html'
    model = Person
    describe_fields = ['id', 'name', 'roles']

    def get_object(self, queryset=None):
        return PersonService.get(self.kwargs['id'])


class PersonCreateView(CreateView):
    template_name = 'personnel/person-create.html'
    form_class = PersonCreateForm

    def get_success_url(self):
        return reverse('ui:person list')
