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


class UpdateDBTargetDetails(object):
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
        'db_type': 'str',
        'host_name': 'str',
        'mongo_db_name': 'str',
        'mongo_uri': 'str',
        'name': 'str',
        'new_version': 'bool',
        'port': 'str',
        'protection_key': 'str',
        'pwd': 'str',
        'token': 'str',
        'uid_token': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'db_type': 'db_type',
        'host_name': 'host_name',
        'mongo_db_name': 'mongo_db_name',
        'mongo_uri': 'mongo_uri',
        'name': 'name',
        'new_version': 'new-version',
        'port': 'port',
        'protection_key': 'protection_key',
        'pwd': 'pwd',
        'token': 'token',
        'uid_token': 'uid-token',
        'user_name': 'user_name'
    }

    def __init__(self, db_type=None, host_name=None, mongo_db_name=None, mongo_uri=None, name=None, new_version=False, port=None, protection_key=None, pwd=None, token=None, uid_token=None, user_name=None, local_vars_configuration=None):  # noqa: E501
        """UpdateDBTargetDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._db_type = None
        self._host_name = None
        self._mongo_db_name = None
        self._mongo_uri = None
        self._name = None
        self._new_version = None
        self._port = None
        self._protection_key = None
        self._pwd = None
        self._token = None
        self._uid_token = None
        self._user_name = None
        self.discriminator = None

        if db_type is not None:
            self.db_type = db_type
        if host_name is not None:
            self.host_name = host_name
        if mongo_db_name is not None:
            self.mongo_db_name = mongo_db_name
        if mongo_uri is not None:
            self.mongo_uri = mongo_uri
        self.name = name
        if new_version is not None:
            self.new_version = new_version
        if port is not None:
            self.port = port
        if protection_key is not None:
            self.protection_key = protection_key
        if pwd is not None:
            self.pwd = pwd
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if user_name is not None:
            self.user_name = user_name

    @property
    def db_type(self):
        """Gets the db_type of this UpdateDBTargetDetails.  # noqa: E501


        :return: The db_type of this UpdateDBTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._db_type

    @db_type.setter
    def db_type(self, db_type):
        """Sets the db_type of this UpdateDBTargetDetails.


        :param db_type: The db_type of this UpdateDBTargetDetails.  # noqa: E501
        :type: str
        """

        self._db_type = db_type

    @property
    def host_name(self):
        """Gets the host_name of this UpdateDBTargetDetails.  # noqa: E501


        :return: The host_name of this UpdateDBTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this UpdateDBTargetDetails.


        :param host_name: The host_name of this UpdateDBTargetDetails.  # noqa: E501
        :type: str
        """

        self._host_name = host_name

    @property
    def mongo_db_name(self):
        """Gets the mongo_db_name of this UpdateDBTargetDetails.  # noqa: E501


        :return: The mongo_db_name of this UpdateDBTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._mongo_db_name

    @mongo_db_name.setter
    def mongo_db_name(self, mongo_db_name):
        """Sets the mongo_db_name of this UpdateDBTargetDetails.


        :param mongo_db_name: The mongo_db_name of this UpdateDBTargetDetails.  # noqa: E501
        :type: str
        """

        self._mongo_db_name = mongo_db_name

    @property
    def mongo_uri(self):
        """Gets the mongo_uri of this UpdateDBTargetDetails.  # noqa: E501


        :return: The mongo_uri of this UpdateDBTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._mongo_uri

    @mongo_uri.setter
    def mongo_uri(self, mongo_uri):
        """Sets the mongo_uri of this UpdateDBTargetDetails.


        :param mongo_uri: The mongo_uri of this UpdateDBTargetDetails.  # noqa: E501
        :type: str
        """

        self._mongo_uri = mongo_uri

    @property
    def name(self):
        """Gets the name of this UpdateDBTargetDetails.  # noqa: E501

        Target name  # noqa: E501

        :return: The name of this UpdateDBTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateDBTargetDetails.

        Target name  # noqa: E501

        :param name: The name of this UpdateDBTargetDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def new_version(self):
        """Gets the new_version of this UpdateDBTargetDetails.  # noqa: E501

        Whether to create a new version of not  # noqa: E501

        :return: The new_version of this UpdateDBTargetDetails.  # noqa: E501
        :rtype: bool
        """
        return self._new_version

    @new_version.setter
    def new_version(self, new_version):
        """Sets the new_version of this UpdateDBTargetDetails.

        Whether to create a new version of not  # noqa: E501

        :param new_version: The new_version of this UpdateDBTargetDetails.  # noqa: E501
        :type: bool
        """

        self._new_version = new_version

    @property
    def port(self):
        """Gets the port of this UpdateDBTargetDetails.  # noqa: E501


        :return: The port of this UpdateDBTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this UpdateDBTargetDetails.


        :param port: The port of this UpdateDBTargetDetails.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def protection_key(self):
        """Gets the protection_key of this UpdateDBTargetDetails.  # noqa: E501

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :return: The protection_key of this UpdateDBTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._protection_key

    @protection_key.setter
    def protection_key(self, protection_key):
        """Sets the protection_key of this UpdateDBTargetDetails.

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :param protection_key: The protection_key of this UpdateDBTargetDetails.  # noqa: E501
        :type: str
        """

        self._protection_key = protection_key

    @property
    def pwd(self):
        """Gets the pwd of this UpdateDBTargetDetails.  # noqa: E501


        :return: The pwd of this UpdateDBTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._pwd

    @pwd.setter
    def pwd(self, pwd):
        """Sets the pwd of this UpdateDBTargetDetails.


        :param pwd: The pwd of this UpdateDBTargetDetails.  # noqa: E501
        :type: str
        """

        self._pwd = pwd

    @property
    def token(self):
        """Gets the token of this UpdateDBTargetDetails.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this UpdateDBTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this UpdateDBTargetDetails.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this UpdateDBTargetDetails.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this UpdateDBTargetDetails.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this UpdateDBTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this UpdateDBTargetDetails.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this UpdateDBTargetDetails.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def user_name(self):
        """Gets the user_name of this UpdateDBTargetDetails.  # noqa: E501


        :return: The user_name of this UpdateDBTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this UpdateDBTargetDetails.


        :param user_name: The user_name of this UpdateDBTargetDetails.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

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
        if not isinstance(other, UpdateDBTargetDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateDBTargetDetails):
            return True

        return self.to_dict() != other.to_dict()
