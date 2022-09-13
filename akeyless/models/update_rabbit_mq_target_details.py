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


class UpdateRabbitMQTargetDetails(object):
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
        'json': 'bool',
        'keep_prev_version': 'str',
        'name': 'str',
        'new_version': 'bool',
        'protection_key': 'str',
        'rabbitmq_server_password': 'str',
        'rabbitmq_server_uri': 'str',
        'rabbitmq_server_user': 'str',
        'token': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'json': 'json',
        'keep_prev_version': 'keep-prev-version',
        'name': 'name',
        'new_version': 'new-version',
        'protection_key': 'protection_key',
        'rabbitmq_server_password': 'rabbitmq_server_password',
        'rabbitmq_server_uri': 'rabbitmq_server_uri',
        'rabbitmq_server_user': 'rabbitmq_server_user',
        'token': 'token',
        'uid_token': 'uid-token'
    }

    def __init__(self, json=None, keep_prev_version=None, name=None, new_version=None, protection_key=None, rabbitmq_server_password=None, rabbitmq_server_uri=None, rabbitmq_server_user=None, token=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """UpdateRabbitMQTargetDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._json = None
        self._keep_prev_version = None
        self._name = None
        self._new_version = None
        self._protection_key = None
        self._rabbitmq_server_password = None
        self._rabbitmq_server_uri = None
        self._rabbitmq_server_user = None
        self._token = None
        self._uid_token = None
        self.discriminator = None

        if json is not None:
            self.json = json
        if keep_prev_version is not None:
            self.keep_prev_version = keep_prev_version
        self.name = name
        if new_version is not None:
            self.new_version = new_version
        if protection_key is not None:
            self.protection_key = protection_key
        if rabbitmq_server_password is not None:
            self.rabbitmq_server_password = rabbitmq_server_password
        if rabbitmq_server_uri is not None:
            self.rabbitmq_server_uri = rabbitmq_server_uri
        if rabbitmq_server_user is not None:
            self.rabbitmq_server_user = rabbitmq_server_user
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def json(self):
        """Gets the json of this UpdateRabbitMQTargetDetails.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this UpdateRabbitMQTargetDetails.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this UpdateRabbitMQTargetDetails.

        Set output format to JSON  # noqa: E501

        :param json: The json of this UpdateRabbitMQTargetDetails.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def keep_prev_version(self):
        """Gets the keep_prev_version of this UpdateRabbitMQTargetDetails.  # noqa: E501


        :return: The keep_prev_version of this UpdateRabbitMQTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._keep_prev_version

    @keep_prev_version.setter
    def keep_prev_version(self, keep_prev_version):
        """Sets the keep_prev_version of this UpdateRabbitMQTargetDetails.


        :param keep_prev_version: The keep_prev_version of this UpdateRabbitMQTargetDetails.  # noqa: E501
        :type: str
        """

        self._keep_prev_version = keep_prev_version

    @property
    def name(self):
        """Gets the name of this UpdateRabbitMQTargetDetails.  # noqa: E501

        Target name  # noqa: E501

        :return: The name of this UpdateRabbitMQTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateRabbitMQTargetDetails.

        Target name  # noqa: E501

        :param name: The name of this UpdateRabbitMQTargetDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def new_version(self):
        """Gets the new_version of this UpdateRabbitMQTargetDetails.  # noqa: E501

        Deprecated  # noqa: E501

        :return: The new_version of this UpdateRabbitMQTargetDetails.  # noqa: E501
        :rtype: bool
        """
        return self._new_version

    @new_version.setter
    def new_version(self, new_version):
        """Sets the new_version of this UpdateRabbitMQTargetDetails.

        Deprecated  # noqa: E501

        :param new_version: The new_version of this UpdateRabbitMQTargetDetails.  # noqa: E501
        :type: bool
        """

        self._new_version = new_version

    @property
    def protection_key(self):
        """Gets the protection_key of this UpdateRabbitMQTargetDetails.  # noqa: E501

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :return: The protection_key of this UpdateRabbitMQTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._protection_key

    @protection_key.setter
    def protection_key(self, protection_key):
        """Sets the protection_key of this UpdateRabbitMQTargetDetails.

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :param protection_key: The protection_key of this UpdateRabbitMQTargetDetails.  # noqa: E501
        :type: str
        """

        self._protection_key = protection_key

    @property
    def rabbitmq_server_password(self):
        """Gets the rabbitmq_server_password of this UpdateRabbitMQTargetDetails.  # noqa: E501


        :return: The rabbitmq_server_password of this UpdateRabbitMQTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._rabbitmq_server_password

    @rabbitmq_server_password.setter
    def rabbitmq_server_password(self, rabbitmq_server_password):
        """Sets the rabbitmq_server_password of this UpdateRabbitMQTargetDetails.


        :param rabbitmq_server_password: The rabbitmq_server_password of this UpdateRabbitMQTargetDetails.  # noqa: E501
        :type: str
        """

        self._rabbitmq_server_password = rabbitmq_server_password

    @property
    def rabbitmq_server_uri(self):
        """Gets the rabbitmq_server_uri of this UpdateRabbitMQTargetDetails.  # noqa: E501


        :return: The rabbitmq_server_uri of this UpdateRabbitMQTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._rabbitmq_server_uri

    @rabbitmq_server_uri.setter
    def rabbitmq_server_uri(self, rabbitmq_server_uri):
        """Sets the rabbitmq_server_uri of this UpdateRabbitMQTargetDetails.


        :param rabbitmq_server_uri: The rabbitmq_server_uri of this UpdateRabbitMQTargetDetails.  # noqa: E501
        :type: str
        """

        self._rabbitmq_server_uri = rabbitmq_server_uri

    @property
    def rabbitmq_server_user(self):
        """Gets the rabbitmq_server_user of this UpdateRabbitMQTargetDetails.  # noqa: E501


        :return: The rabbitmq_server_user of this UpdateRabbitMQTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._rabbitmq_server_user

    @rabbitmq_server_user.setter
    def rabbitmq_server_user(self, rabbitmq_server_user):
        """Sets the rabbitmq_server_user of this UpdateRabbitMQTargetDetails.


        :param rabbitmq_server_user: The rabbitmq_server_user of this UpdateRabbitMQTargetDetails.  # noqa: E501
        :type: str
        """

        self._rabbitmq_server_user = rabbitmq_server_user

    @property
    def token(self):
        """Gets the token of this UpdateRabbitMQTargetDetails.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this UpdateRabbitMQTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this UpdateRabbitMQTargetDetails.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this UpdateRabbitMQTargetDetails.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this UpdateRabbitMQTargetDetails.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this UpdateRabbitMQTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this UpdateRabbitMQTargetDetails.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this UpdateRabbitMQTargetDetails.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

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
        if not isinstance(other, UpdateRabbitMQTargetDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateRabbitMQTargetDetails):
            return True

        return self.to_dict() != other.to_dict()
