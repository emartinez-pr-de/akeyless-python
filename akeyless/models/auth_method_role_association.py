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


class AuthMethodRoleAssociation(object):
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
        'assoc_id': 'str',
        'auth_method_sub_claims': 'dict(str, list[str])',
        'role_name': 'str',
        'rules': 'Rules'
    }

    attribute_map = {
        'assoc_id': 'assoc_id',
        'auth_method_sub_claims': 'auth_method_sub_claims',
        'role_name': 'role_name',
        'rules': 'rules'
    }

    def __init__(self, assoc_id=None, auth_method_sub_claims=None, role_name=None, rules=None, local_vars_configuration=None):  # noqa: E501
        """AuthMethodRoleAssociation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._assoc_id = None
        self._auth_method_sub_claims = None
        self._role_name = None
        self._rules = None
        self.discriminator = None

        if assoc_id is not None:
            self.assoc_id = assoc_id
        if auth_method_sub_claims is not None:
            self.auth_method_sub_claims = auth_method_sub_claims
        if role_name is not None:
            self.role_name = role_name
        if rules is not None:
            self.rules = rules

    @property
    def assoc_id(self):
        """Gets the assoc_id of this AuthMethodRoleAssociation.  # noqa: E501


        :return: The assoc_id of this AuthMethodRoleAssociation.  # noqa: E501
        :rtype: str
        """
        return self._assoc_id

    @assoc_id.setter
    def assoc_id(self, assoc_id):
        """Sets the assoc_id of this AuthMethodRoleAssociation.


        :param assoc_id: The assoc_id of this AuthMethodRoleAssociation.  # noqa: E501
        :type: str
        """

        self._assoc_id = assoc_id

    @property
    def auth_method_sub_claims(self):
        """Gets the auth_method_sub_claims of this AuthMethodRoleAssociation.  # noqa: E501


        :return: The auth_method_sub_claims of this AuthMethodRoleAssociation.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._auth_method_sub_claims

    @auth_method_sub_claims.setter
    def auth_method_sub_claims(self, auth_method_sub_claims):
        """Sets the auth_method_sub_claims of this AuthMethodRoleAssociation.


        :param auth_method_sub_claims: The auth_method_sub_claims of this AuthMethodRoleAssociation.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._auth_method_sub_claims = auth_method_sub_claims

    @property
    def role_name(self):
        """Gets the role_name of this AuthMethodRoleAssociation.  # noqa: E501


        :return: The role_name of this AuthMethodRoleAssociation.  # noqa: E501
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this AuthMethodRoleAssociation.


        :param role_name: The role_name of this AuthMethodRoleAssociation.  # noqa: E501
        :type: str
        """

        self._role_name = role_name

    @property
    def rules(self):
        """Gets the rules of this AuthMethodRoleAssociation.  # noqa: E501


        :return: The rules of this AuthMethodRoleAssociation.  # noqa: E501
        :rtype: Rules
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this AuthMethodRoleAssociation.


        :param rules: The rules of this AuthMethodRoleAssociation.  # noqa: E501
        :type: Rules
        """

        self._rules = rules

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
        if not isinstance(other, AuthMethodRoleAssociation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuthMethodRoleAssociation):
            return True

        return self.to_dict() != other.to_dict()
