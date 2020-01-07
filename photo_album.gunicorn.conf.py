#!/usr/bin/env python
# -*- coding:utf-8 -*-
try:
    from local_config import Config
except:
    from config import Config


# bind = 'unix:/tmp/gunicorn.sock'
bind = f'[{Config.HOST}]:{Config.PORT}'
workers = Config.WORKERS
worker_class = 'gevent'
threads = 2
max_requests = 10000
chdir = str(Config.BASE_PATH)
daemon = False
pidfile = '/tmp/gunicorn.pid'
proc_name = 'gunicorn'

loglevel = Config.LOGLEVEL
access_log_format = Config.ACCESS_LOG_FORMAT
accesslog = str(Config.ACCESSLOG)
errorlog = str(Config.ERRORLOG)

reload = Config.GUNICORN_RELOAD
