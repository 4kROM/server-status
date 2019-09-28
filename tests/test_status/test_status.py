#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
created by: Akrom Khasani | akrom@volantis.io
"""

import unittest
import falcon
import typing
from webtest import TestApp
from status import Status


class TestStatus(unittest.TestCase):

    def setUp(self):
        application = falcon.API()
        status = Status()
        application.add_route("/_status", status)
        self.app = TestApp(application)

    def test_get(self):
        response = self.app.get("/_status")
        self.assertEqual(response.status, falcon.HTTP_OK)
        self.assertIsInstance(response.json, typing.Dict)


if __name__ == "__main__":
    unittest.main()
