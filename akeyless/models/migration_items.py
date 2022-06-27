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


class MigrationItems(object):
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
        'failed': 'int',
        'migrated': 'int',
        'skipped': 'int',
        'total': 'int'
    }

    attribute_map = {
        'failed': 'failed',
        'migrated': 'migrated',
        'skipped': 'skipped',
        'total': 'total'
    }

    def __init__(self, failed=None, migrated=None, skipped=None, total=None, local_vars_configuration=None):  # noqa: E501
        """MigrationItems - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._failed = None
        self._migrated = None
        self._skipped = None
        self._total = None
        self.discriminator = None

        if failed is not None:
            self.failed = failed
        if migrated is not None:
            self.migrated = migrated
        if skipped is not None:
            self.skipped = skipped
        if total is not None:
            self.total = total

    @property
    def failed(self):
        """Gets the failed of this MigrationItems.  # noqa: E501


        :return: The failed of this MigrationItems.  # noqa: E501
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this MigrationItems.


        :param failed: The failed of this MigrationItems.  # noqa: E501
        :type: int
        """

        self._failed = failed

    @property
    def migrated(self):
        """Gets the migrated of this MigrationItems.  # noqa: E501


        :return: The migrated of this MigrationItems.  # noqa: E501
        :rtype: int
        """
        return self._migrated

    @migrated.setter
    def migrated(self, migrated):
        """Sets the migrated of this MigrationItems.


        :param migrated: The migrated of this MigrationItems.  # noqa: E501
        :type: int
        """

        self._migrated = migrated

    @property
    def skipped(self):
        """Gets the skipped of this MigrationItems.  # noqa: E501


        :return: The skipped of this MigrationItems.  # noqa: E501
        :rtype: int
        """
        return self._skipped

    @skipped.setter
    def skipped(self, skipped):
        """Sets the skipped of this MigrationItems.


        :param skipped: The skipped of this MigrationItems.  # noqa: E501
        :type: int
        """

        self._skipped = skipped

    @property
    def total(self):
        """Gets the total of this MigrationItems.  # noqa: E501


        :return: The total of this MigrationItems.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this MigrationItems.


        :param total: The total of this MigrationItems.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if not isinstance(other, MigrationItems):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MigrationItems):
            return True

        return self.to_dict() != other.to_dict()
