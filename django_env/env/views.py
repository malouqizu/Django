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
    resource_base = ResourceBase(base_type='redis', resource_data='i am resource_data', status=1, creator='lmm', is_valid=1)
    resource_base.save()
    resource_base = ResourceBase(base_type='db', resource_data='i am resource_db', status=1, creator='lmm',is_valid=1)
    resource_base.save()
    resource_base = ResourceBase(base_type='kafka', resource_data='i am resource_kafka', status=1, creator='lmm',is_valid=1)
    resource_base.save()

    resource_env_base = ResourceEnvBase(base_id=1, env='test5', ip='10.26.14.5', creator='lmm')
    resource_env_base.save()

    resource_jira = ResourceJira(jira_id=2365, jira_status=1, res_type='Redis', resource_id=2333,
                                 submit_data='redis submit data', result_data='redis result data', creator='lmm')
    resource_jira.save()

    resource_module_archive = ResourceModuleArchive(archive_id='333', ip_flag='10.26.14.33', resource_host='10.26.14.33',
                                                    resource_http_port='8000', module_domain='test3-i.bk-house-api.ke.com',
                                                    https=1, nginx=1, namespace=0, extend_port_num=0, extend_data='/public',
                                                    custom='need custom data', status=1)
    resource_module_archive.save()

    Log.info("resource_base = ResourceBase(base_type='redis', resource_data='i am resource_data', status=1, creator='lmm', is_valid=1)")
    Log.info(type(resource_base))
    Log.info("resource_base.save()")
    return HttpResponse("向数据库env各表中插入数据")



