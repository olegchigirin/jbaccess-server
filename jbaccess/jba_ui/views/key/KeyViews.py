from django.urls import reverse
from django.views.generic import DeleteView, CreateView, ListView, DetailView, UpdateView

from jba_core.models import Key
from jba_core.service import KeyService
from jba_ui.common.mixins import DetailsUrlMixin, TitleMixin, ModelFieldsMixin, IdToContextMixin
from jba_ui.common.view_fields import ID
from jba_ui.forms import KeyForm


class KeyCreate(CreateView, TitleMixin):
    form_class = KeyForm
    title = 'Create key'
    template_name = 'keys/key-create.html'

    def get_success_url(self):
        return reverse('ui:key list')


class KeyList(ListView, DetailsUrlMixin, TitleMixin, ModelFieldsMixin):
    template_name = 'keys/key-list.html'
    model = Key
    details_url_name = 'ui:key details'
    fields = ['id', 'name', 'access_key', 'person']
    title = 'Key List'

    def get_queryset(self):
        return KeyService.get_all()


class KeyDetail(DetailView, ModelFieldsMixin, TitleMixin, IdToContextMixin):
    template_name = 'keys/key-details.html'
    model = Key
    fields = ['id', 'name', 'access_key', 'person']
    title = 'Key details'

    def get_object(self, queryset=None):
        return KeyService.get(id=self.kwargs[ID])


class KeyUpdate(UpdateView, TitleMixin, IdToContextMixin):
    template_name = 'keys/key-update.html'
    form_class = KeyForm
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
