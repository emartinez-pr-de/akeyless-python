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
from akeyless.models.k8_s_migration import K8SMigration  # noqa: E501
from akeyless.rest import ApiException

class TestK8SMigration(unittest.TestCase):
    """K8SMigration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test K8SMigration
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.k8_s_migration.K8SMigration()  # noqa: E501
        if include_optional :
            return K8SMigration(
                general = akeyless.models.migration_general.MigrationGeneral(
                    id = '0', 
                    name = '0', 
                    prefix = '0', 
                    protection_key = '0', ), 
                payload = akeyless.models.k8_s_payload.K8SPayload(
                    ca = [
                        56
                        ], 
                    client_cert = [
                        56
                        ], 
                    client_key = [
                        56
                        ], 
                    namespace = '0', 
                    password = '0', 
                    server = '0', 
                    skip_system = True, 
                    token = '0', 
                    username = '0', )
            )
        else :
            return K8SMigration(
        )

    def testK8SMigration(self):
        """Test K8SMigration"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
