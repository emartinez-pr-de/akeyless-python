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


class CacheConfigPart(object):
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
        'cache_enable': 'bool',
        'cache_ttl': 'str',
        'new_proactive_cache_enable': 'bool',
        'proactive_cache_dump_interval': 'str',
        'proactive_cache_enable': 'bool',
        'proactive_cache_minimum_fetching_time': 'str'
    }

    attribute_map = {
        'cache_enable': 'cache_enable',
        'cache_ttl': 'cache_ttl',
        'new_proactive_cache_enable': 'new_proactive_cache_enable',
        'proactive_cache_dump_interval': 'proactive_cache_dump_interval',
        'proactive_cache_enable': 'proactive_cache_enable',
        'proactive_cache_minimum_fetching_time': 'proactive_cache_minimum_fetching_time'
    }

    def __init__(self, cache_enable=None, cache_ttl=None, new_proactive_cache_enable=None, proactive_cache_dump_interval=None, proactive_cache_enable=None, proactive_cache_minimum_fetching_time=None, local_vars_configuration=None):  # noqa: E501
        """CacheConfigPart - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cache_enable = None
        self._cache_ttl = None
        self._new_proactive_cache_enable = None
        self._proactive_cache_dump_interval = None
        self._proactive_cache_enable = None
        self._proactive_cache_minimum_fetching_time = None
        self.discriminator = None

        if cache_enable is not None:
            self.cache_enable = cache_enable
        if cache_ttl is not None:
            self.cache_ttl = cache_ttl
        if new_proactive_cache_enable is not None:
            self.new_proactive_cache_enable = new_proactive_cache_enable
        if proactive_cache_dump_interval is not None:
            self.proactive_cache_dump_interval = proactive_cache_dump_interval
        if proactive_cache_enable is not None:
            self.proactive_cache_enable = proactive_cache_enable
        if proactive_cache_minimum_fetching_time is not None:
            self.proactive_cache_minimum_fetching_time = proactive_cache_minimum_fetching_time

    @property
    def cache_enable(self):
        """Gets the cache_enable of this CacheConfigPart.  # noqa: E501


        :return: The cache_enable of this CacheConfigPart.  # noqa: E501
        :rtype: bool
        """
        return self._cache_enable

    @cache_enable.setter
    def cache_enable(self, cache_enable):
        """Sets the cache_enable of this CacheConfigPart.


        :param cache_enable: The cache_enable of this CacheConfigPart.  # noqa: E501
        :type: bool
        """

        self._cache_enable = cache_enable

    @property
    def cache_ttl(self):
        """Gets the cache_ttl of this CacheConfigPart.  # noqa: E501


        :return: The cache_ttl of this CacheConfigPart.  # noqa: E501
        :rtype: str
        """
        return self._cache_ttl

    @cache_ttl.setter
    def cache_ttl(self, cache_ttl):
        """Sets the cache_ttl of this CacheConfigPart.


        :param cache_ttl: The cache_ttl of this CacheConfigPart.  # noqa: E501
        :type: str
        """

        self._cache_ttl = cache_ttl

    @property
    def new_proactive_cache_enable(self):
        """Gets the new_proactive_cache_enable of this CacheConfigPart.  # noqa: E501


        :return: The new_proactive_cache_enable of this CacheConfigPart.  # noqa: E501
        :rtype: bool
        """
        return self._new_proactive_cache_enable

    @new_proactive_cache_enable.setter
    def new_proactive_cache_enable(self, new_proactive_cache_enable):
        """Sets the new_proactive_cache_enable of this CacheConfigPart.


        :param new_proactive_cache_enable: The new_proactive_cache_enable of this CacheConfigPart.  # noqa: E501
        :type: bool
        """

        self._new_proactive_cache_enable = new_proactive_cache_enable

    @property
    def proactive_cache_dump_interval(self):
        """Gets the proactive_cache_dump_interval of this CacheConfigPart.  # noqa: E501


        :return: The proactive_cache_dump_interval of this CacheConfigPart.  # noqa: E501
        :rtype: str
        """
        return self._proactive_cache_dump_interval

    @proactive_cache_dump_interval.setter
    def proactive_cache_dump_interval(self, proactive_cache_dump_interval):
        """Sets the proactive_cache_dump_interval of this CacheConfigPart.


        :param proactive_cache_dump_interval: The proactive_cache_dump_interval of this CacheConfigPart.  # noqa: E501
        :type: str
        """

        self._proactive_cache_dump_interval = proactive_cache_dump_interval

    @property
    def proactive_cache_enable(self):
        """Gets the proactive_cache_enable of this CacheConfigPart.  # noqa: E501


        :return: The proactive_cache_enable of this CacheConfigPart.  # noqa: E501
        :rtype: bool
        """
        return self._proactive_cache_enable

    @proactive_cache_enable.setter
    def proactive_cache_enable(self, proactive_cache_enable):
        """Sets the proactive_cache_enable of this CacheConfigPart.


        :param proactive_cache_enable: The proactive_cache_enable of this CacheConfigPart.  # noqa: E501
        :type: bool
        """

        self._proactive_cache_enable = proactive_cache_enable

    @property
    def proactive_cache_minimum_fetching_time(self):
        """Gets the proactive_cache_minimum_fetching_time of this CacheConfigPart.  # noqa: E501


        :return: The proactive_cache_minimum_fetching_time of this CacheConfigPart.  # noqa: E501
        :rtype: str
        """
        return self._proactive_cache_minimum_fetching_time

    @proactive_cache_minimum_fetching_time.setter
    def proactive_cache_minimum_fetching_time(self, proactive_cache_minimum_fetching_time):
        """Sets the proactive_cache_minimum_fetching_time of this CacheConfigPart.


        :param proactive_cache_minimum_fetching_time: The proactive_cache_minimum_fetching_time of this CacheConfigPart.  # noqa: E501
        :type: str
        """

        self._proactive_cache_minimum_fetching_time = proactive_cache_minimum_fetching_time

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
        if not isinstance(other, CacheConfigPart):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CacheConfigPart):
            return True

        return self.to_dict() != other.to_dict()
