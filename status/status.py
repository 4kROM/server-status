#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
created by: Akrom Khasani | akrom@volantis.io
"""

from logging import Logger, getLogger
from falcon import Request, Response
import falcon
import json
from psutil import cpu_count, cpu_percent, virtual_memory, disk_usage

__all__ = ["Status"]

null_logger = getLogger(__name__)
null_logger.disabled = True


class Status(object):

    def __init__(self, logger: Logger = null_logger):
        self.logger = logger

    def on_get(self, request: Request, response: Response, **params):
        self.logger.debug("Receiving a GET request from '{user_agent}' on '{class_name}' in '{file_name}'".format(
            user_agent=request.get_header("user-agent"),
            class_name=self.__class__.__name__,
            file_name=__name__
        ))

        response.body = json.dumps({
            "cpu": {
                "count": cpu_count(),
                "percent": cpu_percent(percpu=True)
            },
            "memory": virtual_memory()._asdict(),
            "disk": disk_usage("/")._asdict()
        })
        response.content_type = falcon.MEDIA_JSON
        response.status = falcon.HTTP_OK
