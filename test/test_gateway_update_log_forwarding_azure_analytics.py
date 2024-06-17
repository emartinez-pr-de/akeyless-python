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
from akeyless.models.gateway_update_log_forwarding_azure_analytics import GatewayUpdateLogForwardingAzureAnalytics  # noqa: E501
from akeyless.rest import ApiException

class TestGatewayUpdateLogForwardingAzureAnalytics(unittest.TestCase):
    """GatewayUpdateLogForwardingAzureAnalytics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GatewayUpdateLogForwardingAzureAnalytics
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.gateway_update_log_forwarding_azure_analytics.GatewayUpdateLogForwardingAzureAnalytics()  # noqa: E501
        if include_optional :
            return GatewayUpdateLogForwardingAzureAnalytics(
                enable = 'true', 
                json = True, 
                output_format = 'text', 
                pull_interval = '10', 
                token = '0', 
                uid_token = '0', 
                workspace_id = '0', 
                workspace_key = '0'
            )
        else :
            return GatewayUpdateLogForwardingAzureAnalytics(
        )

    def testGatewayUpdateLogForwardingAzureAnalytics(self):
        """Test GatewayUpdateLogForwardingAzureAnalytics"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
