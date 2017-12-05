# coding=utf-8
import os
import logging

from tornado.options import options, define

from common import constants

logger = logging.getLogger(__name__)


def run_web_app_by_gunicorn():
    define(name='port', default=8000, type=int, help='run on the given port')
    logger.info('\n================ spider web server(require gunicorn and gevent) has started ================ ')
    logger.info('                       server start at port -> {}, debug mode = {} '.format(options.port,
                                                                                             constants.DEBUG))
    os.system(
        "env/bin/gunicorn 'app.web_app:make_wsgi_app()' -b 0.0.0.0:{port} -w 1 -k gevent".format(
            port=options.port
        )
    )


def run_celery_jobs_count_worker():
    os.system(
        u'env/bin/celery worker -A app.tasks.celery_app -n jobs_count_worker '
        u'--loglevel=debug -Q jobs_count --concurrency=1')


def run_celery_lagou_data_worker():
    os.system(
        u'env/bin/celery worker -A app.tasks.celery_app -n lagou_data_worker '
        u'--loglevel=debug -Q lagou_data --concurrency=1')


def run_celery_beat():
    os.system(u'env/bin/celery -A app.tasks.celery_app beat --loglevel=debug')


def run_celery_flower():
    os.system(u'env/bin/celery flower --broker=redis://localhost:6379/0 --broker_api=redis://localhost:6379/0')
