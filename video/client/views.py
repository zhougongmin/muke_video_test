# coding:utf-8

from django.views.generic import View
from django.shortcuts import render, redirect, reverse
from utils.permission import dashboard_auth
from django.core.paginator import Paginator
from .models import VideoType, FromTo, Nationality, Video
import math

'''
    视频类型
'''


class VideoTypeView(View):
    TEMPLATE = 'video_type.html'

    def get(self, request):
        type_name = VideoType.objects.all()
        # 从url上获取当前请求的页数
        p = request.GET.get('page', 1)
        current_page = int(p)
        # 显示数据库数据，并且规定每页显示多少条数据
        page = Paginator(type_name, 5)

        # 获取当前页数据
        new_type_name = page.get_page(current_page)

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

        data = {'type_name_list': new_type_name,
                'page_list': page_list,
                'current_num': current_page}
        # data = {'type_name': type_name}
        return render(request, self.TEMPLATE, data)


'''
    添加视频类型
'''


class VideoTypeAdd(View):
    TEMPLATE = 'video_type_add.html'

    def get(self, request):
        return render(request, self.TEMPLATE)

    def post(self, request):
        type_name = request.POST.get('type_name', '')
        name = VideoType.objects.filter(type_name=type_name)
        if name:
            data = {'error': '该视频类型已存在：{}'.format(type_name)}
            return render(request, self.TEMPLATE, data)

        type_name = VideoType.objects.create(type_name=type_name)
        type_name.save()
        return redirect(reverse('video_type'))


'''
    视频来源
'''


class VideoFormView(View):
    TEMPLATE = 'video_from.html'

    def get(self, request):
        from_name = FromTo.objects.all()
        # 从url上获取当前请求的页数
        p = request.GET.get('page', 1)
        current_page = int(p)
        # 显示数据库数据，并且规定每页显示多少条数据
        page = Paginator(from_name, 5)

        # 获取当前页数据
        new_from_name = page.get_page(current_page)

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

        data = {'from_name_list': new_from_name,
                'page_list': page_list,
                'current_num': current_page}
        return render(request, self.TEMPLATE, data)


'''
    添加视频来源
'''


class VideoFromAdd(View):
    TEMPLATE = 'video_from_add.html'

    def get(self, request):
        return render(request, self.TEMPLATE)

    def post(self, request):
        from_name = request.POST.get('from_name', '')
        name = FromTo.objects.filter(from_to=from_name)
        if name:
            data = {'error': '该视频类型已存在：{}'.format(from_name)}
            return render(request, self.TEMPLATE, data)

        from_name = FromTo.objects.create(from_to=from_name)
        from_name.save()
        return redirect(reverse('video_from'))


'''
    视频国籍
'''


class VideoNationalityView(View):
    TEMPLATE = 'video_nationality.html'

    def get(self, request):
        nationality_name = Nationality.objects.all()
        # 从url上获取当前请求的页数
        p = request.GET.get('page', 1)
        current_page = int(p)
        # 显示数据库数据，并且规定每页显示多少条数据
        page = Paginator(nationality_name, 5)

        # 获取当前页数据
        new_nationality_name = page.get_page(current_page)

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
        data = {'nationality_name_list': new_nationality_name,
                'page_list': page_list,
                'current_num': current_page}
        return render(request, self.TEMPLATE, data)


'''
    添加视频国籍
'''


class VideoNationalityAdd(View):
    TEMPLATE = 'video_nationality_add.html'

    def get(self, request):
        return render(request, self.TEMPLATE)

    def post(self, request):
        nationality_name = request.POST.get('nationality_name', '')
        names = Nationality.objects.filter(name=nationality_name)
        print(12)
        if names:
            print(22)
            data = {'error': '该视频类型已存在：{}'.format(nationality_name)}
            return render(request, self.TEMPLATE, data)

        nationality_name = Nationality.objects.create(name=nationality_name)
        print(33)
        nationality_name.save()
        return redirect(reverse('video_nationality'))


'''
    外链视频
'''


class ExternalVideo(View):
    TEMPLATE = 'external_video.html'

    def get(self, request):
        videos = Video.objects.all()
        # 从url上获取当前请求的页数
        p = request.GET.get('page', 1)
        current_page = int(p)
        # 显示数据库数据，并且规定每页显示多少条数据
        page = Paginator(videos, 5)

        # 获取当前页数据
        new_nationality_name = page.get_page(current_page)

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
        data = {'nationality_name_list': new_nationality_name,
                'page_list': page_list,
                'current_num': current_page}
        return render(request, self.TEMPLATE, data)


'''
    添加外链视频
'''


class ExternalVideoAdd(View):
    TEMPLATE = 'external_video_add.html'

    @dashboard_auth
    def get(self, request):
        return render(request, self.TEMPLATE)

    def post(self, request):
        video_name = request.POST.get('video_name', '')
