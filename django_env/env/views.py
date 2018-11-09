# -*- coding: utf-8 -*-
from django.shortcuts import render
from env.models import ResourceBase
from env.models import ResourceEnvBase
from env.models import ResourceJira
from env.models import ResourceModuleArchive
from django.http import HttpResponse
from common.logger import Log

# Create your views here.

def testdb(request):
    list1 = ResourceBase.objects.all()
    resource_base = ResourceBase(base_type='redis', resource_data='i am resource_data', status=1)
    resource_base.save()
    Log.info(type(resource_base))
    Log.info("resource_base.save()")
    Log.info("resource_base = ResourceBase(base_type='redis')")
    return HttpResponse("向数据库ResourceBase表中插入一条数据")



