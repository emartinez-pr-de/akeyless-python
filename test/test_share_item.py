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
from akeyless.models.share_item import ShareItem  # noqa: E501
from akeyless.rest import ApiException

class TestShareItem(unittest.TestCase):
    """ShareItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ShareItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.share_item.ShareItem()  # noqa: E501
        if include_optional :
            return ShareItem(
                accessibility = 'regular', 
                action = '0', 
                emails = [
                    '0'
                    ], 
                item_name = '0', 
                json = True, 
                token = '0', 
                ttl = 56, 
                uid_token = '0', 
                view_once = True
            )
        else :
            return ShareItem(
                action = '0',
                item_name = '0',
        )

    def testShareItem(self):
        """Test ShareItem"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
