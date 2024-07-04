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
from akeyless.models.target_update_eks import TargetUpdateEks  # noqa: E501
from akeyless.rest import ApiException

class TestTargetUpdateEks(unittest.TestCase):
    """TargetUpdateEks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TargetUpdateEks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.target_update_eks.TargetUpdateEks()  # noqa: E501
        if include_optional :
            return TargetUpdateEks(
                description = '0', 
                eks_access_key_id = '0', 
                eks_cluster_ca_cert = '0', 
                eks_cluster_endpoint = '0', 
                eks_cluster_name = '0', 
                eks_region = 'us-east-2', 
                eks_secret_access_key = '0', 
                json = True, 
                keep_prev_version = '0', 
                key = '0', 
                max_versions = '0', 
                name = '0', 
                new_name = '0', 
                token = '0', 
                uid_token = '0', 
                use_gw_cloud_identity = True
            )
        else :
            return TargetUpdateEks(
                eks_access_key_id = '0',
                eks_cluster_ca_cert = '0',
                eks_cluster_endpoint = '0',
                eks_cluster_name = '0',
                eks_secret_access_key = '0',
                name = '0',
        )

    def testTargetUpdateEks(self):
        """Test TargetUpdateEks"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
