#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
created by: Akrom Khasani | akrom@volantis.io
"""

from logging import Logger, getLogger
from falcon import Request, Response
import falcon
import json

__all__ = ["Ping"]

null_logger = getLogger(__name__)
null_logger.disabled = True


class Ping(object):

    def __init__(self, logger: Logger = null_logger):
        self.logger = logger

    def on_get(self, request: Request, response: Response, **params):
        self.logger.debug("Receiving a GET request from '{user_agent}' on '{class_name}' in '{file_name}'".format(
            user_agent=request.get_header("user-agent"),
            class_name=self.__class__.__name__,
            file_name=__name__
        ))

        response.body = json.dumps({
            "title": falcon.HTTP_OK,
            "description": "This server is up and running."
        })
        response.content_type = falcon.MEDIA_JSON
        response.status = falcon.HTTP_OK
