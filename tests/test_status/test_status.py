#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
created by: Akrom Khasani | akrom@volantis.io
"""

import unittest
from webtest import TestApp
import falcon
from conf import config
from status import Status
from typing import Dict


class StatusTestCase(unittest.TestCase):

    def setUp(self):

        api = falcon.API()
        api.add_route(config.API_STATUS_PATH, Status())

        self.app = TestApp(api)


class TestStatus(StatusTestCase):

    def test_get(self):

        result = self.app.get(config.API_STATUS_PATH)

        self.assertEqual(result.status, falcon.HTTP_OK)
        self.assertIsInstance(result.json, Dict)


if __name__ == "__main__":
    unittest.main()
