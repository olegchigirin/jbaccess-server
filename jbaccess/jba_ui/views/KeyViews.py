from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from jba_core.service import KeyService, PersonService
from jba_ui.views.CustomViews import CustomDetailView, CustomListView, CustomUpdateView
from jba_core.models import Key
from jba_ui.forms import KeyForm


class KeyCreateView(CreateView):
    form_class = KeyForm
    title = 'Create key'
    template_name = 'keys/key-create.html'

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super(KeyCreateView, self).get_context_data(**kwargs)
        context['title'] = self.get_title()
        return context

    def get_success_url(self):
        return reverse('ui:key list')


class KeyListView(CustomListView):
    template_name = 'keys/key-list.html'
    model = Key
    fields = ['id', 'name', 'access_key', 'person']
    title = 'Key List'

    def get_queryset(self):
        return KeyService.get_all()


class KeyDetailView(CustomDetailView):
    template_name = 'keys/key-details.html'
    model = Key
    describe_fields = ['id', 'name', 'access_key', 'person']
    title = 'Key details'

    def get_object(self, queryset=None):
        return KeyService.get(id=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super(KeyDetailView, self).get_context_data(**kwargs)
        context['id'] = self.kwargs['id']
        return context


class KeyUpdateView(CustomUpdateView):
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


class KeyAttachedToPersonView(CustomListView):
    template_name = 'keys/key-attached-to-person.html'
    model = Key
    title = 'Key for person'
    fields = ['id', 'name', 'access_key', 'person']

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
