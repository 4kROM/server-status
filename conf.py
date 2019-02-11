#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
created by: Akrom Khasani | akrom@volantis.io
"""

from os import getenv
from json import loads
from easydict import EasyDict

__all__ = ["config"]

config = EasyDict({

    "LOGGING_LEVEL": getenv("LOGGING_LEVEL", "DEBUG"),

    "GUNICORN_PORT": int(getenv("GUNICORN_PORT", "8000")),
    "GUNICORN_WORKERS": int(getenv("GUNICORN_WORKERS", "1")),
    "GUNICORN_WORKER_CLASS": getenv("GUNICORN_WORKER_CLASS", "meinheld.gmeinheld.MeinheldWorker")

})
