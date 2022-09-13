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


class GatewayAddAllowedManagementAccess(object):
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
        'allow_gw_api': 'bool',
        'allow_gw_login': 'bool',
        'json': 'bool',
        'sub_admin_access_id': 'str',
        'sub_claims': 'dict(str, str)',
        'token': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'allow_gw_api': 'allow-gw-api',
        'allow_gw_login': 'allow-gw-login',
        'json': 'json',
        'sub_admin_access_id': 'sub-admin-access-id',
        'sub_claims': 'sub-claims',
        'token': 'token',
        'uid_token': 'uid-token'
    }

    def __init__(self, allow_gw_api=None, allow_gw_login=None, json=None, sub_admin_access_id=None, sub_claims=None, token=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """GatewayAddAllowedManagementAccess - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._allow_gw_api = None
        self._allow_gw_login = None
        self._json = None
        self._sub_admin_access_id = None
        self._sub_claims = None
        self._token = None
        self._uid_token = None
        self.discriminator = None

        if allow_gw_api is not None:
            self.allow_gw_api = allow_gw_api
        if allow_gw_login is not None:
            self.allow_gw_login = allow_gw_login
        if json is not None:
            self.json = json
        self.sub_admin_access_id = sub_admin_access_id
        if sub_claims is not None:
            self.sub_claims = sub_claims
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def allow_gw_api(self):
        """Gets the allow_gw_api of this GatewayAddAllowedManagementAccess.  # noqa: E501


        :return: The allow_gw_api of this GatewayAddAllowedManagementAccess.  # noqa: E501
        :rtype: bool
        """
        return self._allow_gw_api

    @allow_gw_api.setter
    def allow_gw_api(self, allow_gw_api):
        """Sets the allow_gw_api of this GatewayAddAllowedManagementAccess.


        :param allow_gw_api: The allow_gw_api of this GatewayAddAllowedManagementAccess.  # noqa: E501
        :type: bool
        """

        self._allow_gw_api = allow_gw_api

    @property
    def allow_gw_login(self):
        """Gets the allow_gw_login of this GatewayAddAllowedManagementAccess.  # noqa: E501


        :return: The allow_gw_login of this GatewayAddAllowedManagementAccess.  # noqa: E501
        :rtype: bool
        """
        return self._allow_gw_login

    @allow_gw_login.setter
    def allow_gw_login(self, allow_gw_login):
        """Sets the allow_gw_login of this GatewayAddAllowedManagementAccess.


        :param allow_gw_login: The allow_gw_login of this GatewayAddAllowedManagementAccess.  # noqa: E501
        :type: bool
        """

        self._allow_gw_login = allow_gw_login

    @property
    def json(self):
        """Gets the json of this GatewayAddAllowedManagementAccess.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this GatewayAddAllowedManagementAccess.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this GatewayAddAllowedManagementAccess.

        Set output format to JSON  # noqa: E501

        :param json: The json of this GatewayAddAllowedManagementAccess.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def sub_admin_access_id(self):
        """Gets the sub_admin_access_id of this GatewayAddAllowedManagementAccess.  # noqa: E501

        SubAdmins to add  # noqa: E501

        :return: The sub_admin_access_id of this GatewayAddAllowedManagementAccess.  # noqa: E501
        :rtype: str
        """
        return self._sub_admin_access_id

    @sub_admin_access_id.setter
    def sub_admin_access_id(self, sub_admin_access_id):
        """Sets the sub_admin_access_id of this GatewayAddAllowedManagementAccess.

        SubAdmins to add  # noqa: E501

        :param sub_admin_access_id: The sub_admin_access_id of this GatewayAddAllowedManagementAccess.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sub_admin_access_id is None:  # noqa: E501
            raise ValueError("Invalid value for `sub_admin_access_id`, must not be `None`")  # noqa: E501

        self._sub_admin_access_id = sub_admin_access_id

    @property
    def sub_claims(self):
        """Gets the sub_claims of this GatewayAddAllowedManagementAccess.  # noqa: E501

        key/val of sub claims, e.g group=admins,developers  # noqa: E501

        :return: The sub_claims of this GatewayAddAllowedManagementAccess.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._sub_claims

    @sub_claims.setter
    def sub_claims(self, sub_claims):
        """Sets the sub_claims of this GatewayAddAllowedManagementAccess.

        key/val of sub claims, e.g group=admins,developers  # noqa: E501

        :param sub_claims: The sub_claims of this GatewayAddAllowedManagementAccess.  # noqa: E501
        :type: dict(str, str)
        """

        self._sub_claims = sub_claims

    @property
    def token(self):
        """Gets the token of this GatewayAddAllowedManagementAccess.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GatewayAddAllowedManagementAccess.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GatewayAddAllowedManagementAccess.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GatewayAddAllowedManagementAccess.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this GatewayAddAllowedManagementAccess.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GatewayAddAllowedManagementAccess.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GatewayAddAllowedManagementAccess.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GatewayAddAllowedManagementAccess.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

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
        if not isinstance(other, GatewayAddAllowedManagementAccess):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayAddAllowedManagementAccess):
            return True

        return self.to_dict() != other.to_dict()
