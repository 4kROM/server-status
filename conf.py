#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
created by: Akrom Khasani | akrom@volantis.io
"""

from os import getenv
from easydict import EasyDict

__all__ = ["config"]

config = EasyDict({

    "LOGGING_LEVEL": getenv("LOGGING_LEVEL", "WARN"),

    "GUNICORN_PORT": int(getenv("GUNICORN_PORT", "8000")),
    "GUNICORN_WORKERS": int(getenv("GUNICORN_WORKERS", "1")),
    "GUNICORN_WORKER_CLASS": getenv("GUNICORN_WORKER_CLASS", "meinheld.gmeinheld.MeinheldWorker"),

    "API_PING_PATH": getenv("API_PING_PATH", "/ping"),
    "API_STATUS_PATH": getenv("API_STATUS_PATH", "/_status")

})
