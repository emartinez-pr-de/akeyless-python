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


class GetSecretValue(object):
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
        'item_accessibility': 'str',
        'names': 'list[str]',
        'pretty_print': 'bool',
        'token': 'str',
        'uid_token': 'str',
        'version': 'int'
    }

    attribute_map = {
        'item_accessibility': 'item-accessibility',
        'names': 'names',
        'pretty_print': 'pretty-print',
        'token': 'token',
        'uid_token': 'uid-token',
        'version': 'version'
    }

    def __init__(self, item_accessibility=None, names=None, pretty_print=None, token=None, uid_token=None, version=None, local_vars_configuration=None):  # noqa: E501
        """GetSecretValue - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._item_accessibility = None
        self._names = None
        self._pretty_print = None
        self._token = None
        self._uid_token = None
        self._version = None
        self.discriminator = None

        if item_accessibility is not None:
            self.item_accessibility = item_accessibility
        self.names = names
        if pretty_print is not None:
            self.pretty_print = pretty_print
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if version is not None:
            self.version = version

    @property
    def item_accessibility(self):
        """Gets the item_accessibility of this GetSecretValue.  # noqa: E501

        for personal password manager  # noqa: E501

        :return: The item_accessibility of this GetSecretValue.  # noqa: E501
        :rtype: str
        """
        return self._item_accessibility

    @item_accessibility.setter
    def item_accessibility(self, item_accessibility):
        """Sets the item_accessibility of this GetSecretValue.

        for personal password manager  # noqa: E501

        :param item_accessibility: The item_accessibility of this GetSecretValue.  # noqa: E501
        :type: str
        """

        self._item_accessibility = item_accessibility

    @property
    def names(self):
        """Gets the names of this GetSecretValue.  # noqa: E501

        Secret name  # noqa: E501

        :return: The names of this GetSecretValue.  # noqa: E501
        :rtype: list[str]
        """
        return self._names

    @names.setter
    def names(self, names):
        """Sets the names of this GetSecretValue.

        Secret name  # noqa: E501

        :param names: The names of this GetSecretValue.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and names is None:  # noqa: E501
            raise ValueError("Invalid value for `names`, must not be `None`")  # noqa: E501

        self._names = names

    @property
    def pretty_print(self):
        """Gets the pretty_print of this GetSecretValue.  # noqa: E501


        :return: The pretty_print of this GetSecretValue.  # noqa: E501
        :rtype: bool
        """
        return self._pretty_print

    @pretty_print.setter
    def pretty_print(self, pretty_print):
        """Sets the pretty_print of this GetSecretValue.


        :param pretty_print: The pretty_print of this GetSecretValue.  # noqa: E501
        :type: bool
        """

        self._pretty_print = pretty_print

    @property
    def token(self):
        """Gets the token of this GetSecretValue.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GetSecretValue.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GetSecretValue.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GetSecretValue.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this GetSecretValue.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GetSecretValue.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GetSecretValue.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GetSecretValue.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def version(self):
        """Gets the version of this GetSecretValue.  # noqa: E501

        Secret version  # noqa: E501

        :return: The version of this GetSecretValue.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this GetSecretValue.

        Secret version  # noqa: E501

        :param version: The version of this GetSecretValue.  # noqa: E501
        :type: int
        """

        self._version = version

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
        if not isinstance(other, GetSecretValue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetSecretValue):
            return True

        return self.to_dict() != other.to_dict()
