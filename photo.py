#!/usr/bin/env python3
#coding=utf-8

import os
import glob
from functools import wraps
from pathlib import Path

from flask import Flask
from flask import Response
from flask import render_template
from flask import jsonify, request
from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension

try:
    from local_config import Config
except:
    from config import Config


__version__ = 0.4
NEED_AUTH = Config.AUTH
BASE_PATH = Config.BASE_PATH
STATIC_URL_PATH = Config.STATIC_URL_PATH
FILE_PATH = Config.PHOTO_FILE_PATH # os.path.join(BASE_PATH, Config.PHOTO_FILE_PATH)
USERNAME_PASSWORD = {
    Config.USERNAME: Config.PASSWORD,
}
HOST = Config.HOST
PORT = Config.PORT


app = Flask(
    __name__,
    static_folder= BASE_PATH.joinpath('static'),
    static_url_path=STATIC_URL_PATH,
    template_folder=BASE_PATH,
    # instance_path="/home/ixhzq/dev/drawing",
    # instance_relative_config=True,
)
app.config["SECRET_KEY"] = Config.SECRET_KEY
app.debug = Config.DEBUG
toolbar = DebugToolbarExtension(app)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})


def basic_auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not NEED_AUTH:
            return f(*args, **kwargs)

        auth = request.authorization
        if not auth or auth.type != 'basic' or not check_auth(auth.username, auth.password):
            return not_authenticated()
        return f(*args, **kwargs)
    return decorated


def check_auth(username, password):
    if username in USERNAME_PASSWORD and USERNAME_PASSWORD.get(username) == password:
        return True
    return False


def not_authenticated():
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials',
        401,
        {
            'WWW-Authenticate': 'Basic realm="Login Required"'
        }
    )


# @app.route('/robots.txt')
# @cache.cached(timeout=3600, key_prefix='view_%s', unless=None)
# def robots():
#     return Response("User-agent: *\nDisallow: /", 200, {"Content-Type": "text/plain"})


@app.route('/')
# @cache.cached(timeout=300, key_prefix='view_%s', unless=None)
@basic_auth_required
def index():
    return render_template("photo.html")


@app.route('/photo/updata', methods=['GET', 'POST'])
def img_up():
    pass


@app.route('/photos')
@basic_auth_required
@cache.cached(timeout=1800, key_prefix='view_%s', unless=None)
def photos():
    paths = ['/'.join(p.split('/')[-3:]) for p in sorted(glob.glob(f"{FILE_PATH}/*"))]
    data = []
    for path in paths:
        data.append(
            {
                "path": path,
                "id": path.split("/")[-1],
                "title_img": search_file(
                    BASE_PATH.joinpath(path),
                    file_types=['[jJ][pP][gG]', '[pP][nN][gG]', 'mp4', 'MP4', 'MOV', 'mov']
                )[0].split("/")[-1] if not os.path.exists(f"{path}/001.jpg") else "001.jpg",
            }
        )
    return jsonify(data)


@app.route('/photo/<string:id>')
@basic_auth_required
@cache.cached(timeout=3600, key_prefix='view_%s', unless=None)
def photo(id):
    return jsonify(
        {
            'img': search_file(
                f"{FILE_PATH}/{id}",
                file_types=['[jJ][pP][gG]', '[pP][nN][gG]', 'mp4', 'MP4', 'MOV', 'mov']
            )
        }
    )


def search_file(path, file_types=('[jJ][pP][gG]', '[pP][nN][gG]')):
    result = []
    for file_type in file_types:
        result.extend(glob.glob(str(path) + r'/*.' + file_type))

    return sorted(['/'.join(r.split('/')[-4:]) for r in result])


#gunicorn photo:app --workers=5 -k gevent --bind=127.0.0.1:5000

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
