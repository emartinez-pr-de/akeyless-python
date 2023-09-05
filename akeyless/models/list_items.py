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
        'accessibility': 'str',
        'advanced_filter': 'str',
        'auto_pagination': 'str',
        'filter': 'str',
        'json': 'bool',
        'minimal_view': 'bool',
        'pagination_token': 'str',
        'path': 'str',
        'sra_only': 'bool',
        'sub_types': 'list[str]',
        'tag': 'str',
        'token': 'str',
        'type': 'list[str]',
        'uid_token': 'str'
    }

    attribute_map = {
        'accessibility': 'accessibility',
        'advanced_filter': 'advanced-filter',
        'auto_pagination': 'auto-pagination',
        'filter': 'filter',
        'json': 'json',
        'minimal_view': 'minimal-view',
        'pagination_token': 'pagination-token',
        'path': 'path',
        'sra_only': 'sra-only',
        'sub_types': 'sub_types',
        'tag': 'tag',
        'token': 'token',
        'type': 'type',
        'uid_token': 'uid-token'
    }

    def __init__(self, accessibility='regular', advanced_filter=None, auto_pagination='enabled', filter=None, json=False, minimal_view=None, pagination_token=None, path=None, sra_only=False, sub_types=None, tag=None, token=None, type=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """ListItems - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._accessibility = None
        self._advanced_filter = None
        self._auto_pagination = None
        self._filter = None
        self._json = None
        self._minimal_view = None
        self._pagination_token = None
        self._path = None
        self._sra_only = None
        self._sub_types = None
        self._tag = None
        self._token = None
        self._type = None
        self._uid_token = None
        self.discriminator = None

        if accessibility is not None:
            self.accessibility = accessibility
        if advanced_filter is not None:
            self.advanced_filter = advanced_filter
        if auto_pagination is not None:
            self.auto_pagination = auto_pagination
        if filter is not None:
            self.filter = filter
        if json is not None:
            self.json = json
        if minimal_view is not None:
            self.minimal_view = minimal_view
        if pagination_token is not None:
            self.pagination_token = pagination_token
        if path is not None:
            self.path = path
        if sra_only is not None:
            self.sra_only = sra_only
        if sub_types is not None:
            self.sub_types = sub_types
        if tag is not None:
            self.tag = tag
        if token is not None:
            self.token = token
        if type is not None:
            self.type = type
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def accessibility(self):
        """Gets the accessibility of this ListItems.  # noqa: E501

        for personal password manager  # noqa: E501

        :return: The accessibility of this ListItems.  # noqa: E501
        :rtype: str
        """
        return self._accessibility

    @accessibility.setter
    def accessibility(self, accessibility):
        """Sets the accessibility of this ListItems.

        for personal password manager  # noqa: E501

        :param accessibility: The accessibility of this ListItems.  # noqa: E501
        :type: str
        """

        self._accessibility = accessibility

    @property
    def advanced_filter(self):
        """Gets the advanced_filter of this ListItems.  # noqa: E501

        Filter by item name/username/website or part of it  # noqa: E501

        :return: The advanced_filter of this ListItems.  # noqa: E501
        :rtype: str
        """
        return self._advanced_filter

    @advanced_filter.setter
    def advanced_filter(self, advanced_filter):
        """Sets the advanced_filter of this ListItems.

        Filter by item name/username/website or part of it  # noqa: E501

        :param advanced_filter: The advanced_filter of this ListItems.  # noqa: E501
        :type: str
        """

        self._advanced_filter = advanced_filter

    @property
    def auto_pagination(self):
        """Gets the auto_pagination of this ListItems.  # noqa: E501

        Retrieve all items using pagination, when disabled retrieving only first 1000 items  # noqa: E501

        :return: The auto_pagination of this ListItems.  # noqa: E501
        :rtype: str
        """
        return self._auto_pagination

    @auto_pagination.setter
    def auto_pagination(self, auto_pagination):
        """Sets the auto_pagination of this ListItems.

        Retrieve all items using pagination, when disabled retrieving only first 1000 items  # noqa: E501

        :param auto_pagination: The auto_pagination of this ListItems.  # noqa: E501
        :type: str
        """

        self._auto_pagination = auto_pagination

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
    def json(self):
        """Gets the json of this ListItems.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this ListItems.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this ListItems.

        Set output format to JSON  # noqa: E501

        :param json: The json of this ListItems.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def minimal_view(self):
        """Gets the minimal_view of this ListItems.  # noqa: E501


        :return: The minimal_view of this ListItems.  # noqa: E501
        :rtype: bool
        """
        return self._minimal_view

    @minimal_view.setter
    def minimal_view(self, minimal_view):
        """Sets the minimal_view of this ListItems.


        :param minimal_view: The minimal_view of this ListItems.  # noqa: E501
        :type: bool
        """

        self._minimal_view = minimal_view

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
    def sra_only(self):
        """Gets the sra_only of this ListItems.  # noqa: E501

        Filter by items with SRA functionality enabled  # noqa: E501

        :return: The sra_only of this ListItems.  # noqa: E501
        :rtype: bool
        """
        return self._sra_only

    @sra_only.setter
    def sra_only(self, sra_only):
        """Sets the sra_only of this ListItems.

        Filter by items with SRA functionality enabled  # noqa: E501

        :param sra_only: The sra_only of this ListItems.  # noqa: E501
        :type: bool
        """

        self._sra_only = sra_only

    @property
    def sub_types(self):
        """Gets the sub_types of this ListItems.  # noqa: E501


        :return: The sub_types of this ListItems.  # noqa: E501
        :rtype: list[str]
        """
        return self._sub_types

    @sub_types.setter
    def sub_types(self, sub_types):
        """Sets the sub_types of this ListItems.


        :param sub_types: The sub_types of this ListItems.  # noqa: E501
        :type: list[str]
        """

        self._sub_types = sub_types

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

        The item types list of the requested items. In case it is empty, all types of items will be returned. options: [key, static-secret, dynamic-secret, classic-key]  # noqa: E501

        :return: The type of this ListItems.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListItems.

        The item types list of the requested items. In case it is empty, all types of items will be returned. options: [key, static-secret, dynamic-secret, classic-key]  # noqa: E501

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
