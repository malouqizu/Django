# -*- coding: utf-8 -*-
from django.shortcuts import render
from env.models import ResourceBase
from env.models import ResourceEnvBase
from env.models import ResourceJira
from env.models import ResourceModuleArchive
from django.http import HttpResponse
from common.logger import Log

# Create your views here.

def testdb_add_method1(request):
    # 先创建对象实例，然后保存数据
    resource_base = ResourceBase(base_type='redis', resource_data='i am resource_data', status=1, creator='lmm', is_valid=1)
    resource_base.save()
    resource_env_base = ResourceEnvBase(base_id=1, env='test7', ip='10.26.14.7', creator='lmm')
    resource_env_base.save()
    resource_jira = ResourceJira(jira_id=2368, jira_status=1, res_type='Redis', resource_id=2338,
                                 submit_data='redis submit data', result_data='redis result data', creator='lmm')
    resource_jira.save()
    resource_module_archive = ResourceModuleArchive(archive_id='337', ip_flag='10.26.14.37', resource_host='10.26.14.37',
                                                    resource_http_port='8000', module_domain='test3-i.bk-house-api.ke.com',
                                                    https=1, nginx=1, namespace=0, extend_port_num=0, extend_data='/public',
                                                    custom='need custom data', status=1)
    resource_module_archive.save()

    return HttpResponse("(先创建对象实例，然后保存数据)向数据库env各表中插入数据")

def testdb_add_method2(request):
    # 创建对象，并同时保存对象的快捷方法，存在关系字段时无法使用此方法
    ResourceBase.objects.create(base_type='redis', resource_data='i am resource_data', status=1, creator='lmm', is_valid=1)
    ResourceEnvBase.objects.create(base_id=2, env='test6', ip='10.26.14.6', creator='lmm')
    ResourceJira.objects.create(jira_id=2366, jira_status=1, res_type='Redis', resource_id=2336,
                                 submit_data='redis submit data', result_data='redis result data', creator='lmm')
    ResourceModuleArchive.objects.create(archive_id='335', ip_flag='10.26.14.35', resource_host='10.26.14.35',
                         resource_http_port='8000', module_domain='test3-i.bk-house-api.ke.com',
                         https=1, nginx=1, namespace=0, extend_port_num=0, extend_data='/public',
                         custom='need custom data', status=1)
    return HttpResponse("(创建对象，并同时保存对象)向数据库env各表中插入数据")

def testdb_add_method3(request):
    # 在表中批量插入多条数据
    ResourceBase_list_to_insert=[]
    ResourceEnvBase_list_to_insert=[]
    ResourceJira_list_to_insert=[]
    ResourceModuleArchive_list_to_insert=[]

    for i in range(10):
        ResourceBase_list_to_insert.append(ResourceBase(base_type='redis', resource_data='i am resource_data'+str(i), status=1, creator='lmm', is_valid=1))
        ResourceEnvBase_list_to_insert.append(ResourceEnvBase(base_id=9 + i, env='test' + str(7 + i), ip='10.26.14.' + str(4 + i), creator='lmm'))
        ResourceJira_list_to_insert.append(ResourceJira(jira_id=2369+i, jira_status=1, res_type='Redis', resource_id=2337+i,
                                 submit_data='redis submit data', result_data='redis result data', creator='lmm'))
        ResourceModuleArchive_list_to_insert.append(ResourceModuleArchive(archive_id='339'+str(i), ip_flag='10.26.14.3'+str(6+i),
                                                                          resource_host='10.26.14.3'+str(6+i),
                         resource_http_port='8000', module_domain='test'+str(4+i)+'-i.bk-house-api.ke.com',
                         https=1, nginx=1, namespace=0, extend_port_num=0, extend_data='/public',
                         custom='need custom data', status=1))

    ResourceBase.objects.bulk_create(ResourceBase_list_to_insert)
    ResourceEnvBase.objects.bulk_create(ResourceEnvBase_list_to_insert)
    ResourceJira.objects.bulk_create(ResourceJira_list_to_insert)
    ResourceModuleArchive.objects.bulk_create(ResourceModuleArchive_list_to_insert)

    return HttpResponse('批量插入多条数据')

def testdb_update_method1(request):
    # 更新一条数据，也只能更新一条数据
    t = ResourceBase.objects.get(id=79)
    t.creator = 'nick'
    t.ip = '10.10.10.10'
    t.save()

    return HttpResponse('更新一条数据，也只能更新一条数据')

