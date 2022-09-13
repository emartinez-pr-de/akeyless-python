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


class GetDynamicSecretValue(object):
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
        'args': 'list[str]',
        'host': 'str',
        'json': 'bool',
        'name': 'str',
        'target': 'str',
        'timeout': 'int',
        'token': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'args': 'args',
        'host': 'host',
        'json': 'json',
        'name': 'name',
        'target': 'target',
        'timeout': 'timeout',
        'token': 'token',
        'uid_token': 'uid-token'
    }

    def __init__(self, args=None, host=None, json=None, name=None, target=None, timeout=15, token=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """GetDynamicSecretValue - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._args = None
        self._host = None
        self._json = None
        self._name = None
        self._target = None
        self._timeout = None
        self._token = None
        self._uid_token = None
        self.discriminator = None

        if args is not None:
            self.args = args
        if host is not None:
            self.host = host
        if json is not None:
            self.json = json
        self.name = name
        if target is not None:
            self.target = target
        if timeout is not None:
            self.timeout = timeout
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def args(self):
        """Gets the args of this GetDynamicSecretValue.  # noqa: E501

        Optional arguments as key=value pairs or JSON strings, e.g - \\\"--args=csr=base64_encoded_csr --args=common_name=bar\\\" or args='{\\\"csr\\\":\\\"base64_encoded_csr\\\"}. It is possible to combine both formats.'  # noqa: E501

        :return: The args of this GetDynamicSecretValue.  # noqa: E501
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this GetDynamicSecretValue.

        Optional arguments as key=value pairs or JSON strings, e.g - \\\"--args=csr=base64_encoded_csr --args=common_name=bar\\\" or args='{\\\"csr\\\":\\\"base64_encoded_csr\\\"}. It is possible to combine both formats.'  # noqa: E501

        :param args: The args of this GetDynamicSecretValue.  # noqa: E501
        :type: list[str]
        """

        self._args = args

    @property
    def host(self):
        """Gets the host of this GetDynamicSecretValue.  # noqa: E501

        Host  # noqa: E501

        :return: The host of this GetDynamicSecretValue.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this GetDynamicSecretValue.

        Host  # noqa: E501

        :param host: The host of this GetDynamicSecretValue.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def json(self):
        """Gets the json of this GetDynamicSecretValue.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this GetDynamicSecretValue.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this GetDynamicSecretValue.

        Set output format to JSON  # noqa: E501

        :param json: The json of this GetDynamicSecretValue.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def name(self):
        """Gets the name of this GetDynamicSecretValue.  # noqa: E501

        Dynamic secret name  # noqa: E501

        :return: The name of this GetDynamicSecretValue.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetDynamicSecretValue.

        Dynamic secret name  # noqa: E501

        :param name: The name of this GetDynamicSecretValue.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def target(self):
        """Gets the target of this GetDynamicSecretValue.  # noqa: E501

        Target Name  # noqa: E501

        :return: The target of this GetDynamicSecretValue.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this GetDynamicSecretValue.

        Target Name  # noqa: E501

        :param target: The target of this GetDynamicSecretValue.  # noqa: E501
        :type: str
        """

        self._target = target

    @property
    def timeout(self):
        """Gets the timeout of this GetDynamicSecretValue.  # noqa: E501

        Timeout in seconds  # noqa: E501

        :return: The timeout of this GetDynamicSecretValue.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this GetDynamicSecretValue.

        Timeout in seconds  # noqa: E501

        :param timeout: The timeout of this GetDynamicSecretValue.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

    @property
    def token(self):
        """Gets the token of this GetDynamicSecretValue.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GetDynamicSecretValue.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GetDynamicSecretValue.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GetDynamicSecretValue.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this GetDynamicSecretValue.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GetDynamicSecretValue.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GetDynamicSecretValue.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GetDynamicSecretValue.  # noqa: E501
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
        if not isinstance(other, GetDynamicSecretValue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetDynamicSecretValue):
            return True

        return self.to_dict() != other.to_dict()
