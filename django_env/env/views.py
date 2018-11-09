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

    for i in range(10,20):
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

def testdb_query_method1(request):
    # 批量获取查询数据
    '''
    objects.all()
    objects.filter(id=82)
    获取到的是一个django.db.models.query.QuerySet，包含了查询到表中匹配到的记录，每个记录用一个对象表示，每个字段是这个对象值
    :param request:
    :return:
    '''
    re1 = ResourceBase.objects.filter(id=82)
    re2 = ResourceEnvBase.objects.filter(creator='nill')
    re3 = ResourceJira.objects.filter(creator='nill')
    re4 = ResourceModuleArchive.objects.filter(extend_data= "/data0/www/htdocs")

    for i in re1:
        Log.info(i.__dict__.items())
        Log.info(i.id)
        Log.info(i.base_type)
        Log.info(i.resource_data)
        Log.info(i.status)
        Log.info(i.creator)
        Log.info(i.is_valid)

    Log.info('\n')
    Log.info(re2[0].__dict__.items())
    Log.info(re2[0].id)
    Log.info(re2[0].base_id)
    Log.info(re2[0].env)
    Log.info(re2[0].ip)
    Log.info(re2[0].creator)

    Log.info('\n')
    Log.info(re3[0].__dict__.items())
    Log.info(re3[0].id)
    Log.info(re3[0].jira_id)
    Log.info(re3[0].jira_status)
    Log.info(re3[0].res_type)
    Log.info(re3[0].resource_id)
    Log.info(re3[0].submit_data)
    Log.info(re3[0].result_data)
    Log.info(re3[0].creator)

    Log.info('\n')
    Log.info(re4[0].__dict__.items())
    Log.info(re4[0].id)
    Log.info(re4[0].archive_id)
    Log.info(re4[0].ip_flag)
    Log.info(re4[0].resource_host)
    Log.info(re4[0].resource_http_port)
    Log.info(re4[0].module_domain)
    Log.info(re4[0].https)
    Log.info(re4[0].nginx)
    Log.info(re4[0].namespace)
    Log.info(re4[0].extend_port_num)
    Log.info(re4[0].extend_data)
    Log.info(re4[0].custom)
    Log.info(re4[0].status)

    return HttpResponse('批量查询获取数据')

def testdb_query_method2(request):
    # 只获取单条数据
    # objects.get()
    t1 = ResourceBase.objects.get(id=79)
    Log.info(t1.creator)
    Log.info(t1.resource_data)

    t2 = ResourceEnvBase.objects.get(id=79)
    Log.info(t2.creator)
    Log.info(t2.ip)
    Log.info(t2.env)

    return HttpResponse('获取单条查询数据')

def testdb_update_method1(request):
    # 更新一条数据，也只能更新一条数据
    # objects.get(id=79) 此方法的参数值在数据库中必须的唯一的，如果有重复数据时就会报错
    '''
    https://www.jb51.net/article/144322.htm
    具有auto_now属性字段的更新
    我们通常会给表添加三个默认字段
    自增ID，这个django已经默认加了，就像上边的建表语句，虽然只写了username和is_active两个字段，但表建好后也会有一个默认的自增id字段
    创建时间，用来标识这条记录的创建时间，具有auto_now_add属性，创建记录时会自动填充当前时间到此字段
    修改时间，用来标识这条记录最后一次的修改时间，具有auto_now属性，当记录发生变化时填充当前时间到此字段
    :param request: 
    :return: 
    '''

    t1 = ResourceBase.objects.get(id=79)
    t1.creator = 'nick'
    t1.resource_data = 'update resource data'
    t1.save()

    t2 = ResourceEnvBase.objects.get(id=79)
    t2.creator = 'nick'
    t2.ip = '10.10.10.10'
    t2.env = 'TEST'
    t2.save()

    # res_type的值不唯一，所以报错
    # t3 = ResourceJira.objects.get(res_type='Redis')
    # t3.creator = 'nick'
    # t3.submit_data = '10.10.10.10'
    # t3.result_data = 'TEST'
    # t3.save()

    t4 = ResourceModuleArchive.objects.get(id=100033)
    t4.creator = 'nick'
    t4.module_domain = '10.10.10.10'
    t4.extend_port_num = '3'
    t4.save()

    return HttpResponse('更新一条数据，也只能更新一条数据')

def testdb_update_method2(request):
    # 批量更新数据
    # 类似于mysql语句 update resource_base set username='nick' where id = 1
    ResourceBase.objects.filter(creator='lmm').update(creator='nill', is_valid=2)
    ResourceEnvBase.objects.filter(env='test9').update(creator='nike', ip='10.26.16.22')
    ResourceJira.objects.filter(creator='lmm').update(creator='nill', res_type='db')
    ResourceModuleArchive.objects.filter(extend_data='/public').update(extend_data= "/data0/www/htdocs")

    return HttpResponse('批量更新数据')

def testdb_delete_method1(request):
    # 删除单条表记录
    ResourceEnvBase.objects.get(creator='nike').delete()
    return HttpResponse('删除单条表记录')

def testdb_delete_method2(request):
    # 批量删除表记录
    ResourceEnvBase.objects.filter(creator='nill').delete()
    return HttpResponse('删除多条表记录')


