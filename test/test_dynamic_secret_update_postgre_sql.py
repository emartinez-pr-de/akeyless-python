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
from akeyless.models.dynamic_secret_update_postgre_sql import DynamicSecretUpdatePostgreSql  # noqa: E501
from akeyless.rest import ApiException

class TestDynamicSecretUpdatePostgreSql(unittest.TestCase):
    """DynamicSecretUpdatePostgreSql unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DynamicSecretUpdatePostgreSql
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.dynamic_secret_update_postgre_sql.DynamicSecretUpdatePostgreSql()  # noqa: E501
        if include_optional :
            return DynamicSecretUpdatePostgreSql(
                creation_statements = '0', 
                delete_protection = '0', 
                description = '0', 
                json = True, 
                name = '0', 
                new_name = '0', 
                password_length = '0', 
                postgresql_db_name = '0', 
                postgresql_host = '127.0.0.1', 
                postgresql_password = '0', 
                postgresql_port = '5432', 
                postgresql_username = '0', 
                producer_encryption_key = '0', 
                revocation_statement = '0', 
                secure_access_bastion_issuer = '0', 
                secure_access_db_schema = '0', 
                secure_access_enable = '0', 
                secure_access_host = [
                    '0'
                    ], 
                secure_access_web = True, 
                ssl = True, 
                tags = [
                    '0'
                    ], 
                target_name = '0', 
                token = '0', 
                uid_token = '0', 
                user_ttl = '60m'
            )
        else :
            return DynamicSecretUpdatePostgreSql(
                name = '0',
        )

    def testDynamicSecretUpdatePostgreSql(self):
        """Test DynamicSecretUpdatePostgreSql"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
