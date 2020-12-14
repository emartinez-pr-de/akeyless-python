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


class DeleteItemOutput(object):
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
        'deletion_date': 'datetime',
        'item_name': 'str',
        'version_deleted': 'int'
    }

    attribute_map = {
        'deletion_date': 'deletion_date',
        'item_name': 'item_name',
        'version_deleted': 'version_deleted'
    }

    def __init__(self, deletion_date=None, item_name=None, version_deleted=None, local_vars_configuration=None):  # noqa: E501
        """DeleteItemOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._deletion_date = None
        self._item_name = None
        self._version_deleted = None
        self.discriminator = None

        if deletion_date is not None:
            self.deletion_date = deletion_date
        if item_name is not None:
            self.item_name = item_name
        if version_deleted is not None:
            self.version_deleted = version_deleted

    @property
    def deletion_date(self):
        """Gets the deletion_date of this DeleteItemOutput.  # noqa: E501


        :return: The deletion_date of this DeleteItemOutput.  # noqa: E501
        :rtype: datetime
        """
        return self._deletion_date

    @deletion_date.setter
    def deletion_date(self, deletion_date):
        """Sets the deletion_date of this DeleteItemOutput.


        :param deletion_date: The deletion_date of this DeleteItemOutput.  # noqa: E501
        :type: datetime
        """

        self._deletion_date = deletion_date

    @property
    def item_name(self):
        """Gets the item_name of this DeleteItemOutput.  # noqa: E501


        :return: The item_name of this DeleteItemOutput.  # noqa: E501
        :rtype: str
        """
        return self._item_name

    @item_name.setter
    def item_name(self, item_name):
        """Sets the item_name of this DeleteItemOutput.


        :param item_name: The item_name of this DeleteItemOutput.  # noqa: E501
        :type: str
        """

        self._item_name = item_name

    @property
    def version_deleted(self):
        """Gets the version_deleted of this DeleteItemOutput.  # noqa: E501


        :return: The version_deleted of this DeleteItemOutput.  # noqa: E501
        :rtype: int
        """
        return self._version_deleted

    @version_deleted.setter
    def version_deleted(self, version_deleted):
        """Sets the version_deleted of this DeleteItemOutput.


        :param version_deleted: The version_deleted of this DeleteItemOutput.  # noqa: E501
        :type: int
        """

        self._version_deleted = version_deleted

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
        if not isinstance(other, DeleteItemOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeleteItemOutput):
            return True

        return self.to_dict() != other.to_dict()
