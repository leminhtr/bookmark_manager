"""bookmark_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from bookmark_app.views import *
from . import views

urlpatterns = [
    #/user/username
    url(r'^user/(?P<username>[-\w]+)/$', views.bookmark_user, name='bookmark_manager_user'),
    url(r'^create/$', views.bookmark_create, name='bookmark_manager_create'),
    url(r'^edit/(?P<pk>\d+)/$', views.bookmark_edit, name='bookmark_manager_edit'),
    url(r'^$', views.bookmark_list, name='bookmark_manager_list'),
]

