#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
created by: Akrom Khasani | akrom@volantis.io
"""

import logging
from falcon import Request, Response
import falcon
import json
import psutil

__all__ = ["Status"]

logger = logging.getLogger(__name__)


class Status(object):

    def __init__(self, *args, **kwargs):
        pass

    def on_get(self, request: Request, response: Response):
        logger.debug("Receiving a GET request from '{user_agent}' on '{class_name}'".format(
            user_agent=request.get_header("user-agent"),
            class_name=self.__class__.__name__
        ))

        response.body = json.dumps({
            "cpu": {
                "count": psutil.cpu_count(),
                "percent": psutil.cpu_percent(percpu=True)
            },
            "memory": psutil.virtual_memory()._asdict(),
            "disk": psutil.disk_usage("/")._asdict()
        })
        response.content_type = falcon.MEDIA_JSON
        response.status = falcon.HTTP_OK
