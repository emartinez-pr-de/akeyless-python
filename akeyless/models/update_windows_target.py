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


class UpdateWindowsTarget(object):
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
        'description': 'str',
        'hostname': 'str',
        'json': 'bool',
        'keep_prev_version': 'str',
        'key': 'str',
        'name': 'str',
        'new_name': 'str',
        'password': 'str',
        'port': 'str',
        'token': 'str',
        'uid_token': 'str',
        'update_version': 'bool',
        'username': 'str'
    }

    attribute_map = {
        'description': 'description',
        'hostname': 'hostname',
        'json': 'json',
        'keep_prev_version': 'keep-prev-version',
        'key': 'key',
        'name': 'name',
        'new_name': 'new-name',
        'password': 'password',
        'port': 'port',
        'token': 'token',
        'uid_token': 'uid-token',
        'update_version': 'update-version',
        'username': 'username'
    }

    def __init__(self, description=None, hostname=None, json=False, keep_prev_version=None, key=None, name=None, new_name=None, password=None, port='5986', token=None, uid_token=None, update_version=None, username=None, local_vars_configuration=None):  # noqa: E501
        """UpdateWindowsTarget - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._hostname = None
        self._json = None
        self._keep_prev_version = None
        self._key = None
        self._name = None
        self._new_name = None
        self._password = None
        self._port = None
        self._token = None
        self._uid_token = None
        self._update_version = None
        self._username = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if hostname is not None:
            self.hostname = hostname
        if json is not None:
            self.json = json
        if keep_prev_version is not None:
            self.keep_prev_version = keep_prev_version
        if key is not None:
            self.key = key
        self.name = name
        if new_name is not None:
            self.new_name = new_name
        if password is not None:
            self.password = password
        if port is not None:
            self.port = port
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if update_version is not None:
            self.update_version = update_version
        if username is not None:
            self.username = username

    @property
    def description(self):
        """Gets the description of this UpdateWindowsTarget.  # noqa: E501

        Description of the object  # noqa: E501

        :return: The description of this UpdateWindowsTarget.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateWindowsTarget.

        Description of the object  # noqa: E501

        :param description: The description of this UpdateWindowsTarget.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def hostname(self):
        """Gets the hostname of this UpdateWindowsTarget.  # noqa: E501

        Server hostname  # noqa: E501

        :return: The hostname of this UpdateWindowsTarget.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this UpdateWindowsTarget.

        Server hostname  # noqa: E501

        :param hostname: The hostname of this UpdateWindowsTarget.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def json(self):
        """Gets the json of this UpdateWindowsTarget.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this UpdateWindowsTarget.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this UpdateWindowsTarget.

        Set output format to JSON  # noqa: E501

        :param json: The json of this UpdateWindowsTarget.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def keep_prev_version(self):
        """Gets the keep_prev_version of this UpdateWindowsTarget.  # noqa: E501

        Whether to keep previous version [true/false]. If not set, use default according to account settings  # noqa: E501

        :return: The keep_prev_version of this UpdateWindowsTarget.  # noqa: E501
        :rtype: str
        """
        return self._keep_prev_version

    @keep_prev_version.setter
    def keep_prev_version(self, keep_prev_version):
        """Sets the keep_prev_version of this UpdateWindowsTarget.

        Whether to keep previous version [true/false]. If not set, use default according to account settings  # noqa: E501

        :param keep_prev_version: The keep_prev_version of this UpdateWindowsTarget.  # noqa: E501
        :type: str
        """

        self._keep_prev_version = keep_prev_version

    @property
    def key(self):
        """Gets the key of this UpdateWindowsTarget.  # noqa: E501

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :return: The key of this UpdateWindowsTarget.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this UpdateWindowsTarget.

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :param key: The key of this UpdateWindowsTarget.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this UpdateWindowsTarget.  # noqa: E501

        Target name  # noqa: E501

        :return: The name of this UpdateWindowsTarget.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateWindowsTarget.

        Target name  # noqa: E501

        :param name: The name of this UpdateWindowsTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def new_name(self):
        """Gets the new_name of this UpdateWindowsTarget.  # noqa: E501

        New target name  # noqa: E501

        :return: The new_name of this UpdateWindowsTarget.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this UpdateWindowsTarget.

        New target name  # noqa: E501

        :param new_name: The new_name of this UpdateWindowsTarget.  # noqa: E501
        :type: str
        """

        self._new_name = new_name

    @property
    def password(self):
        """Gets the password of this UpdateWindowsTarget.  # noqa: E501

        The privileged user password  # noqa: E501

        :return: The password of this UpdateWindowsTarget.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UpdateWindowsTarget.

        The privileged user password  # noqa: E501

        :param password: The password of this UpdateWindowsTarget.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def port(self):
        """Gets the port of this UpdateWindowsTarget.  # noqa: E501

        Server WinRM HTTPS port  # noqa: E501

        :return: The port of this UpdateWindowsTarget.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this UpdateWindowsTarget.

        Server WinRM HTTPS port  # noqa: E501

        :param port: The port of this UpdateWindowsTarget.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def token(self):
        """Gets the token of this UpdateWindowsTarget.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this UpdateWindowsTarget.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this UpdateWindowsTarget.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this UpdateWindowsTarget.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this UpdateWindowsTarget.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this UpdateWindowsTarget.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this UpdateWindowsTarget.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this UpdateWindowsTarget.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def update_version(self):
        """Gets the update_version of this UpdateWindowsTarget.  # noqa: E501

        Deprecated  # noqa: E501

        :return: The update_version of this UpdateWindowsTarget.  # noqa: E501
        :rtype: bool
        """
        return self._update_version

    @update_version.setter
    def update_version(self, update_version):
        """Sets the update_version of this UpdateWindowsTarget.

        Deprecated  # noqa: E501

        :param update_version: The update_version of this UpdateWindowsTarget.  # noqa: E501
        :type: bool
        """

        self._update_version = update_version

    @property
    def username(self):
        """Gets the username of this UpdateWindowsTarget.  # noqa: E501

        Privileged username  # noqa: E501

        :return: The username of this UpdateWindowsTarget.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UpdateWindowsTarget.

        Privileged username  # noqa: E501

        :param username: The username of this UpdateWindowsTarget.  # noqa: E501
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
        if not isinstance(other, UpdateWindowsTarget):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateWindowsTarget):
            return True

        return self.to_dict() != other.to_dict()
