#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
created by: Akrom Khasani | akrom@volantis.io
"""

import logging
import falcon
from ping import Ping
from status import Status
from conf import config

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter("[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(config.LOGGING_LEVEL)

api = falcon.API()

api.add_route(config.API_PING_PATH, Ping())
api.add_route(config.API_STATUS_PATH, Status())
