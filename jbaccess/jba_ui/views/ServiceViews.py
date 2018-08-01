from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import TemplateView, RedirectView

from jba_ui.common.model_types import PERSON, KEY, ROLE, CONTROLLER, DOOR, PLACE
from jba_ui.common.view_fields import MODEL_NAME, ID


class DetailRedirectView(RedirectView):
    model_name = None
    redirect_url_dict = None

    def get_model_name(self):
        if self.model_name is None:
            self.model_name = self.kwargs[MODEL_NAME]
        return self.model_name

    def get_redirect_url_dict(self):
        if self.redirect_url_dict is None:
            kwargs = {ID: self.kwargs[ID]}
            self.redirect_url_dict = {
                PERSON: reverse('ui:person details', kwargs=kwargs),
                KEY: reverse('ui:key details', kwargs=kwargs),
                ROLE: reverse('ui:role details', kwargs=kwargs),
                CONTROLLER: reverse('ui:controller details', kwargs=kwargs),
                DOOR: reverse('ui:door details', kwargs=kwargs),
                PLACE: reverse('ui:place details', kwargs=kwargs)
            }
        return self.redirect_url_dict

    def get_redirect_url(self, *args, **kwargs):
        model_name = self.get_model_name()
        redirect_url_dict = self.get_redirect_url_dict()
        self.url = redirect_url_dict[model_name] or reverse('ui:home')
        return super(DetailRedirectView, self).get_redirect_url(*args, **kwargs)


class HomeView(TemplateView):
    template_name = 'static/home.html'


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = 'ui:home'

    def get_success_url(self):
        return reverse('ui:home')


class LogoutConfirmView(TemplateView):
    template_name = 'registration/logout-confirm.html'


class CustomLogoutView(LogoutView):
    pass
