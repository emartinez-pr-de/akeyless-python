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


class CreateWindowsTarget(object):
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
        'certificate': 'str',
        'description': 'str',
        'hostname': 'str',
        'json': 'bool',
        'key': 'str',
        'name': 'str',
        'password': 'str',
        'port': 'str',
        'token': 'str',
        'uid_token': 'str',
        'use_tls': 'str',
        'username': 'str'
    }

    attribute_map = {
        'certificate': 'certificate',
        'description': 'description',
        'hostname': 'hostname',
        'json': 'json',
        'key': 'key',
        'name': 'name',
        'password': 'password',
        'port': 'port',
        'token': 'token',
        'uid_token': 'uid-token',
        'use_tls': 'use-tls',
        'username': 'username'
    }

    def __init__(self, certificate=None, description=None, hostname=None, json=False, key=None, name=None, password=None, port='5986', token=None, uid_token=None, use_tls='true', username=None, local_vars_configuration=None):  # noqa: E501
        """CreateWindowsTarget - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._certificate = None
        self._description = None
        self._hostname = None
        self._json = None
        self._key = None
        self._name = None
        self._password = None
        self._port = None
        self._token = None
        self._uid_token = None
        self._use_tls = None
        self._username = None
        self.discriminator = None

        if certificate is not None:
            self.certificate = certificate
        if description is not None:
            self.description = description
        self.hostname = hostname
        if json is not None:
            self.json = json
        if key is not None:
            self.key = key
        self.name = name
        self.password = password
        if port is not None:
            self.port = port
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if use_tls is not None:
            self.use_tls = use_tls
        self.username = username

    @property
    def certificate(self):
        """Gets the certificate of this CreateWindowsTarget.  # noqa: E501

        SSL CA certificate in base64 encoding generated from a trusted Certificate Authority (CA)  # noqa: E501

        :return: The certificate of this CreateWindowsTarget.  # noqa: E501
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this CreateWindowsTarget.

        SSL CA certificate in base64 encoding generated from a trusted Certificate Authority (CA)  # noqa: E501

        :param certificate: The certificate of this CreateWindowsTarget.  # noqa: E501
        :type: str
        """

        self._certificate = certificate

    @property
    def description(self):
        """Gets the description of this CreateWindowsTarget.  # noqa: E501

        Description of the object  # noqa: E501

        :return: The description of this CreateWindowsTarget.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateWindowsTarget.

        Description of the object  # noqa: E501

        :param description: The description of this CreateWindowsTarget.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def hostname(self):
        """Gets the hostname of this CreateWindowsTarget.  # noqa: E501

        Server hostname  # noqa: E501

        :return: The hostname of this CreateWindowsTarget.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this CreateWindowsTarget.

        Server hostname  # noqa: E501

        :param hostname: The hostname of this CreateWindowsTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and hostname is None:  # noqa: E501
            raise ValueError("Invalid value for `hostname`, must not be `None`")  # noqa: E501

        self._hostname = hostname

    @property
    def json(self):
        """Gets the json of this CreateWindowsTarget.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this CreateWindowsTarget.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this CreateWindowsTarget.

        Set output format to JSON  # noqa: E501

        :param json: The json of this CreateWindowsTarget.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def key(self):
        """Gets the key of this CreateWindowsTarget.  # noqa: E501

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :return: The key of this CreateWindowsTarget.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CreateWindowsTarget.

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :param key: The key of this CreateWindowsTarget.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this CreateWindowsTarget.  # noqa: E501

        Target name  # noqa: E501

        :return: The name of this CreateWindowsTarget.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateWindowsTarget.

        Target name  # noqa: E501

        :param name: The name of this CreateWindowsTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def password(self):
        """Gets the password of this CreateWindowsTarget.  # noqa: E501

        Privileged user password  # noqa: E501

        :return: The password of this CreateWindowsTarget.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateWindowsTarget.

        Privileged user password  # noqa: E501

        :param password: The password of this CreateWindowsTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and password is None:  # noqa: E501
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def port(self):
        """Gets the port of this CreateWindowsTarget.  # noqa: E501

        Server WinRM port  # noqa: E501

        :return: The port of this CreateWindowsTarget.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this CreateWindowsTarget.

        Server WinRM port  # noqa: E501

        :param port: The port of this CreateWindowsTarget.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def token(self):
        """Gets the token of this CreateWindowsTarget.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this CreateWindowsTarget.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this CreateWindowsTarget.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this CreateWindowsTarget.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this CreateWindowsTarget.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this CreateWindowsTarget.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this CreateWindowsTarget.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this CreateWindowsTarget.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def use_tls(self):
        """Gets the use_tls of this CreateWindowsTarget.  # noqa: E501

        Enable/Disable TLS for WinRM over HTTPS [true/false]  # noqa: E501

        :return: The use_tls of this CreateWindowsTarget.  # noqa: E501
        :rtype: str
        """
        return self._use_tls

    @use_tls.setter
    def use_tls(self, use_tls):
        """Sets the use_tls of this CreateWindowsTarget.

        Enable/Disable TLS for WinRM over HTTPS [true/false]  # noqa: E501

        :param use_tls: The use_tls of this CreateWindowsTarget.  # noqa: E501
        :type: str
        """

        self._use_tls = use_tls

    @property
    def username(self):
        """Gets the username of this CreateWindowsTarget.  # noqa: E501

        Privileged username  # noqa: E501

        :return: The username of this CreateWindowsTarget.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this CreateWindowsTarget.

        Privileged username  # noqa: E501

        :param username: The username of this CreateWindowsTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and username is None:  # noqa: E501
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, CreateWindowsTarget):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateWindowsTarget):
            return True

        return self.to_dict() != other.to_dict()
