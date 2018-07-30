from django.views.generic import ListView


class CustomListView(ListView):
    displayed_headers = None
    context_object_name = 'object_list'

    def get_displayed_headers(self):
        return self.displayed_headers

    def get_context_data(self, **kwargs):
        context = super(CustomListView, self).get_context_data(**kwargs)
        context['headers'] = self.get_displayed_headers()
        return context
