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


class DynamicSecretProducerInfo(object):
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
        'producer_metadata': 'str',
        'producer_status': 'str',
        'producer_type': 'str'
    }

    attribute_map = {
        'producer_metadata': 'producer_metadata',
        'producer_status': 'producer_status',
        'producer_type': 'producer_type'
    }

    def __init__(self, producer_metadata=None, producer_status=None, producer_type=None, local_vars_configuration=None):  # noqa: E501
        """DynamicSecretProducerInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._producer_metadata = None
        self._producer_status = None
        self._producer_type = None
        self.discriminator = None

        if producer_metadata is not None:
            self.producer_metadata = producer_metadata
        if producer_status is not None:
            self.producer_status = producer_status
        if producer_type is not None:
            self.producer_type = producer_type

    @property
    def producer_metadata(self):
        """Gets the producer_metadata of this DynamicSecretProducerInfo.  # noqa: E501


        :return: The producer_metadata of this DynamicSecretProducerInfo.  # noqa: E501
        :rtype: str
        """
        return self._producer_metadata

    @producer_metadata.setter
    def producer_metadata(self, producer_metadata):
        """Sets the producer_metadata of this DynamicSecretProducerInfo.


        :param producer_metadata: The producer_metadata of this DynamicSecretProducerInfo.  # noqa: E501
        :type: str
        """

        self._producer_metadata = producer_metadata

    @property
    def producer_status(self):
        """Gets the producer_status of this DynamicSecretProducerInfo.  # noqa: E501

        ProducerStatus defines types of Producer Status  # noqa: E501

        :return: The producer_status of this DynamicSecretProducerInfo.  # noqa: E501
        :rtype: str
        """
        return self._producer_status

    @producer_status.setter
    def producer_status(self, producer_status):
        """Sets the producer_status of this DynamicSecretProducerInfo.

        ProducerStatus defines types of Producer Status  # noqa: E501

        :param producer_status: The producer_status of this DynamicSecretProducerInfo.  # noqa: E501
        :type: str
        """

        self._producer_status = producer_status

    @property
    def producer_type(self):
        """Gets the producer_type of this DynamicSecretProducerInfo.  # noqa: E501


        :return: The producer_type of this DynamicSecretProducerInfo.  # noqa: E501
        :rtype: str
        """
        return self._producer_type

    @producer_type.setter
    def producer_type(self, producer_type):
        """Sets the producer_type of this DynamicSecretProducerInfo.


        :param producer_type: The producer_type of this DynamicSecretProducerInfo.  # noqa: E501
        :type: str
        """

        self._producer_type = producer_type

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
        if not isinstance(other, DynamicSecretProducerInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DynamicSecretProducerInfo):
            return True

        return self.to_dict() != other.to_dict()
