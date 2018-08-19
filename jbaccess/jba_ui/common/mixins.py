from django.http import Http404
from django.views.generic.base import ContextMixin
from django.views.generic.edit import FormMixin

from jba_ui.common.const import ID, INITIAL


class TitleMixin(ContextMixin):
    title = None
    title_context_name = 'title'

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super(TitleMixin, self).get_context_data(**kwargs)
        context[self.title_context_name] = self.get_title()
        return context


class FormContextMixin(ContextMixin):
    form_type: str = None
    form_type_context_name = 'form_type'
    form_model: str = None
    form_model_context_name = 'form_model'

    def get_form_type(self):
        return self.form_type

    def get_form_model(self):
        return self.form_model

    def get_context_data(self, **kwargs):
        context = super(FormContextMixin, self).get_context_data(**kwargs)
        context[self.form_model_context_name] = self.get_form_model()
        context[self.form_type_context_name] = self.get_form_type()
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


class IdToContextMixin(ContextMixin):
    obj_id = None
    obj_id_context_name = ID

    def get_obj_id(self):
        if self.obj_id is None:
            self.obj_id = self.kwargs[ID]
        return self.obj_id

    def get_context_data(self, **kwargs):
        context = super(IdToContextMixin, self).get_context_data(**kwargs)
        context[self.obj_id_context_name] = self.get_obj_id()
        return context


class AllowDenyFormMixin(FormMixin, IdToContextMixin):
    obj_id_context_name = ID

    def get_form_kwargs(self):
        kwargs = super(AllowDenyFormMixin, self).get_form_kwargs()
        kwargs[INITIAL] = {
            self.obj_id_context_name: self.get_obj_id()
        }
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(AllowDenyFormMixin, self).form_valid(form)


class AttachDetachFormMixin(FormMixin, IdToContextMixin):
    obj_id_form_name = ID

    def get_form_kwargs(self):
        kwargs = super(AttachDetachFormMixin, self).get_form_kwargs()
        kwargs[self.obj_id_form_name] = self.get_obj_id()
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(AttachDetachFormMixin, self).form_valid(form)


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


class ReturnUrlMixin(ContextMixin):
    return_url = None
    return_url_context_name = 'return_url'

    def get_return_url(self):
        if not self.return_url:
            self.return_url = self.request.META.pop('HTTP_REFERER', None)
        return self.return_url

    def get_context_data(self, **kwargs):
        context = super(ReturnUrlMixin, self).get_context_data(**kwargs)
        return_url = self.get_return_url()
        if return_url:
            context[self.return_url_context_name] = return_url
        return context