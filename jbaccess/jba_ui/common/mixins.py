from django.views.generic.base import ContextMixin


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
        context['id'] = self.kwargs['id']
        return context
