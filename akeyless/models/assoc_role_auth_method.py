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


class AssocRoleAuthMethod(object):
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
        'am_name': 'str',
        'role_name': 'str',
        'sub_claims': 'dict(str, str)',
        'token': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'am_name': 'am-name',
        'role_name': 'role-name',
        'sub_claims': 'sub-claims',
        'token': 'token',
        'uid_token': 'uid-token'
    }

    def __init__(self, am_name=None, role_name=None, sub_claims=None, token=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """AssocRoleAuthMethod - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._am_name = None
        self._role_name = None
        self._sub_claims = None
        self._token = None
        self._uid_token = None
        self.discriminator = None

        self.am_name = am_name
        self.role_name = role_name
        if sub_claims is not None:
            self.sub_claims = sub_claims
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def am_name(self):
        """Gets the am_name of this AssocRoleAuthMethod.  # noqa: E501

        The auth method to associate  # noqa: E501

        :return: The am_name of this AssocRoleAuthMethod.  # noqa: E501
        :rtype: str
        """
        return self._am_name

    @am_name.setter
    def am_name(self, am_name):
        """Sets the am_name of this AssocRoleAuthMethod.

        The auth method to associate  # noqa: E501

        :param am_name: The am_name of this AssocRoleAuthMethod.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and am_name is None:  # noqa: E501
            raise ValueError("Invalid value for `am_name`, must not be `None`")  # noqa: E501

        self._am_name = am_name

    @property
    def role_name(self):
        """Gets the role_name of this AssocRoleAuthMethod.  # noqa: E501

        The role to associate  # noqa: E501

        :return: The role_name of this AssocRoleAuthMethod.  # noqa: E501
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this AssocRoleAuthMethod.

        The role to associate  # noqa: E501

        :param role_name: The role_name of this AssocRoleAuthMethod.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and role_name is None:  # noqa: E501
            raise ValueError("Invalid value for `role_name`, must not be `None`")  # noqa: E501

        self._role_name = role_name

    @property
    def sub_claims(self):
        """Gets the sub_claims of this AssocRoleAuthMethod.  # noqa: E501

        key/val of sub claims, e.g group=admins,developers  # noqa: E501

        :return: The sub_claims of this AssocRoleAuthMethod.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._sub_claims

    @sub_claims.setter
    def sub_claims(self, sub_claims):
        """Sets the sub_claims of this AssocRoleAuthMethod.

        key/val of sub claims, e.g group=admins,developers  # noqa: E501

        :param sub_claims: The sub_claims of this AssocRoleAuthMethod.  # noqa: E501
        :type: dict(str, str)
        """

        self._sub_claims = sub_claims

    @property
    def token(self):
        """Gets the token of this AssocRoleAuthMethod.  # noqa: E501

        Use a specific profile from your akeyless/profiles/ folder  # noqa: E501

        :return: The token of this AssocRoleAuthMethod.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this AssocRoleAuthMethod.

        Use a specific profile from your akeyless/profiles/ folder  # noqa: E501

        :param token: The token of this AssocRoleAuthMethod.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this AssocRoleAuthMethod.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this AssocRoleAuthMethod.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this AssocRoleAuthMethod.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this AssocRoleAuthMethod.  # noqa: E501
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
        if not isinstance(other, AssocRoleAuthMethod):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssocRoleAuthMethod):
            return True

        return self.to_dict() != other.to_dict()
