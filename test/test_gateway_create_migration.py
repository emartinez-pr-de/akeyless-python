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
from akeyless.models.gateway_create_migration import GatewayCreateMigration  # noqa: E501
from akeyless.rest import ApiException

class TestGatewayCreateMigration(unittest.TestCase):
    """GatewayCreateMigration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GatewayCreateMigration
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.gateway_create_migration.GatewayCreateMigration()  # noqa: E501
        if include_optional :
            return GatewayCreateMigration(
                aws_key = '0', 
                aws_key_id = '0', 
                aws_region = '0', 
                azure_client_id = '0', 
                azure_kv_name = '0', 
                azure_secret = '0', 
                azure_tenant_id = '0', 
                hashi_json = '0', 
                hashi_ns = [
                    '0'
                    ], 
                hashi_token = '0', 
                hashi_url = '0', 
                name = '0', 
                protection_key = '0', 
                target_location = '0', 
                token = '0', 
                type = '0', 
                uid_token = '0'
            )
        else :
            return GatewayCreateMigration(
                name = '0',
        )

    def testGatewayCreateMigration(self):
        """Test GatewayCreateMigration"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
