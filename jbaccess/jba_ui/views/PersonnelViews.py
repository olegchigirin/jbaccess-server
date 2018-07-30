from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView

from jba_core.models import Person
from jba_core.service import PersonService
from jba_ui.views.CustomViews import CustomDetailView, CustomListView
from jba_ui.forms import PersonForm


class PersonListView(CustomListView):
    template_name = 'personnel/person-list.html'
    model = Person
    fields = ['id', 'name']

    def get_queryset(self):
        return PersonService.get_all()


class PersonDetailView(CustomDetailView):
    template_name = 'personnel/person-detail.html'
    model = Person
    describe_fields = ['id', 'name', 'roles']

    def get_object(self, queryset=None):
        return PersonService.get(self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super(PersonDetailView, self).get_context_data(**kwargs)
        context['id'] = self.kwargs['id']
        return context


class PersonCreateView(CreateView):
    template_name = 'personnel/person-create.html'
    form_class = PersonForm

    def get_success_url(self):
        return reverse('ui:person list')


class PersonUpdateView(UpdateView):
    template_name = 'personnel/person-update.html'
    form_class = PersonForm
    pk_url_kwarg = 'id'

    def get_object(self, queryset=None):
        return PersonService.get(self.kwargs['id'])

    def get_success_url(self):
        return reverse('ui:person details', kwargs={'id': self.kwargs['id']})


class PersonDeleteView(DeleteView):
    template_name = 'personnel/person-delete.html'
    model = Person

    def get_context_data(self, **kwargs):
        context = super(PersonDeleteView, self).get_context_data(**kwargs)
        context['id'] = self.kwargs['id']
        return context

    def get_object(self, queryset=None):
        return PersonService.get(self.kwargs['id'])

    def get_success_url(self):
        return reverse('ui:person list')
