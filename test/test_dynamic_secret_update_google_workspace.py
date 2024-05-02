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
from akeyless.models.dynamic_secret_update_google_workspace import DynamicSecretUpdateGoogleWorkspace  # noqa: E501
from akeyless.rest import ApiException

class TestDynamicSecretUpdateGoogleWorkspace(unittest.TestCase):
    """DynamicSecretUpdateGoogleWorkspace unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DynamicSecretUpdateGoogleWorkspace
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.dynamic_secret_update_google_workspace.DynamicSecretUpdateGoogleWorkspace()  # noqa: E501
        if include_optional :
            return DynamicSecretUpdateGoogleWorkspace(
                access_mode = '0', 
                admin_name = '0', 
                delete_protection = '0', 
                description = '0', 
                gcp_key = '0', 
                group_name = '0', 
                group_role_type = '0', 
                json = True, 
                name = '0', 
                new_name = '0', 
                producer_encryption_key_name = '0', 
                role_name = '0', 
                role_scope = '0', 
                tags = [
                    '0'
                    ], 
                target_name = '0', 
                token = '0', 
                uid_token = '0', 
                user_ttl = '60m'
            )
        else :
            return DynamicSecretUpdateGoogleWorkspace(
                access_mode = '0',
                admin_name = '0',
                name = '0',
        )

    def testDynamicSecretUpdateGoogleWorkspace(self):
        """Test DynamicSecretUpdateGoogleWorkspace"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()