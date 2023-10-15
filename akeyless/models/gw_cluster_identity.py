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


class GwClusterIdentity(object):
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
        'allowed': 'bool',
        'allowed_access_ids': 'list[str]',
        'cluster_name': 'str',
        'cluster_url': 'str',
        'current_gw': 'bool',
        'customer_fragment_ids': 'list[str]',
        'customer_fragments': 'list[CfInfo]',
        'default_protection_key_id': 'int',
        'default_secret_location': 'str',
        'display_name': 'str',
        'id': 'int',
        'status': 'str',
        'status_description': 'str'
    }

    attribute_map = {
        'allowed': 'allowed',
        'allowed_access_ids': 'allowed_access_ids',
        'cluster_name': 'cluster_name',
        'cluster_url': 'cluster_url',
        'current_gw': 'current_gw',
        'customer_fragment_ids': 'customer_fragment_ids',
        'customer_fragments': 'customer_fragments',
        'default_protection_key_id': 'default_protection_key_id',
        'default_secret_location': 'default_secret_location',
        'display_name': 'display_name',
        'id': 'id',
        'status': 'status',
        'status_description': 'status_description'
    }

    def __init__(self, allowed=None, allowed_access_ids=None, cluster_name=None, cluster_url=None, current_gw=None, customer_fragment_ids=None, customer_fragments=None, default_protection_key_id=None, default_secret_location=None, display_name=None, id=None, status=None, status_description=None, local_vars_configuration=None):  # noqa: E501
        """GwClusterIdentity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._allowed = None
        self._allowed_access_ids = None
        self._cluster_name = None
        self._cluster_url = None
        self._current_gw = None
        self._customer_fragment_ids = None
        self._customer_fragments = None
        self._default_protection_key_id = None
        self._default_secret_location = None
        self._display_name = None
        self._id = None
        self._status = None
        self._status_description = None
        self.discriminator = None

        if allowed is not None:
            self.allowed = allowed
        if allowed_access_ids is not None:
            self.allowed_access_ids = allowed_access_ids
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_url is not None:
            self.cluster_url = cluster_url
        if current_gw is not None:
            self.current_gw = current_gw
        if customer_fragment_ids is not None:
            self.customer_fragment_ids = customer_fragment_ids
        if customer_fragments is not None:
            self.customer_fragments = customer_fragments
        if default_protection_key_id is not None:
            self.default_protection_key_id = default_protection_key_id
        if default_secret_location is not None:
            self.default_secret_location = default_secret_location
        if display_name is not None:
            self.display_name = display_name
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if status_description is not None:
            self.status_description = status_description

    @property
    def allowed(self):
        """Gets the allowed of this GwClusterIdentity.  # noqa: E501


        :return: The allowed of this GwClusterIdentity.  # noqa: E501
        :rtype: bool
        """
        return self._allowed

    @allowed.setter
    def allowed(self, allowed):
        """Sets the allowed of this GwClusterIdentity.


        :param allowed: The allowed of this GwClusterIdentity.  # noqa: E501
        :type: bool
        """

        self._allowed = allowed

    @property
    def allowed_access_ids(self):
        """Gets the allowed_access_ids of this GwClusterIdentity.  # noqa: E501


        :return: The allowed_access_ids of this GwClusterIdentity.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_access_ids

    @allowed_access_ids.setter
    def allowed_access_ids(self, allowed_access_ids):
        """Sets the allowed_access_ids of this GwClusterIdentity.


        :param allowed_access_ids: The allowed_access_ids of this GwClusterIdentity.  # noqa: E501
        :type: list[str]
        """

        self._allowed_access_ids = allowed_access_ids

    @property
    def cluster_name(self):
        """Gets the cluster_name of this GwClusterIdentity.  # noqa: E501


        :return: The cluster_name of this GwClusterIdentity.  # noqa: E501
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this GwClusterIdentity.


        :param cluster_name: The cluster_name of this GwClusterIdentity.  # noqa: E501
        :type: str
        """

        self._cluster_name = cluster_name

    @property
    def cluster_url(self):
        """Gets the cluster_url of this GwClusterIdentity.  # noqa: E501


        :return: The cluster_url of this GwClusterIdentity.  # noqa: E501
        :rtype: str
        """
        return self._cluster_url

    @cluster_url.setter
    def cluster_url(self, cluster_url):
        """Sets the cluster_url of this GwClusterIdentity.


        :param cluster_url: The cluster_url of this GwClusterIdentity.  # noqa: E501
        :type: str
        """

        self._cluster_url = cluster_url

    @property
    def current_gw(self):
        """Gets the current_gw of this GwClusterIdentity.  # noqa: E501


        :return: The current_gw of this GwClusterIdentity.  # noqa: E501
        :rtype: bool
        """
        return self._current_gw

    @current_gw.setter
    def current_gw(self, current_gw):
        """Sets the current_gw of this GwClusterIdentity.


        :param current_gw: The current_gw of this GwClusterIdentity.  # noqa: E501
        :type: bool
        """

        self._current_gw = current_gw

    @property
    def customer_fragment_ids(self):
        """Gets the customer_fragment_ids of this GwClusterIdentity.  # noqa: E501

        Deprecated - use CustomerFragments instead  # noqa: E501

        :return: The customer_fragment_ids of this GwClusterIdentity.  # noqa: E501
        :rtype: list[str]
        """
        return self._customer_fragment_ids

    @customer_fragment_ids.setter
    def customer_fragment_ids(self, customer_fragment_ids):
        """Sets the customer_fragment_ids of this GwClusterIdentity.

        Deprecated - use CustomerFragments instead  # noqa: E501

        :param customer_fragment_ids: The customer_fragment_ids of this GwClusterIdentity.  # noqa: E501
        :type: list[str]
        """

        self._customer_fragment_ids = customer_fragment_ids

    @property
    def customer_fragments(self):
        """Gets the customer_fragments of this GwClusterIdentity.  # noqa: E501


        :return: The customer_fragments of this GwClusterIdentity.  # noqa: E501
        :rtype: list[CfInfo]
        """
        return self._customer_fragments

    @customer_fragments.setter
    def customer_fragments(self, customer_fragments):
        """Sets the customer_fragments of this GwClusterIdentity.


        :param customer_fragments: The customer_fragments of this GwClusterIdentity.  # noqa: E501
        :type: list[CfInfo]
        """

        self._customer_fragments = customer_fragments

    @property
    def default_protection_key_id(self):
        """Gets the default_protection_key_id of this GwClusterIdentity.  # noqa: E501


        :return: The default_protection_key_id of this GwClusterIdentity.  # noqa: E501
        :rtype: int
        """
        return self._default_protection_key_id

    @default_protection_key_id.setter
    def default_protection_key_id(self, default_protection_key_id):
        """Sets the default_protection_key_id of this GwClusterIdentity.


        :param default_protection_key_id: The default_protection_key_id of this GwClusterIdentity.  # noqa: E501
        :type: int
        """

        self._default_protection_key_id = default_protection_key_id

    @property
    def default_secret_location(self):
        """Gets the default_secret_location of this GwClusterIdentity.  # noqa: E501


        :return: The default_secret_location of this GwClusterIdentity.  # noqa: E501
        :rtype: str
        """
        return self._default_secret_location

    @default_secret_location.setter
    def default_secret_location(self, default_secret_location):
        """Sets the default_secret_location of this GwClusterIdentity.


        :param default_secret_location: The default_secret_location of this GwClusterIdentity.  # noqa: E501
        :type: str
        """

        self._default_secret_location = default_secret_location

    @property
    def display_name(self):
        """Gets the display_name of this GwClusterIdentity.  # noqa: E501


        :return: The display_name of this GwClusterIdentity.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this GwClusterIdentity.


        :param display_name: The display_name of this GwClusterIdentity.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this GwClusterIdentity.  # noqa: E501


        :return: The id of this GwClusterIdentity.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GwClusterIdentity.


        :param id: The id of this GwClusterIdentity.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this GwClusterIdentity.  # noqa: E501


        :return: The status of this GwClusterIdentity.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GwClusterIdentity.


        :param status: The status of this GwClusterIdentity.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def status_description(self):
        """Gets the status_description of this GwClusterIdentity.  # noqa: E501


        :return: The status_description of this GwClusterIdentity.  # noqa: E501
        :rtype: str
        """
        return self._status_description

    @status_description.setter
    def status_description(self, status_description):
        """Sets the status_description of this GwClusterIdentity.


        :param status_description: The status_description of this GwClusterIdentity.  # noqa: E501
        :type: str
        """

        self._status_description = status_description

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
        if not isinstance(other, GwClusterIdentity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GwClusterIdentity):
            return True

        return self.to_dict() != other.to_dict()
