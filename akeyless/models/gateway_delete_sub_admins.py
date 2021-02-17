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


class GatewayDeleteSubAdmins(object):
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
        'gateway_url': 'str',
        'sub_admin': 'list[str]',
        'token': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'gateway_url': 'gateway-url',
        'sub_admin': 'sub-admin',
        'token': 'token',
        'uid_token': 'uid-token'
    }

    def __init__(self, gateway_url='http://localhost:8000', sub_admin=None, token=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """GatewayDeleteSubAdmins - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._gateway_url = None
        self._sub_admin = None
        self._token = None
        self._uid_token = None
        self.discriminator = None

        if gateway_url is not None:
            self.gateway_url = gateway_url
        self.sub_admin = sub_admin
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def gateway_url(self):
        """Gets the gateway_url of this GatewayDeleteSubAdmins.  # noqa: E501

        Gateway url  # noqa: E501

        :return: The gateway_url of this GatewayDeleteSubAdmins.  # noqa: E501
        :rtype: str
        """
        return self._gateway_url

    @gateway_url.setter
    def gateway_url(self, gateway_url):
        """Sets the gateway_url of this GatewayDeleteSubAdmins.

        Gateway url  # noqa: E501

        :param gateway_url: The gateway_url of this GatewayDeleteSubAdmins.  # noqa: E501
        :type: str
        """

        self._gateway_url = gateway_url

    @property
    def sub_admin(self):
        """Gets the sub_admin of this GatewayDeleteSubAdmins.  # noqa: E501

        SubAdmins to be removed  # noqa: E501

        :return: The sub_admin of this GatewayDeleteSubAdmins.  # noqa: E501
        :rtype: list[str]
        """
        return self._sub_admin

    @sub_admin.setter
    def sub_admin(self, sub_admin):
        """Sets the sub_admin of this GatewayDeleteSubAdmins.

        SubAdmins to be removed  # noqa: E501

        :param sub_admin: The sub_admin of this GatewayDeleteSubAdmins.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and sub_admin is None:  # noqa: E501
            raise ValueError("Invalid value for `sub_admin`, must not be `None`")  # noqa: E501

        self._sub_admin = sub_admin

    @property
    def token(self):
        """Gets the token of this GatewayDeleteSubAdmins.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GatewayDeleteSubAdmins.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GatewayDeleteSubAdmins.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GatewayDeleteSubAdmins.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this GatewayDeleteSubAdmins.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GatewayDeleteSubAdmins.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GatewayDeleteSubAdmins.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GatewayDeleteSubAdmins.  # noqa: E501
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
        if not isinstance(other, GatewayDeleteSubAdmins):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayDeleteSubAdmins):
            return True

        return self.to_dict() != other.to_dict()
