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
from akeyless.models.gateway_update_producer_native_k8_s import GatewayUpdateProducerNativeK8S  # noqa: E501
from akeyless.rest import ApiException

class TestGatewayUpdateProducerNativeK8S(unittest.TestCase):
    """GatewayUpdateProducerNativeK8S unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GatewayUpdateProducerNativeK8S
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.gateway_update_producer_native_k8_s.GatewayUpdateProducerNativeK8S()  # noqa: E501
        if include_optional :
            return GatewayUpdateProducerNativeK8S(
                k8s_cluster_ca_cert = '0', 
                k8s_cluster_endpoint = '0', 
                k8s_cluster_token = '0', 
                k8s_namespace = '0', 
                k8s_service_account = '0', 
                name = '0', 
                new_name = '0', 
                password = '0', 
                producer_encryption_key_name = '0', 
                secure_access_allow_port_forwading = True, 
                secure_access_bastion_issuer = '0', 
                secure_access_cluster_endpoint = '0', 
                secure_access_dashboard_url = '0', 
                secure_access_enable = '0', 
                secure_access_web = True, 
                secure_access_web_browsing = True, 
                tags = [
                    '0'
                    ], 
                target_name = '0', 
                token = '0', 
                uid_token = '0', 
                user_ttl = '60m', 
                username = '0'
            )
        else :
            return GatewayUpdateProducerNativeK8S(
                name = '0',
        )

    def testGatewayUpdateProducerNativeK8S(self):
        """Test GatewayUpdateProducerNativeK8S"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()