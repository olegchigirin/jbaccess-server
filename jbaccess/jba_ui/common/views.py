from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, FormView
from django_tables2.views import SingleTableView

from jba_ui.common.mixins import TitleMixin, ModelFieldsMixin, IdToContextMixin, ListObjectMixin, \
    SingleObjectMixin


class ModelListView(SingleTableView, TitleMixin, ListObjectMixin):
    pass


class ModelCreateView(CreateView, TitleMixin):
    pass


class ModelDetailsView(DetailView, TitleMixin, ModelFieldsMixin, IdToContextMixin, SingleObjectMixin):
    pass


class ModelUpdateView(UpdateView, TitleMixin, IdToContextMixin, SingleObjectMixin):
    pass


class ModelDeleteView(DeleteView, TitleMixin, IdToContextMixin, SingleObjectMixin):
    pass


class AttachedModelToModel(SingleTableView, TitleMixin, IdToContextMixin):
    pass


class AttachModelToModel(FormView, TitleMixin, IdToContextMixin):
    pass


class DetachModelFromModel(FormView, TitleMixin, IdToContextMixin):
    pass


class AllowedRulesView(SingleTableView, TitleMixin, IdToContextMixin):
    pass


class AddAllowRuleView(FormView, TitleMixin, IdToContextMixin):
    pass


class AddDenyRuleView(FormView, TitleMixin, IdToContextMixin):
    pass
