from pathlib import Path


class Config:
    DEBUG = True
    AUTH = True
    PORT = 3333
    HOST = "::1" # "::0"
    GUNICORN_RELOAD = True
    USERNAME = "username"
    PASSWORD = "password"
    BASE_PATH = Path(__file__).parent # f"{'/'.join(__file__.split('/')[0: -1])}"
    PHOTO_FILE_PATH = BASE_PATH.joinpath('static/photo')
    STATIC_URL_PATH = '/static'
    SECRET_KEY = "adafaferqe-faed341adsfJdFds你哈发！！！"
