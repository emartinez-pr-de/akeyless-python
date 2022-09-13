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


class DescribePermissions(object):
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
        'json': 'bool',
        'path': 'str',
        'token': 'str',
        'type': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'json': 'json',
        'path': 'path',
        'token': 'token',
        'type': 'type',
        'uid_token': 'uid-token'
    }

    def __init__(self, json=None, path=None, token=None, type=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """DescribePermissions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._json = None
        self._path = None
        self._token = None
        self._type = None
        self._uid_token = None
        self.discriminator = None

        if json is not None:
            self.json = json
        self.path = path
        if token is not None:
            self.token = token
        self.type = type
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def json(self):
        """Gets the json of this DescribePermissions.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this DescribePermissions.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this DescribePermissions.

        Set output format to JSON  # noqa: E501

        :param json: The json of this DescribePermissions.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def path(self):
        """Gets the path of this DescribePermissions.  # noqa: E501

        Path to an object  # noqa: E501

        :return: The path of this DescribePermissions.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this DescribePermissions.

        Path to an object  # noqa: E501

        :param path: The path of this DescribePermissions.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and path is None:  # noqa: E501
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def token(self):
        """Gets the token of this DescribePermissions.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this DescribePermissions.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this DescribePermissions.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this DescribePermissions.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def type(self):
        """Gets the type of this DescribePermissions.  # noqa: E501

        Type of object (item, am, role, target)  # noqa: E501

        :return: The type of this DescribePermissions.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DescribePermissions.

        Type of object (item, am, role, target)  # noqa: E501

        :param type: The type of this DescribePermissions.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def uid_token(self):
        """Gets the uid_token of this DescribePermissions.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this DescribePermissions.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this DescribePermissions.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this DescribePermissions.  # noqa: E501
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
        if not isinstance(other, DescribePermissions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribePermissions):
            return True

        return self.to_dict() != other.to_dict()
