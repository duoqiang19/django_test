# -*- coding:utf-8 -*-
# @ProjectName  :django_test
# @FileName     :urls.py
# @Time         :2020/12/04 20:50
# @Author       :Wang D.Q
# @Descripion   :users\urls.py

from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('login/',
         LoginView.as_view(
            template_name='users/login.html'
         ),
         name='login'),
]



if __name__ == "__main__":
    run_code = 0
