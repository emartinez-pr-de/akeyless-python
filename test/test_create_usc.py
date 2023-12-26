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
from akeyless.models.create_usc import CreateUSC  # noqa: E501
from akeyless.rest import ApiException

class TestCreateUSC(unittest.TestCase):
    """CreateUSC unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateUSC
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.create_usc.CreateUSC()  # noqa: E501
        if include_optional :
            return CreateUSC(
                azure_kv_name = '0', 
                delete_protection = '0', 
                description = '0', 
                json = True, 
                k8s_namespace = '0', 
                name = '0', 
                tags = [
                    '0'
                    ], 
                target_to_associate = '0', 
                token = '0', 
                uid_token = '0'
            )
        else :
            return CreateUSC(
                name = '0',
                target_to_associate = '0',
        )

    def testCreateUSC(self):
        """Test CreateUSC"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
