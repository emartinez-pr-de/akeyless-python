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


class ClassicKeyDetailsInfo(object):
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
        'classic_key_attributes': 'dict(str, list[str])',
        'classic_key_id': 'str',
        'gw_cluster_id': 'int',
        'has_certificate': 'bool',
        'is_provided_by_user': 'bool',
        'is_unexportable': 'bool',
        'key_state': 'str',
        'key_type': 'str',
        'last_error': 'str',
        'public_key': 'str',
        'target_alias_helper': 'str',
        'target_types': 'list[str]',
        'targets': 'list[ClassicKeyTargetInfo]'
    }

    attribute_map = {
        'classic_key_attributes': 'classic_key_attributes',
        'classic_key_id': 'classic_key_id',
        'gw_cluster_id': 'gw_cluster_id',
        'has_certificate': 'has_certificate',
        'is_provided_by_user': 'is_provided_by_user',
        'is_unexportable': 'is_unexportable',
        'key_state': 'key_state',
        'key_type': 'key_type',
        'last_error': 'last_error',
        'public_key': 'public_key',
        'target_alias_helper': 'target_alias_helper',
        'target_types': 'target_types',
        'targets': 'targets'
    }

    def __init__(self, classic_key_attributes=None, classic_key_id=None, gw_cluster_id=None, has_certificate=None, is_provided_by_user=None, is_unexportable=None, key_state=None, key_type=None, last_error=None, public_key=None, target_alias_helper=None, target_types=None, targets=None, local_vars_configuration=None):  # noqa: E501
        """ClassicKeyDetailsInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._classic_key_attributes = None
        self._classic_key_id = None
        self._gw_cluster_id = None
        self._has_certificate = None
        self._is_provided_by_user = None
        self._is_unexportable = None
        self._key_state = None
        self._key_type = None
        self._last_error = None
        self._public_key = None
        self._target_alias_helper = None
        self._target_types = None
        self._targets = None
        self.discriminator = None

        if classic_key_attributes is not None:
            self.classic_key_attributes = classic_key_attributes
        if classic_key_id is not None:
            self.classic_key_id = classic_key_id
        if gw_cluster_id is not None:
            self.gw_cluster_id = gw_cluster_id
        if has_certificate is not None:
            self.has_certificate = has_certificate
        if is_provided_by_user is not None:
            self.is_provided_by_user = is_provided_by_user
        if is_unexportable is not None:
            self.is_unexportable = is_unexportable
        if key_state is not None:
            self.key_state = key_state
        if key_type is not None:
            self.key_type = key_type
        if last_error is not None:
            self.last_error = last_error
        if public_key is not None:
            self.public_key = public_key
        if target_alias_helper is not None:
            self.target_alias_helper = target_alias_helper
        if target_types is not None:
            self.target_types = target_types
        if targets is not None:
            self.targets = targets

    @property
    def classic_key_attributes(self):
        """Gets the classic_key_attributes of this ClassicKeyDetailsInfo.  # noqa: E501


        :return: The classic_key_attributes of this ClassicKeyDetailsInfo.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._classic_key_attributes

    @classic_key_attributes.setter
    def classic_key_attributes(self, classic_key_attributes):
        """Sets the classic_key_attributes of this ClassicKeyDetailsInfo.


        :param classic_key_attributes: The classic_key_attributes of this ClassicKeyDetailsInfo.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._classic_key_attributes = classic_key_attributes

    @property
    def classic_key_id(self):
        """Gets the classic_key_id of this ClassicKeyDetailsInfo.  # noqa: E501


        :return: The classic_key_id of this ClassicKeyDetailsInfo.  # noqa: E501
        :rtype: str
        """
        return self._classic_key_id

    @classic_key_id.setter
    def classic_key_id(self, classic_key_id):
        """Sets the classic_key_id of this ClassicKeyDetailsInfo.


        :param classic_key_id: The classic_key_id of this ClassicKeyDetailsInfo.  # noqa: E501
        :type: str
        """

        self._classic_key_id = classic_key_id

    @property
    def gw_cluster_id(self):
        """Gets the gw_cluster_id of this ClassicKeyDetailsInfo.  # noqa: E501


        :return: The gw_cluster_id of this ClassicKeyDetailsInfo.  # noqa: E501
        :rtype: int
        """
        return self._gw_cluster_id

    @gw_cluster_id.setter
    def gw_cluster_id(self, gw_cluster_id):
        """Sets the gw_cluster_id of this ClassicKeyDetailsInfo.


        :param gw_cluster_id: The gw_cluster_id of this ClassicKeyDetailsInfo.  # noqa: E501
        :type: int
        """

        self._gw_cluster_id = gw_cluster_id

    @property
    def has_certificate(self):
        """Gets the has_certificate of this ClassicKeyDetailsInfo.  # noqa: E501


        :return: The has_certificate of this ClassicKeyDetailsInfo.  # noqa: E501
        :rtype: bool
        """
        return self._has_certificate

    @has_certificate.setter
    def has_certificate(self, has_certificate):
        """Sets the has_certificate of this ClassicKeyDetailsInfo.


        :param has_certificate: The has_certificate of this ClassicKeyDetailsInfo.  # noqa: E501
        :type: bool
        """

        self._has_certificate = has_certificate

    @property
    def is_provided_by_user(self):
        """Gets the is_provided_by_user of this ClassicKeyDetailsInfo.  # noqa: E501


        :return: The is_provided_by_user of this ClassicKeyDetailsInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_provided_by_user

    @is_provided_by_user.setter
    def is_provided_by_user(self, is_provided_by_user):
        """Sets the is_provided_by_user of this ClassicKeyDetailsInfo.


        :param is_provided_by_user: The is_provided_by_user of this ClassicKeyDetailsInfo.  # noqa: E501
        :type: bool
        """

        self._is_provided_by_user = is_provided_by_user

    @property
    def is_unexportable(self):
        """Gets the is_unexportable of this ClassicKeyDetailsInfo.  # noqa: E501


        :return: The is_unexportable of this ClassicKeyDetailsInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_unexportable

    @is_unexportable.setter
    def is_unexportable(self, is_unexportable):
        """Sets the is_unexportable of this ClassicKeyDetailsInfo.


        :param is_unexportable: The is_unexportable of this ClassicKeyDetailsInfo.  # noqa: E501
        :type: bool
        """

        self._is_unexportable = is_unexportable

    @property
    def key_state(self):
        """Gets the key_state of this ClassicKeyDetailsInfo.  # noqa: E501

        ItemState defines the different states an Item can be in  # noqa: E501

        :return: The key_state of this ClassicKeyDetailsInfo.  # noqa: E501
        :rtype: str
        """
        return self._key_state

    @key_state.setter
    def key_state(self, key_state):
        """Sets the key_state of this ClassicKeyDetailsInfo.

        ItemState defines the different states an Item can be in  # noqa: E501

        :param key_state: The key_state of this ClassicKeyDetailsInfo.  # noqa: E501
        :type: str
        """

        self._key_state = key_state

    @property
    def key_type(self):
        """Gets the key_type of this ClassicKeyDetailsInfo.  # noqa: E501


        :return: The key_type of this ClassicKeyDetailsInfo.  # noqa: E501
        :rtype: str
        """
        return self._key_type

    @key_type.setter
    def key_type(self, key_type):
        """Sets the key_type of this ClassicKeyDetailsInfo.


        :param key_type: The key_type of this ClassicKeyDetailsInfo.  # noqa: E501
        :type: str
        """

        self._key_type = key_type

    @property
    def last_error(self):
        """Gets the last_error of this ClassicKeyDetailsInfo.  # noqa: E501


        :return: The last_error of this ClassicKeyDetailsInfo.  # noqa: E501
        :rtype: str
        """
        return self._last_error

    @last_error.setter
    def last_error(self, last_error):
        """Sets the last_error of this ClassicKeyDetailsInfo.


        :param last_error: The last_error of this ClassicKeyDetailsInfo.  # noqa: E501
        :type: str
        """

        self._last_error = last_error

    @property
    def public_key(self):
        """Gets the public_key of this ClassicKeyDetailsInfo.  # noqa: E501


        :return: The public_key of this ClassicKeyDetailsInfo.  # noqa: E501
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this ClassicKeyDetailsInfo.


        :param public_key: The public_key of this ClassicKeyDetailsInfo.  # noqa: E501
        :type: str
        """

        self._public_key = public_key

    @property
    def target_alias_helper(self):
        """Gets the target_alias_helper of this ClassicKeyDetailsInfo.  # noqa: E501


        :return: The target_alias_helper of this ClassicKeyDetailsInfo.  # noqa: E501
        :rtype: str
        """
        return self._target_alias_helper

    @target_alias_helper.setter
    def target_alias_helper(self, target_alias_helper):
        """Sets the target_alias_helper of this ClassicKeyDetailsInfo.


        :param target_alias_helper: The target_alias_helper of this ClassicKeyDetailsInfo.  # noqa: E501
        :type: str
        """

        self._target_alias_helper = target_alias_helper

    @property
    def target_types(self):
        """Gets the target_types of this ClassicKeyDetailsInfo.  # noqa: E501


        :return: The target_types of this ClassicKeyDetailsInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_types

    @target_types.setter
    def target_types(self, target_types):
        """Sets the target_types of this ClassicKeyDetailsInfo.


        :param target_types: The target_types of this ClassicKeyDetailsInfo.  # noqa: E501
        :type: list[str]
        """

        self._target_types = target_types

    @property
    def targets(self):
        """Gets the targets of this ClassicKeyDetailsInfo.  # noqa: E501


        :return: The targets of this ClassicKeyDetailsInfo.  # noqa: E501
        :rtype: list[ClassicKeyTargetInfo]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this ClassicKeyDetailsInfo.


        :param targets: The targets of this ClassicKeyDetailsInfo.  # noqa: E501
        :type: list[ClassicKeyTargetInfo]
        """

        self._targets = targets

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
        if not isinstance(other, ClassicKeyDetailsInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClassicKeyDetailsInfo):
            return True

        return self.to_dict() != other.to_dict()
