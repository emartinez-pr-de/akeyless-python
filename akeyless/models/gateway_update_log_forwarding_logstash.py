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


class GatewayUpdateLogForwardingLogstash(object):
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
        'dns': 'str',
        'enable': 'str',
        'enable_tls': 'bool',
        'json': 'bool',
        'output_format': 'str',
        'protocol': 'str',
        'pull_interval': 'str',
        'tls_certificate': 'str',
        'token': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'dns': 'dns',
        'enable': 'enable',
        'enable_tls': 'enable-tls',
        'json': 'json',
        'output_format': 'output-format',
        'protocol': 'protocol',
        'pull_interval': 'pull-interval',
        'tls_certificate': 'tls-certificate',
        'token': 'token',
        'uid_token': 'uid-token'
    }

    def __init__(self, dns=None, enable='true', enable_tls=None, json=False, output_format='text', protocol=None, pull_interval='10', tls_certificate='use-existing', token=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """GatewayUpdateLogForwardingLogstash - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dns = None
        self._enable = None
        self._enable_tls = None
        self._json = None
        self._output_format = None
        self._protocol = None
        self._pull_interval = None
        self._tls_certificate = None
        self._token = None
        self._uid_token = None
        self.discriminator = None

        if dns is not None:
            self.dns = dns
        if enable is not None:
            self.enable = enable
        if enable_tls is not None:
            self.enable_tls = enable_tls
        if json is not None:
            self.json = json
        if output_format is not None:
            self.output_format = output_format
        if protocol is not None:
            self.protocol = protocol
        if pull_interval is not None:
            self.pull_interval = pull_interval
        if tls_certificate is not None:
            self.tls_certificate = tls_certificate
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def dns(self):
        """Gets the dns of this GatewayUpdateLogForwardingLogstash.  # noqa: E501

        Logstash dns  # noqa: E501

        :return: The dns of this GatewayUpdateLogForwardingLogstash.  # noqa: E501
        :rtype: str
        """
        return self._dns

    @dns.setter
    def dns(self, dns):
        """Sets the dns of this GatewayUpdateLogForwardingLogstash.

        Logstash dns  # noqa: E501

        :param dns: The dns of this GatewayUpdateLogForwardingLogstash.  # noqa: E501
        :type: str
        """

        self._dns = dns

    @property
    def enable(self):
        """Gets the enable of this GatewayUpdateLogForwardingLogstash.  # noqa: E501

        Enable Log Forwarding [true/false]  # noqa: E501

        :return: The enable of this GatewayUpdateLogForwardingLogstash.  # noqa: E501
        :rtype: str
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this GatewayUpdateLogForwardingLogstash.

        Enable Log Forwarding [true/false]  # noqa: E501

        :param enable: The enable of this GatewayUpdateLogForwardingLogstash.  # noqa: E501
        :type: str
        """

        self._enable = enable

    @property
    def enable_tls(self):
        """Gets the enable_tls of this GatewayUpdateLogForwardingLogstash.  # noqa: E501

        Enable tls  # noqa: E501

        :return: The enable_tls of this GatewayUpdateLogForwardingLogstash.  # noqa: E501
        :rtype: bool
        """
        return self._enable_tls

    @enable_tls.setter
    def enable_tls(self, enable_tls):
        """Sets the enable_tls of this GatewayUpdateLogForwardingLogstash.

        Enable tls  # noqa: E501

        :param enable_tls: The enable_tls of this GatewayUpdateLogForwardingLogstash.  # noqa: E501
        :type: bool
        """

        self._enable_tls = enable_tls

    @property
    def json(self):
        """Gets the json of this GatewayUpdateLogForwardingLogstash.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this GatewayUpdateLogForwardingLogstash.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this GatewayUpdateLogForwardingLogstash.

        Set output format to JSON  # noqa: E501

        :param json: The json of this GatewayUpdateLogForwardingLogstash.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def output_format(self):
        """Gets the output_format of this GatewayUpdateLogForwardingLogstash.  # noqa: E501

        Logs format [text/json]  # noqa: E501

        :return: The output_format of this GatewayUpdateLogForwardingLogstash.  # noqa: E501
        :rtype: str
        """
        return self._output_format

    @output_format.setter
    def output_format(self, output_format):
        """Sets the output_format of this GatewayUpdateLogForwardingLogstash.

        Logs format [text/json]  # noqa: E501

        :param output_format: The output_format of this GatewayUpdateLogForwardingLogstash.  # noqa: E501
        :type: str
        """

        self._output_format = output_format

    @property
    def protocol(self):
        """Gets the protocol of this GatewayUpdateLogForwardingLogstash.  # noqa: E501

        Logstash protocol [tcp/udp]  # noqa: E501

        :return: The protocol of this GatewayUpdateLogForwardingLogstash.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this GatewayUpdateLogForwardingLogstash.

        Logstash protocol [tcp/udp]  # noqa: E501

        :param protocol: The protocol of this GatewayUpdateLogForwardingLogstash.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def pull_interval(self):
        """Gets the pull_interval of this GatewayUpdateLogForwardingLogstash.  # noqa: E501

        Pull interval in seconds  # noqa: E501

        :return: The pull_interval of this GatewayUpdateLogForwardingLogstash.  # noqa: E501
        :rtype: str
        """
        return self._pull_interval

    @pull_interval.setter
    def pull_interval(self, pull_interval):
        """Sets the pull_interval of this GatewayUpdateLogForwardingLogstash.

        Pull interval in seconds  # noqa: E501

        :param pull_interval: The pull_interval of this GatewayUpdateLogForwardingLogstash.  # noqa: E501
        :type: str
        """

        self._pull_interval = pull_interval

    @property
    def tls_certificate(self):
        """Gets the tls_certificate of this GatewayUpdateLogForwardingLogstash.  # noqa: E501

        Logstash tls certificate  # noqa: E501

        :return: The tls_certificate of this GatewayUpdateLogForwardingLogstash.  # noqa: E501
        :rtype: str
        """
        return self._tls_certificate

    @tls_certificate.setter
    def tls_certificate(self, tls_certificate):
        """Sets the tls_certificate of this GatewayUpdateLogForwardingLogstash.

        Logstash tls certificate  # noqa: E501

        :param tls_certificate: The tls_certificate of this GatewayUpdateLogForwardingLogstash.  # noqa: E501
        :type: str
        """

        self._tls_certificate = tls_certificate

    @property
    def token(self):
        """Gets the token of this GatewayUpdateLogForwardingLogstash.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GatewayUpdateLogForwardingLogstash.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GatewayUpdateLogForwardingLogstash.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GatewayUpdateLogForwardingLogstash.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this GatewayUpdateLogForwardingLogstash.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GatewayUpdateLogForwardingLogstash.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GatewayUpdateLogForwardingLogstash.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GatewayUpdateLogForwardingLogstash.  # noqa: E501
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
        if not isinstance(other, GatewayUpdateLogForwardingLogstash):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayUpdateLogForwardingLogstash):
            return True

        return self.to_dict() != other.to_dict()
