import multiprocessing
from pathlib import Path


class Config:
    DEBUG = True
    AUTH = True
    PORT = 3333
    HOST = "::1" # "::0"
    GUNICORN_RELOAD = True
    USERNAME = "username"
    PASSWORD = "password"
    BASE_PATH = Path(__file__).parent
    PHOTO_FILE_PATH = BASE_PATH.joinpath('static/photo')
    STATIC_URL_PATH = '/static'
    SECRET_KEY = "adafaferqe-faed341adsfJdFds你哈发！！！"
    WORKERS = multiprocessing.cpu_count() * 2 + 1
    LOGLEVEL = 'info'
    ACCESS_LOG_FORMAT = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" "%({X-Real-IP}i)s"'
    ACCESSLOG = BASE_PATH.joinpath("log/gunicorn/access.log")
    ERRORLOG = BASE_PATH.joinpath("log/gunicorn/error.log")
