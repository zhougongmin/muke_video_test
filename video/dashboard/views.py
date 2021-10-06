# coding:utf-8

from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.core.paginator import Paginator
import math
from utils.permission import dashboard_auth


class IndexView(View):
    TEMPLATE = 'index.html'

    @dashboard_auth
    def get(self, request):
        return render(request, self.TEMPLATE)


'''
    功能：处理用户登录
'''


class LoginView(View):
    TEMPLATE = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('dashboard_index'))
        request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
        # to = request.GET.get('to', '')
        # _login = redirect(reverse('login'))
        # login_to = _login + to
        data = {'error': ''}
        return render(request, self.TEMPLATE, data)

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        exists = User.objects.filter(username=username).exists()
        if not exists:
            data = {'error': '用户不存在'}
            return render(request, self.TEMPLATE, data=data)
        user = authenticate(username=username, password=password)
        if not user:
            data = {'error': '密码错误'}
            return render(request, self.TEMPLATE, data=data)

        if not user.is_superuser:
            data = {'error': '权限不够，请提升权限！'}
            return render(request, self.TEMPLATE, data=data)
        login(request, user)

        to = request.GET.get('to', '')
        _login = redirect(reverse('login'))
        if to:
            return redirect(to)
        return redirect(reverse('dashboard_index'))


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login'))


class AdminManger(View):
    TEMPLATE = 'admin.html'

    @dashboard_auth
    def get(self, request):
        # 从url上获取当前请求的页数
        p = request.GET.get('page', 1)
        current_page = int(p)
        users = User.objects.all()
        # 显示数据库数据，并且规定每页显示多少条数据
        page = Paginator(users, 1)

        # 获取当前页数据
        new_user = page.get_page(current_page)

        # 显示的总页数
        total_page = page.num_pages

        # 开始页码
        begin = (current_page - int(math.ceil(10.0 / 2)))
        if begin < 1:
            begin = 1

        # 结束页码
        end = begin + 9
        if end > page.num_pages:
            end = page.num_pages

        if end <= 10:
            begin = 1
        else:
            begin = end - 9

        page_list = range(begin, end + 1)

        data = {'pager_users_list': new_user,
                'page_list': page_list,
                'current_num': current_page}
        return render(request, self.TEMPLATE, data)


class UpdateAdminStatus(View):
    def get(self, request):
        status = request.GET.get('status', 'on')

        _status = True if status == 'on' else False
        print(_status)
        request.user.is_superuser = _status
        request.user.save()

        return redirect(reverse('admin_manger'))
