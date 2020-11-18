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


class UniversalIdentityDetails(object):
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
        'max_depth': 'int',
        'number_of_tokens': 'int',
        'root': 'UIDTokenDetails'
    }

    attribute_map = {
        'max_depth': 'max_depth',
        'number_of_tokens': 'number_of_tokens',
        'root': 'root'
    }

    def __init__(self, max_depth=None, number_of_tokens=None, root=None, local_vars_configuration=None):  # noqa: E501
        """UniversalIdentityDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._max_depth = None
        self._number_of_tokens = None
        self._root = None
        self.discriminator = None

        if max_depth is not None:
            self.max_depth = max_depth
        if number_of_tokens is not None:
            self.number_of_tokens = number_of_tokens
        if root is not None:
            self.root = root

    @property
    def max_depth(self):
        """Gets the max_depth of this UniversalIdentityDetails.  # noqa: E501


        :return: The max_depth of this UniversalIdentityDetails.  # noqa: E501
        :rtype: int
        """
        return self._max_depth

    @max_depth.setter
    def max_depth(self, max_depth):
        """Sets the max_depth of this UniversalIdentityDetails.


        :param max_depth: The max_depth of this UniversalIdentityDetails.  # noqa: E501
        :type: int
        """

        self._max_depth = max_depth

    @property
    def number_of_tokens(self):
        """Gets the number_of_tokens of this UniversalIdentityDetails.  # noqa: E501


        :return: The number_of_tokens of this UniversalIdentityDetails.  # noqa: E501
        :rtype: int
        """
        return self._number_of_tokens

    @number_of_tokens.setter
    def number_of_tokens(self, number_of_tokens):
        """Sets the number_of_tokens of this UniversalIdentityDetails.


        :param number_of_tokens: The number_of_tokens of this UniversalIdentityDetails.  # noqa: E501
        :type: int
        """

        self._number_of_tokens = number_of_tokens

    @property
    def root(self):
        """Gets the root of this UniversalIdentityDetails.  # noqa: E501


        :return: The root of this UniversalIdentityDetails.  # noqa: E501
        :rtype: UIDTokenDetails
        """
        return self._root

    @root.setter
    def root(self, root):
        """Sets the root of this UniversalIdentityDetails.


        :param root: The root of this UniversalIdentityDetails.  # noqa: E501
        :type: UIDTokenDetails
        """

        self._root = root

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
        if not isinstance(other, UniversalIdentityDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UniversalIdentityDetails):
            return True

        return self.to_dict() != other.to_dict()
