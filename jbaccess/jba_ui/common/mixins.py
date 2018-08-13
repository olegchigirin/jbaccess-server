from django.http import Http404
from django.views.generic.base import ContextMixin

from jba_ui.common.const import ID


class TitleMixin(ContextMixin):
    title = None
    title_context_name = 'title'

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super(TitleMixin, self).get_context_data(**kwargs)
        context[self.title_context_name] = self.get_title()
        return context


class ModelFieldsMixin(ContextMixin):
    fields = None
    fields_context_name = 'fields'

    def get_fields(self):
        return self.fields or []

    def get_context_data(self, **kwargs):
        context = super(ModelFieldsMixin, self).get_context_data(**kwargs)
        context[self.fields_context_name] = self.get_fields()
        return context


class DetailsUrlMixin(ContextMixin):
    details_url_name = None
    details_url_context_name = 'details_url'

    def get_details_url_name(self):
        return self.details_url_name

    def get_context_data(self, **kwargs):
        context = super(DetailsUrlMixin, self).get_context_data(**kwargs)
        context[self.details_url_context_name] = self.get_details_url_name()
        return context


class IdToContextMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super(IdToContextMixin, self).get_context_data(**kwargs)
        context[ID] = self.kwargs[ID]
        return context


class ServiceMixin(object):
    service = None


class SingleObjectMixin(ServiceMixin):
    obj = None

    def get_obj_by_id(self, id: int, error_message: str = 'Object does not exist'):
        if self.obj is None:
            try:
                self.obj = self.service.get(id=id)
            except:
                raise Http404(error_message)
        return self.obj


class ListObjectMixin(ServiceMixin):
    obj_list = None

    def get_all(self, error_message='Object list was not found'):
        if self.obj_list is None:
            try:
                self.obj_list = self.service.get_all()
            except:
                raise Http404(error_message)
        return self.obj_list
