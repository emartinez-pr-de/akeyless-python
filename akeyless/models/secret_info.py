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


class SecretInfo(object):
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
        'created': 'datetime',
        'description': 'str',
        'expiration': 'datetime',
        'last_retrieved': 'datetime',
        'location': 'object',
        'name': 'str',
        'secret_id': 'str',
        'status': 'bool',
        'tags': 'dict(str, str)',
        'type': 'str'
    }

    attribute_map = {
        'created': 'created',
        'description': 'description',
        'expiration': 'expiration',
        'last_retrieved': 'last_retrieved',
        'location': 'location',
        'name': 'name',
        'secret_id': 'secret_id',
        'status': 'status',
        'tags': 'tags',
        'type': 'type'
    }

    def __init__(self, created=None, description=None, expiration=None, last_retrieved=None, location=None, name=None, secret_id=None, status=None, tags=None, type=None, local_vars_configuration=None):  # noqa: E501
        """SecretInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created = None
        self._description = None
        self._expiration = None
        self._last_retrieved = None
        self._location = None
        self._name = None
        self._secret_id = None
        self._status = None
        self._tags = None
        self._type = None
        self.discriminator = None

        if created is not None:
            self.created = created
        if description is not None:
            self.description = description
        if expiration is not None:
            self.expiration = expiration
        if last_retrieved is not None:
            self.last_retrieved = last_retrieved
        if location is not None:
            self.location = location
        if name is not None:
            self.name = name
        if secret_id is not None:
            self.secret_id = secret_id
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if type is not None:
            self.type = type

    @property
    def created(self):
        """Gets the created of this SecretInfo.  # noqa: E501


        :return: The created of this SecretInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SecretInfo.


        :param created: The created of this SecretInfo.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def description(self):
        """Gets the description of this SecretInfo.  # noqa: E501


        :return: The description of this SecretInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SecretInfo.


        :param description: The description of this SecretInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def expiration(self):
        """Gets the expiration of this SecretInfo.  # noqa: E501


        :return: The expiration of this SecretInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this SecretInfo.


        :param expiration: The expiration of this SecretInfo.  # noqa: E501
        :type: datetime
        """

        self._expiration = expiration

    @property
    def last_retrieved(self):
        """Gets the last_retrieved of this SecretInfo.  # noqa: E501


        :return: The last_retrieved of this SecretInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._last_retrieved

    @last_retrieved.setter
    def last_retrieved(self, last_retrieved):
        """Sets the last_retrieved of this SecretInfo.


        :param last_retrieved: The last_retrieved of this SecretInfo.  # noqa: E501
        :type: datetime
        """

        self._last_retrieved = last_retrieved

    @property
    def location(self):
        """Gets the location of this SecretInfo.  # noqa: E501


        :return: The location of this SecretInfo.  # noqa: E501
        :rtype: object
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this SecretInfo.


        :param location: The location of this SecretInfo.  # noqa: E501
        :type: object
        """

        self._location = location

    @property
    def name(self):
        """Gets the name of this SecretInfo.  # noqa: E501


        :return: The name of this SecretInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SecretInfo.


        :param name: The name of this SecretInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def secret_id(self):
        """Gets the secret_id of this SecretInfo.  # noqa: E501


        :return: The secret_id of this SecretInfo.  # noqa: E501
        :rtype: str
        """
        return self._secret_id

    @secret_id.setter
    def secret_id(self, secret_id):
        """Sets the secret_id of this SecretInfo.


        :param secret_id: The secret_id of this SecretInfo.  # noqa: E501
        :type: str
        """

        self._secret_id = secret_id

    @property
    def status(self):
        """Gets the status of this SecretInfo.  # noqa: E501


        :return: The status of this SecretInfo.  # noqa: E501
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SecretInfo.


        :param status: The status of this SecretInfo.  # noqa: E501
        :type: bool
        """

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this SecretInfo.  # noqa: E501


        :return: The tags of this SecretInfo.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SecretInfo.


        :param tags: The tags of this SecretInfo.  # noqa: E501
        :type: dict(str, str)
        """

        self._tags = tags

    @property
    def type(self):
        """Gets the type of this SecretInfo.  # noqa: E501


        :return: The type of this SecretInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SecretInfo.


        :param type: The type of this SecretInfo.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, SecretInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SecretInfo):
            return True

        return self.to_dict() != other.to_dict()
