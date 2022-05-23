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
from akeyless.models.email_tokenizer_info import EmailTokenizerInfo  # noqa: E501
from akeyless.rest import ApiException

class TestEmailTokenizerInfo(unittest.TestCase):
    """EmailTokenizerInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EmailTokenizerInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.email_tokenizer_info.EmailTokenizerInfo()  # noqa: E501
        if include_optional :
            return EmailTokenizerInfo(
                domain_suffix_length = 56, 
                fixed_domain_suffix = '0', 
                keep_prefix_length = 56
            )
        else :
            return EmailTokenizerInfo(
        )

    def testEmailTokenizerInfo(self):
        """Test EmailTokenizerInfo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
