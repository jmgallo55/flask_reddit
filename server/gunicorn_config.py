# Refer to the following link for help:
# http://docs.gunicorn.org/en/latest/settings.html
command = '/srv/reddit-env/bin/gunicorn'
pythonpath = '/srv/reddit-env/flask_reddit'
bind = '127.0.0.1:8040'
workers = 1
user = 'ec2-user'
accesslog = '/srv/gunicorn-access.log'
errorlog = '/srv/gunicorn-error.log'
