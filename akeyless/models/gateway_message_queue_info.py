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


class GatewayMessageQueueInfo(object):
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
        'mq_type': 'str',
        'queue_name': 'str',
        'queue_url': 'str'
    }

    attribute_map = {
        'mq_type': 'mq_type',
        'queue_name': 'queue_name',
        'queue_url': 'queue_url'
    }

    def __init__(self, mq_type=None, queue_name=None, queue_url=None, local_vars_configuration=None):  # noqa: E501
        """GatewayMessageQueueInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._mq_type = None
        self._queue_name = None
        self._queue_url = None
        self.discriminator = None

        if mq_type is not None:
            self.mq_type = mq_type
        if queue_name is not None:
            self.queue_name = queue_name
        if queue_url is not None:
            self.queue_url = queue_url

    @property
    def mq_type(self):
        """Gets the mq_type of this GatewayMessageQueueInfo.  # noqa: E501


        :return: The mq_type of this GatewayMessageQueueInfo.  # noqa: E501
        :rtype: str
        """
        return self._mq_type

    @mq_type.setter
    def mq_type(self, mq_type):
        """Sets the mq_type of this GatewayMessageQueueInfo.


        :param mq_type: The mq_type of this GatewayMessageQueueInfo.  # noqa: E501
        :type: str
        """

        self._mq_type = mq_type

    @property
    def queue_name(self):
        """Gets the queue_name of this GatewayMessageQueueInfo.  # noqa: E501


        :return: The queue_name of this GatewayMessageQueueInfo.  # noqa: E501
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this GatewayMessageQueueInfo.


        :param queue_name: The queue_name of this GatewayMessageQueueInfo.  # noqa: E501
        :type: str
        """

        self._queue_name = queue_name

    @property
    def queue_url(self):
        """Gets the queue_url of this GatewayMessageQueueInfo.  # noqa: E501


        :return: The queue_url of this GatewayMessageQueueInfo.  # noqa: E501
        :rtype: str
        """
        return self._queue_url

    @queue_url.setter
    def queue_url(self, queue_url):
        """Sets the queue_url of this GatewayMessageQueueInfo.


        :param queue_url: The queue_url of this GatewayMessageQueueInfo.  # noqa: E501
        :type: str
        """

        self._queue_url = queue_url

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
        if not isinstance(other, GatewayMessageQueueInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayMessageQueueInfo):
            return True

        return self.to_dict() != other.to_dict()