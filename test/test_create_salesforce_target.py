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
from akeyless.models.create_salesforce_target import CreateSalesforceTarget  # noqa: E501
from akeyless.rest import ApiException

class TestCreateSalesforceTarget(unittest.TestCase):
    """CreateSalesforceTarget unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateSalesforceTarget
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.create_salesforce_target.CreateSalesforceTarget()  # noqa: E501
        if include_optional :
            return CreateSalesforceTarget(
                ca_cert_data = '0', 
                ca_cert_name = '0', 
                client_id = '0', 
                client_secret = '0', 
                comment = '0', 
                email = '0', 
                key = '0', 
                name = '0', 
                password = '0', 
                security_token = '0', 
                tenant_url = '0', 
                token = '0', 
                uid_token = '0'
            )
        else :
            return CreateSalesforceTarget(
                client_id = '0',
                client_secret = '0',
                email = '0',
                name = '0',
                password = '0',
                security_token = '0',
                tenant_url = '0',
        )

    def testCreateSalesforceTarget(self):
        """Test CreateSalesforceTarget"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
