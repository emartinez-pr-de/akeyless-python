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
from akeyless.models.decrypt_gpg import DecryptGPG  # noqa: E501
from akeyless.rest import ApiException

class TestDecryptGPG(unittest.TestCase):
    """DecryptGPG unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DecryptGPG
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.decrypt_gpg.DecryptGPG()  # noqa: E501
        if include_optional :
            return DecryptGPG(
                ciphertext = '0', 
                display_id = '0', 
                item_id = 56, 
                json = True, 
                key_name = '0', 
                output_format = '0', 
                passphrase = '0', 
                token = '0', 
                uid_token = '0'
            )
        else :
            return DecryptGPG(
                ciphertext = '0',
                key_name = '0',
        )

    def testDecryptGPG(self):
        """Test DecryptGPG"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
