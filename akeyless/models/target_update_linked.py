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


class TargetUpdateLinked(object):
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
        'add_hosts': 'str',
        'description': 'str',
        'hosts': 'str',
        'json': 'bool',
        'keep_prev_version': 'str',
        'name': 'str',
        'new_name': 'str',
        'parent_target_name': 'str',
        'rm_hosts': 'str',
        'token': 'str',
        'type': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'add_hosts': 'add-hosts',
        'description': 'description',
        'hosts': 'hosts',
        'json': 'json',
        'keep_prev_version': 'keep-prev-version',
        'name': 'name',
        'new_name': 'new-name',
        'parent_target_name': 'parent-target-name',
        'rm_hosts': 'rm-hosts',
        'token': 'token',
        'type': 'type',
        'uid_token': 'uid-token'
    }

    def __init__(self, add_hosts=None, description=None, hosts=None, json=False, keep_prev_version=None, name=None, new_name=None, parent_target_name=None, rm_hosts=None, token=None, type=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """TargetUpdateLinked - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._add_hosts = None
        self._description = None
        self._hosts = None
        self._json = None
        self._keep_prev_version = None
        self._name = None
        self._new_name = None
        self._parent_target_name = None
        self._rm_hosts = None
        self._token = None
        self._type = None
        self._uid_token = None
        self.discriminator = None

        if add_hosts is not None:
            self.add_hosts = add_hosts
        if description is not None:
            self.description = description
        if hosts is not None:
            self.hosts = hosts
        if json is not None:
            self.json = json
        if keep_prev_version is not None:
            self.keep_prev_version = keep_prev_version
        self.name = name
        if new_name is not None:
            self.new_name = new_name
        if parent_target_name is not None:
            self.parent_target_name = parent_target_name
        if rm_hosts is not None:
            self.rm_hosts = rm_hosts
        if token is not None:
            self.token = token
        if type is not None:
            self.type = type
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def add_hosts(self):
        """Gets the add_hosts of this TargetUpdateLinked.  # noqa: E501

        A comma seperated list of new server hosts and server descriptions joined by semicolon ';' that will be added to the Linked Target hosts.  # noqa: E501

        :return: The add_hosts of this TargetUpdateLinked.  # noqa: E501
        :rtype: str
        """
        return self._add_hosts

    @add_hosts.setter
    def add_hosts(self, add_hosts):
        """Sets the add_hosts of this TargetUpdateLinked.

        A comma seperated list of new server hosts and server descriptions joined by semicolon ';' that will be added to the Linked Target hosts.  # noqa: E501

        :param add_hosts: The add_hosts of this TargetUpdateLinked.  # noqa: E501
        :type: str
        """

        self._add_hosts = add_hosts

    @property
    def description(self):
        """Gets the description of this TargetUpdateLinked.  # noqa: E501

        Description of the object  # noqa: E501

        :return: The description of this TargetUpdateLinked.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TargetUpdateLinked.

        Description of the object  # noqa: E501

        :param description: The description of this TargetUpdateLinked.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def hosts(self):
        """Gets the hosts of this TargetUpdateLinked.  # noqa: E501

        A comma seperated list of server hosts and server descriptions joined by semicolon ';' (i.e. 'server-dev.com;My Dev server,server-prod.com;My Prod server description')  # noqa: E501

        :return: The hosts of this TargetUpdateLinked.  # noqa: E501
        :rtype: str
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this TargetUpdateLinked.

        A comma seperated list of server hosts and server descriptions joined by semicolon ';' (i.e. 'server-dev.com;My Dev server,server-prod.com;My Prod server description')  # noqa: E501

        :param hosts: The hosts of this TargetUpdateLinked.  # noqa: E501
        :type: str
        """

        self._hosts = hosts

    @property
    def json(self):
        """Gets the json of this TargetUpdateLinked.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this TargetUpdateLinked.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this TargetUpdateLinked.

        Set output format to JSON  # noqa: E501

        :param json: The json of this TargetUpdateLinked.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def keep_prev_version(self):
        """Gets the keep_prev_version of this TargetUpdateLinked.  # noqa: E501

        Whether to keep previous version [true/false]. If not set, use default according to account settings  # noqa: E501

        :return: The keep_prev_version of this TargetUpdateLinked.  # noqa: E501
        :rtype: str
        """
        return self._keep_prev_version

    @keep_prev_version.setter
    def keep_prev_version(self, keep_prev_version):
        """Sets the keep_prev_version of this TargetUpdateLinked.

        Whether to keep previous version [true/false]. If not set, use default according to account settings  # noqa: E501

        :param keep_prev_version: The keep_prev_version of this TargetUpdateLinked.  # noqa: E501
        :type: str
        """

        self._keep_prev_version = keep_prev_version

    @property
    def name(self):
        """Gets the name of this TargetUpdateLinked.  # noqa: E501

        Linked Target name  # noqa: E501

        :return: The name of this TargetUpdateLinked.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TargetUpdateLinked.

        Linked Target name  # noqa: E501

        :param name: The name of this TargetUpdateLinked.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def new_name(self):
        """Gets the new_name of this TargetUpdateLinked.  # noqa: E501

        New Linked Target name  # noqa: E501

        :return: The new_name of this TargetUpdateLinked.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this TargetUpdateLinked.

        New Linked Target name  # noqa: E501

        :param new_name: The new_name of this TargetUpdateLinked.  # noqa: E501
        :type: str
        """

        self._new_name = new_name

    @property
    def parent_target_name(self):
        """Gets the parent_target_name of this TargetUpdateLinked.  # noqa: E501

        The parent Target name  # noqa: E501

        :return: The parent_target_name of this TargetUpdateLinked.  # noqa: E501
        :rtype: str
        """
        return self._parent_target_name

    @parent_target_name.setter
    def parent_target_name(self, parent_target_name):
        """Sets the parent_target_name of this TargetUpdateLinked.

        The parent Target name  # noqa: E501

        :param parent_target_name: The parent_target_name of this TargetUpdateLinked.  # noqa: E501
        :type: str
        """

        self._parent_target_name = parent_target_name

    @property
    def rm_hosts(self):
        """Gets the rm_hosts of this TargetUpdateLinked.  # noqa: E501

        Comma separated list of existing hosts that will be removed from Linked Target hosts.  # noqa: E501

        :return: The rm_hosts of this TargetUpdateLinked.  # noqa: E501
        :rtype: str
        """
        return self._rm_hosts

    @rm_hosts.setter
    def rm_hosts(self, rm_hosts):
        """Sets the rm_hosts of this TargetUpdateLinked.

        Comma separated list of existing hosts that will be removed from Linked Target hosts.  # noqa: E501

        :param rm_hosts: The rm_hosts of this TargetUpdateLinked.  # noqa: E501
        :type: str
        """

        self._rm_hosts = rm_hosts

    @property
    def token(self):
        """Gets the token of this TargetUpdateLinked.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this TargetUpdateLinked.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this TargetUpdateLinked.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this TargetUpdateLinked.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def type(self):
        """Gets the type of this TargetUpdateLinked.  # noqa: E501

        Specifies the hosts type, relevant only when working without parent target  # noqa: E501

        :return: The type of this TargetUpdateLinked.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TargetUpdateLinked.

        Specifies the hosts type, relevant only when working without parent target  # noqa: E501

        :param type: The type of this TargetUpdateLinked.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def uid_token(self):
        """Gets the uid_token of this TargetUpdateLinked.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this TargetUpdateLinked.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this TargetUpdateLinked.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this TargetUpdateLinked.  # noqa: E501
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
        if not isinstance(other, TargetUpdateLinked):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TargetUpdateLinked):
            return True

        return self.to_dict() != other.to_dict()
