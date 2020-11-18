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


class Rules(object):
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
        'admin': 'bool',
        'path_rules': 'list[PathRule]'
    }

    attribute_map = {
        'admin': 'admin',
        'path_rules': 'path_rules'
    }

    def __init__(self, admin=None, path_rules=None, local_vars_configuration=None):  # noqa: E501
        """Rules - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._admin = None
        self._path_rules = None
        self.discriminator = None

        if admin is not None:
            self.admin = admin
        if path_rules is not None:
            self.path_rules = path_rules

    @property
    def admin(self):
        """Gets the admin of this Rules.  # noqa: E501

        Is admin  # noqa: E501

        :return: The admin of this Rules.  # noqa: E501
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this Rules.

        Is admin  # noqa: E501

        :param admin: The admin of this Rules.  # noqa: E501
        :type: bool
        """

        self._admin = admin

    @property
    def path_rules(self):
        """Gets the path_rules of this Rules.  # noqa: E501

        The path the rules refers to  # noqa: E501

        :return: The path_rules of this Rules.  # noqa: E501
        :rtype: list[PathRule]
        """
        return self._path_rules

    @path_rules.setter
    def path_rules(self, path_rules):
        """Sets the path_rules of this Rules.

        The path the rules refers to  # noqa: E501

        :param path_rules: The path_rules of this Rules.  # noqa: E501
        :type: list[PathRule]
        """

        self._path_rules = path_rules

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
        if not isinstance(other, Rules):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Rules):
            return True

        return self.to_dict() != other.to_dict()
