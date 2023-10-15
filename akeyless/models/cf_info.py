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


class CfInfo(object):
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
        'cf_name': 'str',
        'description': 'str',
        'hash': 'str',
        'id': 'str'
    }

    attribute_map = {
        'cf_name': 'cf_name',
        'description': 'description',
        'hash': 'hash',
        'id': 'id'
    }

    def __init__(self, cf_name=None, description=None, hash=None, id=None, local_vars_configuration=None):  # noqa: E501
        """CfInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cf_name = None
        self._description = None
        self._hash = None
        self._id = None
        self.discriminator = None

        if cf_name is not None:
            self.cf_name = cf_name
        if description is not None:
            self.description = description
        if hash is not None:
            self.hash = hash
        if id is not None:
            self.id = id

    @property
    def cf_name(self):
        """Gets the cf_name of this CfInfo.  # noqa: E501


        :return: The cf_name of this CfInfo.  # noqa: E501
        :rtype: str
        """
        return self._cf_name

    @cf_name.setter
    def cf_name(self, cf_name):
        """Sets the cf_name of this CfInfo.


        :param cf_name: The cf_name of this CfInfo.  # noqa: E501
        :type: str
        """

        self._cf_name = cf_name

    @property
    def description(self):
        """Gets the description of this CfInfo.  # noqa: E501


        :return: The description of this CfInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CfInfo.


        :param description: The description of this CfInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def hash(self):
        """Gets the hash of this CfInfo.  # noqa: E501


        :return: The hash of this CfInfo.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this CfInfo.


        :param hash: The hash of this CfInfo.  # noqa: E501
        :type: str
        """

        self._hash = hash

    @property
    def id(self):
        """Gets the id of this CfInfo.  # noqa: E501


        :return: The id of this CfInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CfInfo.


        :param id: The id of this CfInfo.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, CfInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CfInfo):
            return True

        return self.to_dict() != other.to_dict()