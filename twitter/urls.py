from django.urls import path
from . import views

urlpatterns = [
path('', views.twitter, name='twitter'),
]

