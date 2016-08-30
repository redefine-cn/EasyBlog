"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# _*_ coding:utf-8 _*_
from django.conf.urls import patterns,include, url
from django.contrib import admin
from article.views import *
urlpatterns=patterns('',
   # Examples:
    #url(r'^$','my_blog.views.home',name='home'),
    #url(r'^blog/',include('blog.urls')),
    url(r'^admin/',include(admin.site.urls)),
    url(r'^$','article.views.home'),#由于目前只有一个app, 方便起见, 就不设置include了
    #url(r'^(?P<my_args>\d+)/$','article.views.detail',name='detail'),
    #url(r'^test/$','article.views.test'),
)

