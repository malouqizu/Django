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
    ResourceBase(base_type='redis', resource_data='i am resource_data', status=1, creator='lmm', is_valid=1).save()

    return HttpResponse("(先创建对象实例，然后保存数据)向数据库env各表中插入数据")

def testdb_add_method2(request):
    # 创建对象，并同时保存对象的快捷方法，存在关系字段时无法使用此方法
    ResourceBase.objects.create(base_type='redis', resource_data='i am resource_data', status=1, creator='lmm', is_valid=1)

    return HttpResponse("(创建对象，并同时保存对象)向数据库env各表中插入数据")

def testdb_add_method3(request):
    # 在表中批量插入多条数据
    ResourceBase_list_to_insert=[]
    
    for i in range(10,20):
        ResourceBase_list_to_insert.append(ResourceBase(base_type='redis', resource_data='i am resource_data'+str(i), status=1, creator='lmm', is_valid=1))

    ResourceBase.objects.bulk_create(ResourceBase_list_to_insert)

    return HttpResponse('批量插入多条数据')

def testdb_query_method1(request):
    # 批量获取查询数据
    '''
    objects.all()
    objects.filter(id=82)
    获取到的是一个django.db.models.query.QuerySet，包含了查询到表中匹配到的记录，每个记录用一个对象表示，每个字段是这个对象值
    '''
    re1 = ResourceBase.objects.filter(id=82)

    for i in re1:
        Log.info(i.__dict__.items())
        Log.info(i.id)
        Log.info(i.base_type)
        Log.info(i.resource_data)
        Log.info(i.status)
        Log.info(i.creator)
        Log.info(i.is_valid)

    return HttpResponse('批量查询获取数据')

def testdb_query_method2(request):
    # 只获取单条数据
    # objects.get()
    t1 = ResourceBase.objects.get(id=79)
    Log.info(t1.creator)
    Log.info(t1.resource_data)

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
    '''

    t1 = ResourceBase.objects.get(id=79)
    t1.creator = 'nick'
    t1.resource_data = 'update resource data'
    t1.save()

    return HttpResponse('更新一条数据，也只能更新一条数据')

def testdb_update_method2(request):
    # 批量更新数据
    # 类似于mysql语句 update resource_base set username='nick' where id = 1
    ResourceBase.objects.filter(creator='lmm').update(creator='nill', is_valid=2)

    return HttpResponse('批量更新数据')

def testdb_delete_method1(request):
    # 删除单条表记录
    ResourceEnvBase.objects.get(creator='nike').delete()
    return HttpResponse('删除单条表记录')

def testdb_delete_method2(request):
    # 批量删除表记录
    ResourceEnvBase.objects.filter(creator='lmm').delete()
    return HttpResponse('删除多条表记录')


