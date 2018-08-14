from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import FormView, DetailView, DeleteView
from django_tables2 import SingleTableView

from jba_core.models import SimpleRecurringPattern
from jba_core.service import AclService
from jba_ui.common.const import ID
from jba_ui.common.mixins import TitleMixin, IdToContextMixin, ModelFieldsMixin
from jba_ui.forms import ACLForm
from jba_ui.tables import ACLPattern


class AclPatterns(SingleTableView, IdToContextMixin, TitleMixin):
    template_name = 'acls/list.html'
    title = 'Acls patterns'
    table_class = ACLPattern

    def get_queryset(self):
        return AclService.get_patterns(acl_id=self.kwargs[ID])


class AclPatternDetails(DetailView, IdToContextMixin, TitleMixin, ModelFieldsMixin):
    template_name = 'acls/details.html'
    title = 'Pattern details'
    model = SimpleRecurringPattern
    fields = ['id', 'from_time', 'until_time', 'days_of_week', 'days_of_month', 'months']

    def get_object(self, queryset=None):
        return AclService.get_pattern(id=self.kwargs[ID])


class AclPatternCreate(FormView, TitleMixin, IdToContextMixin):
    template_name = 'acls/create-pattern.html'
    title = 'Pattern create'
    form_class = ACLForm

    def get_form_kwargs(self):
        kwargs = super(AclPatternCreate, self).get_form_kwargs()
        kwargs['initial'] = {'acl_id': self.kwargs[ID]}
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(AclPatternCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('ui:acl pattern list', kwargs={ID: self.kwargs[ID]})


class AclPatternUpdate(FormView, TitleMixin, IdToContextMixin):
    template_name = 'acls/update-pattern.html'
    title = 'Update pattern'
    form_class = ACLForm

    def get_form_kwargs(self):
        kwargs = super(AclPatternUpdate, self).get_form_kwargs()
        kwargs['id'] = self.kwargs[ID]
        return kwargs

    def form_valid(self, form):
        form.update(pattern_id=self.kwargs[ID])
        return super(AclPatternUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse('ui:acl pattern details', kwargs={ID: self.kwargs[ID]})


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