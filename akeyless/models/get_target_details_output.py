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


class GetTargetDetailsOutput(object):
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
        'target': 'Target',
        'value': 'TargetTypeDetailsInput'
    }

    attribute_map = {
        'target': 'target',
        'value': 'value'
    }

    def __init__(self, target=None, value=None, local_vars_configuration=None):  # noqa: E501
        """GetTargetDetailsOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._target = None
        self._value = None
        self.discriminator = None

        if target is not None:
            self.target = target
        if value is not None:
            self.value = value

    @property
    def target(self):
        """Gets the target of this GetTargetDetailsOutput.  # noqa: E501


        :return: The target of this GetTargetDetailsOutput.  # noqa: E501
        :rtype: Target
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this GetTargetDetailsOutput.


        :param target: The target of this GetTargetDetailsOutput.  # noqa: E501
        :type: Target
        """

        self._target = target

    @property
    def value(self):
        """Gets the value of this GetTargetDetailsOutput.  # noqa: E501


        :return: The value of this GetTargetDetailsOutput.  # noqa: E501
        :rtype: TargetTypeDetailsInput
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this GetTargetDetailsOutput.


        :param value: The value of this GetTargetDetailsOutput.  # noqa: E501
        :type: TargetTypeDetailsInput
        """

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
        if not isinstance(other, GetTargetDetailsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetTargetDetailsOutput):
            return True

        return self.to_dict() != other.to_dict()
