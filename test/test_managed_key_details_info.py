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
from akeyless.models.managed_key_details_info import ManagedKeyDetailsInfo  # noqa: E501
from akeyless.rest import ApiException

class TestManagedKeyDetailsInfo(unittest.TestCase):
    """ManagedKeyDetailsInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ManagedKeyDetailsInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.managed_key_details_info.ManagedKeyDetailsInfo()  # noqa: E501
        if include_optional :
            return ManagedKeyDetailsInfo(
                is_provided_by_user = True, 
                is_unexportable = True, 
                key_state = '0', 
                key_type = '0', 
                managed_key_id = '0', 
                target_alias_helper = '0', 
                targets = [
                    akeyless.models.managed_key_target_info.ManagedKeyTargetInfo(
                        external_kms_id = akeyless.models.external_kms_key_id.ExternalKMSKeyId(
                            key_id = '0', 
                            key_reference = '0', ), 
                        key_purpose = [
                            '0'
                            ], 
                        key_statuses = [
                            akeyless.models.managed_key_status_info.ManagedKeyStatusInfo(
                                key_id = 56, 
                                last_error = '0', 
                                last_status = '0', )
                            ], 
                        target_assoc_id = '0', )
                    ]
            )
        else :
            return ManagedKeyDetailsInfo(
        )

    def testManagedKeyDetailsInfo(self):
        """Test ManagedKeyDetailsInfo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
