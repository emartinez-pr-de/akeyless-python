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
from akeyless.models.gateway_create_producer_custom import GatewayCreateProducerCustom  # noqa: E501
from akeyless.rest import ApiException

class TestGatewayCreateProducerCustom(unittest.TestCase):
    """GatewayCreateProducerCustom unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GatewayCreateProducerCustom
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.gateway_create_producer_custom.GatewayCreateProducerCustom()  # noqa: E501
        if include_optional :
            return GatewayCreateProducerCustom(
                create_sync_url = '0', 
                gateway_url = 'http://localhost:8000', 
                name = '0', 
                payload = '0', 
                producer_encryption_key_name = '0', 
                revoke_sync_url = '0', 
                rotate_sync_url = '0', 
                timeout_sec = 56, 
                token = '0', 
                uid_token = '0', 
                user_ttl = '60m'
            )
        else :
            return GatewayCreateProducerCustom(
                create_sync_url = '0',
                name = '0',
                revoke_sync_url = '0',
        )

    def testGatewayCreateProducerCustom(self):
        """Test GatewayCreateProducerCustom"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
