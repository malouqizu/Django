# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
# 创建table：resource_base
class ResourceBase(models.Model):
    base_type = models.CharField(max_length=15)
    resource_data = models.CharField(max_length=1024)
    status = models.IntegerField()
    creator = models.CharField(max_length=24)
    is_valid = models.IntegerField(default=1)

    def __unicode__(self):
        return self.base_type

    class Meta:
        db_table = 'resource_base'

# 创建table：resource_jira
class ResourceJira(models.Model):
    jira_id = models.IntegerField()
    jira_status = models.IntegerField()
    sour_type = models.CharField(max_length=15)
    resource_id = models.IntegerField()
    submit_data = models.CharField(max_length=2048)
    result_data = models.CharField(max_length=2048)
    creator = models.CharField(max_length=24)

    def __unicode__(self):
        return self.jira_id

    class Meta:
        db_table = 'resource_jira'

# 创建table：resource_env_base
class ResourceEnvBase(models.Model):
    base_id = models.IntegerField()
    env = models.CharField(max_length=20)
    ip = models.CharField(max_length=16)
    creator = models.CharField(max_length=24)

    def __unicode__(self):
        return self.base_id

    class Meta:
        db_table = 'resource_env_base'

# 创建table：resourece_module_archive
class ResoureceModuleArchive(models.Model):
    archive_id = models.CharField(max_length=48)
    ip_flag = models.CharField(max_length=16)
    resource_host = models.CharField(max_length=20)
    resource_http_port = models.CharField(max_length=8)
    module_domain = models.CharField(max_length=48)
    https = models.IntegerField()
    nginx = models.IntegerField()
    namespace = models.IntegerField()
    extend_port_num = models.IntegerField()
    extend_data = models.CharField(max_length=1024)
    custom = models.CharField(max_length=2048)
    status = models.IntegerField()

    def __unicode__(self):
        return self.archive_id

    class Meta:
        db_table = 'resourece_module_archive'

