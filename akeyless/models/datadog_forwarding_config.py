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


class DatadogForwardingConfig(object):
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
        'datadog_api_key': 'str',
        'datadog_host': 'str',
        'datadog_log_service': 'str',
        'datadog_log_source': 'str',
        'datadog_log_tags': 'str'
    }

    attribute_map = {
        'datadog_api_key': 'datadog_api_key',
        'datadog_host': 'datadog_host',
        'datadog_log_service': 'datadog_log_service',
        'datadog_log_source': 'datadog_log_source',
        'datadog_log_tags': 'datadog_log_tags'
    }

    def __init__(self, datadog_api_key=None, datadog_host=None, datadog_log_service=None, datadog_log_source=None, datadog_log_tags=None, local_vars_configuration=None):  # noqa: E501
        """DatadogForwardingConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._datadog_api_key = None
        self._datadog_host = None
        self._datadog_log_service = None
        self._datadog_log_source = None
        self._datadog_log_tags = None
        self.discriminator = None

        if datadog_api_key is not None:
            self.datadog_api_key = datadog_api_key
        if datadog_host is not None:
            self.datadog_host = datadog_host
        if datadog_log_service is not None:
            self.datadog_log_service = datadog_log_service
        if datadog_log_source is not None:
            self.datadog_log_source = datadog_log_source
        if datadog_log_tags is not None:
            self.datadog_log_tags = datadog_log_tags

    @property
    def datadog_api_key(self):
        """Gets the datadog_api_key of this DatadogForwardingConfig.  # noqa: E501


        :return: The datadog_api_key of this DatadogForwardingConfig.  # noqa: E501
        :rtype: str
        """
        return self._datadog_api_key

    @datadog_api_key.setter
    def datadog_api_key(self, datadog_api_key):
        """Sets the datadog_api_key of this DatadogForwardingConfig.


        :param datadog_api_key: The datadog_api_key of this DatadogForwardingConfig.  # noqa: E501
        :type: str
        """

        self._datadog_api_key = datadog_api_key

    @property
    def datadog_host(self):
        """Gets the datadog_host of this DatadogForwardingConfig.  # noqa: E501


        :return: The datadog_host of this DatadogForwardingConfig.  # noqa: E501
        :rtype: str
        """
        return self._datadog_host

    @datadog_host.setter
    def datadog_host(self, datadog_host):
        """Sets the datadog_host of this DatadogForwardingConfig.


        :param datadog_host: The datadog_host of this DatadogForwardingConfig.  # noqa: E501
        :type: str
        """

        self._datadog_host = datadog_host

    @property
    def datadog_log_service(self):
        """Gets the datadog_log_service of this DatadogForwardingConfig.  # noqa: E501


        :return: The datadog_log_service of this DatadogForwardingConfig.  # noqa: E501
        :rtype: str
        """
        return self._datadog_log_service

    @datadog_log_service.setter
    def datadog_log_service(self, datadog_log_service):
        """Sets the datadog_log_service of this DatadogForwardingConfig.


        :param datadog_log_service: The datadog_log_service of this DatadogForwardingConfig.  # noqa: E501
        :type: str
        """

        self._datadog_log_service = datadog_log_service

    @property
    def datadog_log_source(self):
        """Gets the datadog_log_source of this DatadogForwardingConfig.  # noqa: E501


        :return: The datadog_log_source of this DatadogForwardingConfig.  # noqa: E501
        :rtype: str
        """
        return self._datadog_log_source

    @datadog_log_source.setter
    def datadog_log_source(self, datadog_log_source):
        """Sets the datadog_log_source of this DatadogForwardingConfig.


        :param datadog_log_source: The datadog_log_source of this DatadogForwardingConfig.  # noqa: E501
        :type: str
        """

        self._datadog_log_source = datadog_log_source

    @property
    def datadog_log_tags(self):
        """Gets the datadog_log_tags of this DatadogForwardingConfig.  # noqa: E501


        :return: The datadog_log_tags of this DatadogForwardingConfig.  # noqa: E501
        :rtype: str
        """
        return self._datadog_log_tags

    @datadog_log_tags.setter
    def datadog_log_tags(self, datadog_log_tags):
        """Sets the datadog_log_tags of this DatadogForwardingConfig.


        :param datadog_log_tags: The datadog_log_tags of this DatadogForwardingConfig.  # noqa: E501
        :type: str
        """

        self._datadog_log_tags = datadog_log_tags

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
        if not isinstance(other, DatadogForwardingConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DatadogForwardingConfig):
            return True

        return self.to_dict() != other.to_dict()
