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
from status import Status


class MyTestCase(testing.TestCase):

    def setUp(self):
        super(MyTestCase, self).setUp()

        # Assume the hypothetical `myapp` package has a
        # function called `create()` to initialize and
        # return a `falcon.API` instance.
        # self.app = myapp.create()

        api = falcon.API()
        api.add_route(config.API_STATUS_PATH, Status())

        self.app = api


class TestStatus(MyTestCase):

    def test_get(self):

        result_status = falcon.HTTP_OK

        result = self.simulate_get(config.API_STATUS_PATH)

        self.assertEqual(result.status, result_status)
