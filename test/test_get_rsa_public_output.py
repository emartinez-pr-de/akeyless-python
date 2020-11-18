# coding: utf-8

"""
    Akeyless API

    The purpose of this application is to provide access to Akeyless API.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: support@akeyless.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import akeyless
from akeyless.models.get_rsa_public_output import GetRSAPublicOutput  # noqa: E501
from akeyless.rest import ApiException

class TestGetRSAPublicOutput(unittest.TestCase):
    """GetRSAPublicOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetRSAPublicOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.get_rsa_public_output.GetRSAPublicOutput()  # noqa: E501
        if include_optional :
            return GetRSAPublicOutput(
                raw = '0', 
                ssh = [
                    56
                    ]
            )
        else :
            return GetRSAPublicOutput(
        )

    def testGetRSAPublicOutput(self):
        """Test GetRSAPublicOutput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
