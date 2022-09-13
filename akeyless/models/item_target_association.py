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


class ItemTargetAssociation(object):
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
        'target_id': 'int',
        'target_name': 'str',
        'target_type': 'str'
    }

    attribute_map = {
        'assoc_id': 'assoc_id',
        'target_id': 'target_id',
        'target_name': 'target_name',
        'target_type': 'target_type'
    }

    def __init__(self, assoc_id=None, target_id=None, target_name=None, target_type=None, local_vars_configuration=None):  # noqa: E501
        """ItemTargetAssociation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._assoc_id = None
        self._target_id = None
        self._target_name = None
        self._target_type = None
        self.discriminator = None

        if assoc_id is not None:
            self.assoc_id = assoc_id
        if target_id is not None:
            self.target_id = target_id
        if target_name is not None:
            self.target_name = target_name
        if target_type is not None:
            self.target_type = target_type

    @property
    def assoc_id(self):
        """Gets the assoc_id of this ItemTargetAssociation.  # noqa: E501


        :return: The assoc_id of this ItemTargetAssociation.  # noqa: E501
        :rtype: str
        """
        return self._assoc_id

    @assoc_id.setter
    def assoc_id(self, assoc_id):
        """Sets the assoc_id of this ItemTargetAssociation.


        :param assoc_id: The assoc_id of this ItemTargetAssociation.  # noqa: E501
        :type: str
        """

        self._assoc_id = assoc_id

    @property
    def target_id(self):
        """Gets the target_id of this ItemTargetAssociation.  # noqa: E501


        :return: The target_id of this ItemTargetAssociation.  # noqa: E501
        :rtype: int
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this ItemTargetAssociation.


        :param target_id: The target_id of this ItemTargetAssociation.  # noqa: E501
        :type: int
        """

        self._target_id = target_id

    @property
    def target_name(self):
        """Gets the target_name of this ItemTargetAssociation.  # noqa: E501


        :return: The target_name of this ItemTargetAssociation.  # noqa: E501
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """Sets the target_name of this ItemTargetAssociation.


        :param target_name: The target_name of this ItemTargetAssociation.  # noqa: E501
        :type: str
        """

        self._target_name = target_name

    @property
    def target_type(self):
        """Gets the target_type of this ItemTargetAssociation.  # noqa: E501


        :return: The target_type of this ItemTargetAssociation.  # noqa: E501
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """Sets the target_type of this ItemTargetAssociation.


        :param target_type: The target_type of this ItemTargetAssociation.  # noqa: E501
        :type: str
        """

        self._target_type = target_type

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
        if not isinstance(other, ItemTargetAssociation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemTargetAssociation):
            return True

        return self.to_dict() != other.to_dict()
