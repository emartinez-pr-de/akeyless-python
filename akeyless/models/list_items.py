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


class ListItems(object):
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
        'filter': 'str',
        'pagination_token': 'str',
        'password': 'str',
        'path': 'str',
        'tag': 'str',
        'token': 'str',
        'type': 'list[str]',
        'uid_token': 'str',
        'username': 'str'
    }

    attribute_map = {
        'filter': 'filter',
        'pagination_token': 'pagination-token',
        'password': 'password',
        'path': 'path',
        'tag': 'tag',
        'token': 'token',
        'type': 'type',
        'uid_token': 'uid-token',
        'username': 'username'
    }

    def __init__(self, filter=None, pagination_token=None, password=None, path=None, tag=None, token=None, type=None, uid_token=None, username=None, local_vars_configuration=None):  # noqa: E501
        """ListItems - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._filter = None
        self._pagination_token = None
        self._password = None
        self._path = None
        self._tag = None
        self._token = None
        self._type = None
        self._uid_token = None
        self._username = None
        self.discriminator = None

        if filter is not None:
            self.filter = filter
        if pagination_token is not None:
            self.pagination_token = pagination_token
        if password is not None:
            self.password = password
        if path is not None:
            self.path = path
        if tag is not None:
            self.tag = tag
        if token is not None:
            self.token = token
        if type is not None:
            self.type = type
        if uid_token is not None:
            self.uid_token = uid_token
        if username is not None:
            self.username = username

    @property
    def filter(self):
        """Gets the filter of this ListItems.  # noqa: E501

        Filter by item name or part of it  # noqa: E501

        :return: The filter of this ListItems.  # noqa: E501
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ListItems.

        Filter by item name or part of it  # noqa: E501

        :param filter: The filter of this ListItems.  # noqa: E501
        :type: str
        """

        self._filter = filter

    @property
    def pagination_token(self):
        """Gets the pagination_token of this ListItems.  # noqa: E501

        Next page reference  # noqa: E501

        :return: The pagination_token of this ListItems.  # noqa: E501
        :rtype: str
        """
        return self._pagination_token

    @pagination_token.setter
    def pagination_token(self, pagination_token):
        """Sets the pagination_token of this ListItems.

        Next page reference  # noqa: E501

        :param pagination_token: The pagination_token of this ListItems.  # noqa: E501
        :type: str
        """

        self._pagination_token = pagination_token

    @property
    def password(self):
        """Gets the password of this ListItems.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The password of this ListItems.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ListItems.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param password: The password of this ListItems.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def path(self):
        """Gets the path of this ListItems.  # noqa: E501

        Path to folder  # noqa: E501

        :return: The path of this ListItems.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ListItems.

        Path to folder  # noqa: E501

        :param path: The path of this ListItems.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def tag(self):
        """Gets the tag of this ListItems.  # noqa: E501

        Filter by item tag  # noqa: E501

        :return: The tag of this ListItems.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ListItems.

        Filter by item tag  # noqa: E501

        :param tag: The tag of this ListItems.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def token(self):
        """Gets the token of this ListItems.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this ListItems.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this ListItems.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this ListItems.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def type(self):
        """Gets the type of this ListItems.  # noqa: E501

        The item types list of the requested items. In case it is empty, all types of items will be returned. options: [key, static-secret, dynamic-secret]  # noqa: E501

        :return: The type of this ListItems.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListItems.

        The item types list of the requested items. In case it is empty, all types of items will be returned. options: [key, static-secret, dynamic-secret]  # noqa: E501

        :param type: The type of this ListItems.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def uid_token(self):
        """Gets the uid_token of this ListItems.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this ListItems.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this ListItems.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this ListItems.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def username(self):
        """Gets the username of this ListItems.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The username of this ListItems.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ListItems.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param username: The username of this ListItems.  # noqa: E501
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
        if not isinstance(other, ListItems):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListItems):
            return True

        return self.to_dict() != other.to_dict()
