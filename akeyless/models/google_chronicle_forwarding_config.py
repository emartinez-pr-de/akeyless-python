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


class GoogleChronicleForwardingConfig(object):
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
        'customer_id': 'str',
        'log_type': 'str',
        'region': 'str',
        'service_account_key': 'str'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'log_type': 'log_type',
        'region': 'region',
        'service_account_key': 'service_account_key'
    }

    def __init__(self, customer_id=None, log_type=None, region=None, service_account_key=None, local_vars_configuration=None):  # noqa: E501
        """GoogleChronicleForwardingConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._customer_id = None
        self._log_type = None
        self._region = None
        self._service_account_key = None
        self.discriminator = None

        if customer_id is not None:
            self.customer_id = customer_id
        if log_type is not None:
            self.log_type = log_type
        if region is not None:
            self.region = region
        if service_account_key is not None:
            self.service_account_key = service_account_key

    @property
    def customer_id(self):
        """Gets the customer_id of this GoogleChronicleForwardingConfig.  # noqa: E501


        :return: The customer_id of this GoogleChronicleForwardingConfig.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this GoogleChronicleForwardingConfig.


        :param customer_id: The customer_id of this GoogleChronicleForwardingConfig.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def log_type(self):
        """Gets the log_type of this GoogleChronicleForwardingConfig.  # noqa: E501


        :return: The log_type of this GoogleChronicleForwardingConfig.  # noqa: E501
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        """Sets the log_type of this GoogleChronicleForwardingConfig.


        :param log_type: The log_type of this GoogleChronicleForwardingConfig.  # noqa: E501
        :type: str
        """

        self._log_type = log_type

    @property
    def region(self):
        """Gets the region of this GoogleChronicleForwardingConfig.  # noqa: E501


        :return: The region of this GoogleChronicleForwardingConfig.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this GoogleChronicleForwardingConfig.


        :param region: The region of this GoogleChronicleForwardingConfig.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def service_account_key(self):
        """Gets the service_account_key of this GoogleChronicleForwardingConfig.  # noqa: E501


        :return: The service_account_key of this GoogleChronicleForwardingConfig.  # noqa: E501
        :rtype: str
        """
        return self._service_account_key

    @service_account_key.setter
    def service_account_key(self, service_account_key):
        """Sets the service_account_key of this GoogleChronicleForwardingConfig.


        :param service_account_key: The service_account_key of this GoogleChronicleForwardingConfig.  # noqa: E501
        :type: str
        """

        self._service_account_key = service_account_key

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
        if not isinstance(other, GoogleChronicleForwardingConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GoogleChronicleForwardingConfig):
            return True

        return self.to_dict() != other.to_dict()