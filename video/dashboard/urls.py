# coding:utf-8

from django.urls import path, re_path
from .views import IndexView, LoginView, AdminManger, Logout, UpdateAdminStatus

urlpatterns = [
    path('index', IndexView.as_view(), name='dashboard_index'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path(r'admin/manger', AdminManger.as_view(), name='admin_manger'),
    path('admin/mager/update/status', UpdateAdminStatus.as_view(),
         name='admin_update_status')
]
