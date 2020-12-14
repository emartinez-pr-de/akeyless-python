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


class UidRotateToken(object):
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
        'fork': 'bool',
        'send_manual_ack_token': 'str',
        'uid_token': 'str',
        'with_manual_ack': 'bool'
    }

    attribute_map = {
        'fork': 'fork',
        'send_manual_ack_token': 'send-manual-ack-token',
        'uid_token': 'uid-token',
        'with_manual_ack': 'with-manual-ack'
    }

    def __init__(self, fork=None, send_manual_ack_token=None, uid_token=None, with_manual_ack=None, local_vars_configuration=None):  # noqa: E501
        """UidRotateToken - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._fork = None
        self._send_manual_ack_token = None
        self._uid_token = None
        self._with_manual_ack = None
        self.discriminator = None

        if fork is not None:
            self.fork = fork
        if send_manual_ack_token is not None:
            self.send_manual_ack_token = send_manual_ack_token
        if uid_token is not None:
            self.uid_token = uid_token
        if with_manual_ack is not None:
            self.with_manual_ack = with_manual_ack

    @property
    def fork(self):
        """Gets the fork of this UidRotateToken.  # noqa: E501

        Create a new child token with default parameters  # noqa: E501

        :return: The fork of this UidRotateToken.  # noqa: E501
        :rtype: bool
        """
        return self._fork

    @fork.setter
    def fork(self, fork):
        """Sets the fork of this UidRotateToken.

        Create a new child token with default parameters  # noqa: E501

        :param fork: The fork of this UidRotateToken.  # noqa: E501
        :type: bool
        """

        self._fork = fork

    @property
    def send_manual_ack_token(self):
        """Gets the send_manual_ack_token of this UidRotateToken.  # noqa: E501

        The new rotated token to send manual ack for (with uid-token=the-orig-token)  # noqa: E501

        :return: The send_manual_ack_token of this UidRotateToken.  # noqa: E501
        :rtype: str
        """
        return self._send_manual_ack_token

    @send_manual_ack_token.setter
    def send_manual_ack_token(self, send_manual_ack_token):
        """Sets the send_manual_ack_token of this UidRotateToken.

        The new rotated token to send manual ack for (with uid-token=the-orig-token)  # noqa: E501

        :param send_manual_ack_token: The send_manual_ack_token of this UidRotateToken.  # noqa: E501
        :type: str
        """

        self._send_manual_ack_token = send_manual_ack_token

    @property
    def uid_token(self):
        """Gets the uid_token of this UidRotateToken.  # noqa: E501

        The Universal identity token  # noqa: E501

        :return: The uid_token of this UidRotateToken.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this UidRotateToken.

        The Universal identity token  # noqa: E501

        :param uid_token: The uid_token of this UidRotateToken.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def with_manual_ack(self):
        """Gets the with_manual_ack of this UidRotateToken.  # noqa: E501

        Disable automatic ack  # noqa: E501

        :return: The with_manual_ack of this UidRotateToken.  # noqa: E501
        :rtype: bool
        """
        return self._with_manual_ack

    @with_manual_ack.setter
    def with_manual_ack(self, with_manual_ack):
        """Sets the with_manual_ack of this UidRotateToken.

        Disable automatic ack  # noqa: E501

        :param with_manual_ack: The with_manual_ack of this UidRotateToken.  # noqa: E501
        :type: bool
        """

        self._with_manual_ack = with_manual_ack

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
        if not isinstance(other, UidRotateToken):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UidRotateToken):
            return True

        return self.to_dict() != other.to_dict()
