# coding:utf-8

from django.urls import path
from .views import NavView

urlpatterns = [
    path('base', NavView.as_view(), name='nav'),
]
