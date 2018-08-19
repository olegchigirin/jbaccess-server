from django.urls import reverse

from jba_core.models import Key
from jba_core.service import KeyService
from jba_ui.common.const import ID
from jba_ui.common.views import ModelListView, ModelCreateView, ModelDetailsView, ModelUpdateView, ModelDeleteView
from jba_ui.forms import KeyCreateForm, KeyUpdateForm
from jba_ui.tables import KeyTable


class KeyCreate(ModelCreateView):
    template_name = 'keys/create.html'
    title = 'Create key'
    form_model = 'Key'
    form_class = KeyCreateForm

    def get_success_url(self):
        return reverse('ui:key details', kwargs={ID: self.object.id})


class KeyList(ModelListView):
    template_name = 'keys/list.html'
    model = Key
    table_class = KeyTable
    title = 'Key List'
    service = KeyService


class KeyDetail(ModelDetailsView):
    template_name = 'keys/details.html'
    model = Key
    fields = ['id', 'name', 'access_key', 'person']
    title = 'Key details'
    service = KeyService


class KeyUpdate(ModelUpdateView):
    template_name = 'keys/update.html'
    title = 'Key Update'
    form_class = KeyUpdateForm
    form_model = 'key'
    service = KeyService

    def get_success_url(self):
        return reverse('ui:key details', kwargs={ID: self.kwargs[ID]})


class KeyDelete(ModelDeleteView):
    template_name = 'keys/delete.html'
    title = 'Delete key'
    model = Key
    form_model = 'key'
    service = KeyService

    def get_success_url(self):
        return reverse('ui:key list')
