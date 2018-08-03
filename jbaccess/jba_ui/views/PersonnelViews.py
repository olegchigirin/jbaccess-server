from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from jba_core.models import Person
from jba_core.service import PersonService
from jba_ui.common.CommonViews import DetailView, ListView
from jba_ui.common.view_fields import ID
from jba_ui.forms import PersonForm


class PersonListView(ListView):
    template_name = 'personnel/person-list.html'
    model = Person
    fields = ['id', 'name']
    details_url_name = 'ui:person details'
    title = 'Person list'

    def get_queryset(self):
        return PersonService.get_all()

    def get_context_data(self, **kwargs):
        context = super(PersonListView, self).get_context_data(**kwargs)
        return context


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
        return PersonService.get(self.kwargs[ID])

    def get_context_data(self, **kwargs):
        context = super(PersonDetailView, self).get_context_data(**kwargs)
        context[ID] = self.kwargs[ID]
        return context


class PersonUpdateView(UpdateView):
    template_name = 'personnel/person-update.html'
    form_class = PersonForm

    def get_object(self, queryset=None):
        return PersonService.get(self.kwargs[ID])

    def get_success_url(self):
        return reverse('ui:person details', kwargs={ID: self.kwargs[ID]})


class PersonDeleteView(DeleteView):
    template_name = 'personnel/person-delete.html'
    model = Person

    def get_context_data(self, **kwargs):
        context = super(PersonDeleteView, self).get_context_data(**kwargs)
        context['id'] = self.kwargs[ID]
        return context

    def get_object(self, queryset=None):
        return PersonService.get(self.kwargs[ID])

    def get_success_url(self):
        return reverse('ui:person list')
