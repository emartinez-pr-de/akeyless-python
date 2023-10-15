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
from akeyless.models.create_user_event import CreateUserEvent  # noqa: E501
from akeyless.rest import ApiException

class TestCreateUserEvent(unittest.TestCase):
    """CreateUserEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateUserEvent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.create_user_event.CreateUserEvent()  # noqa: E501
        if include_optional :
            return CreateUserEvent(
                capabilities = [
                    '0'
                    ], 
                comment = '0', 
                description = '0', 
                event_source = '0', 
                event_type = '0', 
                item_name = '0', 
                item_type = '0', 
                json = True, 
                request_access_ttl = 56, 
                token = '0', 
                uid_token = '0'
            )
        else :
            return CreateUserEvent(
                event_type = '0',
                item_name = '0',
                item_type = '0',
        )

    def testCreateUserEvent(self):
        """Test CreateUserEvent"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()