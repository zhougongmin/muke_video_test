# coding:utf-8

import functools
from django.shortcuts import redirect, reverse


def dashboard_auth(func):
    @functools.wraps(func)
    def wrapper(self, request, *args, **kwargs):
        user = request.user
        # request.user.is_authenticated 验证用户是否登录
        if not user.is_authenticated or not user.is_superuser:
            return redirect('{}?to={}'.format(reverse('login'), request.path))
        return func(self, request, *args, **kwargs)

    return wrapper
