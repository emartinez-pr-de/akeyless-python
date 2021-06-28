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


class GeneralConfigPart(object):
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
        'akeyless_url': 'str',
        'api_token_ttl': 'str',
        'enable_tls': 'bool',
        'enable_tls_configure': 'bool',
        'enable_tls_curl': 'bool',
        'enable_tls_hvp': 'bool',
        'gw_cluster_url': 'str',
        'tcp_port': 'str',
        'tls_cert': 'str',
        'tls_key': 'str'
    }

    attribute_map = {
        'akeyless_url': 'akeyless_url',
        'api_token_ttl': 'api_token_ttl',
        'enable_tls': 'enable_tls',
        'enable_tls_configure': 'enable_tls_configure',
        'enable_tls_curl': 'enable_tls_curl',
        'enable_tls_hvp': 'enable_tls_hvp',
        'gw_cluster_url': 'gw_cluster_url',
        'tcp_port': 'tcp_port',
        'tls_cert': 'tls_cert',
        'tls_key': 'tls_key'
    }

    def __init__(self, akeyless_url=None, api_token_ttl=None, enable_tls=None, enable_tls_configure=None, enable_tls_curl=None, enable_tls_hvp=None, gw_cluster_url=None, tcp_port=None, tls_cert=None, tls_key=None, local_vars_configuration=None):  # noqa: E501
        """GeneralConfigPart - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._akeyless_url = None
        self._api_token_ttl = None
        self._enable_tls = None
        self._enable_tls_configure = None
        self._enable_tls_curl = None
        self._enable_tls_hvp = None
        self._gw_cluster_url = None
        self._tcp_port = None
        self._tls_cert = None
        self._tls_key = None
        self.discriminator = None

        if akeyless_url is not None:
            self.akeyless_url = akeyless_url
        if api_token_ttl is not None:
            self.api_token_ttl = api_token_ttl
        if enable_tls is not None:
            self.enable_tls = enable_tls
        if enable_tls_configure is not None:
            self.enable_tls_configure = enable_tls_configure
        if enable_tls_curl is not None:
            self.enable_tls_curl = enable_tls_curl
        if enable_tls_hvp is not None:
            self.enable_tls_hvp = enable_tls_hvp
        if gw_cluster_url is not None:
            self.gw_cluster_url = gw_cluster_url
        if tcp_port is not None:
            self.tcp_port = tcp_port
        if tls_cert is not None:
            self.tls_cert = tls_cert
        if tls_key is not None:
            self.tls_key = tls_key

    @property
    def akeyless_url(self):
        """Gets the akeyless_url of this GeneralConfigPart.  # noqa: E501


        :return: The akeyless_url of this GeneralConfigPart.  # noqa: E501
        :rtype: str
        """
        return self._akeyless_url

    @akeyless_url.setter
    def akeyless_url(self, akeyless_url):
        """Sets the akeyless_url of this GeneralConfigPart.


        :param akeyless_url: The akeyless_url of this GeneralConfigPart.  # noqa: E501
        :type: str
        """

        self._akeyless_url = akeyless_url

    @property
    def api_token_ttl(self):
        """Gets the api_token_ttl of this GeneralConfigPart.  # noqa: E501


        :return: The api_token_ttl of this GeneralConfigPart.  # noqa: E501
        :rtype: str
        """
        return self._api_token_ttl

    @api_token_ttl.setter
    def api_token_ttl(self, api_token_ttl):
        """Sets the api_token_ttl of this GeneralConfigPart.


        :param api_token_ttl: The api_token_ttl of this GeneralConfigPart.  # noqa: E501
        :type: str
        """

        self._api_token_ttl = api_token_ttl

    @property
    def enable_tls(self):
        """Gets the enable_tls of this GeneralConfigPart.  # noqa: E501


        :return: The enable_tls of this GeneralConfigPart.  # noqa: E501
        :rtype: bool
        """
        return self._enable_tls

    @enable_tls.setter
    def enable_tls(self, enable_tls):
        """Sets the enable_tls of this GeneralConfigPart.


        :param enable_tls: The enable_tls of this GeneralConfigPart.  # noqa: E501
        :type: bool
        """

        self._enable_tls = enable_tls

    @property
    def enable_tls_configure(self):
        """Gets the enable_tls_configure of this GeneralConfigPart.  # noqa: E501


        :return: The enable_tls_configure of this GeneralConfigPart.  # noqa: E501
        :rtype: bool
        """
        return self._enable_tls_configure

    @enable_tls_configure.setter
    def enable_tls_configure(self, enable_tls_configure):
        """Sets the enable_tls_configure of this GeneralConfigPart.


        :param enable_tls_configure: The enable_tls_configure of this GeneralConfigPart.  # noqa: E501
        :type: bool
        """

        self._enable_tls_configure = enable_tls_configure

    @property
    def enable_tls_curl(self):
        """Gets the enable_tls_curl of this GeneralConfigPart.  # noqa: E501


        :return: The enable_tls_curl of this GeneralConfigPart.  # noqa: E501
        :rtype: bool
        """
        return self._enable_tls_curl

    @enable_tls_curl.setter
    def enable_tls_curl(self, enable_tls_curl):
        """Sets the enable_tls_curl of this GeneralConfigPart.


        :param enable_tls_curl: The enable_tls_curl of this GeneralConfigPart.  # noqa: E501
        :type: bool
        """

        self._enable_tls_curl = enable_tls_curl

    @property
    def enable_tls_hvp(self):
        """Gets the enable_tls_hvp of this GeneralConfigPart.  # noqa: E501


        :return: The enable_tls_hvp of this GeneralConfigPart.  # noqa: E501
        :rtype: bool
        """
        return self._enable_tls_hvp

    @enable_tls_hvp.setter
    def enable_tls_hvp(self, enable_tls_hvp):
        """Sets the enable_tls_hvp of this GeneralConfigPart.


        :param enable_tls_hvp: The enable_tls_hvp of this GeneralConfigPart.  # noqa: E501
        :type: bool
        """

        self._enable_tls_hvp = enable_tls_hvp

    @property
    def gw_cluster_url(self):
        """Gets the gw_cluster_url of this GeneralConfigPart.  # noqa: E501


        :return: The gw_cluster_url of this GeneralConfigPart.  # noqa: E501
        :rtype: str
        """
        return self._gw_cluster_url

    @gw_cluster_url.setter
    def gw_cluster_url(self, gw_cluster_url):
        """Sets the gw_cluster_url of this GeneralConfigPart.


        :param gw_cluster_url: The gw_cluster_url of this GeneralConfigPart.  # noqa: E501
        :type: str
        """

        self._gw_cluster_url = gw_cluster_url

    @property
    def tcp_port(self):
        """Gets the tcp_port of this GeneralConfigPart.  # noqa: E501


        :return: The tcp_port of this GeneralConfigPart.  # noqa: E501
        :rtype: str
        """
        return self._tcp_port

    @tcp_port.setter
    def tcp_port(self, tcp_port):
        """Sets the tcp_port of this GeneralConfigPart.


        :param tcp_port: The tcp_port of this GeneralConfigPart.  # noqa: E501
        :type: str
        """

        self._tcp_port = tcp_port

    @property
    def tls_cert(self):
        """Gets the tls_cert of this GeneralConfigPart.  # noqa: E501


        :return: The tls_cert of this GeneralConfigPart.  # noqa: E501
        :rtype: str
        """
        return self._tls_cert

    @tls_cert.setter
    def tls_cert(self, tls_cert):
        """Sets the tls_cert of this GeneralConfigPart.


        :param tls_cert: The tls_cert of this GeneralConfigPart.  # noqa: E501
        :type: str
        """

        self._tls_cert = tls_cert

    @property
    def tls_key(self):
        """Gets the tls_key of this GeneralConfigPart.  # noqa: E501


        :return: The tls_key of this GeneralConfigPart.  # noqa: E501
        :rtype: str
        """
        return self._tls_key

    @tls_key.setter
    def tls_key(self, tls_key):
        """Sets the tls_key of this GeneralConfigPart.


        :param tls_key: The tls_key of this GeneralConfigPart.  # noqa: E501
        :type: str
        """

        self._tls_key = tls_key

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
        if not isinstance(other, GeneralConfigPart):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GeneralConfigPart):
            return True

        return self.to_dict() != other.to_dict()
