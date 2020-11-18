# coding: utf-8

"""
    Akeyless API

    The purpose of this application is to provide access to Akeyless API.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: support@akeyless.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from akeyless.configuration import Configuration


class PKICertificateIssueDetails(object):
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
        'allow_any_name': 'bool',
        'allow_subdomains': 'bool',
        'allowed_domains_list': 'list[str]',
        'allowed_uri_sans': 'list[str]',
        'client_flag': 'bool',
        'code_signing_flag': 'bool',
        'country': 'list[str]',
        'enforce_hostnames': 'bool',
        'key_bits': 'int',
        'key_type': 'str',
        'key_usage_list': 'list[str]',
        'locality': 'list[str]',
        'not_before_duration': 'int',
        'organization_list': 'list[str]',
        'organization_unit_list': 'list[str]',
        'postal_code': 'list[str]',
        'province': 'list[str]',
        'require_cn': 'bool',
        'server_flag': 'bool',
        'street_address': 'list[str]'
    }

    attribute_map = {
        'allow_any_name': 'allow_any_name',
        'allow_subdomains': 'allow_subdomains',
        'allowed_domains_list': 'allowed_domains_list',
        'allowed_uri_sans': 'allowed_uri_sans',
        'client_flag': 'client_flag',
        'code_signing_flag': 'code_signing_flag',
        'country': 'country',
        'enforce_hostnames': 'enforce_hostnames',
        'key_bits': 'key_bits',
        'key_type': 'key_type',
        'key_usage_list': 'key_usage_list',
        'locality': 'locality',
        'not_before_duration': 'not_before_duration',
        'organization_list': 'organization_list',
        'organization_unit_list': 'organization_unit_list',
        'postal_code': 'postal_code',
        'province': 'province',
        'require_cn': 'require_cn',
        'server_flag': 'server_flag',
        'street_address': 'street_address'
    }

    def __init__(self, allow_any_name=None, allow_subdomains=None, allowed_domains_list=None, allowed_uri_sans=None, client_flag=None, code_signing_flag=None, country=None, enforce_hostnames=None, key_bits=None, key_type=None, key_usage_list=None, locality=None, not_before_duration=None, organization_list=None, organization_unit_list=None, postal_code=None, province=None, require_cn=None, server_flag=None, street_address=None, local_vars_configuration=None):  # noqa: E501
        """PKICertificateIssueDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._allow_any_name = None
        self._allow_subdomains = None
        self._allowed_domains_list = None
        self._allowed_uri_sans = None
        self._client_flag = None
        self._code_signing_flag = None
        self._country = None
        self._enforce_hostnames = None
        self._key_bits = None
        self._key_type = None
        self._key_usage_list = None
        self._locality = None
        self._not_before_duration = None
        self._organization_list = None
        self._organization_unit_list = None
        self._postal_code = None
        self._province = None
        self._require_cn = None
        self._server_flag = None
        self._street_address = None
        self.discriminator = None

        if allow_any_name is not None:
            self.allow_any_name = allow_any_name
        if allow_subdomains is not None:
            self.allow_subdomains = allow_subdomains
        if allowed_domains_list is not None:
            self.allowed_domains_list = allowed_domains_list
        if allowed_uri_sans is not None:
            self.allowed_uri_sans = allowed_uri_sans
        if client_flag is not None:
            self.client_flag = client_flag
        if code_signing_flag is not None:
            self.code_signing_flag = code_signing_flag
        if country is not None:
            self.country = country
        if enforce_hostnames is not None:
            self.enforce_hostnames = enforce_hostnames
        if key_bits is not None:
            self.key_bits = key_bits
        if key_type is not None:
            self.key_type = key_type
        if key_usage_list is not None:
            self.key_usage_list = key_usage_list
        if locality is not None:
            self.locality = locality
        if not_before_duration is not None:
            self.not_before_duration = not_before_duration
        if organization_list is not None:
            self.organization_list = organization_list
        if organization_unit_list is not None:
            self.organization_unit_list = organization_unit_list
        if postal_code is not None:
            self.postal_code = postal_code
        if province is not None:
            self.province = province
        if require_cn is not None:
            self.require_cn = require_cn
        if server_flag is not None:
            self.server_flag = server_flag
        if street_address is not None:
            self.street_address = street_address

    @property
    def allow_any_name(self):
        """Gets the allow_any_name of this PKICertificateIssueDetails.  # noqa: E501


        :return: The allow_any_name of this PKICertificateIssueDetails.  # noqa: E501
        :rtype: bool
        """
        return self._allow_any_name

    @allow_any_name.setter
    def allow_any_name(self, allow_any_name):
        """Sets the allow_any_name of this PKICertificateIssueDetails.


        :param allow_any_name: The allow_any_name of this PKICertificateIssueDetails.  # noqa: E501
        :type: bool
        """

        self._allow_any_name = allow_any_name

    @property
    def allow_subdomains(self):
        """Gets the allow_subdomains of this PKICertificateIssueDetails.  # noqa: E501


        :return: The allow_subdomains of this PKICertificateIssueDetails.  # noqa: E501
        :rtype: bool
        """
        return self._allow_subdomains

    @allow_subdomains.setter
    def allow_subdomains(self, allow_subdomains):
        """Sets the allow_subdomains of this PKICertificateIssueDetails.


        :param allow_subdomains: The allow_subdomains of this PKICertificateIssueDetails.  # noqa: E501
        :type: bool
        """

        self._allow_subdomains = allow_subdomains

    @property
    def allowed_domains_list(self):
        """Gets the allowed_domains_list of this PKICertificateIssueDetails.  # noqa: E501


        :return: The allowed_domains_list of this PKICertificateIssueDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_domains_list

    @allowed_domains_list.setter
    def allowed_domains_list(self, allowed_domains_list):
        """Sets the allowed_domains_list of this PKICertificateIssueDetails.


        :param allowed_domains_list: The allowed_domains_list of this PKICertificateIssueDetails.  # noqa: E501
        :type: list[str]
        """

        self._allowed_domains_list = allowed_domains_list

    @property
    def allowed_uri_sans(self):
        """Gets the allowed_uri_sans of this PKICertificateIssueDetails.  # noqa: E501


        :return: The allowed_uri_sans of this PKICertificateIssueDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_uri_sans

    @allowed_uri_sans.setter
    def allowed_uri_sans(self, allowed_uri_sans):
        """Sets the allowed_uri_sans of this PKICertificateIssueDetails.


        :param allowed_uri_sans: The allowed_uri_sans of this PKICertificateIssueDetails.  # noqa: E501
        :type: list[str]
        """

        self._allowed_uri_sans = allowed_uri_sans

    @property
    def client_flag(self):
        """Gets the client_flag of this PKICertificateIssueDetails.  # noqa: E501


        :return: The client_flag of this PKICertificateIssueDetails.  # noqa: E501
        :rtype: bool
        """
        return self._client_flag

    @client_flag.setter
    def client_flag(self, client_flag):
        """Sets the client_flag of this PKICertificateIssueDetails.


        :param client_flag: The client_flag of this PKICertificateIssueDetails.  # noqa: E501
        :type: bool
        """

        self._client_flag = client_flag

    @property
    def code_signing_flag(self):
        """Gets the code_signing_flag of this PKICertificateIssueDetails.  # noqa: E501


        :return: The code_signing_flag of this PKICertificateIssueDetails.  # noqa: E501
        :rtype: bool
        """
        return self._code_signing_flag

    @code_signing_flag.setter
    def code_signing_flag(self, code_signing_flag):
        """Sets the code_signing_flag of this PKICertificateIssueDetails.


        :param code_signing_flag: The code_signing_flag of this PKICertificateIssueDetails.  # noqa: E501
        :type: bool
        """

        self._code_signing_flag = code_signing_flag

    @property
    def country(self):
        """Gets the country of this PKICertificateIssueDetails.  # noqa: E501


        :return: The country of this PKICertificateIssueDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this PKICertificateIssueDetails.


        :param country: The country of this PKICertificateIssueDetails.  # noqa: E501
        :type: list[str]
        """

        self._country = country

    @property
    def enforce_hostnames(self):
        """Gets the enforce_hostnames of this PKICertificateIssueDetails.  # noqa: E501


        :return: The enforce_hostnames of this PKICertificateIssueDetails.  # noqa: E501
        :rtype: bool
        """
        return self._enforce_hostnames

    @enforce_hostnames.setter
    def enforce_hostnames(self, enforce_hostnames):
        """Sets the enforce_hostnames of this PKICertificateIssueDetails.


        :param enforce_hostnames: The enforce_hostnames of this PKICertificateIssueDetails.  # noqa: E501
        :type: bool
        """

        self._enforce_hostnames = enforce_hostnames

    @property
    def key_bits(self):
        """Gets the key_bits of this PKICertificateIssueDetails.  # noqa: E501


        :return: The key_bits of this PKICertificateIssueDetails.  # noqa: E501
        :rtype: int
        """
        return self._key_bits

    @key_bits.setter
    def key_bits(self, key_bits):
        """Sets the key_bits of this PKICertificateIssueDetails.


        :param key_bits: The key_bits of this PKICertificateIssueDetails.  # noqa: E501
        :type: int
        """

        self._key_bits = key_bits

    @property
    def key_type(self):
        """Gets the key_type of this PKICertificateIssueDetails.  # noqa: E501


        :return: The key_type of this PKICertificateIssueDetails.  # noqa: E501
        :rtype: str
        """
        return self._key_type

    @key_type.setter
    def key_type(self, key_type):
        """Sets the key_type of this PKICertificateIssueDetails.


        :param key_type: The key_type of this PKICertificateIssueDetails.  # noqa: E501
        :type: str
        """

        self._key_type = key_type

    @property
    def key_usage_list(self):
        """Gets the key_usage_list of this PKICertificateIssueDetails.  # noqa: E501


        :return: The key_usage_list of this PKICertificateIssueDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._key_usage_list

    @key_usage_list.setter
    def key_usage_list(self, key_usage_list):
        """Sets the key_usage_list of this PKICertificateIssueDetails.


        :param key_usage_list: The key_usage_list of this PKICertificateIssueDetails.  # noqa: E501
        :type: list[str]
        """

        self._key_usage_list = key_usage_list

    @property
    def locality(self):
        """Gets the locality of this PKICertificateIssueDetails.  # noqa: E501


        :return: The locality of this PKICertificateIssueDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """Sets the locality of this PKICertificateIssueDetails.


        :param locality: The locality of this PKICertificateIssueDetails.  # noqa: E501
        :type: list[str]
        """

        self._locality = locality

    @property
    def not_before_duration(self):
        """Gets the not_before_duration of this PKICertificateIssueDetails.  # noqa: E501

        A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years.  # noqa: E501

        :return: The not_before_duration of this PKICertificateIssueDetails.  # noqa: E501
        :rtype: int
        """
        return self._not_before_duration

    @not_before_duration.setter
    def not_before_duration(self, not_before_duration):
        """Sets the not_before_duration of this PKICertificateIssueDetails.

        A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years.  # noqa: E501

        :param not_before_duration: The not_before_duration of this PKICertificateIssueDetails.  # noqa: E501
        :type: int
        """

        self._not_before_duration = not_before_duration

    @property
    def organization_list(self):
        """Gets the organization_list of this PKICertificateIssueDetails.  # noqa: E501


        :return: The organization_list of this PKICertificateIssueDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._organization_list

    @organization_list.setter
    def organization_list(self, organization_list):
        """Sets the organization_list of this PKICertificateIssueDetails.


        :param organization_list: The organization_list of this PKICertificateIssueDetails.  # noqa: E501
        :type: list[str]
        """

        self._organization_list = organization_list

    @property
    def organization_unit_list(self):
        """Gets the organization_unit_list of this PKICertificateIssueDetails.  # noqa: E501


        :return: The organization_unit_list of this PKICertificateIssueDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._organization_unit_list

    @organization_unit_list.setter
    def organization_unit_list(self, organization_unit_list):
        """Sets the organization_unit_list of this PKICertificateIssueDetails.


        :param organization_unit_list: The organization_unit_list of this PKICertificateIssueDetails.  # noqa: E501
        :type: list[str]
        """

        self._organization_unit_list = organization_unit_list

    @property
    def postal_code(self):
        """Gets the postal_code of this PKICertificateIssueDetails.  # noqa: E501


        :return: The postal_code of this PKICertificateIssueDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this PKICertificateIssueDetails.


        :param postal_code: The postal_code of this PKICertificateIssueDetails.  # noqa: E501
        :type: list[str]
        """

        self._postal_code = postal_code

    @property
    def province(self):
        """Gets the province of this PKICertificateIssueDetails.  # noqa: E501


        :return: The province of this PKICertificateIssueDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._province

    @province.setter
    def province(self, province):
        """Sets the province of this PKICertificateIssueDetails.


        :param province: The province of this PKICertificateIssueDetails.  # noqa: E501
        :type: list[str]
        """

        self._province = province

    @property
    def require_cn(self):
        """Gets the require_cn of this PKICertificateIssueDetails.  # noqa: E501


        :return: The require_cn of this PKICertificateIssueDetails.  # noqa: E501
        :rtype: bool
        """
        return self._require_cn

    @require_cn.setter
    def require_cn(self, require_cn):
        """Sets the require_cn of this PKICertificateIssueDetails.


        :param require_cn: The require_cn of this PKICertificateIssueDetails.  # noqa: E501
        :type: bool
        """

        self._require_cn = require_cn

    @property
    def server_flag(self):
        """Gets the server_flag of this PKICertificateIssueDetails.  # noqa: E501


        :return: The server_flag of this PKICertificateIssueDetails.  # noqa: E501
        :rtype: bool
        """
        return self._server_flag

    @server_flag.setter
    def server_flag(self, server_flag):
        """Sets the server_flag of this PKICertificateIssueDetails.


        :param server_flag: The server_flag of this PKICertificateIssueDetails.  # noqa: E501
        :type: bool
        """

        self._server_flag = server_flag

    @property
    def street_address(self):
        """Gets the street_address of this PKICertificateIssueDetails.  # noqa: E501


        :return: The street_address of this PKICertificateIssueDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._street_address

    @street_address.setter
    def street_address(self, street_address):
        """Sets the street_address of this PKICertificateIssueDetails.


        :param street_address: The street_address of this PKICertificateIssueDetails.  # noqa: E501
        :type: list[str]
        """

        self._street_address = street_address

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
        if not isinstance(other, PKICertificateIssueDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PKICertificateIssueDetails):
            return True

        return self.to_dict() != other.to_dict()
