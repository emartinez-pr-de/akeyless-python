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
from akeyless.models.generate_csr import GenerateCsr  # noqa: E501
from akeyless.rest import ApiException

class TestGenerateCsr(unittest.TestCase):
    """GenerateCsr unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GenerateCsr
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.generate_csr.GenerateCsr()  # noqa: E501
        if include_optional :
            return GenerateCsr(
                alg = '0', 
                alt_names = '0', 
                certificate_type = '0', 
                city = '0', 
                common_name = '0', 
                country = '0', 
                critical = True, 
                dep = '0', 
                description = '0', 
                email_addresses = '0', 
                generate_key = True, 
                ip_addresses = '0', 
                json = True, 
                metadata = '0', 
                name = '0', 
                org = '0', 
                state = '0', 
                token = '0', 
                uid_token = '0', 
                uri_sans = '0'
            )
        else :
            return GenerateCsr(
                common_name = '0',
                name = '0',
        )

    def testGenerateCsr(self):
        """Test GenerateCsr"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
