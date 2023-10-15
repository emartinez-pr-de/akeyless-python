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
from akeyless.models.global_sign_gcc_target_details import GlobalSignGCCTargetDetails  # noqa: E501
from akeyless.rest import ApiException

class TestGlobalSignGCCTargetDetails(unittest.TestCase):
    """GlobalSignGCCTargetDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GlobalSignGCCTargetDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.global_sign_gcc_target_details.GlobalSignGCCTargetDetails()  # noqa: E501
        if include_optional :
            return GlobalSignGCCTargetDetails(
                email = '0', 
                first_name = '0', 
                last_name = '0', 
                password = '0', 
                phone = '0', 
                profile_id = '0', 
                timeout = 56, 
                username = '0'
            )
        else :
            return GlobalSignGCCTargetDetails(
        )

    def testGlobalSignGCCTargetDetails(self):
        """Test GlobalSignGCCTargetDetails"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()