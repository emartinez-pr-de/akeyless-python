# coding: utf-8

"""
    Akeyless API

    The purpose of this application is to provide access to Akeyless API.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Contact: support@akeyless.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from akeyless.configuration import Configuration


class MongoDBTargetDetails(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'mongodb_atlas_api_private_key': 'str',
        'mongodb_atlas_api_public_key': 'str',
        'mongodb_atlas_project_id': 'str',
        'mongodb_db_name': 'str',
        'mongodb_default_auth_db': 'str',
        'mongodb_host_port': 'str',
        'mongodb_is_atlas': 'bool',
        'mongodb_password': 'str',
        'mongodb_uri_connection': 'str',
        'mongodb_uri_options': 'str',
        'mongodb_username': 'str'
    }

    attribute_map = {
        'mongodb_atlas_api_private_key': 'mongodb_atlas_api_private_key',
        'mongodb_atlas_api_public_key': 'mongodb_atlas_api_public_key',
        'mongodb_atlas_project_id': 'mongodb_atlas_project_id',
        'mongodb_db_name': 'mongodb_db_name',
        'mongodb_default_auth_db': 'mongodb_default_auth_db',
        'mongodb_host_port': 'mongodb_host_port',
        'mongodb_is_atlas': 'mongodb_is_atlas',
        'mongodb_password': 'mongodb_password',
        'mongodb_uri_connection': 'mongodb_uri_connection',
        'mongodb_uri_options': 'mongodb_uri_options',
        'mongodb_username': 'mongodb_username'
    }

    def __init__(self, mongodb_atlas_api_private_key=None, mongodb_atlas_api_public_key=None, mongodb_atlas_project_id=None, mongodb_db_name=None, mongodb_default_auth_db=None, mongodb_host_port=None, mongodb_is_atlas=None, mongodb_password=None, mongodb_uri_connection=None, mongodb_uri_options=None, mongodb_username=None, local_vars_configuration=None):  # noqa: E501
        """MongoDBTargetDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._mongodb_atlas_api_private_key = None
        self._mongodb_atlas_api_public_key = None
        self._mongodb_atlas_project_id = None
        self._mongodb_db_name = None
        self._mongodb_default_auth_db = None
        self._mongodb_host_port = None
        self._mongodb_is_atlas = None
        self._mongodb_password = None
        self._mongodb_uri_connection = None
        self._mongodb_uri_options = None
        self._mongodb_username = None
        self.discriminator = None

        if mongodb_atlas_api_private_key is not None:
            self.mongodb_atlas_api_private_key = mongodb_atlas_api_private_key
        if mongodb_atlas_api_public_key is not None:
            self.mongodb_atlas_api_public_key = mongodb_atlas_api_public_key
        if mongodb_atlas_project_id is not None:
            self.mongodb_atlas_project_id = mongodb_atlas_project_id
        if mongodb_db_name is not None:
            self.mongodb_db_name = mongodb_db_name
        if mongodb_default_auth_db is not None:
            self.mongodb_default_auth_db = mongodb_default_auth_db
        if mongodb_host_port is not None:
            self.mongodb_host_port = mongodb_host_port
        if mongodb_is_atlas is not None:
            self.mongodb_is_atlas = mongodb_is_atlas
        if mongodb_password is not None:
            self.mongodb_password = mongodb_password
        if mongodb_uri_connection is not None:
            self.mongodb_uri_connection = mongodb_uri_connection
        if mongodb_uri_options is not None:
            self.mongodb_uri_options = mongodb_uri_options
        if mongodb_username is not None:
            self.mongodb_username = mongodb_username

    @property
    def mongodb_atlas_api_private_key(self):
        """Gets the mongodb_atlas_api_private_key of this MongoDBTargetDetails.  # noqa: E501


        :return: The mongodb_atlas_api_private_key of this MongoDBTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_atlas_api_private_key

    @mongodb_atlas_api_private_key.setter
    def mongodb_atlas_api_private_key(self, mongodb_atlas_api_private_key):
        """Sets the mongodb_atlas_api_private_key of this MongoDBTargetDetails.


        :param mongodb_atlas_api_private_key: The mongodb_atlas_api_private_key of this MongoDBTargetDetails.  # noqa: E501
        :type: str
        """

        self._mongodb_atlas_api_private_key = mongodb_atlas_api_private_key

    @property
    def mongodb_atlas_api_public_key(self):
        """Gets the mongodb_atlas_api_public_key of this MongoDBTargetDetails.  # noqa: E501


        :return: The mongodb_atlas_api_public_key of this MongoDBTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_atlas_api_public_key

    @mongodb_atlas_api_public_key.setter
    def mongodb_atlas_api_public_key(self, mongodb_atlas_api_public_key):
        """Sets the mongodb_atlas_api_public_key of this MongoDBTargetDetails.


        :param mongodb_atlas_api_public_key: The mongodb_atlas_api_public_key of this MongoDBTargetDetails.  # noqa: E501
        :type: str
        """

        self._mongodb_atlas_api_public_key = mongodb_atlas_api_public_key

    @property
    def mongodb_atlas_project_id(self):
        """Gets the mongodb_atlas_project_id of this MongoDBTargetDetails.  # noqa: E501

        mongodb atlas fields  # noqa: E501

        :return: The mongodb_atlas_project_id of this MongoDBTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_atlas_project_id

    @mongodb_atlas_project_id.setter
    def mongodb_atlas_project_id(self, mongodb_atlas_project_id):
        """Sets the mongodb_atlas_project_id of this MongoDBTargetDetails.

        mongodb atlas fields  # noqa: E501

        :param mongodb_atlas_project_id: The mongodb_atlas_project_id of this MongoDBTargetDetails.  # noqa: E501
        :type: str
        """

        self._mongodb_atlas_project_id = mongodb_atlas_project_id

    @property
    def mongodb_db_name(self):
        """Gets the mongodb_db_name of this MongoDBTargetDetails.  # noqa: E501

        common fields  # noqa: E501

        :return: The mongodb_db_name of this MongoDBTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_db_name

    @mongodb_db_name.setter
    def mongodb_db_name(self, mongodb_db_name):
        """Sets the mongodb_db_name of this MongoDBTargetDetails.

        common fields  # noqa: E501

        :param mongodb_db_name: The mongodb_db_name of this MongoDBTargetDetails.  # noqa: E501
        :type: str
        """

        self._mongodb_db_name = mongodb_db_name

    @property
    def mongodb_default_auth_db(self):
        """Gets the mongodb_default_auth_db of this MongoDBTargetDetails.  # noqa: E501


        :return: The mongodb_default_auth_db of this MongoDBTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_default_auth_db

    @mongodb_default_auth_db.setter
    def mongodb_default_auth_db(self, mongodb_default_auth_db):
        """Sets the mongodb_default_auth_db of this MongoDBTargetDetails.


        :param mongodb_default_auth_db: The mongodb_default_auth_db of this MongoDBTargetDetails.  # noqa: E501
        :type: str
        """

        self._mongodb_default_auth_db = mongodb_default_auth_db

    @property
    def mongodb_host_port(self):
        """Gets the mongodb_host_port of this MongoDBTargetDetails.  # noqa: E501


        :return: The mongodb_host_port of this MongoDBTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_host_port

    @mongodb_host_port.setter
    def mongodb_host_port(self, mongodb_host_port):
        """Sets the mongodb_host_port of this MongoDBTargetDetails.


        :param mongodb_host_port: The mongodb_host_port of this MongoDBTargetDetails.  # noqa: E501
        :type: str
        """

        self._mongodb_host_port = mongodb_host_port

    @property
    def mongodb_is_atlas(self):
        """Gets the mongodb_is_atlas of this MongoDBTargetDetails.  # noqa: E501


        :return: The mongodb_is_atlas of this MongoDBTargetDetails.  # noqa: E501
        :rtype: bool
        """
        return self._mongodb_is_atlas

    @mongodb_is_atlas.setter
    def mongodb_is_atlas(self, mongodb_is_atlas):
        """Sets the mongodb_is_atlas of this MongoDBTargetDetails.


        :param mongodb_is_atlas: The mongodb_is_atlas of this MongoDBTargetDetails.  # noqa: E501
        :type: bool
        """

        self._mongodb_is_atlas = mongodb_is_atlas

    @property
    def mongodb_password(self):
        """Gets the mongodb_password of this MongoDBTargetDetails.  # noqa: E501


        :return: The mongodb_password of this MongoDBTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_password

    @mongodb_password.setter
    def mongodb_password(self, mongodb_password):
        """Sets the mongodb_password of this MongoDBTargetDetails.


        :param mongodb_password: The mongodb_password of this MongoDBTargetDetails.  # noqa: E501
        :type: str
        """

        self._mongodb_password = mongodb_password

    @property
    def mongodb_uri_connection(self):
        """Gets the mongodb_uri_connection of this MongoDBTargetDetails.  # noqa: E501

        mongodb fields  # noqa: E501

        :return: The mongodb_uri_connection of this MongoDBTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_uri_connection

    @mongodb_uri_connection.setter
    def mongodb_uri_connection(self, mongodb_uri_connection):
        """Sets the mongodb_uri_connection of this MongoDBTargetDetails.

        mongodb fields  # noqa: E501

        :param mongodb_uri_connection: The mongodb_uri_connection of this MongoDBTargetDetails.  # noqa: E501
        :type: str
        """

        self._mongodb_uri_connection = mongodb_uri_connection

    @property
    def mongodb_uri_options(self):
        """Gets the mongodb_uri_options of this MongoDBTargetDetails.  # noqa: E501


        :return: The mongodb_uri_options of this MongoDBTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_uri_options

    @mongodb_uri_options.setter
    def mongodb_uri_options(self, mongodb_uri_options):
        """Sets the mongodb_uri_options of this MongoDBTargetDetails.


        :param mongodb_uri_options: The mongodb_uri_options of this MongoDBTargetDetails.  # noqa: E501
        :type: str
        """

        self._mongodb_uri_options = mongodb_uri_options

    @property
    def mongodb_username(self):
        """Gets the mongodb_username of this MongoDBTargetDetails.  # noqa: E501


        :return: The mongodb_username of this MongoDBTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_username

    @mongodb_username.setter
    def mongodb_username(self, mongodb_username):
        """Sets the mongodb_username of this MongoDBTargetDetails.


        :param mongodb_username: The mongodb_username of this MongoDBTargetDetails.  # noqa: E501
        :type: str
        """

        self._mongodb_username = mongodb_username

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MongoDBTargetDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MongoDBTargetDetails):
            return True

        return self.to_dict() != other.to_dict()
