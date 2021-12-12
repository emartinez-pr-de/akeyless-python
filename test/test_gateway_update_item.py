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
from akeyless.models.gateway_update_item import GatewayUpdateItem  # noqa: E501
from akeyless.rest import ApiException

class TestGatewayUpdateItem(unittest.TestCase):
    """GatewayUpdateItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GatewayUpdateItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.gateway_update_item.GatewayUpdateItem()  # noqa: E501
        if include_optional :
            return GatewayUpdateItem(
                add_tag = [
                    '0'
                    ], 
                api_id = '0', 
                api_key = '0', 
                auto_rotate = '0', 
                custom_payload = '0', 
                key = '0', 
                name = '0', 
                new_metadata = 'default_metadata', 
                new_name = '0', 
                new_version = True, 
                password = '0', 
                rm_tag = [
                    '0'
                    ], 
                rotated_password = '0', 
                rotated_username = '0', 
                rotation_hour = 56, 
                rotation_interval = '0', 
                rotator_creds_type = '0', 
                token = '0', 
                type = '0', 
                uid_token = '0', 
                username = '0'
            )
        else :
            return GatewayUpdateItem(
                name = '0',
                type = '0',
        )

    def testGatewayUpdateItem(self):
        """Test GatewayUpdateItem"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
