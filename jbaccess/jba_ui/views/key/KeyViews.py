from django.http import HttpResponseRedirect
from django.urls import reverse

from jba_core.models import Key
from jba_core.service import KeyService
from jba_ui.common.const import ID
from jba_ui.common.views import ModelListView, ModelCreateView, ModelDetailsView, ModelUpdateView, ModelDeleteView
from jba_ui.forms import KeyCreateForm
from jba_ui.tables import KeyTable


class KeyCreate(ModelCreateView):
    form_class = KeyCreateForm
    title = 'Create key'
    template_name = 'keys/create.html'
    key_id = None

    def form_valid(self, form: KeyCreateForm):
        key = KeyService.create(
            name=form.cleaned_data['name'],
            access_key=form.cleaned_data['access_key'],
            person_id=form.cleaned_data.pop('person')
        )
        self.key_id = key.id
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('ui:key details', kwargs={ID: self.key_id})


class KeyList(ModelListView):
    template_name = 'keys/list.html'
    model = Key
    table_class = KeyTable
    title = 'Key List'
    service = KeyService

    def get_queryset(self):
        return self.get_all()


class KeyDetail(ModelDetailsView):
    template_name = 'keys/details.html'
    model = Key
    fields = ['id', 'name', 'access_key', 'person']
    title = 'Key details'
    service = KeyService

    def get_object(self, queryset=None):
        return self.get_obj_by_id(id=self.kwargs[ID])


class KeyUpdate(ModelUpdateView):
    template_name = 'keys/update.html'
    form_class = KeyCreateForm
    title = 'Key Update'
    service = KeyService

    def get_object(self, queryset=None):
        return self.get_obj_by_id(id=self.kwargs[ID])

    def get_success_url(self):
        return reverse('ui:key details', kwargs={ID: self.kwargs[ID]})


class KeyDelete(ModelDeleteView):
    template_name = 'keys/key-delete.html'
    model = Key
    title = 'Delete Key'

    def get_object(self, queryset=None):
        return KeyService.get(self.kwargs[ID])

    def get_success_url(self):
        return reverse('ui:key list')
