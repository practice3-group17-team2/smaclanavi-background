from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from administer_data import views

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('classinfo/', views.ClassInfoList.as_view(), name='classinfo-list'),
    path('classinfo/<uuid:pk>/',
         views.ClassInfoDetail.as_view(),
         name='classinfo-detail'),
    path('review/', views.ReviewList.as_view(), name='review-list'),
    path('review/<uuid:pk>/',
         views.ReviewDetail.as_view(),
         name='review-detail'),
    path('lecinfos/',
         views.UpcomingLecInfoList.as_view(),
         name='lecinfos-list'),
    path('lecinfos/<uuid:pk>/',
         views.UpcomingLecInfodetail.as_view(),
         name='lecinfos-detail'),
])
