# coding:utf-8

from django.urls import path
from .views import (
    VideoTypeView, VideoTypeAdd,
    VideoFormView, VideoFromAdd, VideoNationalityView,
    VideoNationalityAdd, ExternalVideo,  ExternalVideoAdd
)

urlpatterns = [
    path('video/video_type', VideoTypeView.as_view(), name='video_type'),
    path('video/video_type/add', VideoTypeAdd.as_view(), name='video_type_add'),
    path('video/video_from', VideoFormView.as_view(), name='video_from'),
    path('video/video_from/add', VideoFromAdd.as_view(), name='video_from_add'),
    path('video/video_nationality',
         VideoNationalityView.as_view(), name='video_nationality'),
    path('video/video_nationality/add',
         VideoNationalityAdd.as_view(), name='video_nationality_add'),
    path('video/external', ExternalVideo.as_view(), name='external_video'),
    path('video/external/add', ExternalVideoAdd.as_view(), name='external_video_add'),
]
