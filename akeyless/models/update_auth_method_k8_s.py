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


class UpdateAuthMethodK8S(object):
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
        'bound_ips': 'list[str]',
        'bound_namespaces': 'list[str]',
        'bound_pod_names': 'list[str]',
        'bound_sa_names': 'list[str]',
        'force_sub_claims': 'bool',
        'gen_key': 'str',
        'gw_bound_ips': 'list[str]',
        'jwt_ttl': 'int',
        'name': 'str',
        'new_name': 'str',
        'public_key': 'str',
        'token': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'access_expires': 'access-expires',
        'audience': 'audience',
        'bound_ips': 'bound-ips',
        'bound_namespaces': 'bound-namespaces',
        'bound_pod_names': 'bound-pod-names',
        'bound_sa_names': 'bound-sa-names',
        'force_sub_claims': 'force-sub-claims',
        'gen_key': 'gen-key',
        'gw_bound_ips': 'gw-bound-ips',
        'jwt_ttl': 'jwt-ttl',
        'name': 'name',
        'new_name': 'new-name',
        'public_key': 'public-key',
        'token': 'token',
        'uid_token': 'uid-token'
    }

    def __init__(self, access_expires=0, audience=None, bound_ips=None, bound_namespaces=None, bound_pod_names=None, bound_sa_names=None, force_sub_claims=None, gen_key='true', gw_bound_ips=None, jwt_ttl=None, name=None, new_name=None, public_key=None, token=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """UpdateAuthMethodK8S - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_expires = None
        self._audience = None
        self._bound_ips = None
        self._bound_namespaces = None
        self._bound_pod_names = None
        self._bound_sa_names = None
        self._force_sub_claims = None
        self._gen_key = None
        self._gw_bound_ips = None
        self._jwt_ttl = None
        self._name = None
        self._new_name = None
        self._public_key = None
        self._token = None
        self._uid_token = None
        self.discriminator = None

        if access_expires is not None:
            self.access_expires = access_expires
        if audience is not None:
            self.audience = audience
        if bound_ips is not None:
            self.bound_ips = bound_ips
        if bound_namespaces is not None:
            self.bound_namespaces = bound_namespaces
        if bound_pod_names is not None:
            self.bound_pod_names = bound_pod_names
        if bound_sa_names is not None:
            self.bound_sa_names = bound_sa_names
        if force_sub_claims is not None:
            self.force_sub_claims = force_sub_claims
        if gen_key is not None:
            self.gen_key = gen_key
        if gw_bound_ips is not None:
            self.gw_bound_ips = gw_bound_ips
        if jwt_ttl is not None:
            self.jwt_ttl = jwt_ttl
        self.name = name
        if new_name is not None:
            self.new_name = new_name
        if public_key is not None:
            self.public_key = public_key
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def access_expires(self):
        """Gets the access_expires of this UpdateAuthMethodK8S.  # noqa: E501

        Access expiration date in Unix timestamp (select 0 for access without expiry date)  # noqa: E501

        :return: The access_expires of this UpdateAuthMethodK8S.  # noqa: E501
        :rtype: int
        """
        return self._access_expires

    @access_expires.setter
    def access_expires(self, access_expires):
        """Sets the access_expires of this UpdateAuthMethodK8S.

        Access expiration date in Unix timestamp (select 0 for access without expiry date)  # noqa: E501

        :param access_expires: The access_expires of this UpdateAuthMethodK8S.  # noqa: E501
        :type: int
        """

        self._access_expires = access_expires

    @property
    def audience(self):
        """Gets the audience of this UpdateAuthMethodK8S.  # noqa: E501

        The audience in the Kubernetes JWT that the access is restricted to  # noqa: E501

        :return: The audience of this UpdateAuthMethodK8S.  # noqa: E501
        :rtype: str
        """
        return self._audience

    @audience.setter
    def audience(self, audience):
        """Sets the audience of this UpdateAuthMethodK8S.

        The audience in the Kubernetes JWT that the access is restricted to  # noqa: E501

        :param audience: The audience of this UpdateAuthMethodK8S.  # noqa: E501
        :type: str
        """

        self._audience = audience

    @property
    def bound_ips(self):
        """Gets the bound_ips of this UpdateAuthMethodK8S.  # noqa: E501

        A CIDR whitelist with the IPs that the access is restricted to  # noqa: E501

        :return: The bound_ips of this UpdateAuthMethodK8S.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_ips

    @bound_ips.setter
    def bound_ips(self, bound_ips):
        """Sets the bound_ips of this UpdateAuthMethodK8S.

        A CIDR whitelist with the IPs that the access is restricted to  # noqa: E501

        :param bound_ips: The bound_ips of this UpdateAuthMethodK8S.  # noqa: E501
        :type: list[str]
        """

        self._bound_ips = bound_ips

    @property
    def bound_namespaces(self):
        """Gets the bound_namespaces of this UpdateAuthMethodK8S.  # noqa: E501

        A list of namespaces that the access is restricted to  # noqa: E501

        :return: The bound_namespaces of this UpdateAuthMethodK8S.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_namespaces

    @bound_namespaces.setter
    def bound_namespaces(self, bound_namespaces):
        """Sets the bound_namespaces of this UpdateAuthMethodK8S.

        A list of namespaces that the access is restricted to  # noqa: E501

        :param bound_namespaces: The bound_namespaces of this UpdateAuthMethodK8S.  # noqa: E501
        :type: list[str]
        """

        self._bound_namespaces = bound_namespaces

    @property
    def bound_pod_names(self):
        """Gets the bound_pod_names of this UpdateAuthMethodK8S.  # noqa: E501

        A list of pod names that the access is restricted to  # noqa: E501

        :return: The bound_pod_names of this UpdateAuthMethodK8S.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_pod_names

    @bound_pod_names.setter
    def bound_pod_names(self, bound_pod_names):
        """Sets the bound_pod_names of this UpdateAuthMethodK8S.

        A list of pod names that the access is restricted to  # noqa: E501

        :param bound_pod_names: The bound_pod_names of this UpdateAuthMethodK8S.  # noqa: E501
        :type: list[str]
        """

        self._bound_pod_names = bound_pod_names

    @property
    def bound_sa_names(self):
        """Gets the bound_sa_names of this UpdateAuthMethodK8S.  # noqa: E501

        A list of service account names that the access is restricted to  # noqa: E501

        :return: The bound_sa_names of this UpdateAuthMethodK8S.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_sa_names

    @bound_sa_names.setter
    def bound_sa_names(self, bound_sa_names):
        """Sets the bound_sa_names of this UpdateAuthMethodK8S.

        A list of service account names that the access is restricted to  # noqa: E501

        :param bound_sa_names: The bound_sa_names of this UpdateAuthMethodK8S.  # noqa: E501
        :type: list[str]
        """

        self._bound_sa_names = bound_sa_names

    @property
    def force_sub_claims(self):
        """Gets the force_sub_claims of this UpdateAuthMethodK8S.  # noqa: E501

        if true: enforce role-association must include sub claims  # noqa: E501

        :return: The force_sub_claims of this UpdateAuthMethodK8S.  # noqa: E501
        :rtype: bool
        """
        return self._force_sub_claims

    @force_sub_claims.setter
    def force_sub_claims(self, force_sub_claims):
        """Sets the force_sub_claims of this UpdateAuthMethodK8S.

        if true: enforce role-association must include sub claims  # noqa: E501

        :param force_sub_claims: The force_sub_claims of this UpdateAuthMethodK8S.  # noqa: E501
        :type: bool
        """

        self._force_sub_claims = force_sub_claims

    @property
    def gen_key(self):
        """Gets the gen_key of this UpdateAuthMethodK8S.  # noqa: E501

        If this flag is set to true, there is no need to manually provide a public key for the Kubernetes Auth Method, and instead, a key pair, will be generated as part of the command and the private part of the key will be returned (the private key is required for the K8S Auth Config in the Akeyless Gateway)  # noqa: E501

        :return: The gen_key of this UpdateAuthMethodK8S.  # noqa: E501
        :rtype: str
        """
        return self._gen_key

    @gen_key.setter
    def gen_key(self, gen_key):
        """Sets the gen_key of this UpdateAuthMethodK8S.

        If this flag is set to true, there is no need to manually provide a public key for the Kubernetes Auth Method, and instead, a key pair, will be generated as part of the command and the private part of the key will be returned (the private key is required for the K8S Auth Config in the Akeyless Gateway)  # noqa: E501

        :param gen_key: The gen_key of this UpdateAuthMethodK8S.  # noqa: E501
        :type: str
        """

        self._gen_key = gen_key

    @property
    def gw_bound_ips(self):
        """Gets the gw_bound_ips of this UpdateAuthMethodK8S.  # noqa: E501

        A CIDR whitelist with the GW IPs that the access is restricted to  # noqa: E501

        :return: The gw_bound_ips of this UpdateAuthMethodK8S.  # noqa: E501
        :rtype: list[str]
        """
        return self._gw_bound_ips

    @gw_bound_ips.setter
    def gw_bound_ips(self, gw_bound_ips):
        """Sets the gw_bound_ips of this UpdateAuthMethodK8S.

        A CIDR whitelist with the GW IPs that the access is restricted to  # noqa: E501

        :param gw_bound_ips: The gw_bound_ips of this UpdateAuthMethodK8S.  # noqa: E501
        :type: list[str]
        """

        self._gw_bound_ips = gw_bound_ips

    @property
    def jwt_ttl(self):
        """Gets the jwt_ttl of this UpdateAuthMethodK8S.  # noqa: E501

        Jwt TTL  # noqa: E501

        :return: The jwt_ttl of this UpdateAuthMethodK8S.  # noqa: E501
        :rtype: int
        """
        return self._jwt_ttl

    @jwt_ttl.setter
    def jwt_ttl(self, jwt_ttl):
        """Sets the jwt_ttl of this UpdateAuthMethodK8S.

        Jwt TTL  # noqa: E501

        :param jwt_ttl: The jwt_ttl of this UpdateAuthMethodK8S.  # noqa: E501
        :type: int
        """

        self._jwt_ttl = jwt_ttl

    @property
    def name(self):
        """Gets the name of this UpdateAuthMethodK8S.  # noqa: E501

        Auth Method name  # noqa: E501

        :return: The name of this UpdateAuthMethodK8S.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateAuthMethodK8S.

        Auth Method name  # noqa: E501

        :param name: The name of this UpdateAuthMethodK8S.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def new_name(self):
        """Gets the new_name of this UpdateAuthMethodK8S.  # noqa: E501

        Auth Method new name  # noqa: E501

        :return: The new_name of this UpdateAuthMethodK8S.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this UpdateAuthMethodK8S.

        Auth Method new name  # noqa: E501

        :param new_name: The new_name of this UpdateAuthMethodK8S.  # noqa: E501
        :type: str
        """

        self._new_name = new_name

    @property
    def public_key(self):
        """Gets the public_key of this UpdateAuthMethodK8S.  # noqa: E501

        Base64-encoded public key text for K8S authentication method is required [RSA2048]  # noqa: E501

        :return: The public_key of this UpdateAuthMethodK8S.  # noqa: E501
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this UpdateAuthMethodK8S.

        Base64-encoded public key text for K8S authentication method is required [RSA2048]  # noqa: E501

        :param public_key: The public_key of this UpdateAuthMethodK8S.  # noqa: E501
        :type: str
        """

        self._public_key = public_key

    @property
    def token(self):
        """Gets the token of this UpdateAuthMethodK8S.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this UpdateAuthMethodK8S.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this UpdateAuthMethodK8S.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this UpdateAuthMethodK8S.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this UpdateAuthMethodK8S.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this UpdateAuthMethodK8S.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this UpdateAuthMethodK8S.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this UpdateAuthMethodK8S.  # noqa: E501
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
        if not isinstance(other, UpdateAuthMethodK8S):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateAuthMethodK8S):
            return True

        return self.to_dict() != other.to_dict()
