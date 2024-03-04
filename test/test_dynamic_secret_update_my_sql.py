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
from akeyless.models.dynamic_secret_update_my_sql import DynamicSecretUpdateMySql  # noqa: E501
from akeyless.rest import ApiException

class TestDynamicSecretUpdateMySql(unittest.TestCase):
    """DynamicSecretUpdateMySql unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DynamicSecretUpdateMySql
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.dynamic_secret_update_my_sql.DynamicSecretUpdateMySql()  # noqa: E501
        if include_optional :
            return DynamicSecretUpdateMySql(
                db_server_certificates = '0', 
                db_server_name = '0', 
                delete_protection = '0', 
                description = '0', 
                json = True, 
                mysql_dbname = '0', 
                mysql_host = '127.0.0.1', 
                mysql_password = '0', 
                mysql_port = '3306', 
                mysql_revocation_statements = '0', 
                mysql_screation_statements = '0', 
                mysql_username = '0', 
                name = '0', 
                new_name = '0', 
                password_length = '0', 
                producer_encryption_key_name = '0', 
                secure_access_bastion_issuer = '0', 
                secure_access_enable = '0', 
                secure_access_host = [
                    '0'
                    ], 
                secure_access_web = True, 
                ssl = True, 
                ssl_certificate = '0', 
                tags = [
                    '0'
                    ], 
                target_name = '0', 
                token = '0', 
                uid_token = '0', 
                user_ttl = '60m'
            )
        else :
            return DynamicSecretUpdateMySql(
                name = '0',
        )

    def testDynamicSecretUpdateMySql(self):
        """Test DynamicSecretUpdateMySql"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
