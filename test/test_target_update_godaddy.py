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
from akeyless.models.target_update_godaddy import TargetUpdateGodaddy  # noqa: E501
from akeyless.rest import ApiException

class TestTargetUpdateGodaddy(unittest.TestCase):
    """TargetUpdateGodaddy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TargetUpdateGodaddy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.target_update_godaddy.TargetUpdateGodaddy()  # noqa: E501
        if include_optional :
            return TargetUpdateGodaddy(
                api_key = '0', 
                description = '0', 
                imap_fqdn = '0', 
                imap_password = '0', 
                imap_port = '993', 
                imap_username = '0', 
                json = True, 
                keep_prev_version = '0', 
                key = '0', 
                max_versions = '0', 
                name = '0', 
                new_name = '0', 
                secret = '0', 
                timeout = '5m', 
                token = '0', 
                uid_token = '0'
            )
        else :
            return TargetUpdateGodaddy(
                api_key = '0',
                imap_fqdn = '0',
                imap_password = '0',
                imap_username = '0',
                name = '0',
                secret = '0',
        )

    def testTargetUpdateGodaddy(self):
        """Test TargetUpdateGodaddy"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
