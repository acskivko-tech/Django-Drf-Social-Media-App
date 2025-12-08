from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from rest_framework.reverse import reverse_lazy

from core.forms import AddPostForm
from core.models import Post

# Create your views here.

"""Render main page depends on authentication of user """
class MainPageView(TemplateView):
    #Func to check if user is logged in
    def get_template_names(self):
        if self.request.user.is_authenticated:
            return ['feed.html']
        return ['welcome.html']

    #Func to get context data for feed.html
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['posts'] = Post.objects.all()[:10]
        return context

class AddPostView(LoginRequiredMixin,CreateView):
    form_class = AddPostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('welcome')
