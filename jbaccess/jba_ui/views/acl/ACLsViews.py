from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.views.generic import FormView, DetailView, DeleteView
from django_tables2 import SingleTableView

from jba_core.models import SimpleRecurringPattern
from jba_core.service import AclService
from jba_ui.common.const import ID
from jba_ui.common.mixins import TitleMixin, IdToContextMixin, ModelFieldsMixin, FormContextMixin, ReturnUrlMixin
from jba_ui.common.utils import drop_squared_brackets, replace_days_of_week_for_names, replace_months_for_names
from jba_ui.forms import ACLCreateForm, ACLUpdateForm
from jba_ui.tables import ACLPattern


class AclPatterns(SingleTableView, IdToContextMixin, TitleMixin, ReturnUrlMixin):
    template_name = 'acls/list.html'
    title = 'Acls patterns'
    table_class = ACLPattern

    def get_queryset(self):
        return AclService.get_patterns(acl_id=self.kwargs[ID])


class AclPatternDetails(DetailView, IdToContextMixin, TitleMixin, ModelFieldsMixin, ReturnUrlMixin):
    template_name = 'acls/details.html'
    title = 'Pattern details'
    model = SimpleRecurringPattern
    fields = ['id', 'from_time', 'until_time', 'days_of_week', 'days_of_month', 'months']

    def get_object(self, queryset=None):
        return AclService.get_pattern(id=self.kwargs[ID])

    def get_context_data(self, **kwargs):
        context = super(AclPatternDetails, self).get_context_data(**kwargs)
        context['object'].days_of_week = self._render_days_of_week(context['object'].days_of_week)
        context['object'].days_of_month = self._render_days_of_month(context['object'].days_of_month)
        context['object'].months = self._render_months(context['object'].months)
        return context

    @staticmethod
    def _render_days_of_week(value: str):
        value = drop_squared_brackets(value)
        return replace_days_of_week_for_names(value)

    @staticmethod
    def _render_days_of_month(value: str):
        return drop_squared_brackets(value)

    @staticmethod
    def _render_months(value: str):
        value = drop_squared_brackets(value)
        return replace_months_for_names(value)


class AclPatternCreate(FormView, TitleMixin, IdToContextMixin, FormContextMixin, ReturnUrlMixin):
    template_name = 'acls/create-pattern.html'
    title = 'Pattern create'
    form_model = 'Acl pattern'
    form_type = 'Create'
    form_class = ACLCreateForm

    def get_form_kwargs(self):
        kwargs = super(AclPatternCreate, self).get_form_kwargs()
        try:
            AclService.get_acl(id=self.get_obj_id())
            kwargs['initial'] = {'acl_id': self.get_obj_id()}
            return kwargs
        except:
            raise Http404

    def form_valid(self, form):
        form.save()
        return super(AclPatternCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('ui:acl pattern list', kwargs={ID: self.get_obj_id()})


class AclPatternUpdate(FormView, TitleMixin, IdToContextMixin, FormContextMixin):
    template_name = 'acls/update-pattern.html'
    title = 'Update pattern'
    form_type = 'Update'
    form_model = 'pattern'
    form_class = ACLUpdateForm

    def get_form_kwargs(self):
        kwargs = super(AclPatternUpdate, self).get_form_kwargs()
        try:
            AclService.get_pattern(id=self.get_obj_id())
            kwargs['pattern_id'] = self.get_obj_id()
            return kwargs
        except:
            raise Http404

    def form_valid(self, form):
        form.save()
        return super(AclPatternUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse('ui:acl pattern details', kwargs={ID: self.get_obj_id()})


class AclPatternDelete(DeleteView, TitleMixin, IdToContextMixin):
    template_name = 'acls/delete-pattern.html'
    title = 'Delete pattern'
    obj: SimpleRecurringPattern = None
    acl_id = None

    def get_object(self, queryset=None):
        if self.obj is None:
            self.obj = AclService.get_pattern(id=self.kwargs[ID])
        return self.obj

    def delete(self, request, *args, **kwargs):
        self.acl_id = self.get_object().acl_id
        AclService.delete_pattern(pattern_id=self.kwargs[ID])
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('ui:acl pattern list', kwargs={ID: self.acl_id})


class AclDelete(DeleteView, TitleMixin, IdToContextMixin):
    template_name = 'acls/delete.html'
    title = 'Delete acls'
    obj = None

    def get_object(self, queryset=None):
        if self.obj is None:
            self.obj = AclService.get_acl(id=self.kwargs[ID])
        return self.obj

    def delete(self, request, *args, **kwargs):
        AclService.delete_acl(id=self.kwargs[ID])
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('ui:home')
