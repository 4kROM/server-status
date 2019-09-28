#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
created by: Akrom Khasani | akrom@volantis.io
"""

import logging
import datetime

__all__ = ["Formatter"]


class Formatter(logging.Formatter):

    subsecond_digits = 3
    timezone = datetime.datetime.now(tz=datetime.timezone.utc).astimezone().tzinfo

    def converter(self, t):
        return datetime.datetime.fromtimestamp(round(t, self.subsecond_digits), tz=datetime.timezone.utc)

    def formatTime(self, record, datefmt=None):
        ct = self.converter(record.created)
        if datefmt:
            s = ct.strftime(datefmt)
        else:
            t = ct.astimezone(self.timezone).strftime("%Y-%m-%d %H:%M:%S.%f%z")
            s = t[:-11 + self.subsecond_digits] + t[-5:]
        return s
