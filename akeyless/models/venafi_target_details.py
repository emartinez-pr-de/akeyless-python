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


class VenafiTargetDetails(object):
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
        'venafi_api_key': 'str',
        'venafi_base_url': 'str',
        'venafi_tpp_access_token': 'str',
        'venafi_tpp_client_id': 'str',
        'venafi_tpp_password': 'str',
        'venafi_tpp_refresh_token': 'str',
        'venafi_tpp_username': 'str',
        'venafi_use_tpp': 'bool',
        'venafi_zone': 'str'
    }

    attribute_map = {
        'venafi_api_key': 'venafi_api_key',
        'venafi_base_url': 'venafi_base_url',
        'venafi_tpp_access_token': 'venafi_tpp_access_token',
        'venafi_tpp_client_id': 'venafi_tpp_client_id',
        'venafi_tpp_password': 'venafi_tpp_password',
        'venafi_tpp_refresh_token': 'venafi_tpp_refresh_token',
        'venafi_tpp_username': 'venafi_tpp_username',
        'venafi_use_tpp': 'venafi_use_tpp',
        'venafi_zone': 'venafi_zone'
    }

    def __init__(self, venafi_api_key=None, venafi_base_url=None, venafi_tpp_access_token=None, venafi_tpp_client_id=None, venafi_tpp_password=None, venafi_tpp_refresh_token=None, venafi_tpp_username=None, venafi_use_tpp=None, venafi_zone=None, local_vars_configuration=None):  # noqa: E501
        """VenafiTargetDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._venafi_api_key = None
        self._venafi_base_url = None
        self._venafi_tpp_access_token = None
        self._venafi_tpp_client_id = None
        self._venafi_tpp_password = None
        self._venafi_tpp_refresh_token = None
        self._venafi_tpp_username = None
        self._venafi_use_tpp = None
        self._venafi_zone = None
        self.discriminator = None

        if venafi_api_key is not None:
            self.venafi_api_key = venafi_api_key
        if venafi_base_url is not None:
            self.venafi_base_url = venafi_base_url
        if venafi_tpp_access_token is not None:
            self.venafi_tpp_access_token = venafi_tpp_access_token
        if venafi_tpp_client_id is not None:
            self.venafi_tpp_client_id = venafi_tpp_client_id
        if venafi_tpp_password is not None:
            self.venafi_tpp_password = venafi_tpp_password
        if venafi_tpp_refresh_token is not None:
            self.venafi_tpp_refresh_token = venafi_tpp_refresh_token
        if venafi_tpp_username is not None:
            self.venafi_tpp_username = venafi_tpp_username
        if venafi_use_tpp is not None:
            self.venafi_use_tpp = venafi_use_tpp
        if venafi_zone is not None:
            self.venafi_zone = venafi_zone

    @property
    def venafi_api_key(self):
        """Gets the venafi_api_key of this VenafiTargetDetails.  # noqa: E501


        :return: The venafi_api_key of this VenafiTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._venafi_api_key

    @venafi_api_key.setter
    def venafi_api_key(self, venafi_api_key):
        """Sets the venafi_api_key of this VenafiTargetDetails.


        :param venafi_api_key: The venafi_api_key of this VenafiTargetDetails.  # noqa: E501
        :type: str
        """

        self._venafi_api_key = venafi_api_key

    @property
    def venafi_base_url(self):
        """Gets the venafi_base_url of this VenafiTargetDetails.  # noqa: E501


        :return: The venafi_base_url of this VenafiTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._venafi_base_url

    @venafi_base_url.setter
    def venafi_base_url(self, venafi_base_url):
        """Sets the venafi_base_url of this VenafiTargetDetails.


        :param venafi_base_url: The venafi_base_url of this VenafiTargetDetails.  # noqa: E501
        :type: str
        """

        self._venafi_base_url = venafi_base_url

    @property
    def venafi_tpp_access_token(self):
        """Gets the venafi_tpp_access_token of this VenafiTargetDetails.  # noqa: E501


        :return: The venafi_tpp_access_token of this VenafiTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._venafi_tpp_access_token

    @venafi_tpp_access_token.setter
    def venafi_tpp_access_token(self, venafi_tpp_access_token):
        """Sets the venafi_tpp_access_token of this VenafiTargetDetails.


        :param venafi_tpp_access_token: The venafi_tpp_access_token of this VenafiTargetDetails.  # noqa: E501
        :type: str
        """

        self._venafi_tpp_access_token = venafi_tpp_access_token

    @property
    def venafi_tpp_client_id(self):
        """Gets the venafi_tpp_client_id of this VenafiTargetDetails.  # noqa: E501


        :return: The venafi_tpp_client_id of this VenafiTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._venafi_tpp_client_id

    @venafi_tpp_client_id.setter
    def venafi_tpp_client_id(self, venafi_tpp_client_id):
        """Sets the venafi_tpp_client_id of this VenafiTargetDetails.


        :param venafi_tpp_client_id: The venafi_tpp_client_id of this VenafiTargetDetails.  # noqa: E501
        :type: str
        """

        self._venafi_tpp_client_id = venafi_tpp_client_id

    @property
    def venafi_tpp_password(self):
        """Gets the venafi_tpp_password of this VenafiTargetDetails.  # noqa: E501

        Deprecated: VenafiAccessToken and VenafiRefreshToken should be used instead  # noqa: E501

        :return: The venafi_tpp_password of this VenafiTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._venafi_tpp_password

    @venafi_tpp_password.setter
    def venafi_tpp_password(self, venafi_tpp_password):
        """Sets the venafi_tpp_password of this VenafiTargetDetails.

        Deprecated: VenafiAccessToken and VenafiRefreshToken should be used instead  # noqa: E501

        :param venafi_tpp_password: The venafi_tpp_password of this VenafiTargetDetails.  # noqa: E501
        :type: str
        """

        self._venafi_tpp_password = venafi_tpp_password

    @property
    def venafi_tpp_refresh_token(self):
        """Gets the venafi_tpp_refresh_token of this VenafiTargetDetails.  # noqa: E501


        :return: The venafi_tpp_refresh_token of this VenafiTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._venafi_tpp_refresh_token

    @venafi_tpp_refresh_token.setter
    def venafi_tpp_refresh_token(self, venafi_tpp_refresh_token):
        """Sets the venafi_tpp_refresh_token of this VenafiTargetDetails.


        :param venafi_tpp_refresh_token: The venafi_tpp_refresh_token of this VenafiTargetDetails.  # noqa: E501
        :type: str
        """

        self._venafi_tpp_refresh_token = venafi_tpp_refresh_token

    @property
    def venafi_tpp_username(self):
        """Gets the venafi_tpp_username of this VenafiTargetDetails.  # noqa: E501

        Deprecated: VenafiAccessToken and VenafiRefreshToken should be used instead  # noqa: E501

        :return: The venafi_tpp_username of this VenafiTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._venafi_tpp_username

    @venafi_tpp_username.setter
    def venafi_tpp_username(self, venafi_tpp_username):
        """Sets the venafi_tpp_username of this VenafiTargetDetails.

        Deprecated: VenafiAccessToken and VenafiRefreshToken should be used instead  # noqa: E501

        :param venafi_tpp_username: The venafi_tpp_username of this VenafiTargetDetails.  # noqa: E501
        :type: str
        """

        self._venafi_tpp_username = venafi_tpp_username

    @property
    def venafi_use_tpp(self):
        """Gets the venafi_use_tpp of this VenafiTargetDetails.  # noqa: E501


        :return: The venafi_use_tpp of this VenafiTargetDetails.  # noqa: E501
        :rtype: bool
        """
        return self._venafi_use_tpp

    @venafi_use_tpp.setter
    def venafi_use_tpp(self, venafi_use_tpp):
        """Sets the venafi_use_tpp of this VenafiTargetDetails.


        :param venafi_use_tpp: The venafi_use_tpp of this VenafiTargetDetails.  # noqa: E501
        :type: bool
        """

        self._venafi_use_tpp = venafi_use_tpp

    @property
    def venafi_zone(self):
        """Gets the venafi_zone of this VenafiTargetDetails.  # noqa: E501


        :return: The venafi_zone of this VenafiTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._venafi_zone

    @venafi_zone.setter
    def venafi_zone(self, venafi_zone):
        """Sets the venafi_zone of this VenafiTargetDetails.


        :param venafi_zone: The venafi_zone of this VenafiTargetDetails.  # noqa: E501
        :type: str
        """

        self._venafi_zone = venafi_zone

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
        if not isinstance(other, VenafiTargetDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VenafiTargetDetails):
            return True

        return self.to_dict() != other.to_dict()