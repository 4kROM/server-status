#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
created by: Akrom Khasani | akrom@volantis.io
"""

import conf

reload = True
bind = "0.0.0.0:{port}".format(port=conf.config.GUNICORN_PORT)

workers = conf.config.GUNICORN_WORKERS
worker_class = conf.config.GUNICORN_WORKER_CLASS
