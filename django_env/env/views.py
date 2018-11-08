# -*- coding: utf-8 -*-
from django.shortcuts import render
from env.models import ResourceBase
from env.models import ResourceEnvBase
from env.models import ResourceJira
from env.models import ResourceModuleArchive
from django.http import HttpResponse

# Create your views here.

def testdb(request):
    list1 = ResourceBase.objects.all()
    return HttpResponse(list1)



