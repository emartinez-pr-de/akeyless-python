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


class SetRoleRule(object):
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
        'capability': 'list[str]',
        'path': 'str',
        'role_name': 'str',
        'rule_type': 'str',
        'token': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'capability': 'capability',
        'path': 'path',
        'role_name': 'role-name',
        'rule_type': 'rule-type',
        'token': 'token',
        'uid_token': 'uid-token'
    }

    def __init__(self, capability=None, path=None, role_name=None, rule_type='item-rule', token=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """SetRoleRule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._capability = None
        self._path = None
        self._role_name = None
        self._rule_type = None
        self._token = None
        self._uid_token = None
        self.discriminator = None

        self.capability = capability
        self.path = path
        self.role_name = role_name
        if rule_type is not None:
            self.rule_type = rule_type
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def capability(self):
        """Gets the capability of this SetRoleRule.  # noqa: E501

        List of the approved/denied capabilities in the path options: [read, create, update, delete, list, deny]  # noqa: E501

        :return: The capability of this SetRoleRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._capability

    @capability.setter
    def capability(self, capability):
        """Sets the capability of this SetRoleRule.

        List of the approved/denied capabilities in the path options: [read, create, update, delete, list, deny]  # noqa: E501

        :param capability: The capability of this SetRoleRule.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and capability is None:  # noqa: E501
            raise ValueError("Invalid value for `capability`, must not be `None`")  # noqa: E501

        self._capability = capability

    @property
    def path(self):
        """Gets the path of this SetRoleRule.  # noqa: E501

        The path the rule refers to  # noqa: E501

        :return: The path of this SetRoleRule.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this SetRoleRule.

        The path the rule refers to  # noqa: E501

        :param path: The path of this SetRoleRule.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and path is None:  # noqa: E501
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def role_name(self):
        """Gets the role_name of this SetRoleRule.  # noqa: E501

        The role name to be updated  # noqa: E501

        :return: The role_name of this SetRoleRule.  # noqa: E501
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this SetRoleRule.

        The role name to be updated  # noqa: E501

        :param role_name: The role_name of this SetRoleRule.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and role_name is None:  # noqa: E501
            raise ValueError("Invalid value for `role_name`, must not be `None`")  # noqa: E501

        self._role_name = role_name

    @property
    def rule_type(self):
        """Gets the rule_type of this SetRoleRule.  # noqa: E501

        item-rule, role-rule or auth-method-rule  # noqa: E501

        :return: The rule_type of this SetRoleRule.  # noqa: E501
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """Sets the rule_type of this SetRoleRule.

        item-rule, role-rule or auth-method-rule  # noqa: E501

        :param rule_type: The rule_type of this SetRoleRule.  # noqa: E501
        :type: str
        """

        self._rule_type = rule_type

    @property
    def token(self):
        """Gets the token of this SetRoleRule.  # noqa: E501

        Use a specific profile from your akeyless/profiles/ folder  # noqa: E501

        :return: The token of this SetRoleRule.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this SetRoleRule.

        Use a specific profile from your akeyless/profiles/ folder  # noqa: E501

        :param token: The token of this SetRoleRule.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this SetRoleRule.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this SetRoleRule.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this SetRoleRule.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this SetRoleRule.  # noqa: E501
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
        if not isinstance(other, SetRoleRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SetRoleRule):
            return True

        return self.to_dict() != other.to_dict()
