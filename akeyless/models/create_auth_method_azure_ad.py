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


class CreateAuthMethodAzureAD(object):
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
        'access_expires': 'int',
        'audience': 'str',
        'bound_group_id': 'list[str]',
        'bound_ips': 'list[str]',
        'bound_providers': 'list[str]',
        'bound_resource_id': 'list[str]',
        'bound_resource_names': 'list[str]',
        'bound_resource_types': 'list[str]',
        'bound_rg_id': 'list[str]',
        'bound_spid': 'list[str]',
        'bound_sub_id': 'list[str]',
        'bound_tenant_id': 'str',
        'force_sub_claims': 'bool',
        'issuer': 'str',
        'jwks_uri': 'str',
        'jwt_ttl': 'int',
        'name': 'str',
        'token': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'access_expires': 'access-expires',
        'audience': 'audience',
        'bound_group_id': 'bound-group-id',
        'bound_ips': 'bound-ips',
        'bound_providers': 'bound-providers',
        'bound_resource_id': 'bound-resource-id',
        'bound_resource_names': 'bound-resource-names',
        'bound_resource_types': 'bound-resource-types',
        'bound_rg_id': 'bound-rg-id',
        'bound_spid': 'bound-spid',
        'bound_sub_id': 'bound-sub-id',
        'bound_tenant_id': 'bound-tenant-id',
        'force_sub_claims': 'force-sub-claims',
        'issuer': 'issuer',
        'jwks_uri': 'jwks-uri',
        'jwt_ttl': 'jwt-ttl',
        'name': 'name',
        'token': 'token',
        'uid_token': 'uid-token'
    }

    def __init__(self, access_expires=0, audience='https://management.azure.com/', bound_group_id=None, bound_ips=None, bound_providers=None, bound_resource_id=None, bound_resource_names=None, bound_resource_types=None, bound_rg_id=None, bound_spid=None, bound_sub_id=None, bound_tenant_id=None, force_sub_claims=None, issuer='https://sts.windows.net/---bound_tenant_id---', jwks_uri='https://login.microsoftonline.com/common/discovery/keys', jwt_ttl=None, name=None, token=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """CreateAuthMethodAzureAD - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_expires = None
        self._audience = None
        self._bound_group_id = None
        self._bound_ips = None
        self._bound_providers = None
        self._bound_resource_id = None
        self._bound_resource_names = None
        self._bound_resource_types = None
        self._bound_rg_id = None
        self._bound_spid = None
        self._bound_sub_id = None
        self._bound_tenant_id = None
        self._force_sub_claims = None
        self._issuer = None
        self._jwks_uri = None
        self._jwt_ttl = None
        self._name = None
        self._token = None
        self._uid_token = None
        self.discriminator = None

        if access_expires is not None:
            self.access_expires = access_expires
        if audience is not None:
            self.audience = audience
        if bound_group_id is not None:
            self.bound_group_id = bound_group_id
        if bound_ips is not None:
            self.bound_ips = bound_ips
        if bound_providers is not None:
            self.bound_providers = bound_providers
        if bound_resource_id is not None:
            self.bound_resource_id = bound_resource_id
        if bound_resource_names is not None:
            self.bound_resource_names = bound_resource_names
        if bound_resource_types is not None:
            self.bound_resource_types = bound_resource_types
        if bound_rg_id is not None:
            self.bound_rg_id = bound_rg_id
        if bound_spid is not None:
            self.bound_spid = bound_spid
        if bound_sub_id is not None:
            self.bound_sub_id = bound_sub_id
        self.bound_tenant_id = bound_tenant_id
        if force_sub_claims is not None:
            self.force_sub_claims = force_sub_claims
        if issuer is not None:
            self.issuer = issuer
        if jwks_uri is not None:
            self.jwks_uri = jwks_uri
        if jwt_ttl is not None:
            self.jwt_ttl = jwt_ttl
        self.name = name
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def access_expires(self):
        """Gets the access_expires of this CreateAuthMethodAzureAD.  # noqa: E501

        Access expiration date in Unix timestamp (select 0 for access without expiry date)  # noqa: E501

        :return: The access_expires of this CreateAuthMethodAzureAD.  # noqa: E501
        :rtype: int
        """
        return self._access_expires

    @access_expires.setter
    def access_expires(self, access_expires):
        """Sets the access_expires of this CreateAuthMethodAzureAD.

        Access expiration date in Unix timestamp (select 0 for access without expiry date)  # noqa: E501

        :param access_expires: The access_expires of this CreateAuthMethodAzureAD.  # noqa: E501
        :type: int
        """

        self._access_expires = access_expires

    @property
    def audience(self):
        """Gets the audience of this CreateAuthMethodAzureAD.  # noqa: E501

        The audience in the JWT  # noqa: E501

        :return: The audience of this CreateAuthMethodAzureAD.  # noqa: E501
        :rtype: str
        """
        return self._audience

    @audience.setter
    def audience(self, audience):
        """Sets the audience of this CreateAuthMethodAzureAD.

        The audience in the JWT  # noqa: E501

        :param audience: The audience of this CreateAuthMethodAzureAD.  # noqa: E501
        :type: str
        """

        self._audience = audience

    @property
    def bound_group_id(self):
        """Gets the bound_group_id of this CreateAuthMethodAzureAD.  # noqa: E501

        A list of group ids that the access is restricted to  # noqa: E501

        :return: The bound_group_id of this CreateAuthMethodAzureAD.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_group_id

    @bound_group_id.setter
    def bound_group_id(self, bound_group_id):
        """Sets the bound_group_id of this CreateAuthMethodAzureAD.

        A list of group ids that the access is restricted to  # noqa: E501

        :param bound_group_id: The bound_group_id of this CreateAuthMethodAzureAD.  # noqa: E501
        :type: list[str]
        """

        self._bound_group_id = bound_group_id

    @property
    def bound_ips(self):
        """Gets the bound_ips of this CreateAuthMethodAzureAD.  # noqa: E501

        A CIDR whitelist with the IPs that the access is restricted to  # noqa: E501

        :return: The bound_ips of this CreateAuthMethodAzureAD.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_ips

    @bound_ips.setter
    def bound_ips(self, bound_ips):
        """Sets the bound_ips of this CreateAuthMethodAzureAD.

        A CIDR whitelist with the IPs that the access is restricted to  # noqa: E501

        :param bound_ips: The bound_ips of this CreateAuthMethodAzureAD.  # noqa: E501
        :type: list[str]
        """

        self._bound_ips = bound_ips

    @property
    def bound_providers(self):
        """Gets the bound_providers of this CreateAuthMethodAzureAD.  # noqa: E501

        A list of resource providers that the access is restricted to (e.g, Microsoft.Compute, Microsoft.ManagedIdentity, etc)  # noqa: E501

        :return: The bound_providers of this CreateAuthMethodAzureAD.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_providers

    @bound_providers.setter
    def bound_providers(self, bound_providers):
        """Sets the bound_providers of this CreateAuthMethodAzureAD.

        A list of resource providers that the access is restricted to (e.g, Microsoft.Compute, Microsoft.ManagedIdentity, etc)  # noqa: E501

        :param bound_providers: The bound_providers of this CreateAuthMethodAzureAD.  # noqa: E501
        :type: list[str]
        """

        self._bound_providers = bound_providers

    @property
    def bound_resource_id(self):
        """Gets the bound_resource_id of this CreateAuthMethodAzureAD.  # noqa: E501

        A list of full resource ids that the access is restricted to  # noqa: E501

        :return: The bound_resource_id of this CreateAuthMethodAzureAD.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_resource_id

    @bound_resource_id.setter
    def bound_resource_id(self, bound_resource_id):
        """Sets the bound_resource_id of this CreateAuthMethodAzureAD.

        A list of full resource ids that the access is restricted to  # noqa: E501

        :param bound_resource_id: The bound_resource_id of this CreateAuthMethodAzureAD.  # noqa: E501
        :type: list[str]
        """

        self._bound_resource_id = bound_resource_id

    @property
    def bound_resource_names(self):
        """Gets the bound_resource_names of this CreateAuthMethodAzureAD.  # noqa: E501

        A list of resource names that the access is restricted to (e.g, a virtual machine name, scale set name, etc).  # noqa: E501

        :return: The bound_resource_names of this CreateAuthMethodAzureAD.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_resource_names

    @bound_resource_names.setter
    def bound_resource_names(self, bound_resource_names):
        """Sets the bound_resource_names of this CreateAuthMethodAzureAD.

        A list of resource names that the access is restricted to (e.g, a virtual machine name, scale set name, etc).  # noqa: E501

        :param bound_resource_names: The bound_resource_names of this CreateAuthMethodAzureAD.  # noqa: E501
        :type: list[str]
        """

        self._bound_resource_names = bound_resource_names

    @property
    def bound_resource_types(self):
        """Gets the bound_resource_types of this CreateAuthMethodAzureAD.  # noqa: E501

        A list of resource types that the access is restricted to (e.g, virtualMachines, userAssignedIdentities, etc)  # noqa: E501

        :return: The bound_resource_types of this CreateAuthMethodAzureAD.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_resource_types

    @bound_resource_types.setter
    def bound_resource_types(self, bound_resource_types):
        """Sets the bound_resource_types of this CreateAuthMethodAzureAD.

        A list of resource types that the access is restricted to (e.g, virtualMachines, userAssignedIdentities, etc)  # noqa: E501

        :param bound_resource_types: The bound_resource_types of this CreateAuthMethodAzureAD.  # noqa: E501
        :type: list[str]
        """

        self._bound_resource_types = bound_resource_types

    @property
    def bound_rg_id(self):
        """Gets the bound_rg_id of this CreateAuthMethodAzureAD.  # noqa: E501

        A list of resource groups that the access is restricted to  # noqa: E501

        :return: The bound_rg_id of this CreateAuthMethodAzureAD.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_rg_id

    @bound_rg_id.setter
    def bound_rg_id(self, bound_rg_id):
        """Sets the bound_rg_id of this CreateAuthMethodAzureAD.

        A list of resource groups that the access is restricted to  # noqa: E501

        :param bound_rg_id: The bound_rg_id of this CreateAuthMethodAzureAD.  # noqa: E501
        :type: list[str]
        """

        self._bound_rg_id = bound_rg_id

    @property
    def bound_spid(self):
        """Gets the bound_spid of this CreateAuthMethodAzureAD.  # noqa: E501

        A list of service principal IDs that the access is restricted to  # noqa: E501

        :return: The bound_spid of this CreateAuthMethodAzureAD.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_spid

    @bound_spid.setter
    def bound_spid(self, bound_spid):
        """Sets the bound_spid of this CreateAuthMethodAzureAD.

        A list of service principal IDs that the access is restricted to  # noqa: E501

        :param bound_spid: The bound_spid of this CreateAuthMethodAzureAD.  # noqa: E501
        :type: list[str]
        """

        self._bound_spid = bound_spid

    @property
    def bound_sub_id(self):
        """Gets the bound_sub_id of this CreateAuthMethodAzureAD.  # noqa: E501

        A list of subscription ids that the access is restricted to  # noqa: E501

        :return: The bound_sub_id of this CreateAuthMethodAzureAD.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_sub_id

    @bound_sub_id.setter
    def bound_sub_id(self, bound_sub_id):
        """Sets the bound_sub_id of this CreateAuthMethodAzureAD.

        A list of subscription ids that the access is restricted to  # noqa: E501

        :param bound_sub_id: The bound_sub_id of this CreateAuthMethodAzureAD.  # noqa: E501
        :type: list[str]
        """

        self._bound_sub_id = bound_sub_id

    @property
    def bound_tenant_id(self):
        """Gets the bound_tenant_id of this CreateAuthMethodAzureAD.  # noqa: E501

        The Azure tenant id that the access is restricted to  # noqa: E501

        :return: The bound_tenant_id of this CreateAuthMethodAzureAD.  # noqa: E501
        :rtype: str
        """
        return self._bound_tenant_id

    @bound_tenant_id.setter
    def bound_tenant_id(self, bound_tenant_id):
        """Sets the bound_tenant_id of this CreateAuthMethodAzureAD.

        The Azure tenant id that the access is restricted to  # noqa: E501

        :param bound_tenant_id: The bound_tenant_id of this CreateAuthMethodAzureAD.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and bound_tenant_id is None:  # noqa: E501
            raise ValueError("Invalid value for `bound_tenant_id`, must not be `None`")  # noqa: E501

        self._bound_tenant_id = bound_tenant_id

    @property
    def force_sub_claims(self):
        """Gets the force_sub_claims of this CreateAuthMethodAzureAD.  # noqa: E501

        if true: enforce role-association must include sub claims  # noqa: E501

        :return: The force_sub_claims of this CreateAuthMethodAzureAD.  # noqa: E501
        :rtype: bool
        """
        return self._force_sub_claims

    @force_sub_claims.setter
    def force_sub_claims(self, force_sub_claims):
        """Sets the force_sub_claims of this CreateAuthMethodAzureAD.

        if true: enforce role-association must include sub claims  # noqa: E501

        :param force_sub_claims: The force_sub_claims of this CreateAuthMethodAzureAD.  # noqa: E501
        :type: bool
        """

        self._force_sub_claims = force_sub_claims

    @property
    def issuer(self):
        """Gets the issuer of this CreateAuthMethodAzureAD.  # noqa: E501

        Issuer URL  # noqa: E501

        :return: The issuer of this CreateAuthMethodAzureAD.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this CreateAuthMethodAzureAD.

        Issuer URL  # noqa: E501

        :param issuer: The issuer of this CreateAuthMethodAzureAD.  # noqa: E501
        :type: str
        """

        self._issuer = issuer

    @property
    def jwks_uri(self):
        """Gets the jwks_uri of this CreateAuthMethodAzureAD.  # noqa: E501

        The URL to the JSON Web Key Set (JWKS) that containing the public keys that should be used to verify any JSON Web Token (JWT) issued by the authorization server.  # noqa: E501

        :return: The jwks_uri of this CreateAuthMethodAzureAD.  # noqa: E501
        :rtype: str
        """
        return self._jwks_uri

    @jwks_uri.setter
    def jwks_uri(self, jwks_uri):
        """Sets the jwks_uri of this CreateAuthMethodAzureAD.

        The URL to the JSON Web Key Set (JWKS) that containing the public keys that should be used to verify any JSON Web Token (JWT) issued by the authorization server.  # noqa: E501

        :param jwks_uri: The jwks_uri of this CreateAuthMethodAzureAD.  # noqa: E501
        :type: str
        """

        self._jwks_uri = jwks_uri

    @property
    def jwt_ttl(self):
        """Gets the jwt_ttl of this CreateAuthMethodAzureAD.  # noqa: E501

        Jwt TTL  # noqa: E501

        :return: The jwt_ttl of this CreateAuthMethodAzureAD.  # noqa: E501
        :rtype: int
        """
        return self._jwt_ttl

    @jwt_ttl.setter
    def jwt_ttl(self, jwt_ttl):
        """Sets the jwt_ttl of this CreateAuthMethodAzureAD.

        Jwt TTL  # noqa: E501

        :param jwt_ttl: The jwt_ttl of this CreateAuthMethodAzureAD.  # noqa: E501
        :type: int
        """

        self._jwt_ttl = jwt_ttl

    @property
    def name(self):
        """Gets the name of this CreateAuthMethodAzureAD.  # noqa: E501

        Auth Method name  # noqa: E501

        :return: The name of this CreateAuthMethodAzureAD.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateAuthMethodAzureAD.

        Auth Method name  # noqa: E501

        :param name: The name of this CreateAuthMethodAzureAD.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def token(self):
        """Gets the token of this CreateAuthMethodAzureAD.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this CreateAuthMethodAzureAD.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this CreateAuthMethodAzureAD.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this CreateAuthMethodAzureAD.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this CreateAuthMethodAzureAD.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this CreateAuthMethodAzureAD.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this CreateAuthMethodAzureAD.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this CreateAuthMethodAzureAD.  # noqa: E501
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
        if not isinstance(other, CreateAuthMethodAzureAD):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateAuthMethodAzureAD):
            return True

        return self.to_dict() != other.to_dict()
