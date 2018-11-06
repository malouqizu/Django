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
        migrations.CreateModel(
            name='ResourceEnvBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('base_id', models.PositiveSmallIntegerField()),
                ('env', models.CharField(max_length=20)),
                ('ip', models.CharField(max_length=16)),
                ('creator', models.CharField(max_length=24)),
            ],
            options={
                'db_table': 'resource_env_base',
            },
        ),
        migrations.CreateModel(
            name='ResourceJira',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jira_id', models.BigIntegerField()),
                ('jira_status', models.SmallIntegerField()),
                ('sour_type', models.CharField(max_length=15)),
                ('resource_id', models.PositiveSmallIntegerField()),
                ('submit_data', models.CharField(max_length=2048)),
                ('result_data', models.CharField(max_length=2048)),
                ('creator', models.CharField(max_length=24)),
            ],
            options={
                'db_table': 'resource_jira',
            },
        ),
        migrations.CreateModel(
            name='ResoureceModuleArchive',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('archive_id', models.CharField(max_length=48)),
                ('ip_flag', models.CharField(max_length=16)),
                ('resource_host', models.CharField(max_length=20)),
                ('resource_http_port', models.CharField(max_length=8)),
                ('module_domain', models.CharField(max_length=48)),
                ('https', models.PositiveSmallIntegerField()),
                ('nginx', models.PositiveSmallIntegerField()),
                ('namespace', models.PositiveSmallIntegerField()),
                ('extend_port_num', models.PositiveSmallIntegerField()),
                ('extend_data', models.CharField(max_length=1024)),
                ('custom', models.CharField(max_length=2048)),
                ('status', models.PositiveSmallIntegerField()),
            ],
            options={
                'db_table': 'resourece_module_archive',
            },
        ),
    ]
