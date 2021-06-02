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


class UpdateRole(object):
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
        'analytics_access': 'str',
        'audit_access': 'str',
        'name': 'str',
        'new_comment': 'str',
        'new_name': 'str',
        'password': 'str',
        'token': 'str',
        'uid_token': 'str',
        'username': 'str'
    }

    attribute_map = {
        'analytics_access': 'analytics-access',
        'audit_access': 'audit-access',
        'name': 'name',
        'new_comment': 'new-comment',
        'new_name': 'new-name',
        'password': 'password',
        'token': 'token',
        'uid_token': 'uid-token',
        'username': 'username'
    }

    def __init__(self, analytics_access=None, audit_access=None, name=None, new_comment='default_comment', new_name=None, password=None, token=None, uid_token=None, username=None, local_vars_configuration=None):  # noqa: E501
        """UpdateRole - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._analytics_access = None
        self._audit_access = None
        self._name = None
        self._new_comment = None
        self._new_name = None
        self._password = None
        self._token = None
        self._uid_token = None
        self._username = None
        self.discriminator = None

        if analytics_access is not None:
            self.analytics_access = analytics_access
        if audit_access is not None:
            self.audit_access = audit_access
        self.name = name
        if new_comment is not None:
            self.new_comment = new_comment
        if new_name is not None:
            self.new_name = new_name
        if password is not None:
            self.password = password
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if username is not None:
            self.username = username

    @property
    def analytics_access(self):
        """Gets the analytics_access of this UpdateRole.  # noqa: E501

        Allow this role to view analytics. Currently only 'none' and 'self' values are supported, allowing associated auth methods to view reports produced by the same auth methods.  # noqa: E501

        :return: The analytics_access of this UpdateRole.  # noqa: E501
        :rtype: str
        """
        return self._analytics_access

    @analytics_access.setter
    def analytics_access(self, analytics_access):
        """Sets the analytics_access of this UpdateRole.

        Allow this role to view analytics. Currently only 'none' and 'self' values are supported, allowing associated auth methods to view reports produced by the same auth methods.  # noqa: E501

        :param analytics_access: The analytics_access of this UpdateRole.  # noqa: E501
        :type: str
        """

        self._analytics_access = analytics_access

    @property
    def audit_access(self):
        """Gets the audit_access of this UpdateRole.  # noqa: E501

        Allow this role to view audit logs. Currently only 'none' and 'self' values are supported, allowing associated auth methods to view audit logs produced by the same auth methods.  # noqa: E501

        :return: The audit_access of this UpdateRole.  # noqa: E501
        :rtype: str
        """
        return self._audit_access

    @audit_access.setter
    def audit_access(self, audit_access):
        """Sets the audit_access of this UpdateRole.

        Allow this role to view audit logs. Currently only 'none' and 'self' values are supported, allowing associated auth methods to view audit logs produced by the same auth methods.  # noqa: E501

        :param audit_access: The audit_access of this UpdateRole.  # noqa: E501
        :type: str
        """

        self._audit_access = audit_access

    @property
    def name(self):
        """Gets the name of this UpdateRole.  # noqa: E501

        Role name  # noqa: E501

        :return: The name of this UpdateRole.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateRole.

        Role name  # noqa: E501

        :param name: The name of this UpdateRole.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def new_comment(self):
        """Gets the new_comment of this UpdateRole.  # noqa: E501

        New comment about the role  # noqa: E501

        :return: The new_comment of this UpdateRole.  # noqa: E501
        :rtype: str
        """
        return self._new_comment

    @new_comment.setter
    def new_comment(self, new_comment):
        """Sets the new_comment of this UpdateRole.

        New comment about the role  # noqa: E501

        :param new_comment: The new_comment of this UpdateRole.  # noqa: E501
        :type: str
        """

        self._new_comment = new_comment

    @property
    def new_name(self):
        """Gets the new_name of this UpdateRole.  # noqa: E501

        New Role name  # noqa: E501

        :return: The new_name of this UpdateRole.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this UpdateRole.

        New Role name  # noqa: E501

        :param new_name: The new_name of this UpdateRole.  # noqa: E501
        :type: str
        """

        self._new_name = new_name

    @property
    def password(self):
        """Gets the password of this UpdateRole.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The password of this UpdateRole.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UpdateRole.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param password: The password of this UpdateRole.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def token(self):
        """Gets the token of this UpdateRole.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this UpdateRole.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this UpdateRole.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this UpdateRole.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this UpdateRole.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this UpdateRole.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this UpdateRole.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this UpdateRole.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def username(self):
        """Gets the username of this UpdateRole.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The username of this UpdateRole.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UpdateRole.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param username: The username of this UpdateRole.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if not isinstance(other, UpdateRole):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateRole):
            return True

        return self.to_dict() != other.to_dict()
