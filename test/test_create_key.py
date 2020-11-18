# coding: utf-8

"""
    Akeyless API

    The purpose of this application is to provide access to Akeyless API.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: support@akeyless.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import akeyless
from akeyless.models.create_key import CreateKey  # noqa: E501
from akeyless.rest import ApiException

class TestCreateKey(unittest.TestCase):
    """CreateKey unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateKey
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.create_key.CreateKey()  # noqa: E501
        if include_optional :
            return CreateKey(
                alg = '0', 
                customer_frg_id = '0', 
                metadata = '0', 
                name = '0', 
                split_level = 56, 
                tag = [
                    '0'
                    ], 
                token = '0', 
                uid_token = '0'
            )
        else :
            return CreateKey(
                alg = '0',
                name = '0',
        )

    def testCreateKey(self):
        """Test CreateKey"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
