#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
created by: Akrom Khasani | akrom@volantis.io
"""

import unittest
import falcon
from webtest import TestApp
from ping import Ping


class TestPing(unittest.TestCase):

    def setUp(self):
        api = falcon.API()
        api.add_route("/ping", Ping())
        self.app = TestApp(api)

    def test_get(self):
        response = self.app.get("/ping")
        self.assertEqual(response.status, falcon.HTTP_OK)


if __name__ == "__main__":
    unittest.main()
