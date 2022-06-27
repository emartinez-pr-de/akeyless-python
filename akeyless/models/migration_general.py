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


class MigrationGeneral(object):
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
        'id': 'str',
        'name': 'str',
        'new_name': 'str',
        'prefix': 'str',
        'protection_key': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'new_name': 'new_name',
        'prefix': 'prefix',
        'protection_key': 'protection_key'
    }

    def __init__(self, id=None, name=None, new_name=None, prefix=None, protection_key=None, local_vars_configuration=None):  # noqa: E501
        """MigrationGeneral - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._new_name = None
        self._prefix = None
        self._protection_key = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if new_name is not None:
            self.new_name = new_name
        if prefix is not None:
            self.prefix = prefix
        if protection_key is not None:
            self.protection_key = protection_key

    @property
    def id(self):
        """Gets the id of this MigrationGeneral.  # noqa: E501


        :return: The id of this MigrationGeneral.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MigrationGeneral.


        :param id: The id of this MigrationGeneral.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this MigrationGeneral.  # noqa: E501


        :return: The name of this MigrationGeneral.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MigrationGeneral.


        :param name: The name of this MigrationGeneral.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def new_name(self):
        """Gets the new_name of this MigrationGeneral.  # noqa: E501


        :return: The new_name of this MigrationGeneral.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this MigrationGeneral.


        :param new_name: The new_name of this MigrationGeneral.  # noqa: E501
        :type: str
        """

        self._new_name = new_name

    @property
    def prefix(self):
        """Gets the prefix of this MigrationGeneral.  # noqa: E501


        :return: The prefix of this MigrationGeneral.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this MigrationGeneral.


        :param prefix: The prefix of this MigrationGeneral.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

    @property
    def protection_key(self):
        """Gets the protection_key of this MigrationGeneral.  # noqa: E501


        :return: The protection_key of this MigrationGeneral.  # noqa: E501
        :rtype: str
        """
        return self._protection_key

    @protection_key.setter
    def protection_key(self, protection_key):
        """Sets the protection_key of this MigrationGeneral.


        :param protection_key: The protection_key of this MigrationGeneral.  # noqa: E501
        :type: str
        """

        self._protection_key = protection_key

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
        if not isinstance(other, MigrationGeneral):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MigrationGeneral):
            return True

        return self.to_dict() != other.to_dict()
