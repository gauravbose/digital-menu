"""digimenu2 URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns,include,url 
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'restaurant.views.login'),
    url(r'^accounts/auth/$', 'restaurant.views.auth_view'),
    url(r'^restaurant/logout/$', 'restaurant.views.logout'),
    url(r'^restaurant/login/$', 'restaurant.views.login'),
    url(r'^accounts/loggedin/$', 'restaurant.views.loggedin'),
    url(r'^accounts/invalid/$', 'restaurant.views.invalid_login'),
    url(r'^accounts/register/$', 'restaurant.views.register_user'),
    url(r'^restaurant/login/register/$', 'restaurant.views.register_user'),
    url(r'^accounts/login/register/$', 'restaurant.views.register_user'),
    url(r'^accounts/register/login.?$', 'restaurant.views.login'),
    url(r'^rango/register/$', 'restaurant.views.register_user'),
    url(r'^accounts/register_success/$', 'restaurant.views.register_success'),
   # url(r'^restaurant/index/welcome.*$','restaurant.views.welcome'),    

    url(r'^restaurant/', include('restaurant.urls')),
  #  url(r'^restaurant/index.?$','restaurant.views.index'),
  #  url(r'^restaurant/index/Indian.*$','restaurant.views.indian'),
  #  url(r'^restaurant/index/Chinese.*$','restaurant.views.chinese'),
  #  url(r'^restaurant/index/Desserts.*$','restaurant.views.desserts'),
  #  url(r'^restaurant/index/Chaat.*$','restaurant.views.chaat'),
  #  url(r'^restaurant/index/Italian.*$','restaurant.views.italian'),
  #  url(r'^restaurant/index/South.*$','restaurant.views.southindian'),
   # url(r'^restaurant/index/Beverages.*$','restaurant.views.beverages'),
  #  url(r'^restaurant/welcome.*$','restaurant.views.welcome'),
  #  url(r'^restaurant/index/cart.*$','restaurant.views.cart'),
  #  url(r'^restaurant/welcome/index.*$','restaurant.views.index'),
  #  url(r'^restaurant/index/welcome.*$','restaurant.views.welcome'),
  #  url(r'^restaurant/index/index.*$','restaurant.views.index'),
  #  url(r'^restaurant/index/Cart.*$','restaurant.views.cart'),
    url(r'^(?P<question_id>[0-9]+)/$','restaurant.views.italian'),

)
