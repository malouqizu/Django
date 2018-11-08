# -*- coding: utf-8 -*-
from django.shortcuts import render
from django_env.env.models import ResourceBase
from django_env.env.models import ResourceEnvBase
from django_env.env.models import ResourceJira
from django_env.env.models import ResourceModuleArchive
from django.http import HttpResponse

# Create your views here.

def testdb(request):
    return HttpResponse("这是一个测试DB的函数。")



