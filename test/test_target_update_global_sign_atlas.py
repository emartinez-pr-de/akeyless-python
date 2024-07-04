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
from akeyless.models.target_update_global_sign_atlas import TargetUpdateGlobalSignAtlas  # noqa: E501
from akeyless.rest import ApiException

class TestTargetUpdateGlobalSignAtlas(unittest.TestCase):
    """TargetUpdateGlobalSignAtlas unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TargetUpdateGlobalSignAtlas
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.target_update_global_sign_atlas.TargetUpdateGlobalSignAtlas()  # noqa: E501
        if include_optional :
            return TargetUpdateGlobalSignAtlas(
                api_key = '0', 
                api_secret = '0', 
                description = '0', 
                json = True, 
                keep_prev_version = '0', 
                key = '0', 
                max_versions = '0', 
                mtls_cert_data_base64 = '0', 
                mtls_key_data_base64 = '0', 
                name = '0', 
                new_name = '0', 
                timeout = '5m', 
                token = '0', 
                uid_token = '0'
            )
        else :
            return TargetUpdateGlobalSignAtlas(
                api_key = '0',
                api_secret = '0',
                name = '0',
        )

    def testTargetUpdateGlobalSignAtlas(self):
        """Test TargetUpdateGlobalSignAtlas"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
