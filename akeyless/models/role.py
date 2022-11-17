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


class Role(object):
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
        'access_date': 'datetime',
        'client_permissions': 'list[str]',
        'comment': 'str',
        'creation_date': 'datetime',
        'modification_date': 'datetime',
        'role_auth_methods_assoc': 'list[RoleAuthMethodAssociation]',
        'role_name': 'str',
        'rules': 'Rules'
    }

    attribute_map = {
        'access_date': 'access_date',
        'client_permissions': 'client_permissions',
        'comment': 'comment',
        'creation_date': 'creation_date',
        'modification_date': 'modification_date',
        'role_auth_methods_assoc': 'role_auth_methods_assoc',
        'role_name': 'role_name',
        'rules': 'rules'
    }

    def __init__(self, access_date=None, client_permissions=None, comment=None, creation_date=None, modification_date=None, role_auth_methods_assoc=None, role_name=None, rules=None, local_vars_configuration=None):  # noqa: E501
        """Role - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_date = None
        self._client_permissions = None
        self._comment = None
        self._creation_date = None
        self._modification_date = None
        self._role_auth_methods_assoc = None
        self._role_name = None
        self._rules = None
        self.discriminator = None

        if access_date is not None:
            self.access_date = access_date
        if client_permissions is not None:
            self.client_permissions = client_permissions
        if comment is not None:
            self.comment = comment
        if creation_date is not None:
            self.creation_date = creation_date
        if modification_date is not None:
            self.modification_date = modification_date
        if role_auth_methods_assoc is not None:
            self.role_auth_methods_assoc = role_auth_methods_assoc
        if role_name is not None:
            self.role_name = role_name
        if rules is not None:
            self.rules = rules

    @property
    def access_date(self):
        """Gets the access_date of this Role.  # noqa: E501


        :return: The access_date of this Role.  # noqa: E501
        :rtype: datetime
        """
        return self._access_date

    @access_date.setter
    def access_date(self, access_date):
        """Sets the access_date of this Role.


        :param access_date: The access_date of this Role.  # noqa: E501
        :type: datetime
        """

        self._access_date = access_date

    @property
    def client_permissions(self):
        """Gets the client_permissions of this Role.  # noqa: E501


        :return: The client_permissions of this Role.  # noqa: E501
        :rtype: list[str]
        """
        return self._client_permissions

    @client_permissions.setter
    def client_permissions(self, client_permissions):
        """Sets the client_permissions of this Role.


        :param client_permissions: The client_permissions of this Role.  # noqa: E501
        :type: list[str]
        """

        self._client_permissions = client_permissions

    @property
    def comment(self):
        """Gets the comment of this Role.  # noqa: E501


        :return: The comment of this Role.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this Role.


        :param comment: The comment of this Role.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def creation_date(self):
        """Gets the creation_date of this Role.  # noqa: E501


        :return: The creation_date of this Role.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this Role.


        :param creation_date: The creation_date of this Role.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def modification_date(self):
        """Gets the modification_date of this Role.  # noqa: E501


        :return: The modification_date of this Role.  # noqa: E501
        :rtype: datetime
        """
        return self._modification_date

    @modification_date.setter
    def modification_date(self, modification_date):
        """Sets the modification_date of this Role.


        :param modification_date: The modification_date of this Role.  # noqa: E501
        :type: datetime
        """

        self._modification_date = modification_date

    @property
    def role_auth_methods_assoc(self):
        """Gets the role_auth_methods_assoc of this Role.  # noqa: E501


        :return: The role_auth_methods_assoc of this Role.  # noqa: E501
        :rtype: list[RoleAuthMethodAssociation]
        """
        return self._role_auth_methods_assoc

    @role_auth_methods_assoc.setter
    def role_auth_methods_assoc(self, role_auth_methods_assoc):
        """Sets the role_auth_methods_assoc of this Role.


        :param role_auth_methods_assoc: The role_auth_methods_assoc of this Role.  # noqa: E501
        :type: list[RoleAuthMethodAssociation]
        """

        self._role_auth_methods_assoc = role_auth_methods_assoc

    @property
    def role_name(self):
        """Gets the role_name of this Role.  # noqa: E501


        :return: The role_name of this Role.  # noqa: E501
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this Role.


        :param role_name: The role_name of this Role.  # noqa: E501
        :type: str
        """

        self._role_name = role_name

    @property
    def rules(self):
        """Gets the rules of this Role.  # noqa: E501


        :return: The rules of this Role.  # noqa: E501
        :rtype: Rules
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this Role.


        :param rules: The rules of this Role.  # noqa: E501
        :type: Rules
        """

        self._rules = rules

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
        if not isinstance(other, Role):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Role):
            return True

        return self.to_dict() != other.to_dict()
