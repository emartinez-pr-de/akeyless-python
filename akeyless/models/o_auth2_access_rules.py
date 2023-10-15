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


class OAuth2AccessRules(object):
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
        'audience': 'str',
        'authorized_gw_cluster_name': 'str',
        'bound_claims': 'list[OAuth2CustomClaim]',
        'bound_clients_id': 'list[str]',
        'issuer': 'str',
        'jwks_json_data': 'str',
        'jwks_uri': 'str',
        'unique_identifier': 'str'
    }

    attribute_map = {
        'audience': 'audience',
        'authorized_gw_cluster_name': 'authorized_gw_cluster_name',
        'bound_claims': 'bound_claims',
        'bound_clients_id': 'bound_clients_id',
        'issuer': 'issuer',
        'jwks_json_data': 'jwks_json_data',
        'jwks_uri': 'jwks_uri',
        'unique_identifier': 'unique_identifier'
    }

    def __init__(self, audience=None, authorized_gw_cluster_name=None, bound_claims=None, bound_clients_id=None, issuer=None, jwks_json_data=None, jwks_uri=None, unique_identifier=None, local_vars_configuration=None):  # noqa: E501
        """OAuth2AccessRules - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._audience = None
        self._authorized_gw_cluster_name = None
        self._bound_claims = None
        self._bound_clients_id = None
        self._issuer = None
        self._jwks_json_data = None
        self._jwks_uri = None
        self._unique_identifier = None
        self.discriminator = None

        if audience is not None:
            self.audience = audience
        if authorized_gw_cluster_name is not None:
            self.authorized_gw_cluster_name = authorized_gw_cluster_name
        if bound_claims is not None:
            self.bound_claims = bound_claims
        if bound_clients_id is not None:
            self.bound_clients_id = bound_clients_id
        if issuer is not None:
            self.issuer = issuer
        if jwks_json_data is not None:
            self.jwks_json_data = jwks_json_data
        if jwks_uri is not None:
            self.jwks_uri = jwks_uri
        if unique_identifier is not None:
            self.unique_identifier = unique_identifier

    @property
    def audience(self):
        """Gets the audience of this OAuth2AccessRules.  # noqa: E501

        The audience in the JWT.  # noqa: E501

        :return: The audience of this OAuth2AccessRules.  # noqa: E501
        :rtype: str
        """
        return self._audience

    @audience.setter
    def audience(self, audience):
        """Sets the audience of this OAuth2AccessRules.

        The audience in the JWT.  # noqa: E501

        :param audience: The audience of this OAuth2AccessRules.  # noqa: E501
        :type: str
        """

        self._audience = audience

    @property
    def authorized_gw_cluster_name(self):
        """Gets the authorized_gw_cluster_name of this OAuth2AccessRules.  # noqa: E501

        The gateway cluster name that is authorized to access JWKeySetURL  # noqa: E501

        :return: The authorized_gw_cluster_name of this OAuth2AccessRules.  # noqa: E501
        :rtype: str
        """
        return self._authorized_gw_cluster_name

    @authorized_gw_cluster_name.setter
    def authorized_gw_cluster_name(self, authorized_gw_cluster_name):
        """Sets the authorized_gw_cluster_name of this OAuth2AccessRules.

        The gateway cluster name that is authorized to access JWKeySetURL  # noqa: E501

        :param authorized_gw_cluster_name: The authorized_gw_cluster_name of this OAuth2AccessRules.  # noqa: E501
        :type: str
        """

        self._authorized_gw_cluster_name = authorized_gw_cluster_name

    @property
    def bound_claims(self):
        """Gets the bound_claims of this OAuth2AccessRules.  # noqa: E501

        The claims that login is restricted to.  # noqa: E501

        :return: The bound_claims of this OAuth2AccessRules.  # noqa: E501
        :rtype: list[OAuth2CustomClaim]
        """
        return self._bound_claims

    @bound_claims.setter
    def bound_claims(self, bound_claims):
        """Sets the bound_claims of this OAuth2AccessRules.

        The claims that login is restricted to.  # noqa: E501

        :param bound_claims: The bound_claims of this OAuth2AccessRules.  # noqa: E501
        :type: list[OAuth2CustomClaim]
        """

        self._bound_claims = bound_claims

    @property
    def bound_clients_id(self):
        """Gets the bound_clients_id of this OAuth2AccessRules.  # noqa: E501

        The clients ids that login is restricted to.  # noqa: E501

        :return: The bound_clients_id of this OAuth2AccessRules.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_clients_id

    @bound_clients_id.setter
    def bound_clients_id(self, bound_clients_id):
        """Sets the bound_clients_id of this OAuth2AccessRules.

        The clients ids that login is restricted to.  # noqa: E501

        :param bound_clients_id: The bound_clients_id of this OAuth2AccessRules.  # noqa: E501
        :type: list[str]
        """

        self._bound_clients_id = bound_clients_id

    @property
    def issuer(self):
        """Gets the issuer of this OAuth2AccessRules.  # noqa: E501

        Issuer URL  # noqa: E501

        :return: The issuer of this OAuth2AccessRules.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this OAuth2AccessRules.

        Issuer URL  # noqa: E501

        :param issuer: The issuer of this OAuth2AccessRules.  # noqa: E501
        :type: str
        """

        self._issuer = issuer

    @property
    def jwks_json_data(self):
        """Gets the jwks_json_data of this OAuth2AccessRules.  # noqa: E501

        The JSON Web Key Set (JWKS) that containing the public keys that should be used to verify any JSON Web Token (JWT) issued by the authorization server. base64 encoded string  # noqa: E501

        :return: The jwks_json_data of this OAuth2AccessRules.  # noqa: E501
        :rtype: str
        """
        return self._jwks_json_data

    @jwks_json_data.setter
    def jwks_json_data(self, jwks_json_data):
        """Sets the jwks_json_data of this OAuth2AccessRules.

        The JSON Web Key Set (JWKS) that containing the public keys that should be used to verify any JSON Web Token (JWT) issued by the authorization server. base64 encoded string  # noqa: E501

        :param jwks_json_data: The jwks_json_data of this OAuth2AccessRules.  # noqa: E501
        :type: str
        """

        self._jwks_json_data = jwks_json_data

    @property
    def jwks_uri(self):
        """Gets the jwks_uri of this OAuth2AccessRules.  # noqa: E501

        The URL to the JSON Web Key Set (JWKS) that containing the public keys that should be used to verify any JSON Web Token (JWT) issued by the authorization server.  # noqa: E501

        :return: The jwks_uri of this OAuth2AccessRules.  # noqa: E501
        :rtype: str
        """
        return self._jwks_uri

    @jwks_uri.setter
    def jwks_uri(self, jwks_uri):
        """Sets the jwks_uri of this OAuth2AccessRules.

        The URL to the JSON Web Key Set (JWKS) that containing the public keys that should be used to verify any JSON Web Token (JWT) issued by the authorization server.  # noqa: E501

        :param jwks_uri: The jwks_uri of this OAuth2AccessRules.  # noqa: E501
        :type: str
        """

        self._jwks_uri = jwks_uri

    @property
    def unique_identifier(self):
        """Gets the unique_identifier of this OAuth2AccessRules.  # noqa: E501

        A unique identifier to distinguish different users  # noqa: E501

        :return: The unique_identifier of this OAuth2AccessRules.  # noqa: E501
        :rtype: str
        """
        return self._unique_identifier

    @unique_identifier.setter
    def unique_identifier(self, unique_identifier):
        """Sets the unique_identifier of this OAuth2AccessRules.

        A unique identifier to distinguish different users  # noqa: E501

        :param unique_identifier: The unique_identifier of this OAuth2AccessRules.  # noqa: E501
        :type: str
        """

        self._unique_identifier = unique_identifier

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
        if not isinstance(other, OAuth2AccessRules):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OAuth2AccessRules):
            return True

        return self.to_dict() != other.to_dict()
