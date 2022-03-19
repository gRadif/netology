command = '/app/env/bin/gunicorn'
pythonpath = '/app/stocks_products'
bind = '0.0.0.0:8000'
workers = 3
user = 'root'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=stocks_products.settings'
