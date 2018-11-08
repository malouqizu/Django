# -*- coding: utf-8 -*-
#记录运行log
import sys
import os
import time
import logging

class MyLogger():
    def __init__(self):
        self.timeNow = time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time()))
        self.log_file_name = os.environ.get('AUTO_JIRA_LOG_FILE', self.timeNow + 'django.log')
        self.file1 = sys.path[0] + '\\log' + "\\" + self.log_file_name

        self.myformatter = logging.Formatter(
            '%(levelname)s:%(asctime)s %(pathname)s %(module)s %(funcName)s %(lineno)d:  %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S')

    def create_logger(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger()
        self.h1 = logging.FileHandler(self.file1)
        self.h1.setFormatter(self.myformatter)
        self.h1.setLevel(logging.DEBUG)
        self.logger.addHandler(self.h1)

        return self.logger

log=MyLogger()
Log=log.create_logger()

if __name__=="__main__":
    Log.info('This is a Logger moudle.')



