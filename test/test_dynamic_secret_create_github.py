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
from akeyless.models.dynamic_secret_create_github import DynamicSecretCreateGithub  # noqa: E501
from akeyless.rest import ApiException

class TestDynamicSecretCreateGithub(unittest.TestCase):
    """DynamicSecretCreateGithub unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DynamicSecretCreateGithub
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.dynamic_secret_create_github.DynamicSecretCreateGithub()  # noqa: E501
        if include_optional :
            return DynamicSecretCreateGithub(
                delete_protection = '0', 
                description = '0', 
                github_app_id = 56, 
                github_app_private_key = '0', 
                github_base_url = 'https://api.github.com/', 
                installation_id = 56, 
                installation_organization = '0', 
                installation_repository = '0', 
                json = True, 
                name = '0', 
                tags = [
                    '0'
                    ], 
                target_name = '0', 
                token = '0', 
                token_permissions = [
                    '0'
                    ], 
                token_repositories = [
                    '0'
                    ], 
                uid_token = '0'
            )
        else :
            return DynamicSecretCreateGithub(
                name = '0',
        )

    def testDynamicSecretCreateGithub(self):
        """Test DynamicSecretCreateGithub"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
