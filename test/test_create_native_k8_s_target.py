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
from akeyless.models.create_native_k8_s_target import CreateNativeK8STarget  # noqa: E501
from akeyless.rest import ApiException

class TestCreateNativeK8STarget(unittest.TestCase):
    """CreateNativeK8STarget unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateNativeK8STarget
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.create_native_k8_s_target.CreateNativeK8STarget()  # noqa: E501
        if include_optional :
            return CreateNativeK8STarget(
                comment = '0', 
                k8s_cluster_ca_cert = '0', 
                k8s_cluster_endpoint = '0', 
                k8s_cluster_token = '0', 
                key = '0', 
                name = '0', 
                password = '0', 
                token = '0', 
                uid_token = '0', 
                username = '0'
            )
        else :
            return CreateNativeK8STarget(
                k8s_cluster_ca_cert = '0',
                k8s_cluster_endpoint = '0',
                k8s_cluster_token = '0',
                name = '0',
        )

    def testCreateNativeK8STarget(self):
        """Test CreateNativeK8STarget"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
