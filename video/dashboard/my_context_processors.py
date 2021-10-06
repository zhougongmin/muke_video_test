# coding:utf-8
from django.shortcuts import redirect, reverse
from utils.permission import dashboard_auth


def get_user_info(request):
    return {'suser': request.user}

