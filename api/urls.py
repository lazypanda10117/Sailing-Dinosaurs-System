from django.urls import path
from . import views

urlpatterns = [
    path('functional/search', views.search, name='api.search'),
]
