from django.urls import path, include

from core.views import MainPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
]