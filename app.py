#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
created by: Akrom Khasani | akrom@volantis.io
"""

import sys
import logging
import falcon
from conf import config
from logging_formatter import Formatter
from ping import Ping
from status import Status

logger_names = [__name__, "ping", "status"]
formatter = Formatter(config.LOGGING.FORMAT)

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)

for name in logger_names:
    logging.getLogger(name).addHandler(handler)
    logging.getLogger(name).setLevel(config.LOGGING.LEVEL)

logger = logging.getLogger(__name__)

application = falcon.API()

ping = Ping()
application.add_route("/ping", ping)
logger.info("route added: '/ping'")

status = Status()
application.add_route("/_status", status)
logger.info("route added: '/_status'")
