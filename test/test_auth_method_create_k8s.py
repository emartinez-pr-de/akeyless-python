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
from akeyless.models.auth_method_create_k8s import AuthMethodCreateK8s  # noqa: E501
from akeyless.rest import ApiException

class TestAuthMethodCreateK8s(unittest.TestCase):
    """AuthMethodCreateK8s unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AuthMethodCreateK8s
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.auth_method_create_k8s.AuthMethodCreateK8s()  # noqa: E501
        if include_optional :
            return AuthMethodCreateK8s(
                access_expires = 56, 
                audience = '0', 
                audit_logs_claims = [
                    '0'
                    ], 
                bound_ips = [
                    '0'
                    ], 
                bound_namespaces = [
                    '0'
                    ], 
                bound_pod_names = [
                    '0'
                    ], 
                bound_sa_names = [
                    '0'
                    ], 
                description = '0', 
                force_sub_claims = True, 
                gen_key = 'true', 
                gw_bound_ips = [
                    '0'
                    ], 
                json = True, 
                jwt_ttl = 56, 
                name = '0', 
                product_type = [
                    '0'
                    ], 
                public_key = '0', 
                token = '0', 
                uid_token = '0'
            )
        else :
            return AuthMethodCreateK8s(
                name = '0',
        )

    def testAuthMethodCreateK8s(self):
        """Test AuthMethodCreateK8s"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
