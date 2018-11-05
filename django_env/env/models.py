from django.db import models

# Create your models here.
# 创建table：resource_base
class ResourceBase(models.Model):
    base_type = models.CharField(max_length=15)
    resource_data = models.CharField(max_length=1024)
    status = models.PositiveSmallIntegerField()
    creator = models.CharField(max_length=24)
    is_valid = models.BooleanField(default=1)
    
    def __unicode__(self):
        return self.base_type

    class Meta:
        db_table = 'resource_base'
