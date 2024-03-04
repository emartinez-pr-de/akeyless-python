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
from akeyless.models.dynamic_secret_create_cassandra import DynamicSecretCreateCassandra  # noqa: E501
from akeyless.rest import ApiException

class TestDynamicSecretCreateCassandra(unittest.TestCase):
    """DynamicSecretCreateCassandra unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DynamicSecretCreateCassandra
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.dynamic_secret_create_cassandra.DynamicSecretCreateCassandra()  # noqa: E501
        if include_optional :
            return DynamicSecretCreateCassandra(
                cassandra_creation_statements = '0', 
                cassandra_hosts = '0', 
                cassandra_password = '0', 
                cassandra_port = '9042', 
                cassandra_username = '0', 
                delete_protection = '0', 
                description = '0', 
                json = True, 
                name = '0', 
                password_length = '0', 
                producer_encryption_key_name = '0', 
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
            return DynamicSecretCreateCassandra(
                name = '0',
        )

    def testDynamicSecretCreateCassandra(self):
        """Test DynamicSecretCreateCassandra"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
