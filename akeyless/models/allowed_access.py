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


class AllowedAccess(object):
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
        'access_id': 'str',
        'access_type': 'str',
        'cluster_id': 'int',
        'created_at': 'datetime',
        'description': 'str',
        'editable': 'bool',
        'error': 'str',
        'id': 'int',
        'is_valid': 'bool',
        'name': 'str',
        'permissions': 'list[str]',
        'sub_claims': 'dict(str, list[str])',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'access_id': 'access_id',
        'access_type': 'access_type',
        'cluster_id': 'cluster_id',
        'created_at': 'created_at',
        'description': 'description',
        'editable': 'editable',
        'error': 'error',
        'id': 'id',
        'is_valid': 'is_valid',
        'name': 'name',
        'permissions': 'permissions',
        'sub_claims': 'sub_claims',
        'updated_at': 'updated_at'
    }

    def __init__(self, access_id=None, access_type=None, cluster_id=None, created_at=None, description=None, editable=None, error=None, id=None, is_valid=None, name=None, permissions=None, sub_claims=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """AllowedAccess - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_id = None
        self._access_type = None
        self._cluster_id = None
        self._created_at = None
        self._description = None
        self._editable = None
        self._error = None
        self._id = None
        self._is_valid = None
        self._name = None
        self._permissions = None
        self._sub_claims = None
        self._updated_at = None
        self.discriminator = None

        if access_id is not None:
            self.access_id = access_id
        if access_type is not None:
            self.access_type = access_type
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if editable is not None:
            self.editable = editable
        if error is not None:
            self.error = error
        if id is not None:
            self.id = id
        if is_valid is not None:
            self.is_valid = is_valid
        if name is not None:
            self.name = name
        if permissions is not None:
            self.permissions = permissions
        if sub_claims is not None:
            self.sub_claims = sub_claims
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def access_id(self):
        """Gets the access_id of this AllowedAccess.  # noqa: E501


        :return: The access_id of this AllowedAccess.  # noqa: E501
        :rtype: str
        """
        return self._access_id

    @access_id.setter
    def access_id(self, access_id):
        """Sets the access_id of this AllowedAccess.


        :param access_id: The access_id of this AllowedAccess.  # noqa: E501
        :type: str
        """

        self._access_id = access_id

    @property
    def access_type(self):
        """Gets the access_type of this AllowedAccess.  # noqa: E501


        :return: The access_type of this AllowedAccess.  # noqa: E501
        :rtype: str
        """
        return self._access_type

    @access_type.setter
    def access_type(self, access_type):
        """Sets the access_type of this AllowedAccess.


        :param access_type: The access_type of this AllowedAccess.  # noqa: E501
        :type: str
        """

        self._access_type = access_type

    @property
    def cluster_id(self):
        """Gets the cluster_id of this AllowedAccess.  # noqa: E501


        :return: The cluster_id of this AllowedAccess.  # noqa: E501
        :rtype: int
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this AllowedAccess.


        :param cluster_id: The cluster_id of this AllowedAccess.  # noqa: E501
        :type: int
        """

        self._cluster_id = cluster_id

    @property
    def created_at(self):
        """Gets the created_at of this AllowedAccess.  # noqa: E501


        :return: The created_at of this AllowedAccess.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AllowedAccess.


        :param created_at: The created_at of this AllowedAccess.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this AllowedAccess.  # noqa: E501


        :return: The description of this AllowedAccess.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AllowedAccess.


        :param description: The description of this AllowedAccess.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def editable(self):
        """Gets the editable of this AllowedAccess.  # noqa: E501


        :return: The editable of this AllowedAccess.  # noqa: E501
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        """Sets the editable of this AllowedAccess.


        :param editable: The editable of this AllowedAccess.  # noqa: E501
        :type: bool
        """

        self._editable = editable

    @property
    def error(self):
        """Gets the error of this AllowedAccess.  # noqa: E501


        :return: The error of this AllowedAccess.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this AllowedAccess.


        :param error: The error of this AllowedAccess.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def id(self):
        """Gets the id of this AllowedAccess.  # noqa: E501


        :return: The id of this AllowedAccess.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AllowedAccess.


        :param id: The id of this AllowedAccess.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def is_valid(self):
        """Gets the is_valid of this AllowedAccess.  # noqa: E501


        :return: The is_valid of this AllowedAccess.  # noqa: E501
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """Sets the is_valid of this AllowedAccess.


        :param is_valid: The is_valid of this AllowedAccess.  # noqa: E501
        :type: bool
        """

        self._is_valid = is_valid

    @property
    def name(self):
        """Gets the name of this AllowedAccess.  # noqa: E501


        :return: The name of this AllowedAccess.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AllowedAccess.


        :param name: The name of this AllowedAccess.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def permissions(self):
        """Gets the permissions of this AllowedAccess.  # noqa: E501


        :return: The permissions of this AllowedAccess.  # noqa: E501
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this AllowedAccess.


        :param permissions: The permissions of this AllowedAccess.  # noqa: E501
        :type: list[str]
        """

        self._permissions = permissions

    @property
    def sub_claims(self):
        """Gets the sub_claims of this AllowedAccess.  # noqa: E501


        :return: The sub_claims of this AllowedAccess.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._sub_claims

    @sub_claims.setter
    def sub_claims(self, sub_claims):
        """Sets the sub_claims of this AllowedAccess.


        :param sub_claims: The sub_claims of this AllowedAccess.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._sub_claims = sub_claims

    @property
    def updated_at(self):
        """Gets the updated_at of this AllowedAccess.  # noqa: E501


        :return: The updated_at of this AllowedAccess.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AllowedAccess.


        :param updated_at: The updated_at of this AllowedAccess.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, AllowedAccess):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AllowedAccess):
            return True

        return self.to_dict() != other.to_dict()
