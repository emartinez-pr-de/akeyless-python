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
from akeyless.models.get_ssh_certificate import GetSSHCertificate  # noqa: E501
from akeyless.rest import ApiException

class TestGetSSHCertificate(unittest.TestCase):
    """GetSSHCertificate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetSSHCertificate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.get_ssh_certificate.GetSSHCertificate()  # noqa: E501
        if include_optional :
            return GetSSHCertificate(
                cert_issuer_name = '0', 
                cert_username = '0', 
                public_key_data = '0', 
                token = '0', 
                uid_token = '0'
            )
        else :
            return GetSSHCertificate(
                cert_issuer_name = '0',
                cert_username = '0',
        )

    def testGetSSHCertificate(self):
        """Test GetSSHCertificate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
