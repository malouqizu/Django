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
    re = ResourceBase.objects.get(id=1)
    Log.info(type(ResourceBase.objects.get(id=1)))
    Log.info('ResourceBase.objects.get(id=1):')
    Log.error(re)
    return HttpResponse(re)



