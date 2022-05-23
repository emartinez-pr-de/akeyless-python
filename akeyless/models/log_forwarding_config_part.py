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


class LogForwardingConfigPart(object):
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
        'aws_s3_config': 'AwsS3LogForwardingConfig',
        'azure_analytics_config': 'AzureLogAnalyticsForwardingConfig',
        'datadog_config': 'DatadogForwardingConfig',
        'elasticsearch_config': 'ElasticsearchLogForwardingConfig',
        'logan_enable': 'bool',
        'logan_url': 'str',
        'logstash_config': 'LogstashLogForwardingConfig',
        'logz_io_config': 'LogzIoLogForwardingConfig',
        'pull_interval_sec': 'str',
        'splunk_config': 'SplunkLogForwardingConfig',
        'syslog_config': 'SyslogLogForwardingConfig',
        'target_log_type': 'str'
    }

    attribute_map = {
        'aws_s3_config': 'aws_s3_config',
        'azure_analytics_config': 'azure_analytics_config',
        'datadog_config': 'datadog_config',
        'elasticsearch_config': 'elasticsearch_config',
        'logan_enable': 'logan_enable',
        'logan_url': 'logan_url',
        'logstash_config': 'logstash_config',
        'logz_io_config': 'logz_io_config',
        'pull_interval_sec': 'pull_interval_sec',
        'splunk_config': 'splunk_config',
        'syslog_config': 'syslog_config',
        'target_log_type': 'target_log_type'
    }

    def __init__(self, aws_s3_config=None, azure_analytics_config=None, datadog_config=None, elasticsearch_config=None, logan_enable=None, logan_url=None, logstash_config=None, logz_io_config=None, pull_interval_sec=None, splunk_config=None, syslog_config=None, target_log_type=None, local_vars_configuration=None):  # noqa: E501
        """LogForwardingConfigPart - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._aws_s3_config = None
        self._azure_analytics_config = None
        self._datadog_config = None
        self._elasticsearch_config = None
        self._logan_enable = None
        self._logan_url = None
        self._logstash_config = None
        self._logz_io_config = None
        self._pull_interval_sec = None
        self._splunk_config = None
        self._syslog_config = None
        self._target_log_type = None
        self.discriminator = None

        if aws_s3_config is not None:
            self.aws_s3_config = aws_s3_config
        if azure_analytics_config is not None:
            self.azure_analytics_config = azure_analytics_config
        if datadog_config is not None:
            self.datadog_config = datadog_config
        if elasticsearch_config is not None:
            self.elasticsearch_config = elasticsearch_config
        if logan_enable is not None:
            self.logan_enable = logan_enable
        if logan_url is not None:
            self.logan_url = logan_url
        if logstash_config is not None:
            self.logstash_config = logstash_config
        if logz_io_config is not None:
            self.logz_io_config = logz_io_config
        if pull_interval_sec is not None:
            self.pull_interval_sec = pull_interval_sec
        if splunk_config is not None:
            self.splunk_config = splunk_config
        if syslog_config is not None:
            self.syslog_config = syslog_config
        if target_log_type is not None:
            self.target_log_type = target_log_type

    @property
    def aws_s3_config(self):
        """Gets the aws_s3_config of this LogForwardingConfigPart.  # noqa: E501


        :return: The aws_s3_config of this LogForwardingConfigPart.  # noqa: E501
        :rtype: AwsS3LogForwardingConfig
        """
        return self._aws_s3_config

    @aws_s3_config.setter
    def aws_s3_config(self, aws_s3_config):
        """Sets the aws_s3_config of this LogForwardingConfigPart.


        :param aws_s3_config: The aws_s3_config of this LogForwardingConfigPart.  # noqa: E501
        :type: AwsS3LogForwardingConfig
        """

        self._aws_s3_config = aws_s3_config

    @property
    def azure_analytics_config(self):
        """Gets the azure_analytics_config of this LogForwardingConfigPart.  # noqa: E501


        :return: The azure_analytics_config of this LogForwardingConfigPart.  # noqa: E501
        :rtype: AzureLogAnalyticsForwardingConfig
        """
        return self._azure_analytics_config

    @azure_analytics_config.setter
    def azure_analytics_config(self, azure_analytics_config):
        """Sets the azure_analytics_config of this LogForwardingConfigPart.


        :param azure_analytics_config: The azure_analytics_config of this LogForwardingConfigPart.  # noqa: E501
        :type: AzureLogAnalyticsForwardingConfig
        """

        self._azure_analytics_config = azure_analytics_config

    @property
    def datadog_config(self):
        """Gets the datadog_config of this LogForwardingConfigPart.  # noqa: E501


        :return: The datadog_config of this LogForwardingConfigPart.  # noqa: E501
        :rtype: DatadogForwardingConfig
        """
        return self._datadog_config

    @datadog_config.setter
    def datadog_config(self, datadog_config):
        """Sets the datadog_config of this LogForwardingConfigPart.


        :param datadog_config: The datadog_config of this LogForwardingConfigPart.  # noqa: E501
        :type: DatadogForwardingConfig
        """

        self._datadog_config = datadog_config

    @property
    def elasticsearch_config(self):
        """Gets the elasticsearch_config of this LogForwardingConfigPart.  # noqa: E501


        :return: The elasticsearch_config of this LogForwardingConfigPart.  # noqa: E501
        :rtype: ElasticsearchLogForwardingConfig
        """
        return self._elasticsearch_config

    @elasticsearch_config.setter
    def elasticsearch_config(self, elasticsearch_config):
        """Sets the elasticsearch_config of this LogForwardingConfigPart.


        :param elasticsearch_config: The elasticsearch_config of this LogForwardingConfigPart.  # noqa: E501
        :type: ElasticsearchLogForwardingConfig
        """

        self._elasticsearch_config = elasticsearch_config

    @property
    def logan_enable(self):
        """Gets the logan_enable of this LogForwardingConfigPart.  # noqa: E501


        :return: The logan_enable of this LogForwardingConfigPart.  # noqa: E501
        :rtype: bool
        """
        return self._logan_enable

    @logan_enable.setter
    def logan_enable(self, logan_enable):
        """Sets the logan_enable of this LogForwardingConfigPart.


        :param logan_enable: The logan_enable of this LogForwardingConfigPart.  # noqa: E501
        :type: bool
        """

        self._logan_enable = logan_enable

    @property
    def logan_url(self):
        """Gets the logan_url of this LogForwardingConfigPart.  # noqa: E501


        :return: The logan_url of this LogForwardingConfigPart.  # noqa: E501
        :rtype: str
        """
        return self._logan_url

    @logan_url.setter
    def logan_url(self, logan_url):
        """Sets the logan_url of this LogForwardingConfigPart.


        :param logan_url: The logan_url of this LogForwardingConfigPart.  # noqa: E501
        :type: str
        """

        self._logan_url = logan_url

    @property
    def logstash_config(self):
        """Gets the logstash_config of this LogForwardingConfigPart.  # noqa: E501


        :return: The logstash_config of this LogForwardingConfigPart.  # noqa: E501
        :rtype: LogstashLogForwardingConfig
        """
        return self._logstash_config

    @logstash_config.setter
    def logstash_config(self, logstash_config):
        """Sets the logstash_config of this LogForwardingConfigPart.


        :param logstash_config: The logstash_config of this LogForwardingConfigPart.  # noqa: E501
        :type: LogstashLogForwardingConfig
        """

        self._logstash_config = logstash_config

    @property
    def logz_io_config(self):
        """Gets the logz_io_config of this LogForwardingConfigPart.  # noqa: E501


        :return: The logz_io_config of this LogForwardingConfigPart.  # noqa: E501
        :rtype: LogzIoLogForwardingConfig
        """
        return self._logz_io_config

    @logz_io_config.setter
    def logz_io_config(self, logz_io_config):
        """Sets the logz_io_config of this LogForwardingConfigPart.


        :param logz_io_config: The logz_io_config of this LogForwardingConfigPart.  # noqa: E501
        :type: LogzIoLogForwardingConfig
        """

        self._logz_io_config = logz_io_config

    @property
    def pull_interval_sec(self):
        """Gets the pull_interval_sec of this LogForwardingConfigPart.  # noqa: E501


        :return: The pull_interval_sec of this LogForwardingConfigPart.  # noqa: E501
        :rtype: str
        """
        return self._pull_interval_sec

    @pull_interval_sec.setter
    def pull_interval_sec(self, pull_interval_sec):
        """Sets the pull_interval_sec of this LogForwardingConfigPart.


        :param pull_interval_sec: The pull_interval_sec of this LogForwardingConfigPart.  # noqa: E501
        :type: str
        """

        self._pull_interval_sec = pull_interval_sec

    @property
    def splunk_config(self):
        """Gets the splunk_config of this LogForwardingConfigPart.  # noqa: E501


        :return: The splunk_config of this LogForwardingConfigPart.  # noqa: E501
        :rtype: SplunkLogForwardingConfig
        """
        return self._splunk_config

    @splunk_config.setter
    def splunk_config(self, splunk_config):
        """Sets the splunk_config of this LogForwardingConfigPart.


        :param splunk_config: The splunk_config of this LogForwardingConfigPart.  # noqa: E501
        :type: SplunkLogForwardingConfig
        """

        self._splunk_config = splunk_config

    @property
    def syslog_config(self):
        """Gets the syslog_config of this LogForwardingConfigPart.  # noqa: E501


        :return: The syslog_config of this LogForwardingConfigPart.  # noqa: E501
        :rtype: SyslogLogForwardingConfig
        """
        return self._syslog_config

    @syslog_config.setter
    def syslog_config(self, syslog_config):
        """Sets the syslog_config of this LogForwardingConfigPart.


        :param syslog_config: The syslog_config of this LogForwardingConfigPart.  # noqa: E501
        :type: SyslogLogForwardingConfig
        """

        self._syslog_config = syslog_config

    @property
    def target_log_type(self):
        """Gets the target_log_type of this LogForwardingConfigPart.  # noqa: E501


        :return: The target_log_type of this LogForwardingConfigPart.  # noqa: E501
        :rtype: str
        """
        return self._target_log_type

    @target_log_type.setter
    def target_log_type(self, target_log_type):
        """Sets the target_log_type of this LogForwardingConfigPart.


        :param target_log_type: The target_log_type of this LogForwardingConfigPart.  # noqa: E501
        :type: str
        """

        self._target_log_type = target_log_type

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
        if not isinstance(other, LogForwardingConfigPart):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LogForwardingConfigPart):
            return True

        return self.to_dict() != other.to_dict()
