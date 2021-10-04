# coding:utf-8

from django.shortcuts import render
from django.views import View


class NavView(View):

    def get(self, request):
        data = {}
        return render(request, 'nav.html', data)


