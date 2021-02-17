# coding: utf-8

"""
    Akeyless API

    The purpose of this application is to provide access to Akeyless API.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Contact: support@akeyless.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import akeyless
from akeyless.models.cache_config_part import CacheConfigPart  # noqa: E501
from akeyless.rest import ApiException

class TestCacheConfigPart(unittest.TestCase):
    """CacheConfigPart unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CacheConfigPart
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.cache_config_part.CacheConfigPart()  # noqa: E501
        if include_optional :
            return CacheConfigPart(
                cache_enable = True, 
                cache_ttl = '0', 
                proactive_cache_dump_interval = '0', 
                proactive_cache_enable = True, 
                proactive_cache_minimum_fetching_time = '0'
            )
        else :
            return CacheConfigPart(
        )

    def testCacheConfigPart(self):
        """Test CacheConfigPart"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
