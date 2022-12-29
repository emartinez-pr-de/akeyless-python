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
from akeyless.models.create_event_forwarder import CreateEventForwarder  # noqa: E501
from akeyless.rest import ApiException

class TestCreateEventForwarder(unittest.TestCase):
    """CreateEventForwarder unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateEventForwarder
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.create_event_forwarder.CreateEventForwarder()  # noqa: E501
        if include_optional :
            return CreateEventForwarder(
                admin_name = '0', 
                admin_pwd = '0', 
                comment = '0', 
                email_to = '0', 
                event_source_locations = [
                    '0'
                    ], 
                event_source_type = 'item', 
                event_types = [
                    '0'
                    ], 
                every = '0', 
                forwarder_type = '0', 
                host = '0', 
                json = True, 
                key = '0', 
                name = '0', 
                runner_type = '0', 
                token = '0', 
                uid_token = '0'
            )
        else :
            return CreateEventForwarder(
                event_source_locations = [
                    '0'
                    ],
                forwarder_type = '0',
                name = '0',
                runner_type = '0',
        )

    def testCreateEventForwarder(self):
        """Test CreateEventForwarder"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
