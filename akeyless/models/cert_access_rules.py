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


class CertAccessRules(object):
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
        'allowed_cors': 'list[str]',
        'bound_common_names': 'list[str]',
        'bound_dns_sans': 'list[str]',
        'bound_email_sans': 'list[str]',
        'bound_extensions': 'list[str]',
        'bound_organizational_units': 'list[str]',
        'bound_uri_sans': 'list[str]',
        'certificate': 'str',
        'revoked_cert_ids': 'list[str]',
        'unique_identifier': 'str'
    }

    attribute_map = {
        'allowed_cors': 'allowed_cors',
        'bound_common_names': 'bound_common_names',
        'bound_dns_sans': 'bound_dns_sans',
        'bound_email_sans': 'bound_email_sans',
        'bound_extensions': 'bound_extensions',
        'bound_organizational_units': 'bound_organizational_units',
        'bound_uri_sans': 'bound_uri_sans',
        'certificate': 'certificate',
        'revoked_cert_ids': 'revoked_cert_ids',
        'unique_identifier': 'unique_identifier'
    }

    def __init__(self, allowed_cors=None, bound_common_names=None, bound_dns_sans=None, bound_email_sans=None, bound_extensions=None, bound_organizational_units=None, bound_uri_sans=None, certificate=None, revoked_cert_ids=None, unique_identifier=None, local_vars_configuration=None):  # noqa: E501
        """CertAccessRules - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._allowed_cors = None
        self._bound_common_names = None
        self._bound_dns_sans = None
        self._bound_email_sans = None
        self._bound_extensions = None
        self._bound_organizational_units = None
        self._bound_uri_sans = None
        self._certificate = None
        self._revoked_cert_ids = None
        self._unique_identifier = None
        self.discriminator = None

        if allowed_cors is not None:
            self.allowed_cors = allowed_cors
        if bound_common_names is not None:
            self.bound_common_names = bound_common_names
        if bound_dns_sans is not None:
            self.bound_dns_sans = bound_dns_sans
        if bound_email_sans is not None:
            self.bound_email_sans = bound_email_sans
        if bound_extensions is not None:
            self.bound_extensions = bound_extensions
        if bound_organizational_units is not None:
            self.bound_organizational_units = bound_organizational_units
        if bound_uri_sans is not None:
            self.bound_uri_sans = bound_uri_sans
        if certificate is not None:
            self.certificate = certificate
        if revoked_cert_ids is not None:
            self.revoked_cert_ids = revoked_cert_ids
        if unique_identifier is not None:
            self.unique_identifier = unique_identifier

    @property
    def allowed_cors(self):
        """Gets the allowed_cors of this CertAccessRules.  # noqa: E501

        a list of allowed cors domains if used for browser authentication  # noqa: E501

        :return: The allowed_cors of this CertAccessRules.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_cors

    @allowed_cors.setter
    def allowed_cors(self, allowed_cors):
        """Sets the allowed_cors of this CertAccessRules.

        a list of allowed cors domains if used for browser authentication  # noqa: E501

        :param allowed_cors: The allowed_cors of this CertAccessRules.  # noqa: E501
        :type: list[str]
        """

        self._allowed_cors = allowed_cors

    @property
    def bound_common_names(self):
        """Gets the bound_common_names of this CertAccessRules.  # noqa: E501

        A list of names. At least one must exist in the Common Name. Supports globbing.  # noqa: E501

        :return: The bound_common_names of this CertAccessRules.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_common_names

    @bound_common_names.setter
    def bound_common_names(self, bound_common_names):
        """Sets the bound_common_names of this CertAccessRules.

        A list of names. At least one must exist in the Common Name. Supports globbing.  # noqa: E501

        :param bound_common_names: The bound_common_names of this CertAccessRules.  # noqa: E501
        :type: list[str]
        """

        self._bound_common_names = bound_common_names

    @property
    def bound_dns_sans(self):
        """Gets the bound_dns_sans of this CertAccessRules.  # noqa: E501

        A list of DNS names. At least one must exist in the SANs. Supports globbing.  # noqa: E501

        :return: The bound_dns_sans of this CertAccessRules.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_dns_sans

    @bound_dns_sans.setter
    def bound_dns_sans(self, bound_dns_sans):
        """Sets the bound_dns_sans of this CertAccessRules.

        A list of DNS names. At least one must exist in the SANs. Supports globbing.  # noqa: E501

        :param bound_dns_sans: The bound_dns_sans of this CertAccessRules.  # noqa: E501
        :type: list[str]
        """

        self._bound_dns_sans = bound_dns_sans

    @property
    def bound_email_sans(self):
        """Gets the bound_email_sans of this CertAccessRules.  # noqa: E501

        A list of Email Addresses. At least one must exist in the SANs. Supports globbing.  # noqa: E501

        :return: The bound_email_sans of this CertAccessRules.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_email_sans

    @bound_email_sans.setter
    def bound_email_sans(self, bound_email_sans):
        """Sets the bound_email_sans of this CertAccessRules.

        A list of Email Addresses. At least one must exist in the SANs. Supports globbing.  # noqa: E501

        :param bound_email_sans: The bound_email_sans of this CertAccessRules.  # noqa: E501
        :type: list[str]
        """

        self._bound_email_sans = bound_email_sans

    @property
    def bound_extensions(self):
        """Gets the bound_extensions of this CertAccessRules.  # noqa: E501

        A list of extensions formatted as \"oid:value\". Expects the extension value to be some type of ASN1 encoded string. All values must match. Supports globbing on \"value\".  # noqa: E501

        :return: The bound_extensions of this CertAccessRules.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_extensions

    @bound_extensions.setter
    def bound_extensions(self, bound_extensions):
        """Sets the bound_extensions of this CertAccessRules.

        A list of extensions formatted as \"oid:value\". Expects the extension value to be some type of ASN1 encoded string. All values must match. Supports globbing on \"value\".  # noqa: E501

        :param bound_extensions: The bound_extensions of this CertAccessRules.  # noqa: E501
        :type: list[str]
        """

        self._bound_extensions = bound_extensions

    @property
    def bound_organizational_units(self):
        """Gets the bound_organizational_units of this CertAccessRules.  # noqa: E501

        A list of Organizational Units names. At least one must exist in the OU field.  # noqa: E501

        :return: The bound_organizational_units of this CertAccessRules.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_organizational_units

    @bound_organizational_units.setter
    def bound_organizational_units(self, bound_organizational_units):
        """Sets the bound_organizational_units of this CertAccessRules.

        A list of Organizational Units names. At least one must exist in the OU field.  # noqa: E501

        :param bound_organizational_units: The bound_organizational_units of this CertAccessRules.  # noqa: E501
        :type: list[str]
        """

        self._bound_organizational_units = bound_organizational_units

    @property
    def bound_uri_sans(self):
        """Gets the bound_uri_sans of this CertAccessRules.  # noqa: E501

        A list of URIs. At least one must exist in the SANs. Supports globbing.  # noqa: E501

        :return: The bound_uri_sans of this CertAccessRules.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_uri_sans

    @bound_uri_sans.setter
    def bound_uri_sans(self, bound_uri_sans):
        """Sets the bound_uri_sans of this CertAccessRules.

        A list of URIs. At least one must exist in the SANs. Supports globbing.  # noqa: E501

        :param bound_uri_sans: The bound_uri_sans of this CertAccessRules.  # noqa: E501
        :type: list[str]
        """

        self._bound_uri_sans = bound_uri_sans

    @property
    def certificate(self):
        """Gets the certificate of this CertAccessRules.  # noqa: E501

        Base64 encdoed PEM certificate  # noqa: E501

        :return: The certificate of this CertAccessRules.  # noqa: E501
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this CertAccessRules.

        Base64 encdoed PEM certificate  # noqa: E501

        :param certificate: The certificate of this CertAccessRules.  # noqa: E501
        :type: str
        """

        self._certificate = certificate

    @property
    def revoked_cert_ids(self):
        """Gets the revoked_cert_ids of this CertAccessRules.  # noqa: E501

        A list of revoked cert ids  # noqa: E501

        :return: The revoked_cert_ids of this CertAccessRules.  # noqa: E501
        :rtype: list[str]
        """
        return self._revoked_cert_ids

    @revoked_cert_ids.setter
    def revoked_cert_ids(self, revoked_cert_ids):
        """Sets the revoked_cert_ids of this CertAccessRules.

        A list of revoked cert ids  # noqa: E501

        :param revoked_cert_ids: The revoked_cert_ids of this CertAccessRules.  # noqa: E501
        :type: list[str]
        """

        self._revoked_cert_ids = revoked_cert_ids

    @property
    def unique_identifier(self):
        """Gets the unique_identifier of this CertAccessRules.  # noqa: E501

        A unique identifier to distinguish different users  # noqa: E501

        :return: The unique_identifier of this CertAccessRules.  # noqa: E501
        :rtype: str
        """
        return self._unique_identifier

    @unique_identifier.setter
    def unique_identifier(self, unique_identifier):
        """Sets the unique_identifier of this CertAccessRules.

        A unique identifier to distinguish different users  # noqa: E501

        :param unique_identifier: The unique_identifier of this CertAccessRules.  # noqa: E501
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
        if not isinstance(other, CertAccessRules):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CertAccessRules):
            return True

        return self.to_dict() != other.to_dict()
