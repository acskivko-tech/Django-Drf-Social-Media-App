from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

"""Render main page depends on authentication of user """
class MainPageView(TemplateView):
    """Func to check if user is logged in"""
    def get_template_names(self):
        if self.request.user.is_authenticated:
            return ['base.html']
        else:
            return ['welcome.html']

