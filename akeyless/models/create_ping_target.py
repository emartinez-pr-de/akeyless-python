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


class CreatePingTarget(object):
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
        'administrative_port': 'str',
        'authorization_port': 'str',
        'comment': 'str',
        'description': 'str',
        'json': 'bool',
        'key': 'str',
        'max_versions': 'str',
        'name': 'str',
        'password': 'str',
        'ping_url': 'str',
        'privileged_user': 'str',
        'token': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'administrative_port': 'administrative-port',
        'authorization_port': 'authorization-port',
        'comment': 'comment',
        'description': 'description',
        'json': 'json',
        'key': 'key',
        'max_versions': 'max-versions',
        'name': 'name',
        'password': 'password',
        'ping_url': 'ping-url',
        'privileged_user': 'privileged-user',
        'token': 'token',
        'uid_token': 'uid-token'
    }

    def __init__(self, administrative_port='9999', authorization_port='9031', comment=None, description=None, json=False, key=None, max_versions=None, name=None, password=None, ping_url=None, privileged_user=None, token=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """CreatePingTarget - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._administrative_port = None
        self._authorization_port = None
        self._comment = None
        self._description = None
        self._json = None
        self._key = None
        self._max_versions = None
        self._name = None
        self._password = None
        self._ping_url = None
        self._privileged_user = None
        self._token = None
        self._uid_token = None
        self.discriminator = None

        if administrative_port is not None:
            self.administrative_port = administrative_port
        if authorization_port is not None:
            self.authorization_port = authorization_port
        if comment is not None:
            self.comment = comment
        if description is not None:
            self.description = description
        if json is not None:
            self.json = json
        if key is not None:
            self.key = key
        if max_versions is not None:
            self.max_versions = max_versions
        self.name = name
        if password is not None:
            self.password = password
        if ping_url is not None:
            self.ping_url = ping_url
        if privileged_user is not None:
            self.privileged_user = privileged_user
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def administrative_port(self):
        """Gets the administrative_port of this CreatePingTarget.  # noqa: E501

        Ping Federate administrative port  # noqa: E501

        :return: The administrative_port of this CreatePingTarget.  # noqa: E501
        :rtype: str
        """
        return self._administrative_port

    @administrative_port.setter
    def administrative_port(self, administrative_port):
        """Sets the administrative_port of this CreatePingTarget.

        Ping Federate administrative port  # noqa: E501

        :param administrative_port: The administrative_port of this CreatePingTarget.  # noqa: E501
        :type: str
        """

        self._administrative_port = administrative_port

    @property
    def authorization_port(self):
        """Gets the authorization_port of this CreatePingTarget.  # noqa: E501

        Ping Federate authorization port  # noqa: E501

        :return: The authorization_port of this CreatePingTarget.  # noqa: E501
        :rtype: str
        """
        return self._authorization_port

    @authorization_port.setter
    def authorization_port(self, authorization_port):
        """Sets the authorization_port of this CreatePingTarget.

        Ping Federate authorization port  # noqa: E501

        :param authorization_port: The authorization_port of this CreatePingTarget.  # noqa: E501
        :type: str
        """

        self._authorization_port = authorization_port

    @property
    def comment(self):
        """Gets the comment of this CreatePingTarget.  # noqa: E501

        Deprecated - use description  # noqa: E501

        :return: The comment of this CreatePingTarget.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this CreatePingTarget.

        Deprecated - use description  # noqa: E501

        :param comment: The comment of this CreatePingTarget.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def description(self):
        """Gets the description of this CreatePingTarget.  # noqa: E501

        Description of the object  # noqa: E501

        :return: The description of this CreatePingTarget.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreatePingTarget.

        Description of the object  # noqa: E501

        :param description: The description of this CreatePingTarget.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def json(self):
        """Gets the json of this CreatePingTarget.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this CreatePingTarget.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this CreatePingTarget.

        Set output format to JSON  # noqa: E501

        :param json: The json of this CreatePingTarget.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def key(self):
        """Gets the key of this CreatePingTarget.  # noqa: E501

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :return: The key of this CreatePingTarget.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CreatePingTarget.

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :param key: The key of this CreatePingTarget.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def max_versions(self):
        """Gets the max_versions of this CreatePingTarget.  # noqa: E501

        Set the maximum number of versions, limited by the account settings defaults.  # noqa: E501

        :return: The max_versions of this CreatePingTarget.  # noqa: E501
        :rtype: str
        """
        return self._max_versions

    @max_versions.setter
    def max_versions(self, max_versions):
        """Sets the max_versions of this CreatePingTarget.

        Set the maximum number of versions, limited by the account settings defaults.  # noqa: E501

        :param max_versions: The max_versions of this CreatePingTarget.  # noqa: E501
        :type: str
        """

        self._max_versions = max_versions

    @property
    def name(self):
        """Gets the name of this CreatePingTarget.  # noqa: E501

        Target name  # noqa: E501

        :return: The name of this CreatePingTarget.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreatePingTarget.

        Target name  # noqa: E501

        :param name: The name of this CreatePingTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def password(self):
        """Gets the password of this CreatePingTarget.  # noqa: E501

        Ping Federate privileged user password  # noqa: E501

        :return: The password of this CreatePingTarget.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreatePingTarget.

        Ping Federate privileged user password  # noqa: E501

        :param password: The password of this CreatePingTarget.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def ping_url(self):
        """Gets the ping_url of this CreatePingTarget.  # noqa: E501

        Ping URL  # noqa: E501

        :return: The ping_url of this CreatePingTarget.  # noqa: E501
        :rtype: str
        """
        return self._ping_url

    @ping_url.setter
    def ping_url(self, ping_url):
        """Sets the ping_url of this CreatePingTarget.

        Ping URL  # noqa: E501

        :param ping_url: The ping_url of this CreatePingTarget.  # noqa: E501
        :type: str
        """

        self._ping_url = ping_url

    @property
    def privileged_user(self):
        """Gets the privileged_user of this CreatePingTarget.  # noqa: E501

        Ping Federate privileged user  # noqa: E501

        :return: The privileged_user of this CreatePingTarget.  # noqa: E501
        :rtype: str
        """
        return self._privileged_user

    @privileged_user.setter
    def privileged_user(self, privileged_user):
        """Sets the privileged_user of this CreatePingTarget.

        Ping Federate privileged user  # noqa: E501

        :param privileged_user: The privileged_user of this CreatePingTarget.  # noqa: E501
        :type: str
        """

        self._privileged_user = privileged_user

    @property
    def token(self):
        """Gets the token of this CreatePingTarget.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this CreatePingTarget.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this CreatePingTarget.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this CreatePingTarget.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this CreatePingTarget.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this CreatePingTarget.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this CreatePingTarget.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this CreatePingTarget.  # noqa: E501
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
        if not isinstance(other, CreatePingTarget):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreatePingTarget):
            return True

        return self.to_dict() != other.to_dict()
