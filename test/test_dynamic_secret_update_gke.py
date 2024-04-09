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
from akeyless.models.dynamic_secret_update_gke import DynamicSecretUpdateGke  # noqa: E501
from akeyless.rest import ApiException

class TestDynamicSecretUpdateGke(unittest.TestCase):
    """DynamicSecretUpdateGke unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DynamicSecretUpdateGke
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.dynamic_secret_update_gke.DynamicSecretUpdateGke()  # noqa: E501
        if include_optional :
            return DynamicSecretUpdateGke(
                delete_protection = '0', 
                description = '0', 
                gke_account_key = '0', 
                gke_cluster_cert = '0', 
                gke_cluster_endpoint = '0', 
                gke_cluster_name = '0', 
                gke_service_account_email = '0', 
                json = True, 
                name = '0', 
                new_name = '0', 
                producer_encryption_key_name = '0', 
                secure_access_allow_port_forwading = True, 
                secure_access_bastion_issuer = '0', 
                secure_access_cluster_endpoint = '0', 
                secure_access_enable = '0', 
                secure_access_web = True, 
                tags = [
                    '0'
                    ], 
                target_name = '0', 
                token = '0', 
                uid_token = '0', 
                user_ttl = '60m'
            )
        else :
            return DynamicSecretUpdateGke(
                name = '0',
        )

    def testDynamicSecretUpdateGke(self):
        """Test DynamicSecretUpdateGke"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()