from django.urls import path

from core.views import MainPageView, AddPostView

urlpatterns = [
    path('', MainPageView.as_view(), name='welcome'),
    path('create-post/',AddPostView.as_view(), name='create_post'),
]