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


class Target(object):
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
        'access_request_status': 'str',
        'attributes': 'dict(str, object)',
        'client_permissions': 'list[str]',
        'comment': 'str',
        'creation_date': 'datetime',
        'credentials_less': 'bool',
        'is_access_request_enabled': 'bool',
        'last_version': 'int',
        'modification_date': 'datetime',
        'protection_key_name': 'str',
        'target_details': 'str',
        'target_id': 'int',
        'target_items_assoc': 'list[TargetItemAssociation]',
        'target_name': 'str',
        'target_type': 'str',
        'target_versions': 'list[ItemVersion]',
        'with_customer_fragment': 'bool'
    }

    attribute_map = {
        'access_date': 'access_date',
        'access_request_status': 'access_request_status',
        'attributes': 'attributes',
        'client_permissions': 'client_permissions',
        'comment': 'comment',
        'creation_date': 'creation_date',
        'credentials_less': 'credentials_less',
        'is_access_request_enabled': 'is_access_request_enabled',
        'last_version': 'last_version',
        'modification_date': 'modification_date',
        'protection_key_name': 'protection_key_name',
        'target_details': 'target_details',
        'target_id': 'target_id',
        'target_items_assoc': 'target_items_assoc',
        'target_name': 'target_name',
        'target_type': 'target_type',
        'target_versions': 'target_versions',
        'with_customer_fragment': 'with_customer_fragment'
    }

    def __init__(self, access_date=None, access_request_status=None, attributes=None, client_permissions=None, comment=None, creation_date=None, credentials_less=None, is_access_request_enabled=None, last_version=None, modification_date=None, protection_key_name=None, target_details=None, target_id=None, target_items_assoc=None, target_name=None, target_type=None, target_versions=None, with_customer_fragment=None, local_vars_configuration=None):  # noqa: E501
        """Target - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_date = None
        self._access_request_status = None
        self._attributes = None
        self._client_permissions = None
        self._comment = None
        self._creation_date = None
        self._credentials_less = None
        self._is_access_request_enabled = None
        self._last_version = None
        self._modification_date = None
        self._protection_key_name = None
        self._target_details = None
        self._target_id = None
        self._target_items_assoc = None
        self._target_name = None
        self._target_type = None
        self._target_versions = None
        self._with_customer_fragment = None
        self.discriminator = None

        if access_date is not None:
            self.access_date = access_date
        if access_request_status is not None:
            self.access_request_status = access_request_status
        if attributes is not None:
            self.attributes = attributes
        if client_permissions is not None:
            self.client_permissions = client_permissions
        if comment is not None:
            self.comment = comment
        if creation_date is not None:
            self.creation_date = creation_date
        if credentials_less is not None:
            self.credentials_less = credentials_less
        if is_access_request_enabled is not None:
            self.is_access_request_enabled = is_access_request_enabled
        if last_version is not None:
            self.last_version = last_version
        if modification_date is not None:
            self.modification_date = modification_date
        if protection_key_name is not None:
            self.protection_key_name = protection_key_name
        if target_details is not None:
            self.target_details = target_details
        if target_id is not None:
            self.target_id = target_id
        if target_items_assoc is not None:
            self.target_items_assoc = target_items_assoc
        if target_name is not None:
            self.target_name = target_name
        if target_type is not None:
            self.target_type = target_type
        if target_versions is not None:
            self.target_versions = target_versions
        if with_customer_fragment is not None:
            self.with_customer_fragment = with_customer_fragment

    @property
    def access_date(self):
        """Gets the access_date of this Target.  # noqa: E501


        :return: The access_date of this Target.  # noqa: E501
        :rtype: datetime
        """
        return self._access_date

    @access_date.setter
    def access_date(self, access_date):
        """Sets the access_date of this Target.


        :param access_date: The access_date of this Target.  # noqa: E501
        :type: datetime
        """

        self._access_date = access_date

    @property
    def access_request_status(self):
        """Gets the access_request_status of this Target.  # noqa: E501


        :return: The access_request_status of this Target.  # noqa: E501
        :rtype: str
        """
        return self._access_request_status

    @access_request_status.setter
    def access_request_status(self, access_request_status):
        """Sets the access_request_status of this Target.


        :param access_request_status: The access_request_status of this Target.  # noqa: E501
        :type: str
        """

        self._access_request_status = access_request_status

    @property
    def attributes(self):
        """Gets the attributes of this Target.  # noqa: E501

        this is not \"omitempty\" since an empty value causes no update while an empty map will clear the attributes  # noqa: E501

        :return: The attributes of this Target.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Target.

        this is not \"omitempty\" since an empty value causes no update while an empty map will clear the attributes  # noqa: E501

        :param attributes: The attributes of this Target.  # noqa: E501
        :type: dict(str, object)
        """

        self._attributes = attributes

    @property
    def client_permissions(self):
        """Gets the client_permissions of this Target.  # noqa: E501


        :return: The client_permissions of this Target.  # noqa: E501
        :rtype: list[str]
        """
        return self._client_permissions

    @client_permissions.setter
    def client_permissions(self, client_permissions):
        """Sets the client_permissions of this Target.


        :param client_permissions: The client_permissions of this Target.  # noqa: E501
        :type: list[str]
        """

        self._client_permissions = client_permissions

    @property
    def comment(self):
        """Gets the comment of this Target.  # noqa: E501


        :return: The comment of this Target.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this Target.


        :param comment: The comment of this Target.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def creation_date(self):
        """Gets the creation_date of this Target.  # noqa: E501


        :return: The creation_date of this Target.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this Target.


        :param creation_date: The creation_date of this Target.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def credentials_less(self):
        """Gets the credentials_less of this Target.  # noqa: E501


        :return: The credentials_less of this Target.  # noqa: E501
        :rtype: bool
        """
        return self._credentials_less

    @credentials_less.setter
    def credentials_less(self, credentials_less):
        """Sets the credentials_less of this Target.


        :param credentials_less: The credentials_less of this Target.  # noqa: E501
        :type: bool
        """

        self._credentials_less = credentials_less

    @property
    def is_access_request_enabled(self):
        """Gets the is_access_request_enabled of this Target.  # noqa: E501


        :return: The is_access_request_enabled of this Target.  # noqa: E501
        :rtype: bool
        """
        return self._is_access_request_enabled

    @is_access_request_enabled.setter
    def is_access_request_enabled(self, is_access_request_enabled):
        """Sets the is_access_request_enabled of this Target.


        :param is_access_request_enabled: The is_access_request_enabled of this Target.  # noqa: E501
        :type: bool
        """

        self._is_access_request_enabled = is_access_request_enabled

    @property
    def last_version(self):
        """Gets the last_version of this Target.  # noqa: E501


        :return: The last_version of this Target.  # noqa: E501
        :rtype: int
        """
        return self._last_version

    @last_version.setter
    def last_version(self, last_version):
        """Sets the last_version of this Target.


        :param last_version: The last_version of this Target.  # noqa: E501
        :type: int
        """

        self._last_version = last_version

    @property
    def modification_date(self):
        """Gets the modification_date of this Target.  # noqa: E501


        :return: The modification_date of this Target.  # noqa: E501
        :rtype: datetime
        """
        return self._modification_date

    @modification_date.setter
    def modification_date(self, modification_date):
        """Sets the modification_date of this Target.


        :param modification_date: The modification_date of this Target.  # noqa: E501
        :type: datetime
        """

        self._modification_date = modification_date

    @property
    def protection_key_name(self):
        """Gets the protection_key_name of this Target.  # noqa: E501


        :return: The protection_key_name of this Target.  # noqa: E501
        :rtype: str
        """
        return self._protection_key_name

    @protection_key_name.setter
    def protection_key_name(self, protection_key_name):
        """Sets the protection_key_name of this Target.


        :param protection_key_name: The protection_key_name of this Target.  # noqa: E501
        :type: str
        """

        self._protection_key_name = protection_key_name

    @property
    def target_details(self):
        """Gets the target_details of this Target.  # noqa: E501


        :return: The target_details of this Target.  # noqa: E501
        :rtype: str
        """
        return self._target_details

    @target_details.setter
    def target_details(self, target_details):
        """Sets the target_details of this Target.


        :param target_details: The target_details of this Target.  # noqa: E501
        :type: str
        """

        self._target_details = target_details

    @property
    def target_id(self):
        """Gets the target_id of this Target.  # noqa: E501


        :return: The target_id of this Target.  # noqa: E501
        :rtype: int
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this Target.


        :param target_id: The target_id of this Target.  # noqa: E501
        :type: int
        """

        self._target_id = target_id

    @property
    def target_items_assoc(self):
        """Gets the target_items_assoc of this Target.  # noqa: E501


        :return: The target_items_assoc of this Target.  # noqa: E501
        :rtype: list[TargetItemAssociation]
        """
        return self._target_items_assoc

    @target_items_assoc.setter
    def target_items_assoc(self, target_items_assoc):
        """Sets the target_items_assoc of this Target.


        :param target_items_assoc: The target_items_assoc of this Target.  # noqa: E501
        :type: list[TargetItemAssociation]
        """

        self._target_items_assoc = target_items_assoc

    @property
    def target_name(self):
        """Gets the target_name of this Target.  # noqa: E501


        :return: The target_name of this Target.  # noqa: E501
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """Sets the target_name of this Target.


        :param target_name: The target_name of this Target.  # noqa: E501
        :type: str
        """

        self._target_name = target_name

    @property
    def target_type(self):
        """Gets the target_type of this Target.  # noqa: E501


        :return: The target_type of this Target.  # noqa: E501
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """Sets the target_type of this Target.


        :param target_type: The target_type of this Target.  # noqa: E501
        :type: str
        """

        self._target_type = target_type

    @property
    def target_versions(self):
        """Gets the target_versions of this Target.  # noqa: E501


        :return: The target_versions of this Target.  # noqa: E501
        :rtype: list[ItemVersion]
        """
        return self._target_versions

    @target_versions.setter
    def target_versions(self, target_versions):
        """Sets the target_versions of this Target.


        :param target_versions: The target_versions of this Target.  # noqa: E501
        :type: list[ItemVersion]
        """

        self._target_versions = target_versions

    @property
    def with_customer_fragment(self):
        """Gets the with_customer_fragment of this Target.  # noqa: E501


        :return: The with_customer_fragment of this Target.  # noqa: E501
        :rtype: bool
        """
        return self._with_customer_fragment

    @with_customer_fragment.setter
    def with_customer_fragment(self, with_customer_fragment):
        """Sets the with_customer_fragment of this Target.


        :param with_customer_fragment: The with_customer_fragment of this Target.  # noqa: E501
        :type: bool
        """

        self._with_customer_fragment = with_customer_fragment

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
        if not isinstance(other, Target):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Target):
            return True

        return self.to_dict() != other.to_dict()
