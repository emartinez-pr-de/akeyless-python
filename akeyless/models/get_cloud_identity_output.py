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


class GetCloudIdentityOutput(object):
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
        'provider': 'str',
        'token': 'str'
    }

    attribute_map = {
        'provider': 'provider',
        'token': 'token'
    }

    def __init__(self, provider=None, token=None, local_vars_configuration=None):  # noqa: E501
        """GetCloudIdentityOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._provider = None
        self._token = None
        self.discriminator = None

        if provider is not None:
            self.provider = provider
        if token is not None:
            self.token = token

    @property
    def provider(self):
        """Gets the provider of this GetCloudIdentityOutput.  # noqa: E501


        :return: The provider of this GetCloudIdentityOutput.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this GetCloudIdentityOutput.


        :param provider: The provider of this GetCloudIdentityOutput.  # noqa: E501
        :type: str
        """

        self._provider = provider

    @property
    def token(self):
        """Gets the token of this GetCloudIdentityOutput.  # noqa: E501


        :return: The token of this GetCloudIdentityOutput.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GetCloudIdentityOutput.


        :param token: The token of this GetCloudIdentityOutput.  # noqa: E501
        :type: str
        """

        self._token = token

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
        if not isinstance(other, GetCloudIdentityOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetCloudIdentityOutput):
            return True

        return self.to_dict() != other.to_dict()
