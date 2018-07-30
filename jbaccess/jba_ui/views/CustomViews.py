from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView


class CustomCreateView(CreateView):
    title = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super(CustomCreateView, self).get_context_data(**kwargs)
        context['title'] = self.get_title()
        return context


class CustomDetailView(DetailView):
    context_object_name = 'object'
    describe_fields = None
    title = None

    def get_title(self):
        return self.title

    def get_describe_fields(self):
        return self.describe_fields

    def get_context_data(self, **kwargs):
        context = super(CustomDetailView, self).get_context_data(**kwargs)
        context['fields'] = self.get_describe_fields()
        context['title'] = self.get_title()
        return context


class CustomListView(ListView):
    fields = None
    context_object_name = 'object_list'
    title = None

    def get_title(self):
        return self.title

    def get_fields(self):
        return self.fields

    def get_context_data(self, **kwargs):
        context = super(CustomListView, self).get_context_data(**kwargs)
        context['headers'] = self.get_fields()
        context['title'] = self.get_title()
        return context


class CustomUpdateView(UpdateView):
    title = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super(CustomUpdateView, self).get_context_data(**kwargs)
        context['title'] = self.get_title()
        return context


class CustomDeleteView(DeleteView):
    title = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super(CustomDeleteView, self).get_context_data(**kwargs)
        context['title'] = self.get_title()
        return context

