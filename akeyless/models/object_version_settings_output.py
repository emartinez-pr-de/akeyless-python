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


class ObjectVersionSettingsOutput(object):
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
        'item_type': 'str',
        'max_versions': 'str'
    }

    attribute_map = {
        'item_type': 'item-type',
        'max_versions': 'max-versions'
    }

    def __init__(self, item_type=None, max_versions=None, local_vars_configuration=None):  # noqa: E501
        """ObjectVersionSettingsOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._item_type = None
        self._max_versions = None
        self.discriminator = None

        if item_type is not None:
            self.item_type = item_type
        if max_versions is not None:
            self.max_versions = max_versions

    @property
    def item_type(self):
        """Gets the item_type of this ObjectVersionSettingsOutput.  # noqa: E501

        VersionSettingsObjectType defines object types for account version settings  # noqa: E501

        :return: The item_type of this ObjectVersionSettingsOutput.  # noqa: E501
        :rtype: str
        """
        return self._item_type

    @item_type.setter
    def item_type(self, item_type):
        """Sets the item_type of this ObjectVersionSettingsOutput.

        VersionSettingsObjectType defines object types for account version settings  # noqa: E501

        :param item_type: The item_type of this ObjectVersionSettingsOutput.  # noqa: E501
        :type: str
        """

        self._item_type = item_type

    @property
    def max_versions(self):
        """Gets the max_versions of this ObjectVersionSettingsOutput.  # noqa: E501


        :return: The max_versions of this ObjectVersionSettingsOutput.  # noqa: E501
        :rtype: str
        """
        return self._max_versions

    @max_versions.setter
    def max_versions(self, max_versions):
        """Sets the max_versions of this ObjectVersionSettingsOutput.


        :param max_versions: The max_versions of this ObjectVersionSettingsOutput.  # noqa: E501
        :type: str
        """

        self._max_versions = max_versions

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
        if not isinstance(other, ObjectVersionSettingsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ObjectVersionSettingsOutput):
            return True

        return self.to_dict() != other.to_dict()