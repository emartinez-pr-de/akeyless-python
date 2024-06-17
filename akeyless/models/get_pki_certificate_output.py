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


class GetPKICertificateOutput(object):
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
        'cert_display_id': 'str',
        'cert_item_id': 'int',
        'data': 'str',
        'parent_cert': 'str',
        'path': 'str',
        'reading_token': 'str'
    }

    attribute_map = {
        'cert_display_id': 'cert_display_id',
        'cert_item_id': 'cert_item_id',
        'data': 'data',
        'parent_cert': 'parent_cert',
        'path': 'path',
        'reading_token': 'reading_token'
    }

    def __init__(self, cert_display_id=None, cert_item_id=None, data=None, parent_cert=None, path=None, reading_token=None, local_vars_configuration=None):  # noqa: E501
        """GetPKICertificateOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cert_display_id = None
        self._cert_item_id = None
        self._data = None
        self._parent_cert = None
        self._path = None
        self._reading_token = None
        self.discriminator = None

        if cert_display_id is not None:
            self.cert_display_id = cert_display_id
        if cert_item_id is not None:
            self.cert_item_id = cert_item_id
        if data is not None:
            self.data = data
        if parent_cert is not None:
            self.parent_cert = parent_cert
        if path is not None:
            self.path = path
        if reading_token is not None:
            self.reading_token = reading_token

    @property
    def cert_display_id(self):
        """Gets the cert_display_id of this GetPKICertificateOutput.  # noqa: E501


        :return: The cert_display_id of this GetPKICertificateOutput.  # noqa: E501
        :rtype: str
        """
        return self._cert_display_id

    @cert_display_id.setter
    def cert_display_id(self, cert_display_id):
        """Sets the cert_display_id of this GetPKICertificateOutput.


        :param cert_display_id: The cert_display_id of this GetPKICertificateOutput.  # noqa: E501
        :type: str
        """

        self._cert_display_id = cert_display_id

    @property
    def cert_item_id(self):
        """Gets the cert_item_id of this GetPKICertificateOutput.  # noqa: E501


        :return: The cert_item_id of this GetPKICertificateOutput.  # noqa: E501
        :rtype: int
        """
        return self._cert_item_id

    @cert_item_id.setter
    def cert_item_id(self, cert_item_id):
        """Sets the cert_item_id of this GetPKICertificateOutput.


        :param cert_item_id: The cert_item_id of this GetPKICertificateOutput.  # noqa: E501
        :type: int
        """

        self._cert_item_id = cert_item_id

    @property
    def data(self):
        """Gets the data of this GetPKICertificateOutput.  # noqa: E501


        :return: The data of this GetPKICertificateOutput.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this GetPKICertificateOutput.


        :param data: The data of this GetPKICertificateOutput.  # noqa: E501
        :type: str
        """

        self._data = data

    @property
    def parent_cert(self):
        """Gets the parent_cert of this GetPKICertificateOutput.  # noqa: E501


        :return: The parent_cert of this GetPKICertificateOutput.  # noqa: E501
        :rtype: str
        """
        return self._parent_cert

    @parent_cert.setter
    def parent_cert(self, parent_cert):
        """Sets the parent_cert of this GetPKICertificateOutput.


        :param parent_cert: The parent_cert of this GetPKICertificateOutput.  # noqa: E501
        :type: str
        """

        self._parent_cert = parent_cert

    @property
    def path(self):
        """Gets the path of this GetPKICertificateOutput.  # noqa: E501


        :return: The path of this GetPKICertificateOutput.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this GetPKICertificateOutput.


        :param path: The path of this GetPKICertificateOutput.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def reading_token(self):
        """Gets the reading_token of this GetPKICertificateOutput.  # noqa: E501


        :return: The reading_token of this GetPKICertificateOutput.  # noqa: E501
        :rtype: str
        """
        return self._reading_token

    @reading_token.setter
    def reading_token(self, reading_token):
        """Sets the reading_token of this GetPKICertificateOutput.


        :param reading_token: The reading_token of this GetPKICertificateOutput.  # noqa: E501
        :type: str
        """

        self._reading_token = reading_token

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
        if not isinstance(other, GetPKICertificateOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetPKICertificateOutput):
            return True

        return self.to_dict() != other.to_dict()
