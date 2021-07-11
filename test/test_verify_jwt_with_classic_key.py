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
from akeyless.models.verify_jwt_with_classic_key import VerifyJWTWithClassicKey  # noqa: E501
from akeyless.rest import ApiException

class TestVerifyJWTWithClassicKey(unittest.TestCase):
    """VerifyJWTWithClassicKey unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VerifyJWTWithClassicKey
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.verify_jwt_with_classic_key.VerifyJWTWithClassicKey()  # noqa: E501
        if include_optional :
            return VerifyJWTWithClassicKey(
                display_id = '0', 
                jwt_claims = '0', 
                password = '0', 
                signature = '0', 
                token = '0', 
                uid_token = '0', 
                username = '0', 
                version = 56
            )
        else :
            return VerifyJWTWithClassicKey(
                display_id = '0',
                jwt_claims = '0',
                signature = '0',
                version = 56,
        )

    def testVerifyJWTWithClassicKey(self):
        """Test VerifyJWTWithClassicKey"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
