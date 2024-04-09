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


class CertificateVersionInfo(object):
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
        'not_after': 'datetime',
        'not_before': 'datetime',
        'status': 'str'
    }

    attribute_map = {
        'not_after': 'not_after',
        'not_before': 'not_before',
        'status': 'status'
    }

    def __init__(self, not_after=None, not_before=None, status=None, local_vars_configuration=None):  # noqa: E501
        """CertificateVersionInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._not_after = None
        self._not_before = None
        self._status = None
        self.discriminator = None

        if not_after is not None:
            self.not_after = not_after
        if not_before is not None:
            self.not_before = not_before
        if status is not None:
            self.status = status

    @property
    def not_after(self):
        """Gets the not_after of this CertificateVersionInfo.  # noqa: E501


        :return: The not_after of this CertificateVersionInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._not_after

    @not_after.setter
    def not_after(self, not_after):
        """Sets the not_after of this CertificateVersionInfo.


        :param not_after: The not_after of this CertificateVersionInfo.  # noqa: E501
        :type: datetime
        """

        self._not_after = not_after

    @property
    def not_before(self):
        """Gets the not_before of this CertificateVersionInfo.  # noqa: E501


        :return: The not_before of this CertificateVersionInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._not_before

    @not_before.setter
    def not_before(self, not_before):
        """Sets the not_before of this CertificateVersionInfo.


        :param not_before: The not_before of this CertificateVersionInfo.  # noqa: E501
        :type: datetime
        """

        self._not_before = not_before

    @property
    def status(self):
        """Gets the status of this CertificateVersionInfo.  # noqa: E501


        :return: The status of this CertificateVersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CertificateVersionInfo.


        :param status: The status of this CertificateVersionInfo.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if not isinstance(other, CertificateVersionInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CertificateVersionInfo):
            return True

        return self.to_dict() != other.to_dict()