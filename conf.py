#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
created by: Akrom Khasani | akrom@volantis.io
"""

from os import getenv
from easydict import EasyDict

__all__ = ["config"]

config = EasyDict({

    "LOGGING": {
        "LEVEL": getenv("LOGGING_LEVEL", "DEBUG"),
        "FORMAT": getenv("LOGGING_FORMAT", "%(asctime)s [%(process)d] [%(levelname)s] %(name)s - %(message)s")
    },


    "GUNICORN": {
        "LOGGING_LEVEL": getenv("GUNICORN_LOGGING_LEVEL", "INFO"),
        "PORT": int(getenv("GUNICORN_PORT", "8000")),
        "THREADS": int(getenv("GUNICORN_THREADS", "2")),
        "WORKERS": int(getenv("GUNICORN_WORKERS", "1")),
        "WORKER_CLASS": getenv("GUNICORN_WORKER_CLASS", "meinheld.gmeinheld.MeinheldWorker"),
    }

})
