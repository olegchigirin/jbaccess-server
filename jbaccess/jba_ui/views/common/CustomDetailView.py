from django.views.generic import DetailView


class CustomDetailView(DetailView):
    context_object_name = 'object'
    describe_fields = None
    pk_url_kwarg = 'id'

    def get_describe_fields(self):
        return self.describe_fields

    def get_context_data(self, **kwargs):
        context = super(CustomDetailView, self).get_context_data(**kwargs)
        context['fields'] = self.get_describe_fields()
        return context
