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


class ItemSraStatus(object):
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
        'bastion_access_id': 'str',
        'bastion_cluster_name': 'str',
        'bastion_instance_id': 'str',
        'is_in_used': 'bool',
        'session_id': 'str',
        'time': 'datetime'
    }

    attribute_map = {
        'bastion_access_id': 'bastion_access_id',
        'bastion_cluster_name': 'bastion_cluster_name',
        'bastion_instance_id': 'bastion_instance_id',
        'is_in_used': 'is_in_used',
        'session_id': 'session_id',
        'time': 'time'
    }

    def __init__(self, bastion_access_id=None, bastion_cluster_name=None, bastion_instance_id=None, is_in_used=None, session_id=None, time=None, local_vars_configuration=None):  # noqa: E501
        """ItemSraStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bastion_access_id = None
        self._bastion_cluster_name = None
        self._bastion_instance_id = None
        self._is_in_used = None
        self._session_id = None
        self._time = None
        self.discriminator = None

        if bastion_access_id is not None:
            self.bastion_access_id = bastion_access_id
        if bastion_cluster_name is not None:
            self.bastion_cluster_name = bastion_cluster_name
        if bastion_instance_id is not None:
            self.bastion_instance_id = bastion_instance_id
        if is_in_used is not None:
            self.is_in_used = is_in_used
        if session_id is not None:
            self.session_id = session_id
        if time is not None:
            self.time = time

    @property
    def bastion_access_id(self):
        """Gets the bastion_access_id of this ItemSraStatus.  # noqa: E501


        :return: The bastion_access_id of this ItemSraStatus.  # noqa: E501
        :rtype: str
        """
        return self._bastion_access_id

    @bastion_access_id.setter
    def bastion_access_id(self, bastion_access_id):
        """Sets the bastion_access_id of this ItemSraStatus.


        :param bastion_access_id: The bastion_access_id of this ItemSraStatus.  # noqa: E501
        :type: str
        """

        self._bastion_access_id = bastion_access_id

    @property
    def bastion_cluster_name(self):
        """Gets the bastion_cluster_name of this ItemSraStatus.  # noqa: E501


        :return: The bastion_cluster_name of this ItemSraStatus.  # noqa: E501
        :rtype: str
        """
        return self._bastion_cluster_name

    @bastion_cluster_name.setter
    def bastion_cluster_name(self, bastion_cluster_name):
        """Sets the bastion_cluster_name of this ItemSraStatus.


        :param bastion_cluster_name: The bastion_cluster_name of this ItemSraStatus.  # noqa: E501
        :type: str
        """

        self._bastion_cluster_name = bastion_cluster_name

    @property
    def bastion_instance_id(self):
        """Gets the bastion_instance_id of this ItemSraStatus.  # noqa: E501


        :return: The bastion_instance_id of this ItemSraStatus.  # noqa: E501
        :rtype: str
        """
        return self._bastion_instance_id

    @bastion_instance_id.setter
    def bastion_instance_id(self, bastion_instance_id):
        """Sets the bastion_instance_id of this ItemSraStatus.


        :param bastion_instance_id: The bastion_instance_id of this ItemSraStatus.  # noqa: E501
        :type: str
        """

        self._bastion_instance_id = bastion_instance_id

    @property
    def is_in_used(self):
        """Gets the is_in_used of this ItemSraStatus.  # noqa: E501


        :return: The is_in_used of this ItemSraStatus.  # noqa: E501
        :rtype: bool
        """
        return self._is_in_used

    @is_in_used.setter
    def is_in_used(self, is_in_used):
        """Sets the is_in_used of this ItemSraStatus.


        :param is_in_used: The is_in_used of this ItemSraStatus.  # noqa: E501
        :type: bool
        """

        self._is_in_used = is_in_used

    @property
    def session_id(self):
        """Gets the session_id of this ItemSraStatus.  # noqa: E501


        :return: The session_id of this ItemSraStatus.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this ItemSraStatus.


        :param session_id: The session_id of this ItemSraStatus.  # noqa: E501
        :type: str
        """

        self._session_id = session_id

    @property
    def time(self):
        """Gets the time of this ItemSraStatus.  # noqa: E501


        :return: The time of this ItemSraStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ItemSraStatus.


        :param time: The time of this ItemSraStatus.  # noqa: E501
        :type: datetime
        """

        self._time = time

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
        if not isinstance(other, ItemSraStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemSraStatus):
            return True

        return self.to_dict() != other.to_dict()