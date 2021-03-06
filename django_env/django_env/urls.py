"""django_env URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from env import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^testdb_add_method/$', views.testdb_add_method),
    url(r'^testdb_update_method/$', views.testdb_update_method),
    url(r'^testdb_query_method/$', views.testdb_query_method),
    url(r'^testdb_delete_method/$', views.testdb_delete_method),
    url(r'^hello/$', views.hello),
    url(r'^add/$', views.add,name='add'),
    url(r'^add/(\d+)/(\d+)/$', views.add2,name='add2')
]
