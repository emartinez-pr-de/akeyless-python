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


class WebHookNotiForwarderPublicDetails(object):
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
        'auth_type': 'str',
        'endpoint_url': 'str',
        'username': 'str'
    }

    attribute_map = {
        'auth_type': 'auth_type',
        'endpoint_url': 'endpoint_url',
        'username': 'username'
    }

    def __init__(self, auth_type=None, endpoint_url=None, username=None, local_vars_configuration=None):  # noqa: E501
        """WebHookNotiForwarderPublicDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._auth_type = None
        self._endpoint_url = None
        self._username = None
        self.discriminator = None

        if auth_type is not None:
            self.auth_type = auth_type
        if endpoint_url is not None:
            self.endpoint_url = endpoint_url
        if username is not None:
            self.username = username

    @property
    def auth_type(self):
        """Gets the auth_type of this WebHookNotiForwarderPublicDetails.  # noqa: E501


        :return: The auth_type of this WebHookNotiForwarderPublicDetails.  # noqa: E501
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this WebHookNotiForwarderPublicDetails.


        :param auth_type: The auth_type of this WebHookNotiForwarderPublicDetails.  # noqa: E501
        :type: str
        """

        self._auth_type = auth_type

    @property
    def endpoint_url(self):
        """Gets the endpoint_url of this WebHookNotiForwarderPublicDetails.  # noqa: E501


        :return: The endpoint_url of this WebHookNotiForwarderPublicDetails.  # noqa: E501
        :rtype: str
        """
        return self._endpoint_url

    @endpoint_url.setter
    def endpoint_url(self, endpoint_url):
        """Sets the endpoint_url of this WebHookNotiForwarderPublicDetails.


        :param endpoint_url: The endpoint_url of this WebHookNotiForwarderPublicDetails.  # noqa: E501
        :type: str
        """

        self._endpoint_url = endpoint_url

    @property
    def username(self):
        """Gets the username of this WebHookNotiForwarderPublicDetails.  # noqa: E501

        Auth type - User Password  # noqa: E501

        :return: The username of this WebHookNotiForwarderPublicDetails.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this WebHookNotiForwarderPublicDetails.

        Auth type - User Password  # noqa: E501

        :param username: The username of this WebHookNotiForwarderPublicDetails.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if not isinstance(other, WebHookNotiForwarderPublicDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebHookNotiForwarderPublicDetails):
            return True

        return self.to_dict() != other.to_dict()
