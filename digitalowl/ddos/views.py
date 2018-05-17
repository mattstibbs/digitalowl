## ccbv.co.uk

from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.conf import settings
from django.contrib.auth import mixins
from ddos.models import DosResult

import nhs_dos


def get_dos_client(user):
    user = nhs_dos.User(user.dosuser.username, user.dosuser.password)
    client = nhs_dos.RestApiClient(user)
    return client


class ServiceView(mixins.LoginRequiredMixin, ListView):
    template_name = 'service_list.html'

    model = DosResult


class ServiceDetailView(mixins.LoginRequiredMixin, TemplateView):
    template_name = 'service_detail.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        client = get_dos_client(self.request.user)
        response = client.get_service_by_id(self.kwargs['identifier'])
        ctx['name'] = response[0].name
        DosResult.objects.create(name=ctx['name'],
                                 identifier=self.kwargs['identifier'],
                                 user=self.request.user)
        return ctx
