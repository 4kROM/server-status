#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
created by: Akrom Khasani | akrom@volantis.io
"""

from falcon import testing
import falcon

from os.path import dirname, join, abspath
import sys
sys.path.insert(0, abspath(join(dirname(__file__), "..", "..")))

from conf import config
from ping import Ping


class MyTestCase(testing.TestCase):

    def setUp(self):
        super(MyTestCase, self).setUp()

        # Assume the hypothetical `myapp` package has a
        # function called `create()` to initialize and
        # return a `falcon.API` instance.
        # self.app = myapp.create()

        api = falcon.API()
        api.add_route(config.API_PING_PATH, Ping())

        self.app = api


class TestPing(MyTestCase):

    def test_get(self):

        result_message = {
            "title": falcon.HTTP_OK,
            "description": "This server is up and running."
        }

        result = self.simulate_get(config.API_PING_PATH)

        self.assertEqual(result.json, result_message)
