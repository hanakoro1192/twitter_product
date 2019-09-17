from django.urls import path
from . import views

urlpatterns = [
path('', views.polls, name='polls'),
]

