#!/usr/bin/env bash

#配置参数
project_port=8000

#项目路径
script_path=$(cd `dirname $0`; pwd)
project_path=$(cd $script_path; cd ..; pwd)
echo "projectpath is:"$project_path

#环境变量
export PYTHONPATH="$PYTHONPATH:$project_path"
export DJANGO_SETTINGS_MODULE="django_env.settings"
echo "pythonpath is:"$PYTHONPATH
echo "configuration is:"$DJANGO_SETTINGS_MODULE

#启动django
sleep 1
sudo netstat -npl | grep $project_port | awk '{print $7}' | awk -F'/' '{print $1}' | xargs kill -9
cd $project_path
python -u manage.py runserver 10.26.27.133:$project_port
