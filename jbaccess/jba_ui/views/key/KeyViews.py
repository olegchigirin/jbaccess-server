from django.urls import reverse
from django.views.generic import DeleteView, CreateView, DetailView, UpdateView
from django_tables2 import SingleTableView

from jba_core.models import Key
from jba_core.service import KeyService
from jba_ui.common.mixins import TitleMixin, ModelFieldsMixin, IdToContextMixin
from jba_ui.common.view_fields import ID
from jba_ui.forms import KeyCreateForm
from jba_ui.tables import KeyTable


class KeyCreate(CreateView, TitleMixin):
    form_class = KeyCreateForm
    title = 'Create key'
    template_name = 'keys/create.html'
    key_id = None

    def form_valid(self, form: KeyCreateForm):
        name = form.cleaned_data['name']
        access_key = form.cleaned_data['access_key']
        person = form.cleaned_data.pop('person')
        key = KeyService.create(
            name=name,
            access_key=access_key,
            person_id=person.id
        )
        self.key_id = key.id
        return super(KeyCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('ui:key details', kwargs={ID: self.key_id})


class KeyList(SingleTableView, TitleMixin):
    template_name = 'keys/list.html'
    model = Key
    table_class = KeyTable
    title = 'Key List'

    def get_queryset(self):
        return KeyService.get_all()


class KeyDetail(DetailView, ModelFieldsMixin, TitleMixin, IdToContextMixin):
    template_name = 'keys/details.html'
    model = Key
    fields = ['id', 'name', 'access_key', 'person']
    title = 'Key details'

    def get_object(self, queryset=None):
        return KeyService.get(id=self.kwargs[ID])


class KeyUpdate(UpdateView, TitleMixin, IdToContextMixin):
    template_name = 'keys/update.html'
    form_class = KeyCreateForm
    title = 'Key Update'

    def get_object(self, queryset=None):
        return KeyService.get(id=self.kwargs[ID])

    def get_success_url(self):
        return reverse('ui:key details', kwargs={ID: self.kwargs[ID]})


class KeyDelete(DeleteView, TitleMixin, IdToContextMixin):
    template_name = 'keys/key-delete.html'
    model = Key
    title = 'Delete Key'

    def get_object(self, queryset=None):
        return KeyService.get(self.kwargs[ID])

    def get_success_url(self):
        return reverse('ui:key list')
