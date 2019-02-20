#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
created by: Akrom Khasani | akrom@volantis.io
"""

import logging
import falcon
from conf import config
from ping import Ping
from status import Status

handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s [%(process)d] [%(levelname)s] %(name)s - %(message)s")
handler.setFormatter(formatter)
logger_names = ["ping", "status"]
for name in logger_names:
    logging.getLogger(name).addHandler(handler)
    logging.getLogger(name).setLevel(config.LOGGING_LEVEL)

api = falcon.API()

api.add_route(config.API_PING_PATH, Ping())
api.add_route(config.API_STATUS_PATH, Status())
