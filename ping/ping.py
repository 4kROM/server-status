#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
created by: Akrom Khasani | akrom@volantis.io
"""

import logging
import falcon
from falcon import Request, Response

__all__ = ["Ping"]
logger = logging.getLogger(__name__)


class Ping(object):

    def __init__(self, *args, **kwargs):
        pass

    def on_get(self, request: Request, response: Response):
        logger.debug("Receiving a GET request from '{user_agent}'".format(
            user_agent=request.get_header("user-agent")
        ))
        response.status = falcon.HTTP_OK
