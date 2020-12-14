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


class ClientData(object):
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
        'client_certificate_data': 'str',
        'client_key_data': 'str'
    }

    attribute_map = {
        'client_certificate_data': 'clientCertificateData',
        'client_key_data': 'clientKeyData'
    }

    def __init__(self, client_certificate_data=None, client_key_data=None, local_vars_configuration=None):  # noqa: E501
        """ClientData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._client_certificate_data = None
        self._client_key_data = None
        self.discriminator = None

        if client_certificate_data is not None:
            self.client_certificate_data = client_certificate_data
        if client_key_data is not None:
            self.client_key_data = client_key_data

    @property
    def client_certificate_data(self):
        """Gets the client_certificate_data of this ClientData.  # noqa: E501


        :return: The client_certificate_data of this ClientData.  # noqa: E501
        :rtype: str
        """
        return self._client_certificate_data

    @client_certificate_data.setter
    def client_certificate_data(self, client_certificate_data):
        """Sets the client_certificate_data of this ClientData.


        :param client_certificate_data: The client_certificate_data of this ClientData.  # noqa: E501
        :type: str
        """

        self._client_certificate_data = client_certificate_data

    @property
    def client_key_data(self):
        """Gets the client_key_data of this ClientData.  # noqa: E501


        :return: The client_key_data of this ClientData.  # noqa: E501
        :rtype: str
        """
        return self._client_key_data

    @client_key_data.setter
    def client_key_data(self, client_key_data):
        """Sets the client_key_data of this ClientData.


        :param client_key_data: The client_key_data of this ClientData.  # noqa: E501
        :type: str
        """

        self._client_key_data = client_key_data

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
        if not isinstance(other, ClientData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClientData):
            return True

        return self.to_dict() != other.to_dict()
