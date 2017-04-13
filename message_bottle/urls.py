"""message_bottle URL Configuration

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
from django.contrib import admin

from message_board_app.views import HomeView, ThreadCreateView, UpdateThreadView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^thread/add/$', ThreadCreateView.as_view(), name='thread_add'),
    url(r'^admin/', admin.site.urls),
    
    url(r'^thread/edit/(?P<pk>\d+)/$', UpdateThreadView.as_view(), name = 'thread_update')
]
