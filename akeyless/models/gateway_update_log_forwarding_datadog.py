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


class GatewayUpdateLogForwardingDatadog(object):
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
        'api_key': 'str',
        'enable': 'str',
        'host': 'str',
        'json': 'bool',
        'log_service': 'str',
        'log_source': 'str',
        'log_tags': 'str',
        'output_format': 'str',
        'pull_interval': 'str',
        'token': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'api_key': 'api-key',
        'enable': 'enable',
        'host': 'host',
        'json': 'json',
        'log_service': 'log-service',
        'log_source': 'log-source',
        'log_tags': 'log-tags',
        'output_format': 'output-format',
        'pull_interval': 'pull-interval',
        'token': 'token',
        'uid_token': 'uid-token'
    }

    def __init__(self, api_key=None, enable='true', host=None, json=False, log_service='use-existing', log_source='use-existing', log_tags='use-existing', output_format='text', pull_interval='10', token=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """GatewayUpdateLogForwardingDatadog - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._api_key = None
        self._enable = None
        self._host = None
        self._json = None
        self._log_service = None
        self._log_source = None
        self._log_tags = None
        self._output_format = None
        self._pull_interval = None
        self._token = None
        self._uid_token = None
        self.discriminator = None

        if api_key is not None:
            self.api_key = api_key
        if enable is not None:
            self.enable = enable
        if host is not None:
            self.host = host
        if json is not None:
            self.json = json
        if log_service is not None:
            self.log_service = log_service
        if log_source is not None:
            self.log_source = log_source
        if log_tags is not None:
            self.log_tags = log_tags
        if output_format is not None:
            self.output_format = output_format
        if pull_interval is not None:
            self.pull_interval = pull_interval
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def api_key(self):
        """Gets the api_key of this GatewayUpdateLogForwardingDatadog.  # noqa: E501

        Datadog api key  # noqa: E501

        :return: The api_key of this GatewayUpdateLogForwardingDatadog.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this GatewayUpdateLogForwardingDatadog.

        Datadog api key  # noqa: E501

        :param api_key: The api_key of this GatewayUpdateLogForwardingDatadog.  # noqa: E501
        :type: str
        """

        self._api_key = api_key

    @property
    def enable(self):
        """Gets the enable of this GatewayUpdateLogForwardingDatadog.  # noqa: E501

        Enable Log Forwarding [true/false]  # noqa: E501

        :return: The enable of this GatewayUpdateLogForwardingDatadog.  # noqa: E501
        :rtype: str
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this GatewayUpdateLogForwardingDatadog.

        Enable Log Forwarding [true/false]  # noqa: E501

        :param enable: The enable of this GatewayUpdateLogForwardingDatadog.  # noqa: E501
        :type: str
        """

        self._enable = enable

    @property
    def host(self):
        """Gets the host of this GatewayUpdateLogForwardingDatadog.  # noqa: E501

        Datadog host  # noqa: E501

        :return: The host of this GatewayUpdateLogForwardingDatadog.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this GatewayUpdateLogForwardingDatadog.

        Datadog host  # noqa: E501

        :param host: The host of this GatewayUpdateLogForwardingDatadog.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def json(self):
        """Gets the json of this GatewayUpdateLogForwardingDatadog.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this GatewayUpdateLogForwardingDatadog.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this GatewayUpdateLogForwardingDatadog.

        Set output format to JSON  # noqa: E501

        :param json: The json of this GatewayUpdateLogForwardingDatadog.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def log_service(self):
        """Gets the log_service of this GatewayUpdateLogForwardingDatadog.  # noqa: E501

        Datadog log service  # noqa: E501

        :return: The log_service of this GatewayUpdateLogForwardingDatadog.  # noqa: E501
        :rtype: str
        """
        return self._log_service

    @log_service.setter
    def log_service(self, log_service):
        """Sets the log_service of this GatewayUpdateLogForwardingDatadog.

        Datadog log service  # noqa: E501

        :param log_service: The log_service of this GatewayUpdateLogForwardingDatadog.  # noqa: E501
        :type: str
        """

        self._log_service = log_service

    @property
    def log_source(self):
        """Gets the log_source of this GatewayUpdateLogForwardingDatadog.  # noqa: E501

        Datadog log source  # noqa: E501

        :return: The log_source of this GatewayUpdateLogForwardingDatadog.  # noqa: E501
        :rtype: str
        """
        return self._log_source

    @log_source.setter
    def log_source(self, log_source):
        """Sets the log_source of this GatewayUpdateLogForwardingDatadog.

        Datadog log source  # noqa: E501

        :param log_source: The log_source of this GatewayUpdateLogForwardingDatadog.  # noqa: E501
        :type: str
        """

        self._log_source = log_source

    @property
    def log_tags(self):
        """Gets the log_tags of this GatewayUpdateLogForwardingDatadog.  # noqa: E501

        A comma-separated list of Datadog log tags formatted as \"key:value\" strings  # noqa: E501

        :return: The log_tags of this GatewayUpdateLogForwardingDatadog.  # noqa: E501
        :rtype: str
        """
        return self._log_tags

    @log_tags.setter
    def log_tags(self, log_tags):
        """Sets the log_tags of this GatewayUpdateLogForwardingDatadog.

        A comma-separated list of Datadog log tags formatted as \"key:value\" strings  # noqa: E501

        :param log_tags: The log_tags of this GatewayUpdateLogForwardingDatadog.  # noqa: E501
        :type: str
        """

        self._log_tags = log_tags

    @property
    def output_format(self):
        """Gets the output_format of this GatewayUpdateLogForwardingDatadog.  # noqa: E501

        Logs format [text/json]  # noqa: E501

        :return: The output_format of this GatewayUpdateLogForwardingDatadog.  # noqa: E501
        :rtype: str
        """
        return self._output_format

    @output_format.setter
    def output_format(self, output_format):
        """Sets the output_format of this GatewayUpdateLogForwardingDatadog.

        Logs format [text/json]  # noqa: E501

        :param output_format: The output_format of this GatewayUpdateLogForwardingDatadog.  # noqa: E501
        :type: str
        """

        self._output_format = output_format

    @property
    def pull_interval(self):
        """Gets the pull_interval of this GatewayUpdateLogForwardingDatadog.  # noqa: E501

        Pull interval in seconds  # noqa: E501

        :return: The pull_interval of this GatewayUpdateLogForwardingDatadog.  # noqa: E501
        :rtype: str
        """
        return self._pull_interval

    @pull_interval.setter
    def pull_interval(self, pull_interval):
        """Sets the pull_interval of this GatewayUpdateLogForwardingDatadog.

        Pull interval in seconds  # noqa: E501

        :param pull_interval: The pull_interval of this GatewayUpdateLogForwardingDatadog.  # noqa: E501
        :type: str
        """

        self._pull_interval = pull_interval

    @property
    def token(self):
        """Gets the token of this GatewayUpdateLogForwardingDatadog.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GatewayUpdateLogForwardingDatadog.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GatewayUpdateLogForwardingDatadog.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GatewayUpdateLogForwardingDatadog.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this GatewayUpdateLogForwardingDatadog.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GatewayUpdateLogForwardingDatadog.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GatewayUpdateLogForwardingDatadog.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GatewayUpdateLogForwardingDatadog.  # noqa: E501
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
        if not isinstance(other, GatewayUpdateLogForwardingDatadog):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayUpdateLogForwardingDatadog):
            return True

        return self.to_dict() != other.to_dict()
