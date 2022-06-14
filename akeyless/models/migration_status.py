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


class MigrationStatus(object):
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
        'last_messages': 'dict(str, str)',
        'last_reports': 'dict(str, str)',
        'last_statuses': 'dict(str, str)'
    }

    attribute_map = {
        'last_messages': 'last_messages',
        'last_reports': 'last_reports',
        'last_statuses': 'last_statuses'
    }

    def __init__(self, last_messages=None, last_reports=None, last_statuses=None, local_vars_configuration=None):  # noqa: E501
        """MigrationStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._last_messages = None
        self._last_reports = None
        self._last_statuses = None
        self.discriminator = None

        if last_messages is not None:
            self.last_messages = last_messages
        if last_reports is not None:
            self.last_reports = last_reports
        if last_statuses is not None:
            self.last_statuses = last_statuses

    @property
    def last_messages(self):
        """Gets the last_messages of this MigrationStatus.  # noqa: E501


        :return: The last_messages of this MigrationStatus.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._last_messages

    @last_messages.setter
    def last_messages(self, last_messages):
        """Sets the last_messages of this MigrationStatus.


        :param last_messages: The last_messages of this MigrationStatus.  # noqa: E501
        :type: dict(str, str)
        """

        self._last_messages = last_messages

    @property
    def last_reports(self):
        """Gets the last_reports of this MigrationStatus.  # noqa: E501


        :return: The last_reports of this MigrationStatus.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._last_reports

    @last_reports.setter
    def last_reports(self, last_reports):
        """Sets the last_reports of this MigrationStatus.


        :param last_reports: The last_reports of this MigrationStatus.  # noqa: E501
        :type: dict(str, str)
        """

        self._last_reports = last_reports

    @property
    def last_statuses(self):
        """Gets the last_statuses of this MigrationStatus.  # noqa: E501


        :return: The last_statuses of this MigrationStatus.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._last_statuses

    @last_statuses.setter
    def last_statuses(self, last_statuses):
        """Sets the last_statuses of this MigrationStatus.


        :param last_statuses: The last_statuses of this MigrationStatus.  # noqa: E501
        :type: dict(str, str)
        """

        self._last_statuses = last_statuses

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
        if not isinstance(other, MigrationStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MigrationStatus):
            return True

        return self.to_dict() != other.to_dict()
