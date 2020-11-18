# coding: utf-8

"""
    Akeyless API

    The purpose of this application is to provide access to Akeyless API.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: support@akeyless.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from akeyless.configuration import Configuration


class CreateSecret(object):
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
        'metadata': 'str',
        'multiline_value': 'bool',
        'name': 'str',
        'protection_key': 'str',
        'tags': 'list[str]',
        'token': 'str',
        'uid_token': 'str',
        'value': 'str'
    }

    attribute_map = {
        'metadata': 'metadata',
        'multiline_value': 'multiline_value',
        'name': 'name',
        'protection_key': 'protection_key',
        'tags': 'tags',
        'token': 'token',
        'uid_token': 'uid-token',
        'value': 'value'
    }

    def __init__(self, metadata=None, multiline_value=None, name=None, protection_key=None, tags=None, token=None, uid_token=None, value=None, local_vars_configuration=None):  # noqa: E501
        """CreateSecret - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._metadata = None
        self._multiline_value = None
        self._name = None
        self._protection_key = None
        self._tags = None
        self._token = None
        self._uid_token = None
        self._value = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if multiline_value is not None:
            self.multiline_value = multiline_value
        self.name = name
        if protection_key is not None:
            self.protection_key = protection_key
        if tags is not None:
            self.tags = tags
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        self.value = value

    @property
    def metadata(self):
        """Gets the metadata of this CreateSecret.  # noqa: E501

        Metadata about the secret  # noqa: E501

        :return: The metadata of this CreateSecret.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CreateSecret.

        Metadata about the secret  # noqa: E501

        :param metadata: The metadata of this CreateSecret.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def multiline_value(self):
        """Gets the multiline_value of this CreateSecret.  # noqa: E501

        The provided value is a multiline value (separated by '\\n')  # noqa: E501

        :return: The multiline_value of this CreateSecret.  # noqa: E501
        :rtype: bool
        """
        return self._multiline_value

    @multiline_value.setter
    def multiline_value(self, multiline_value):
        """Sets the multiline_value of this CreateSecret.

        The provided value is a multiline value (separated by '\\n')  # noqa: E501

        :param multiline_value: The multiline_value of this CreateSecret.  # noqa: E501
        :type: bool
        """

        self._multiline_value = multiline_value

    @property
    def name(self):
        """Gets the name of this CreateSecret.  # noqa: E501

        Secret name  # noqa: E501

        :return: The name of this CreateSecret.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateSecret.

        Secret name  # noqa: E501

        :param name: The name of this CreateSecret.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def protection_key(self):
        """Gets the protection_key of this CreateSecret.  # noqa: E501

        The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :return: The protection_key of this CreateSecret.  # noqa: E501
        :rtype: str
        """
        return self._protection_key

    @protection_key.setter
    def protection_key(self, protection_key):
        """Sets the protection_key of this CreateSecret.

        The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :param protection_key: The protection_key of this CreateSecret.  # noqa: E501
        :type: str
        """

        self._protection_key = protection_key

    @property
    def tags(self):
        """Gets the tags of this CreateSecret.  # noqa: E501

        List of the tags attached to this secret  # noqa: E501

        :return: The tags of this CreateSecret.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateSecret.

        List of the tags attached to this secret  # noqa: E501

        :param tags: The tags of this CreateSecret.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def token(self):
        """Gets the token of this CreateSecret.  # noqa: E501

        Use a specific profile from your akeyless/profiles/ folder  # noqa: E501

        :return: The token of this CreateSecret.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this CreateSecret.

        Use a specific profile from your akeyless/profiles/ folder  # noqa: E501

        :param token: The token of this CreateSecret.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this CreateSecret.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this CreateSecret.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this CreateSecret.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this CreateSecret.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def value(self):
        """Gets the value of this CreateSecret.  # noqa: E501

        The secret value  # noqa: E501

        :return: The value of this CreateSecret.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CreateSecret.

        The secret value  # noqa: E501

        :param value: The value of this CreateSecret.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if not isinstance(other, CreateSecret):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateSecret):
            return True

        return self.to_dict() != other.to_dict()
