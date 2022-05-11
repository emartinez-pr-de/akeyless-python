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


class AwsS3LogForwardingConfig(object):
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
        'aws_access_id': 'str',
        'aws_access_key': 'str',
        'aws_region': 'str',
        'aws_use_gateway_cloud_identity': 'bool',
        'bucket_name': 'str',
        'log_folder': 'str'
    }

    attribute_map = {
        'aws_access_id': 'aws_access_id',
        'aws_access_key': 'aws_access_key',
        'aws_region': 'aws_region',
        'aws_use_gateway_cloud_identity': 'aws_use_gateway_cloud_identity',
        'bucket_name': 'bucket_name',
        'log_folder': 'log_folder'
    }

    def __init__(self, aws_access_id=None, aws_access_key=None, aws_region=None, aws_use_gateway_cloud_identity=None, bucket_name=None, log_folder=None, local_vars_configuration=None):  # noqa: E501
        """AwsS3LogForwardingConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._aws_access_id = None
        self._aws_access_key = None
        self._aws_region = None
        self._aws_use_gateway_cloud_identity = None
        self._bucket_name = None
        self._log_folder = None
        self.discriminator = None

        if aws_access_id is not None:
            self.aws_access_id = aws_access_id
        if aws_access_key is not None:
            self.aws_access_key = aws_access_key
        if aws_region is not None:
            self.aws_region = aws_region
        if aws_use_gateway_cloud_identity is not None:
            self.aws_use_gateway_cloud_identity = aws_use_gateway_cloud_identity
        if bucket_name is not None:
            self.bucket_name = bucket_name
        if log_folder is not None:
            self.log_folder = log_folder

    @property
    def aws_access_id(self):
        """Gets the aws_access_id of this AwsS3LogForwardingConfig.  # noqa: E501


        :return: The aws_access_id of this AwsS3LogForwardingConfig.  # noqa: E501
        :rtype: str
        """
        return self._aws_access_id

    @aws_access_id.setter
    def aws_access_id(self, aws_access_id):
        """Sets the aws_access_id of this AwsS3LogForwardingConfig.


        :param aws_access_id: The aws_access_id of this AwsS3LogForwardingConfig.  # noqa: E501
        :type: str
        """

        self._aws_access_id = aws_access_id

    @property
    def aws_access_key(self):
        """Gets the aws_access_key of this AwsS3LogForwardingConfig.  # noqa: E501


        :return: The aws_access_key of this AwsS3LogForwardingConfig.  # noqa: E501
        :rtype: str
        """
        return self._aws_access_key

    @aws_access_key.setter
    def aws_access_key(self, aws_access_key):
        """Sets the aws_access_key of this AwsS3LogForwardingConfig.


        :param aws_access_key: The aws_access_key of this AwsS3LogForwardingConfig.  # noqa: E501
        :type: str
        """

        self._aws_access_key = aws_access_key

    @property
    def aws_region(self):
        """Gets the aws_region of this AwsS3LogForwardingConfig.  # noqa: E501


        :return: The aws_region of this AwsS3LogForwardingConfig.  # noqa: E501
        :rtype: str
        """
        return self._aws_region

    @aws_region.setter
    def aws_region(self, aws_region):
        """Sets the aws_region of this AwsS3LogForwardingConfig.


        :param aws_region: The aws_region of this AwsS3LogForwardingConfig.  # noqa: E501
        :type: str
        """

        self._aws_region = aws_region

    @property
    def aws_use_gateway_cloud_identity(self):
        """Gets the aws_use_gateway_cloud_identity of this AwsS3LogForwardingConfig.  # noqa: E501


        :return: The aws_use_gateway_cloud_identity of this AwsS3LogForwardingConfig.  # noqa: E501
        :rtype: bool
        """
        return self._aws_use_gateway_cloud_identity

    @aws_use_gateway_cloud_identity.setter
    def aws_use_gateway_cloud_identity(self, aws_use_gateway_cloud_identity):
        """Sets the aws_use_gateway_cloud_identity of this AwsS3LogForwardingConfig.


        :param aws_use_gateway_cloud_identity: The aws_use_gateway_cloud_identity of this AwsS3LogForwardingConfig.  # noqa: E501
        :type: bool
        """

        self._aws_use_gateway_cloud_identity = aws_use_gateway_cloud_identity

    @property
    def bucket_name(self):
        """Gets the bucket_name of this AwsS3LogForwardingConfig.  # noqa: E501


        :return: The bucket_name of this AwsS3LogForwardingConfig.  # noqa: E501
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this AwsS3LogForwardingConfig.


        :param bucket_name: The bucket_name of this AwsS3LogForwardingConfig.  # noqa: E501
        :type: str
        """

        self._bucket_name = bucket_name

    @property
    def log_folder(self):
        """Gets the log_folder of this AwsS3LogForwardingConfig.  # noqa: E501


        :return: The log_folder of this AwsS3LogForwardingConfig.  # noqa: E501
        :rtype: str
        """
        return self._log_folder

    @log_folder.setter
    def log_folder(self, log_folder):
        """Sets the log_folder of this AwsS3LogForwardingConfig.


        :param log_folder: The log_folder of this AwsS3LogForwardingConfig.  # noqa: E501
        :type: str
        """

        self._log_folder = log_folder

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
        if not isinstance(other, AwsS3LogForwardingConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AwsS3LogForwardingConfig):
            return True

        return self.to_dict() != other.to_dict()
