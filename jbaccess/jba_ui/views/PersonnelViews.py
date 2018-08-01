from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from jba_core.models import Person
from jba_core.service import PersonService
from jba_ui.common.CommonViews import DetailView, ListView
from jba_ui.common.model_types import PERSON
from jba_ui.forms import PersonForm


class PersonListView(ListView):
    template_name = 'personnel/person-list.html'
    model = Person
    fields = ['id', 'name']
    details_url_name = 'ui:person details'
    title = 'Person list'
    model_name = PERSON

    def get_queryset(self):
        return PersonService.get_all()


class PersonCreateView(CreateView):
    template_name = 'personnel/person-create.html'
    form_class = PersonForm

    def get_success_url(self):
        return reverse('ui:person list')


class PersonDetailView(DetailView):
    template_name = 'personnel/person-detail.html'
    model = Person
    fields = ['id', 'name']

    def get_object(self, queryset=None):
        return PersonService.get(self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super(PersonDetailView, self).get_context_data(**kwargs)
        context['id'] = self.kwargs['id']
        return context


class PersonUpdateView(UpdateView):
    template_name = 'personnel/person-update.html'
    form_class = PersonForm

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
