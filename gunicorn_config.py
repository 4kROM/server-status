#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
created by: Akrom Khasani | akrom@volantis.io
"""

import gunicorn.glogging
import conf
from logging_formatter import Formatter


class GunicornLogger(gunicorn.glogging.Logger):

    def _set_handler(self, log, output, fmt, stream=None):
        super()._set_handler(
            log=log,
            output=output,
            fmt=Formatter("%(asctime)s [%(process)d] [%(levelname)s] %(message)s"),
            stream=stream
        )


logger_class = GunicornLogger
loglevel = conf.config.GUNICORN.LOGGING_LEVEL

accesslog = None
access_log_format = "%(h)s %(r)s %(s)s %(b)s %(f)s %(a)s"

reload = True
bind = "0.0.0.0:{}".format(conf.config.GUNICORN.PORT)

threads = conf.config.GUNICORN.THREADS
workers = conf.config.GUNICORN.WORKERS
worker_class = conf.config.GUNICORN.WORKER_CLASS
