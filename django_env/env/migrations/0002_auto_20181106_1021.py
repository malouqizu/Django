# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('env', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcebase',
            name='is_valid',
            field=models.IntegerField(default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='resourcebase',
            name='status',
            field=models.IntegerField(max_length=1),
        ),
        migrations.AlterField(
            model_name='resourceenvbase',
            name='base_id',
            field=models.IntegerField(max_length=11),
        ),
        migrations.AlterField(
            model_name='resourcejira',
            name='jira_id',
            field=models.IntegerField(max_length=11),
        ),
        migrations.AlterField(
            model_name='resourcejira',
            name='jira_status',
            field=models.IntegerField(max_length=1),
        ),
        migrations.AlterField(
            model_name='resourcejira',
            name='resource_id',
            field=models.IntegerField(max_length=11),
        ),
        migrations.AlterField(
            model_name='resourecemodulearchive',
            name='extend_port_num',
            field=models.IntegerField(max_length=1),
        ),
        migrations.AlterField(
            model_name='resourecemodulearchive',
            name='https',
            field=models.IntegerField(max_length=1),
        ),
        migrations.AlterField(
            model_name='resourecemodulearchive',
            name='namespace',
            field=models.IntegerField(max_length=1),
        ),
        migrations.AlterField(
            model_name='resourecemodulearchive',
            name='nginx',
            field=models.IntegerField(max_length=1),
        ),
        migrations.AlterField(
            model_name='resourecemodulearchive',
            name='status',
            field=models.IntegerField(max_length=1),
        ),
    ]
