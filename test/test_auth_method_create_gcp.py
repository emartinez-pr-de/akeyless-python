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
from akeyless.models.auth_method_create_gcp import AuthMethodCreateGcp  # noqa: E501
from akeyless.rest import ApiException

class TestAuthMethodCreateGcp(unittest.TestCase):
    """AuthMethodCreateGcp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AuthMethodCreateGcp
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.auth_method_create_gcp.AuthMethodCreateGcp()  # noqa: E501
        if include_optional :
            return AuthMethodCreateGcp(
                access_expires = 56, 
                audience = 'akeyless.io', 
                audit_logs_claims = [
                    '0'
                    ], 
                bound_ips = [
                    '0'
                    ], 
                bound_labels = [
                    '0'
                    ], 
                bound_projects = [
                    '0'
                    ], 
                bound_regions = [
                    '0'
                    ], 
                bound_service_accounts = [
                    '0'
                    ], 
                bound_zones = [
                    '0'
                    ], 
                description = '0', 
                force_sub_claims = True, 
                gw_bound_ips = [
                    '0'
                    ], 
                json = True, 
                jwt_ttl = 56, 
                name = '0', 
                product_type = [
                    '0'
                    ], 
                service_account_creds_data = '0', 
                token = '0', 
                type = '0', 
                uid_token = '0'
            )
        else :
            return AuthMethodCreateGcp(
                audience = 'akeyless.io',
                name = '0',
                type = '0',
        )

    def testAuthMethodCreateGcp(self):
        """Test AuthMethodCreateGcp"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
