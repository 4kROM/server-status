#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
created by: Akrom Khasani | akrom@volantis.io
"""

import unittest
from webtest import TestApp
import falcon
from conf import config
from ping import Ping


class PingTestCase(unittest.TestCase):

    def setUp(self):

        api = falcon.API()
        api.add_route(config.API_PING_PATH, Ping())

        self.app = TestApp(api)


class TestPing(PingTestCase):

    def test_get(self):

        result_message = {
            "title": falcon.HTTP_OK,
            "description": "This server is up and running."
        }

        result = self.app.get(config.API_PING_PATH)

        self.assertEqual(result.status, falcon.HTTP_OK)
        self.assertEqual(result.json, result_message)


if __name__ == "__main__":
    unittest.main()
