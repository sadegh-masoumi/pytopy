from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    # def get_context_data(self, **kwargs):
    #     context = super(Dashboard, self).get_context_data(**kwargs)
    #
