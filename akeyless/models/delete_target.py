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


class DeleteTarget(object):
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
        'enforce_deletion': 'bool',
        'name': 'str',
        'target_version': 'int',
        'token': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'enforce_deletion': 'enforce-deletion',
        'name': 'name',
        'target_version': 'target-version',
        'token': 'token',
        'uid_token': 'uid-token'
    }

    def __init__(self, enforce_deletion=False, name=None, target_version=None, token=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """DeleteTarget - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._enforce_deletion = None
        self._name = None
        self._target_version = None
        self._token = None
        self._uid_token = None
        self.discriminator = None

        if enforce_deletion is not None:
            self.enforce_deletion = enforce_deletion
        self.name = name
        if target_version is not None:
            self.target_version = target_version
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def enforce_deletion(self):
        """Gets the enforce_deletion of this DeleteTarget.  # noqa: E501

        Enforce deletion  # noqa: E501

        :return: The enforce_deletion of this DeleteTarget.  # noqa: E501
        :rtype: bool
        """
        return self._enforce_deletion

    @enforce_deletion.setter
    def enforce_deletion(self, enforce_deletion):
        """Sets the enforce_deletion of this DeleteTarget.

        Enforce deletion  # noqa: E501

        :param enforce_deletion: The enforce_deletion of this DeleteTarget.  # noqa: E501
        :type: bool
        """

        self._enforce_deletion = enforce_deletion

    @property
    def name(self):
        """Gets the name of this DeleteTarget.  # noqa: E501

        Target name  # noqa: E501

        :return: The name of this DeleteTarget.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeleteTarget.

        Target name  # noqa: E501

        :param name: The name of this DeleteTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def target_version(self):
        """Gets the target_version of this DeleteTarget.  # noqa: E501

        Target version  # noqa: E501

        :return: The target_version of this DeleteTarget.  # noqa: E501
        :rtype: int
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        """Sets the target_version of this DeleteTarget.

        Target version  # noqa: E501

        :param target_version: The target_version of this DeleteTarget.  # noqa: E501
        :type: int
        """

        self._target_version = target_version

    @property
    def token(self):
        """Gets the token of this DeleteTarget.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this DeleteTarget.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this DeleteTarget.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this DeleteTarget.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this DeleteTarget.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this DeleteTarget.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this DeleteTarget.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this DeleteTarget.  # noqa: E501
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
        if not isinstance(other, DeleteTarget):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeleteTarget):
            return True

        return self.to_dict() != other.to_dict()
