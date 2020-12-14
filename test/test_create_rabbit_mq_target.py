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
from akeyless.models.create_rabbit_mq_target import CreateRabbitMQTarget  # noqa: E501
from akeyless.rest import ApiException

class TestCreateRabbitMQTarget(unittest.TestCase):
    """CreateRabbitMQTarget unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateRabbitMQTarget
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.create_rabbit_mq_target.CreateRabbitMQTarget()  # noqa: E501
        if include_optional :
            return CreateRabbitMQTarget(
                comment = '0', 
                name = '0', 
                protection_key = '0', 
                rabbitmq_server_password = '0', 
                rabbitmq_server_uri = '0', 
                rabbitmq_server_user = '0', 
                token = '0', 
                uid_token = '0'
            )
        else :
            return CreateRabbitMQTarget(
                name = '0',
        )

    def testCreateRabbitMQTarget(self):
        """Test CreateRabbitMQTarget"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
