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
from akeyless.models.gateway_create_producer_gcp import GatewayCreateProducerGcp  # noqa: E501
from akeyless.rest import ApiException

class TestGatewayCreateProducerGcp(unittest.TestCase):
    """GatewayCreateProducerGcp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GatewayCreateProducerGcp
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.gateway_create_producer_gcp.GatewayCreateProducerGcp()  # noqa: E501
        if include_optional :
            return GatewayCreateProducerGcp(
                gateway_url = 'http://localhost:8000', 
                gcp_cred_type = '0', 
                gcp_key = '0', 
                gcp_key_algo = '0', 
                gcp_sa_email = '0', 
                gcp_token_scopes = '0', 
                name = '0', 
                producer_encryption_key_name = '0', 
                token = '0', 
                uid_token = '0', 
                user_ttl = '60m'
            )
        else :
            return GatewayCreateProducerGcp(
                gcp_cred_type = '0',
                gcp_sa_email = '0',
                name = '0',
        )

    def testGatewayCreateProducerGcp(self):
        """Test GatewayCreateProducerGcp"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
