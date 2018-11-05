# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('base_type', models.CharField(max_length=15)),
                ('resource_data', models.CharField(max_length=1024)),
                ('status', models.PositiveSmallIntegerField()),
                ('creator', models.CharField(max_length=24)),
                ('is_valid', models.BooleanField(default=1)),
            ],
            options={
                'db_table': 'resource_base',
            },
        ),
    ]
