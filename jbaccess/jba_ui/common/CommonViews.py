from django.views import generic

from jba_ui.common.view_fields import TITLE, FIELDS, OBJECT_LIST, MODEL_NAME, OBJECT, ID, DETAILS_URL


class TitleMixin(object):
    title = ''
    title_context_name = TITLE

    def get_title(self):
        return self.title


class ModelFieldsMixin(object):
    fields = None
    fields_context_name = FIELDS

    def get_fields(self):
        return self.fields or []


class ModelDetailsUrlMixin(object):
    details_url_name = None
    details_url_context_name = DETAILS_URL

    def get_details_url_name(self):
        return self.details_url_name


class ListView(TitleMixin, ModelFieldsMixin, ModelDetailsUrlMixin, generic.ListView):
    context_object_name = OBJECT_LIST

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context[self.title_context_name] = self.get_title()
        context[self.fields_context_name] = self.get_fields()
        context[self.details_url_context_name] = self.get_details_url_name()
        return context


class CreateView(TitleMixin, generic.CreateView):

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context[self.title_context_name] = self.get_title()
        return context


class DetailView(TitleMixin, ModelFieldsMixin, generic.DetailView):
    context_object_name = OBJECT

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context[self.fields_context_name] = self.get_fields()
        context[self.title_context_name] = self.get_title()
        if self.kwargs[ID]:
            context[ID] = self.kwargs[ID]
        return context


class UpdateView(TitleMixin, generic.UpdateView):

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context[self.title_context_name] = self.get_title()
        if self.kwargs[ID]:
            context[ID] = self.kwargs[ID]
        return context


class DeleteView(TitleMixin, generic.DeleteView):

    def get_context_data(self, **kwargs):
        context = super(DeleteView, self).get_context_data(**kwargs)
        context[self.title_context_name] = self.get_title()
        if self.kwargs[ID]:
            context[ID] = self.kwargs[ID]
        return context


class FormView(TitleMixin, generic.FormView):

    def get_context_data(self, **kwargs):
        context = super(FormView, self).get_context_data(**kwargs)
        context[self.title_context_name] = self.get_title()
        return context
