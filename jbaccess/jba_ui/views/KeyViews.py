from django.urls import reverse
from django.views.generic import DeleteView

from jba_core.service import KeyService, PersonService
from jba_ui.common.CommonViews import DetailView, ListView, UpdateView, CreateView
from jba_core.models import Key
from jba_ui.common.model_types import KEY
from jba_ui.forms import KeyForm


class KeyCreateView(CreateView):
    form_class = KeyForm
    title = 'Create key'
    template_name = 'keys/key-create.html'

    def get_success_url(self):
        return reverse('ui:key list')


class KeyListView(ListView):
    template_name = 'keys/key-list.html'
    model = Key
    model_name = KEY
    fields = ['id', 'name', 'access_key', 'person']
    title = 'Key List'

    def get_queryset(self):
        return KeyService.get_all()


class KeyDetailView(DetailView):
    template_name = 'keys/key-details.html'
    model = Key
    fields = ['id', 'name', 'access_key', 'person']
    title = 'Key details'

    def get_object(self, queryset=None):
        return KeyService.get(id=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super(KeyDetailView, self).get_context_data(**kwargs)
        context['id'] = self.kwargs['id']
        return context


class KeyUpdateView(UpdateView):
    template_name = 'keys/key-update.html'
    form_class = KeyForm
    title = 'Key Update'

    def get_object(self, queryset=None):
        return KeyService.get(id=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super(KeyUpdateView, self).get_context_data(**kwargs)
        context['id'] = self.kwargs['id']
        return context

    def get_success_url(self):
        return reverse('ui:key details', kwargs={'id': self.kwargs['id']})


class KeyAttachedToPersonView(ListView):
    template_name = 'keys/key-attached-to-person.html'
    model = Key
    model_name = KEY
    title = 'Key for person'
    fields = ['id', 'name', 'access_key']

    def get_queryset(self):
        return PersonService.get_keys(self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super(KeyAttachedToPersonView, self).get_context_data(**kwargs)
        context['person_id'] = self.kwargs['id']
        return context


class KeyDeleteView(DeleteView):
    template_name = 'keys/key-delete.html'
    model = Key

    def get_context_data(self, **kwargs):
        context = super(KeyDeleteView, self).get_context_data(**kwargs)
        context['id'] = self.kwargs['id']
        return context

    def get_object(self, queryset=None):
        return KeyService.get(self.kwargs['id'])

    def get_success_url(self):
        return reverse('ui:key list')
