from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, FormView
from django_tables2.views import SingleTableView

from jba_ui.common.const import ID, INITIAL
from jba_ui.common.mixins import TitleMixin, ListObjectMixin, FormContextMixin, ModelFieldsMixin, IdToContextMixin, \
    SingleObjectMixin, AttachDetachFormMixin, AllowDenyFormMixin, ReturnUrlMixin


class ModelListView(SingleTableView, ReturnUrlMixin, TitleMixin, ListObjectMixin):
    return_url = None
    return_url_context_name = 'return_url'
    title = 'Model list page'

    def get_queryset(self):
        return self.get_all()

    def get_return_url(self):
        if not self.return_url:
            self.return_url = self.request.META.pop('HTTP_REFERER', None)
        return self.return_url

    def get_context_data(self, **kwargs):
        context = super(ModelListView, self).get_context_data(**kwargs)
        return_url = self.get_return_url()
        if return_url:
            context[self.return_url_context_name] = return_url
        return context


class ModelCreateView(CreateView, ReturnUrlMixin, TitleMixin, FormContextMixin):
    form_type = 'Create'
    title = 'Create page'


class ModelDetailsView(DetailView, ReturnUrlMixin, TitleMixin, ModelFieldsMixin, IdToContextMixin, SingleObjectMixin):
    title = 'Details page'

    def get_object(self, queryset=None):
        return self.get_obj_by_id(id=self.get_obj_id())


class ModelUpdateView(UpdateView, ReturnUrlMixin, TitleMixin, IdToContextMixin, SingleObjectMixin, FormContextMixin):
    form_type = 'Update'
    title = 'Update model page'

    def get_form_kwargs(self):
        kwargs = super(ModelUpdateView, self).get_form_kwargs()
        kwargs[INITIAL] = {ID: self.get_obj_id()}
        return kwargs

    def get_object(self, queryset=None):
        return self.get_obj_by_id(id=self.get_obj_id())


class ModelDeleteView(DeleteView, ReturnUrlMixin, TitleMixin, IdToContextMixin, SingleObjectMixin, FormContextMixin):
    form_type = 'Delete'
    title = 'Delete model page'

    def get_object(self, queryset=None):
        return self.get_obj_by_id(id=self.get_obj_id())

    def delete(self, request, *args, **kwargs):
        self.service.delete(id=self.get_object().id)
        return HttpResponseRedirect(self.get_success_url())


class AttachedModelToModel(SingleTableView, ReturnUrlMixin, TitleMixin, IdToContextMixin):
    title = 'Attached models page'


class AttachOrDetachModels(FormView, ReturnUrlMixin, TitleMixin, AttachDetachFormMixin, FormContextMixin):
    form_type = 'Attach'
    title = 'Attach page'


class RulesView(SingleTableView, ReturnUrlMixin, TitleMixin, IdToContextMixin):
    title = 'Allowed rules page'


class AddRuleView(FormView, ReturnUrlMixin, TitleMixin, AllowDenyFormMixin, FormContextMixin):
    form_type = 'Allow'
    title = 'Allow page'
