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


class GcpTargetDetails(object):
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
        'gcp_service_account_email': 'str',
        'gcp_service_account_key': 'str',
        'gcp_service_account_key_base64': 'str',
        'use_gw_cloud_identity': 'bool'
    }

    attribute_map = {
        'gcp_service_account_email': 'gcp_service_account_email',
        'gcp_service_account_key': 'gcp_service_account_key',
        'gcp_service_account_key_base64': 'gcp_service_account_key_base64',
        'use_gw_cloud_identity': 'use_gw_cloud_identity'
    }

    def __init__(self, gcp_service_account_email=None, gcp_service_account_key=None, gcp_service_account_key_base64=None, use_gw_cloud_identity=None, local_vars_configuration=None):  # noqa: E501
        """GcpTargetDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._gcp_service_account_email = None
        self._gcp_service_account_key = None
        self._gcp_service_account_key_base64 = None
        self._use_gw_cloud_identity = None
        self.discriminator = None

        if gcp_service_account_email is not None:
            self.gcp_service_account_email = gcp_service_account_email
        if gcp_service_account_key is not None:
            self.gcp_service_account_key = gcp_service_account_key
        if gcp_service_account_key_base64 is not None:
            self.gcp_service_account_key_base64 = gcp_service_account_key_base64
        if use_gw_cloud_identity is not None:
            self.use_gw_cloud_identity = use_gw_cloud_identity

    @property
    def gcp_service_account_email(self):
        """Gets the gcp_service_account_email of this GcpTargetDetails.  # noqa: E501

        deprecated  # noqa: E501

        :return: The gcp_service_account_email of this GcpTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._gcp_service_account_email

    @gcp_service_account_email.setter
    def gcp_service_account_email(self, gcp_service_account_email):
        """Sets the gcp_service_account_email of this GcpTargetDetails.

        deprecated  # noqa: E501

        :param gcp_service_account_email: The gcp_service_account_email of this GcpTargetDetails.  # noqa: E501
        :type: str
        """

        self._gcp_service_account_email = gcp_service_account_email

    @property
    def gcp_service_account_key(self):
        """Gets the gcp_service_account_key of this GcpTargetDetails.  # noqa: E501


        :return: The gcp_service_account_key of this GcpTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._gcp_service_account_key

    @gcp_service_account_key.setter
    def gcp_service_account_key(self, gcp_service_account_key):
        """Sets the gcp_service_account_key of this GcpTargetDetails.


        :param gcp_service_account_key: The gcp_service_account_key of this GcpTargetDetails.  # noqa: E501
        :type: str
        """

        self._gcp_service_account_key = gcp_service_account_key

    @property
    def gcp_service_account_key_base64(self):
        """Gets the gcp_service_account_key_base64 of this GcpTargetDetails.  # noqa: E501


        :return: The gcp_service_account_key_base64 of this GcpTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._gcp_service_account_key_base64

    @gcp_service_account_key_base64.setter
    def gcp_service_account_key_base64(self, gcp_service_account_key_base64):
        """Sets the gcp_service_account_key_base64 of this GcpTargetDetails.


        :param gcp_service_account_key_base64: The gcp_service_account_key_base64 of this GcpTargetDetails.  # noqa: E501
        :type: str
        """

        self._gcp_service_account_key_base64 = gcp_service_account_key_base64

    @property
    def use_gw_cloud_identity(self):
        """Gets the use_gw_cloud_identity of this GcpTargetDetails.  # noqa: E501


        :return: The use_gw_cloud_identity of this GcpTargetDetails.  # noqa: E501
        :rtype: bool
        """
        return self._use_gw_cloud_identity

    @use_gw_cloud_identity.setter
    def use_gw_cloud_identity(self, use_gw_cloud_identity):
        """Sets the use_gw_cloud_identity of this GcpTargetDetails.


        :param use_gw_cloud_identity: The use_gw_cloud_identity of this GcpTargetDetails.  # noqa: E501
        :type: bool
        """

        self._use_gw_cloud_identity = use_gw_cloud_identity

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
        if not isinstance(other, GcpTargetDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GcpTargetDetails):
            return True

        return self.to_dict() != other.to_dict()
