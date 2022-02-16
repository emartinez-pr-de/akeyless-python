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
from akeyless.models.gateway_update_producer_github import GatewayUpdateProducerGithub  # noqa: E501
from akeyless.rest import ApiException

class TestGatewayUpdateProducerGithub(unittest.TestCase):
    """GatewayUpdateProducerGithub unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GatewayUpdateProducerGithub
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.gateway_update_producer_github.GatewayUpdateProducerGithub()  # noqa: E501
        if include_optional :
            return GatewayUpdateProducerGithub(
                github_app_id = 56, 
                github_app_private_key = '0', 
                github_base_url = '0', 
                installation_id = 56, 
                installation_repository = '0', 
                name = '0', 
                new_name = '0', 
                password = '0', 
                target_name = '0', 
                token = '0', 
                token_permissions = [
                    '0'
                    ], 
                token_repositories = [
                    '0'
                    ], 
                uid_token = '0', 
                username = '0'
            )
        else :
            return GatewayUpdateProducerGithub(
                name = '0',
        )

    def testGatewayUpdateProducerGithub(self):
        """Test GatewayUpdateProducerGithub"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
