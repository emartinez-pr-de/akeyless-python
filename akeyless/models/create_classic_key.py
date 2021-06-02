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


class CreateClassicKey(object):
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
        'alg': 'str',
        'key': 'str',
        'key_data': 'str',
        'metadata': 'str',
        'name': 'str',
        'password': 'str',
        'tags': 'list[str]',
        'target_name': 'str',
        'token': 'str',
        'uid_token': 'str',
        'username': 'str'
    }

    attribute_map = {
        'alg': 'alg',
        'key': 'key',
        'key_data': 'key-data',
        'metadata': 'metadata',
        'name': 'name',
        'password': 'password',
        'tags': 'tags',
        'target_name': 'target-name',
        'token': 'token',
        'uid_token': 'uid-token',
        'username': 'username'
    }

    def __init__(self, alg=None, key=None, key_data=None, metadata=None, name=None, password=None, tags=None, target_name=None, token=None, uid_token=None, username=None, local_vars_configuration=None):  # noqa: E501
        """CreateClassicKey - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._alg = None
        self._key = None
        self._key_data = None
        self._metadata = None
        self._name = None
        self._password = None
        self._tags = None
        self._target_name = None
        self._token = None
        self._uid_token = None
        self._username = None
        self.discriminator = None

        self.alg = alg
        if key is not None:
            self.key = key
        if key_data is not None:
            self.key_data = key_data
        if metadata is not None:
            self.metadata = metadata
        self.name = name
        if password is not None:
            self.password = password
        if tags is not None:
            self.tags = tags
        if target_name is not None:
            self.target_name = target_name
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if username is not None:
            self.username = username

    @property
    def alg(self):
        """Gets the alg of this CreateClassicKey.  # noqa: E501

        Classic Key type; options: [AES256GCM, RSA2048]  # noqa: E501

        :return: The alg of this CreateClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._alg

    @alg.setter
    def alg(self, alg):
        """Sets the alg of this CreateClassicKey.

        Classic Key type; options: [AES256GCM, RSA2048]  # noqa: E501

        :param alg: The alg of this CreateClassicKey.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and alg is None:  # noqa: E501
            raise ValueError("Invalid value for `alg`, must not be `None`")  # noqa: E501

        self._alg = alg

    @property
    def key(self):
        """Gets the key of this CreateClassicKey.  # noqa: E501

        The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :return: The key of this CreateClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CreateClassicKey.

        The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :param key: The key of this CreateClassicKey.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def key_data(self):
        """Gets the key_data of this CreateClassicKey.  # noqa: E501

        Base64-encoded classic key value  # noqa: E501

        :return: The key_data of this CreateClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._key_data

    @key_data.setter
    def key_data(self, key_data):
        """Sets the key_data of this CreateClassicKey.

        Base64-encoded classic key value  # noqa: E501

        :param key_data: The key_data of this CreateClassicKey.  # noqa: E501
        :type: str
        """

        self._key_data = key_data

    @property
    def metadata(self):
        """Gets the metadata of this CreateClassicKey.  # noqa: E501

        Metadata about the classic key  # noqa: E501

        :return: The metadata of this CreateClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CreateClassicKey.

        Metadata about the classic key  # noqa: E501

        :param metadata: The metadata of this CreateClassicKey.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this CreateClassicKey.  # noqa: E501

        ClassicKey name  # noqa: E501

        :return: The name of this CreateClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateClassicKey.

        ClassicKey name  # noqa: E501

        :param name: The name of this CreateClassicKey.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def password(self):
        """Gets the password of this CreateClassicKey.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The password of this CreateClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateClassicKey.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param password: The password of this CreateClassicKey.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def tags(self):
        """Gets the tags of this CreateClassicKey.  # noqa: E501

        List of the tags attached to this classic key  # noqa: E501

        :return: The tags of this CreateClassicKey.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateClassicKey.

        List of the tags attached to this classic key  # noqa: E501

        :param tags: The tags of this CreateClassicKey.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def target_name(self):
        """Gets the target_name of this CreateClassicKey.  # noqa: E501

        Target name  # noqa: E501

        :return: The target_name of this CreateClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """Sets the target_name of this CreateClassicKey.

        Target name  # noqa: E501

        :param target_name: The target_name of this CreateClassicKey.  # noqa: E501
        :type: str
        """

        self._target_name = target_name

    @property
    def token(self):
        """Gets the token of this CreateClassicKey.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this CreateClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this CreateClassicKey.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this CreateClassicKey.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this CreateClassicKey.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this CreateClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this CreateClassicKey.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this CreateClassicKey.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def username(self):
        """Gets the username of this CreateClassicKey.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The username of this CreateClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this CreateClassicKey.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param username: The username of this CreateClassicKey.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if not isinstance(other, CreateClassicKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateClassicKey):
            return True

        return self.to_dict() != other.to_dict()
