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


class UpdateAuthMethodCert(object):
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
        'bound_common_names': 'list[str]',
        'bound_dns_sans': 'list[str]',
        'bound_email_sans': 'list[str]',
        'bound_extensions': 'list[str]',
        'bound_ips': 'list[str]',
        'bound_organizational_units': 'list[str]',
        'bound_uri_sans': 'list[str]',
        'certificate_data': 'str',
        'force_sub_claims': 'bool',
        'jwt_ttl': 'int',
        'name': 'str',
        'new_name': 'str',
        'revoked_cert_ids': 'list[str]',
        'token': 'str',
        'uid_token': 'str',
        'unique_identifier': 'str'
    }

    attribute_map = {
        'access_expires': 'access-expires',
        'bound_common_names': 'bound-common-names',
        'bound_dns_sans': 'bound-dns-sans',
        'bound_email_sans': 'bound-email-sans',
        'bound_extensions': 'bound-extensions',
        'bound_ips': 'bound-ips',
        'bound_organizational_units': 'bound-organizational-units',
        'bound_uri_sans': 'bound-uri-sans',
        'certificate_data': 'certificate-data',
        'force_sub_claims': 'force-sub-claims',
        'jwt_ttl': 'jwt-ttl',
        'name': 'name',
        'new_name': 'new-name',
        'revoked_cert_ids': 'revoked-cert-ids',
        'token': 'token',
        'uid_token': 'uid-token',
        'unique_identifier': 'unique-identifier'
    }

    def __init__(self, access_expires=0, bound_common_names=None, bound_dns_sans=None, bound_email_sans=None, bound_extensions=None, bound_ips=None, bound_organizational_units=None, bound_uri_sans=None, certificate_data=None, force_sub_claims=None, jwt_ttl=None, name=None, new_name=None, revoked_cert_ids=None, token=None, uid_token=None, unique_identifier=None, local_vars_configuration=None):  # noqa: E501
        """UpdateAuthMethodCert - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_expires = None
        self._bound_common_names = None
        self._bound_dns_sans = None
        self._bound_email_sans = None
        self._bound_extensions = None
        self._bound_ips = None
        self._bound_organizational_units = None
        self._bound_uri_sans = None
        self._certificate_data = None
        self._force_sub_claims = None
        self._jwt_ttl = None
        self._name = None
        self._new_name = None
        self._revoked_cert_ids = None
        self._token = None
        self._uid_token = None
        self._unique_identifier = None
        self.discriminator = None

        if access_expires is not None:
            self.access_expires = access_expires
        if bound_common_names is not None:
            self.bound_common_names = bound_common_names
        if bound_dns_sans is not None:
            self.bound_dns_sans = bound_dns_sans
        if bound_email_sans is not None:
            self.bound_email_sans = bound_email_sans
        if bound_extensions is not None:
            self.bound_extensions = bound_extensions
        if bound_ips is not None:
            self.bound_ips = bound_ips
        if bound_organizational_units is not None:
            self.bound_organizational_units = bound_organizational_units
        if bound_uri_sans is not None:
            self.bound_uri_sans = bound_uri_sans
        if certificate_data is not None:
            self.certificate_data = certificate_data
        if force_sub_claims is not None:
            self.force_sub_claims = force_sub_claims
        if jwt_ttl is not None:
            self.jwt_ttl = jwt_ttl
        self.name = name
        if new_name is not None:
            self.new_name = new_name
        if revoked_cert_ids is not None:
            self.revoked_cert_ids = revoked_cert_ids
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        self.unique_identifier = unique_identifier

    @property
    def access_expires(self):
        """Gets the access_expires of this UpdateAuthMethodCert.  # noqa: E501

        Access expiration date in Unix timestamp (select 0 for access without expiry date)  # noqa: E501

        :return: The access_expires of this UpdateAuthMethodCert.  # noqa: E501
        :rtype: int
        """
        return self._access_expires

    @access_expires.setter
    def access_expires(self, access_expires):
        """Sets the access_expires of this UpdateAuthMethodCert.

        Access expiration date in Unix timestamp (select 0 for access without expiry date)  # noqa: E501

        :param access_expires: The access_expires of this UpdateAuthMethodCert.  # noqa: E501
        :type: int
        """

        self._access_expires = access_expires

    @property
    def bound_common_names(self):
        """Gets the bound_common_names of this UpdateAuthMethodCert.  # noqa: E501

        A list of names. At least one must exist in the Common Name. Supports globbing.  # noqa: E501

        :return: The bound_common_names of this UpdateAuthMethodCert.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_common_names

    @bound_common_names.setter
    def bound_common_names(self, bound_common_names):
        """Sets the bound_common_names of this UpdateAuthMethodCert.

        A list of names. At least one must exist in the Common Name. Supports globbing.  # noqa: E501

        :param bound_common_names: The bound_common_names of this UpdateAuthMethodCert.  # noqa: E501
        :type: list[str]
        """

        self._bound_common_names = bound_common_names

    @property
    def bound_dns_sans(self):
        """Gets the bound_dns_sans of this UpdateAuthMethodCert.  # noqa: E501

        A list of DNS names. At least one must exist in the SANs. Supports globbing.  # noqa: E501

        :return: The bound_dns_sans of this UpdateAuthMethodCert.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_dns_sans

    @bound_dns_sans.setter
    def bound_dns_sans(self, bound_dns_sans):
        """Sets the bound_dns_sans of this UpdateAuthMethodCert.

        A list of DNS names. At least one must exist in the SANs. Supports globbing.  # noqa: E501

        :param bound_dns_sans: The bound_dns_sans of this UpdateAuthMethodCert.  # noqa: E501
        :type: list[str]
        """

        self._bound_dns_sans = bound_dns_sans

    @property
    def bound_email_sans(self):
        """Gets the bound_email_sans of this UpdateAuthMethodCert.  # noqa: E501

        A list of Email Addresses. At least one must exist in the SANs. Supports globbing.  # noqa: E501

        :return: The bound_email_sans of this UpdateAuthMethodCert.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_email_sans

    @bound_email_sans.setter
    def bound_email_sans(self, bound_email_sans):
        """Sets the bound_email_sans of this UpdateAuthMethodCert.

        A list of Email Addresses. At least one must exist in the SANs. Supports globbing.  # noqa: E501

        :param bound_email_sans: The bound_email_sans of this UpdateAuthMethodCert.  # noqa: E501
        :type: list[str]
        """

        self._bound_email_sans = bound_email_sans

    @property
    def bound_extensions(self):
        """Gets the bound_extensions of this UpdateAuthMethodCert.  # noqa: E501

        A list of extensions formatted as \"oid:value\". Expects the extension value to be some type of ASN1 encoded string. All values much match. Supports globbing on \"value\".  # noqa: E501

        :return: The bound_extensions of this UpdateAuthMethodCert.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_extensions

    @bound_extensions.setter
    def bound_extensions(self, bound_extensions):
        """Sets the bound_extensions of this UpdateAuthMethodCert.

        A list of extensions formatted as \"oid:value\". Expects the extension value to be some type of ASN1 encoded string. All values much match. Supports globbing on \"value\".  # noqa: E501

        :param bound_extensions: The bound_extensions of this UpdateAuthMethodCert.  # noqa: E501
        :type: list[str]
        """

        self._bound_extensions = bound_extensions

    @property
    def bound_ips(self):
        """Gets the bound_ips of this UpdateAuthMethodCert.  # noqa: E501

        A CIDR whitelist with the IPs that the access is restricted to  # noqa: E501

        :return: The bound_ips of this UpdateAuthMethodCert.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_ips

    @bound_ips.setter
    def bound_ips(self, bound_ips):
        """Sets the bound_ips of this UpdateAuthMethodCert.

        A CIDR whitelist with the IPs that the access is restricted to  # noqa: E501

        :param bound_ips: The bound_ips of this UpdateAuthMethodCert.  # noqa: E501
        :type: list[str]
        """

        self._bound_ips = bound_ips

    @property
    def bound_organizational_units(self):
        """Gets the bound_organizational_units of this UpdateAuthMethodCert.  # noqa: E501

        A list of Organizational Units names. At least one must exist in the OU field.  # noqa: E501

        :return: The bound_organizational_units of this UpdateAuthMethodCert.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_organizational_units

    @bound_organizational_units.setter
    def bound_organizational_units(self, bound_organizational_units):
        """Sets the bound_organizational_units of this UpdateAuthMethodCert.

        A list of Organizational Units names. At least one must exist in the OU field.  # noqa: E501

        :param bound_organizational_units: The bound_organizational_units of this UpdateAuthMethodCert.  # noqa: E501
        :type: list[str]
        """

        self._bound_organizational_units = bound_organizational_units

    @property
    def bound_uri_sans(self):
        """Gets the bound_uri_sans of this UpdateAuthMethodCert.  # noqa: E501

        A list of URIs. At least one must exist in the SANs. Supports globbing.  # noqa: E501

        :return: The bound_uri_sans of this UpdateAuthMethodCert.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_uri_sans

    @bound_uri_sans.setter
    def bound_uri_sans(self, bound_uri_sans):
        """Sets the bound_uri_sans of this UpdateAuthMethodCert.

        A list of URIs. At least one must exist in the SANs. Supports globbing.  # noqa: E501

        :param bound_uri_sans: The bound_uri_sans of this UpdateAuthMethodCert.  # noqa: E501
        :type: list[str]
        """

        self._bound_uri_sans = bound_uri_sans

    @property
    def certificate_data(self):
        """Gets the certificate_data of this UpdateAuthMethodCert.  # noqa: E501

        The certificate data in base64, if no file was provided  # noqa: E501

        :return: The certificate_data of this UpdateAuthMethodCert.  # noqa: E501
        :rtype: str
        """
        return self._certificate_data

    @certificate_data.setter
    def certificate_data(self, certificate_data):
        """Sets the certificate_data of this UpdateAuthMethodCert.

        The certificate data in base64, if no file was provided  # noqa: E501

        :param certificate_data: The certificate_data of this UpdateAuthMethodCert.  # noqa: E501
        :type: str
        """

        self._certificate_data = certificate_data

    @property
    def force_sub_claims(self):
        """Gets the force_sub_claims of this UpdateAuthMethodCert.  # noqa: E501

        if true: enforce role-association must include sub claims  # noqa: E501

        :return: The force_sub_claims of this UpdateAuthMethodCert.  # noqa: E501
        :rtype: bool
        """
        return self._force_sub_claims

    @force_sub_claims.setter
    def force_sub_claims(self, force_sub_claims):
        """Sets the force_sub_claims of this UpdateAuthMethodCert.

        if true: enforce role-association must include sub claims  # noqa: E501

        :param force_sub_claims: The force_sub_claims of this UpdateAuthMethodCert.  # noqa: E501
        :type: bool
        """

        self._force_sub_claims = force_sub_claims

    @property
    def jwt_ttl(self):
        """Gets the jwt_ttl of this UpdateAuthMethodCert.  # noqa: E501

        Jwt TTL  # noqa: E501

        :return: The jwt_ttl of this UpdateAuthMethodCert.  # noqa: E501
        :rtype: int
        """
        return self._jwt_ttl

    @jwt_ttl.setter
    def jwt_ttl(self, jwt_ttl):
        """Sets the jwt_ttl of this UpdateAuthMethodCert.

        Jwt TTL  # noqa: E501

        :param jwt_ttl: The jwt_ttl of this UpdateAuthMethodCert.  # noqa: E501
        :type: int
        """

        self._jwt_ttl = jwt_ttl

    @property
    def name(self):
        """Gets the name of this UpdateAuthMethodCert.  # noqa: E501

        Auth Method name  # noqa: E501

        :return: The name of this UpdateAuthMethodCert.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateAuthMethodCert.

        Auth Method name  # noqa: E501

        :param name: The name of this UpdateAuthMethodCert.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def new_name(self):
        """Gets the new_name of this UpdateAuthMethodCert.  # noqa: E501

        Auth Method new name  # noqa: E501

        :return: The new_name of this UpdateAuthMethodCert.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this UpdateAuthMethodCert.

        Auth Method new name  # noqa: E501

        :param new_name: The new_name of this UpdateAuthMethodCert.  # noqa: E501
        :type: str
        """

        self._new_name = new_name

    @property
    def revoked_cert_ids(self):
        """Gets the revoked_cert_ids of this UpdateAuthMethodCert.  # noqa: E501

        A list of revoked cert ids  # noqa: E501

        :return: The revoked_cert_ids of this UpdateAuthMethodCert.  # noqa: E501
        :rtype: list[str]
        """
        return self._revoked_cert_ids

    @revoked_cert_ids.setter
    def revoked_cert_ids(self, revoked_cert_ids):
        """Sets the revoked_cert_ids of this UpdateAuthMethodCert.

        A list of revoked cert ids  # noqa: E501

        :param revoked_cert_ids: The revoked_cert_ids of this UpdateAuthMethodCert.  # noqa: E501
        :type: list[str]
        """

        self._revoked_cert_ids = revoked_cert_ids

    @property
    def token(self):
        """Gets the token of this UpdateAuthMethodCert.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this UpdateAuthMethodCert.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this UpdateAuthMethodCert.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this UpdateAuthMethodCert.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this UpdateAuthMethodCert.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this UpdateAuthMethodCert.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this UpdateAuthMethodCert.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this UpdateAuthMethodCert.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def unique_identifier(self):
        """Gets the unique_identifier of this UpdateAuthMethodCert.  # noqa: E501

        A unique identifier (ID) value should be configured, such as common_name or organizational_unit Whenever a user logs in with a token, these authentication types issue a \"sub claim\" that contains details uniquely identifying that user. This sub claim includes a key containing the ID value that you configured, and is used to distinguish between different users from within the same organization.  # noqa: E501

        :return: The unique_identifier of this UpdateAuthMethodCert.  # noqa: E501
        :rtype: str
        """
        return self._unique_identifier

    @unique_identifier.setter
    def unique_identifier(self, unique_identifier):
        """Sets the unique_identifier of this UpdateAuthMethodCert.

        A unique identifier (ID) value should be configured, such as common_name or organizational_unit Whenever a user logs in with a token, these authentication types issue a \"sub claim\" that contains details uniquely identifying that user. This sub claim includes a key containing the ID value that you configured, and is used to distinguish between different users from within the same organization.  # noqa: E501

        :param unique_identifier: The unique_identifier of this UpdateAuthMethodCert.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and unique_identifier is None:  # noqa: E501
            raise ValueError("Invalid value for `unique_identifier`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, UpdateAuthMethodCert):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateAuthMethodCert):
            return True

        return self.to_dict() != other.to_dict()
