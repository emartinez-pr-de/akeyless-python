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


class GetCloudIdentity(object):
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
        'azure_ad_object_id': 'str',
        'debug': 'bool',
        'gcp_audience': 'str',
        'url_safe': 'bool'
    }

    attribute_map = {
        'azure_ad_object_id': 'azure_ad_object_id',
        'debug': 'debug',
        'gcp_audience': 'gcp-audience',
        'url_safe': 'url_safe'
    }

    def __init__(self, azure_ad_object_id=None, debug=None, gcp_audience=None, url_safe=None, local_vars_configuration=None):  # noqa: E501
        """GetCloudIdentity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._azure_ad_object_id = None
        self._debug = None
        self._gcp_audience = None
        self._url_safe = None
        self.discriminator = None

        if azure_ad_object_id is not None:
            self.azure_ad_object_id = azure_ad_object_id
        if debug is not None:
            self.debug = debug
        if gcp_audience is not None:
            self.gcp_audience = gcp_audience
        if url_safe is not None:
            self.url_safe = url_safe

    @property
    def azure_ad_object_id(self):
        """Gets the azure_ad_object_id of this GetCloudIdentity.  # noqa: E501

        Azure Active Directory ObjectId (relevant only for access-type=azure_ad)  # noqa: E501

        :return: The azure_ad_object_id of this GetCloudIdentity.  # noqa: E501
        :rtype: str
        """
        return self._azure_ad_object_id

    @azure_ad_object_id.setter
    def azure_ad_object_id(self, azure_ad_object_id):
        """Sets the azure_ad_object_id of this GetCloudIdentity.

        Azure Active Directory ObjectId (relevant only for access-type=azure_ad)  # noqa: E501

        :param azure_ad_object_id: The azure_ad_object_id of this GetCloudIdentity.  # noqa: E501
        :type: str
        """

        self._azure_ad_object_id = azure_ad_object_id

    @property
    def debug(self):
        """Gets the debug of this GetCloudIdentity.  # noqa: E501


        :return: The debug of this GetCloudIdentity.  # noqa: E501
        :rtype: bool
        """
        return self._debug

    @debug.setter
    def debug(self, debug):
        """Sets the debug of this GetCloudIdentity.


        :param debug: The debug of this GetCloudIdentity.  # noqa: E501
        :type: bool
        """

        self._debug = debug

    @property
    def gcp_audience(self):
        """Gets the gcp_audience of this GetCloudIdentity.  # noqa: E501

        GCP JWT audience  # noqa: E501

        :return: The gcp_audience of this GetCloudIdentity.  # noqa: E501
        :rtype: str
        """
        return self._gcp_audience

    @gcp_audience.setter
    def gcp_audience(self, gcp_audience):
        """Sets the gcp_audience of this GetCloudIdentity.

        GCP JWT audience  # noqa: E501

        :param gcp_audience: The gcp_audience of this GetCloudIdentity.  # noqa: E501
        :type: str
        """

        self._gcp_audience = gcp_audience

    @property
    def url_safe(self):
        """Gets the url_safe of this GetCloudIdentity.  # noqa: E501

        Escapes the token so it can be safely placed inside a URL query  # noqa: E501

        :return: The url_safe of this GetCloudIdentity.  # noqa: E501
        :rtype: bool
        """
        return self._url_safe

    @url_safe.setter
    def url_safe(self, url_safe):
        """Sets the url_safe of this GetCloudIdentity.

        Escapes the token so it can be safely placed inside a URL query  # noqa: E501

        :param url_safe: The url_safe of this GetCloudIdentity.  # noqa: E501
        :type: bool
        """

        self._url_safe = url_safe

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
        if not isinstance(other, GetCloudIdentity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetCloudIdentity):
            return True

        return self.to_dict() != other.to_dict()
