# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('env', '0002_auto_20181106_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcebase',
            name='is_valid',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='resourcebase',
            name='status',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='resourceenvbase',
            name='base_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='resourcejira',
            name='jira_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='resourcejira',
            name='jira_status',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='resourcejira',
            name='resource_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='resourecemodulearchive',
            name='extend_port_num',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='resourecemodulearchive',
            name='https',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='resourecemodulearchive',
            name='namespace',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='resourecemodulearchive',
            name='nginx',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='resourecemodulearchive',
            name='status',
            field=models.IntegerField(),
        ),
    ]
