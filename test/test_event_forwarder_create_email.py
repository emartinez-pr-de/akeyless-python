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
from akeyless.models.event_forwarder_create_email import EventForwarderCreateEmail  # noqa: E501
from akeyless.rest import ApiException

class TestEventForwarderCreateEmail(unittest.TestCase):
    """EventForwarderCreateEmail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EventForwarderCreateEmail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.event_forwarder_create_email.EventForwarderCreateEmail()  # noqa: E501
        if include_optional :
            return EventForwarderCreateEmail(
                auth_methods_event_source_locations = [
                    '0'
                    ], 
                description = '0', 
                email_to = '0', 
                event_types = [
                    '0'
                    ], 
                every = '0', 
                gateways_event_source_locations = [
                    '0'
                    ], 
                items_event_source_locations = [
                    '0'
                    ], 
                json = True, 
                key = '0', 
                name = '0', 
                runner_type = '0', 
                targets_event_source_locations = [
                    '0'
                    ], 
                token = '0', 
                uid_token = '0'
            )
        else :
            return EventForwarderCreateEmail(
                gateways_event_source_locations = [
                    '0'
                    ],
                name = '0',
                runner_type = '0',
        )

    def testEventForwarderCreateEmail(self):
        """Test EventForwarderCreateEmail"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()