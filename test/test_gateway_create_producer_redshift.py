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
from akeyless.models.gateway_create_producer_redshift import GatewayCreateProducerRedshift  # noqa: E501
from akeyless.rest import ApiException

class TestGatewayCreateProducerRedshift(unittest.TestCase):
    """GatewayCreateProducerRedshift unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GatewayCreateProducerRedshift
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.gateway_create_producer_redshift.GatewayCreateProducerRedshift()  # noqa: E501
        if include_optional :
            return GatewayCreateProducerRedshift(
                creation_statements = '0', 
                name = '0', 
                password = '0', 
                producer_encryption_key = '0', 
                redshift_db_name = '0', 
                redshift_host = '127.0.0.1', 
                redshift_password = '0', 
                redshift_port = '5439', 
                redshift_username = '0', 
                target_name = '0', 
                token = '0', 
                uid_token = '0', 
                user_ttl = '60m', 
                username = '0'
            )
        else :
            return GatewayCreateProducerRedshift(
                name = '0',
        )

    def testGatewayCreateProducerRedshift(self):
        """Test GatewayCreateProducerRedshift"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
