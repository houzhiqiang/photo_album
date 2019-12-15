# photo_album
album/相册

- 测试

    ```
    git clone https://github.com/houzhiqiang/photo_album.git
    cd photo_album
    cp config.py local_config.py
    python3 -m venv venv
    source venv/bin/activate
    pip install -U -r requirements.txt
    ```

    编辑 `local_config.py`
    修改配置

    运行测试
    ```shell
    python photo.py
    ```

- 运行:

    编辑photo_album.gunicorn.conf.py文件
    修改配置

    -D 参数放到后台运行

    ```shell
    gunicorn -c photo_album.gunicorn.conf.py photo:app -D
    ```
