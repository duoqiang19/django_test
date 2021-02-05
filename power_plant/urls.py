# -*- coding:utf-8 -*-
# @ProjectName  :django_test
# @FileName     :urls.py.py
# @Time         :2020/11/21 21:30
# @Author       :Wang D.Q
# @Description  :定义power_plant的URL模式

from django.conf.urls import url
from django.urls import path,include,re_path


from . import views

app_name = 'power_plant' # url改成path后必须加，不然会报错 “xxx is not a registered namespace错误”

urlpatterns = [
    # url(r'^$', views.index, name='index'), #等效下面path函数用法
    # url(r'^systems/$', views.systems, name='systems'), #等效下面path函数用法
    path('', views.index, name='index'),
    path('systems/', views.systems, name='systems'),
    re_path('systems/(?P<system_id>\d+)/', views.system, name='system'),
    path('new_system/', views.new_system, name='new_system'),
    re_path('new_entry/(?P<system_id>\d+)/', views.new_entry, name='new_entry'),
    re_path('edit_entry/(?P<entry_id>\d+)/', views.edit_entry, name='edit_entry'),
]

if __name__ == "__main__":
    run_code = 0