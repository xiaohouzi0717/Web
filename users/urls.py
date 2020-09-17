#!/usr/bin/python
# -*- coding: UTF-8 -*-
# tester = 'Xiao'
from django.conf.urls import url
from django.contrib.auth.views import LoginView  # 注意这是django2X的写法

from . import views

urlpatterns = [
    # 设置登录页面,LoginView.as_view后面要加上()
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),

    # 设置注销页面
    url(r'^logout/$', views.logout_view, name='logout'),

    # 设置注册页面
    url(r'^register/$', views.register, name='register'),
]

# from django.contrib.auth import login  #这是django1x的写法
# urlpatterns = [
#     # 设置登录页面
#     url(r'^login/$',login,{'template_name'='users/login.html'},name='login')
# ]
