#!/bin/bash
sourse /home/rgham/docker_django/env/bin/activate
exec gunicorn -c "/home/rgham/docker_django/gunicorn_config.py"stocks_products.wsgi

