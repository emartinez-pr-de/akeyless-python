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


class OidcClientInfo(object):
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
        'access_permission_assignment': 'list[AccessOrGroupPermissionAssignment]',
        'audience': 'list[str]',
        'client_id': 'str',
        'grant_types': 'list[str]',
        'issuer_url': 'str',
        'logout_uris': 'list[str]',
        'public': 'bool',
        'redirect_uris': 'list[str]',
        'response_types': 'list[str]',
        'scopes': 'list[str]'
    }

    attribute_map = {
        'access_permission_assignment': 'access_permission_assignment',
        'audience': 'audience',
        'client_id': 'client_id',
        'grant_types': 'grant_types',
        'issuer_url': 'issuer_url',
        'logout_uris': 'logout_uris',
        'public': 'public',
        'redirect_uris': 'redirect_uris',
        'response_types': 'response_types',
        'scopes': 'scopes'
    }

    def __init__(self, access_permission_assignment=None, audience=None, client_id=None, grant_types=None, issuer_url=None, logout_uris=None, public=None, redirect_uris=None, response_types=None, scopes=None, local_vars_configuration=None):  # noqa: E501
        """OidcClientInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_permission_assignment = None
        self._audience = None
        self._client_id = None
        self._grant_types = None
        self._issuer_url = None
        self._logout_uris = None
        self._public = None
        self._redirect_uris = None
        self._response_types = None
        self._scopes = None
        self.discriminator = None

        if access_permission_assignment is not None:
            self.access_permission_assignment = access_permission_assignment
        if audience is not None:
            self.audience = audience
        if client_id is not None:
            self.client_id = client_id
        if grant_types is not None:
            self.grant_types = grant_types
        if issuer_url is not None:
            self.issuer_url = issuer_url
        if logout_uris is not None:
            self.logout_uris = logout_uris
        if public is not None:
            self.public = public
        if redirect_uris is not None:
            self.redirect_uris = redirect_uris
        if response_types is not None:
            self.response_types = response_types
        if scopes is not None:
            self.scopes = scopes

    @property
    def access_permission_assignment(self):
        """Gets the access_permission_assignment of this OidcClientInfo.  # noqa: E501


        :return: The access_permission_assignment of this OidcClientInfo.  # noqa: E501
        :rtype: list[AccessOrGroupPermissionAssignment]
        """
        return self._access_permission_assignment

    @access_permission_assignment.setter
    def access_permission_assignment(self, access_permission_assignment):
        """Sets the access_permission_assignment of this OidcClientInfo.


        :param access_permission_assignment: The access_permission_assignment of this OidcClientInfo.  # noqa: E501
        :type: list[AccessOrGroupPermissionAssignment]
        """

        self._access_permission_assignment = access_permission_assignment

    @property
    def audience(self):
        """Gets the audience of this OidcClientInfo.  # noqa: E501


        :return: The audience of this OidcClientInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._audience

    @audience.setter
    def audience(self, audience):
        """Sets the audience of this OidcClientInfo.


        :param audience: The audience of this OidcClientInfo.  # noqa: E501
        :type: list[str]
        """

        self._audience = audience

    @property
    def client_id(self):
        """Gets the client_id of this OidcClientInfo.  # noqa: E501


        :return: The client_id of this OidcClientInfo.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this OidcClientInfo.


        :param client_id: The client_id of this OidcClientInfo.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def grant_types(self):
        """Gets the grant_types of this OidcClientInfo.  # noqa: E501


        :return: The grant_types of this OidcClientInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._grant_types

    @grant_types.setter
    def grant_types(self, grant_types):
        """Sets the grant_types of this OidcClientInfo.


        :param grant_types: The grant_types of this OidcClientInfo.  # noqa: E501
        :type: list[str]
        """

        self._grant_types = grant_types

    @property
    def issuer_url(self):
        """Gets the issuer_url of this OidcClientInfo.  # noqa: E501


        :return: The issuer_url of this OidcClientInfo.  # noqa: E501
        :rtype: str
        """
        return self._issuer_url

    @issuer_url.setter
    def issuer_url(self, issuer_url):
        """Sets the issuer_url of this OidcClientInfo.


        :param issuer_url: The issuer_url of this OidcClientInfo.  # noqa: E501
        :type: str
        """

        self._issuer_url = issuer_url

    @property
    def logout_uris(self):
        """Gets the logout_uris of this OidcClientInfo.  # noqa: E501


        :return: The logout_uris of this OidcClientInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._logout_uris

    @logout_uris.setter
    def logout_uris(self, logout_uris):
        """Sets the logout_uris of this OidcClientInfo.


        :param logout_uris: The logout_uris of this OidcClientInfo.  # noqa: E501
        :type: list[str]
        """

        self._logout_uris = logout_uris

    @property
    def public(self):
        """Gets the public of this OidcClientInfo.  # noqa: E501


        :return: The public of this OidcClientInfo.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this OidcClientInfo.


        :param public: The public of this OidcClientInfo.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def redirect_uris(self):
        """Gets the redirect_uris of this OidcClientInfo.  # noqa: E501


        :return: The redirect_uris of this OidcClientInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._redirect_uris

    @redirect_uris.setter
    def redirect_uris(self, redirect_uris):
        """Sets the redirect_uris of this OidcClientInfo.


        :param redirect_uris: The redirect_uris of this OidcClientInfo.  # noqa: E501
        :type: list[str]
        """

        self._redirect_uris = redirect_uris

    @property
    def response_types(self):
        """Gets the response_types of this OidcClientInfo.  # noqa: E501


        :return: The response_types of this OidcClientInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._response_types

    @response_types.setter
    def response_types(self, response_types):
        """Sets the response_types of this OidcClientInfo.


        :param response_types: The response_types of this OidcClientInfo.  # noqa: E501
        :type: list[str]
        """

        self._response_types = response_types

    @property
    def scopes(self):
        """Gets the scopes of this OidcClientInfo.  # noqa: E501


        :return: The scopes of this OidcClientInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this OidcClientInfo.


        :param scopes: The scopes of this OidcClientInfo.  # noqa: E501
        :type: list[str]
        """

        self._scopes = scopes

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
        if not isinstance(other, OidcClientInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OidcClientInfo):
            return True

        return self.to_dict() != other.to_dict()
