#!/usr/bin/env python
# -*- coding:utf-8 -*-
import multiprocessing

try:
    from local_config import Config
except:
    from config import Config


# bind = 'unix:/tmp/gunicorn.sock'
bind = f'{Config.HOST}:{Config.PORT}'
workers = 2 # multiprocessing.cpu_count() * 2 + 1
worker_class = 'gevent'
threads = 2
max_requests = 10000
# chdir = '/home/ixhzq/web/photo_album'
daemon = False
pidfile = '/tmp/gunicorn.pid'
proc_name = 'gunicorn'

loglevel = 'info'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" "%({X-Real-IP}i)s"'
accesslog = "/home/ixhzq/web/photo_album/log/gunicorn/access.log"
errorlog = "/home/ixhzq/web/photo_album/log/gunicorn/error.log"

reload = Config.GUNICORN_RELOAD
