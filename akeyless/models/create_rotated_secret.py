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


class CreateRotatedSecret(object):
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
        'api_id': 'str',
        'api_key': 'str',
        'auto_rotate': 'str',
        'key': 'str',
        'metadata': 'str',
        'name': 'str',
        'password': 'str',
        'rotation_hour': 'int',
        'rotation_interval': 'str',
        'rotator_creds_type': 'str',
        'rotator_type': 'str',
        'ssh_password': 'str',
        'ssh_username': 'str',
        'tags': 'list[str]',
        'target_name': 'str',
        'token': 'str',
        'uid_token': 'str',
        'username': 'str'
    }

    attribute_map = {
        'api_id': 'api-id',
        'api_key': 'api-key',
        'auto_rotate': 'auto-rotate',
        'key': 'key',
        'metadata': 'metadata',
        'name': 'name',
        'password': 'password',
        'rotation_hour': 'rotation-hour',
        'rotation_interval': 'rotation-interval',
        'rotator_creds_type': 'rotator-creds-type',
        'rotator_type': 'rotator-type',
        'ssh_password': 'ssh-password',
        'ssh_username': 'ssh-username',
        'tags': 'tags',
        'target_name': 'target-name',
        'token': 'token',
        'uid_token': 'uid-token',
        'username': 'username'
    }

    def __init__(self, api_id=None, api_key=None, auto_rotate=None, key=None, metadata=None, name=None, password=None, rotation_hour=None, rotation_interval=None, rotator_creds_type=None, rotator_type=None, ssh_password=None, ssh_username=None, tags=None, target_name=None, token=None, uid_token=None, username=None, local_vars_configuration=None):  # noqa: E501
        """CreateRotatedSecret - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._api_id = None
        self._api_key = None
        self._auto_rotate = None
        self._key = None
        self._metadata = None
        self._name = None
        self._password = None
        self._rotation_hour = None
        self._rotation_interval = None
        self._rotator_creds_type = None
        self._rotator_type = None
        self._ssh_password = None
        self._ssh_username = None
        self._tags = None
        self._target_name = None
        self._token = None
        self._uid_token = None
        self._username = None
        self.discriminator = None

        if api_id is not None:
            self.api_id = api_id
        if api_key is not None:
            self.api_key = api_key
        if auto_rotate is not None:
            self.auto_rotate = auto_rotate
        if key is not None:
            self.key = key
        if metadata is not None:
            self.metadata = metadata
        self.name = name
        if password is not None:
            self.password = password
        if rotation_hour is not None:
            self.rotation_hour = rotation_hour
        if rotation_interval is not None:
            self.rotation_interval = rotation_interval
        if rotator_creds_type is not None:
            self.rotator_creds_type = rotator_creds_type
        if rotator_type is not None:
            self.rotator_type = rotator_type
        if ssh_password is not None:
            self.ssh_password = ssh_password
        if ssh_username is not None:
            self.ssh_username = ssh_username
        if tags is not None:
            self.tags = tags
        if target_name is not None:
            self.target_name = target_name
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if username is not None:
            self.username = username

    @property
    def api_id(self):
        """Gets the api_id of this CreateRotatedSecret.  # noqa: E501


        :return: The api_id of this CreateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this CreateRotatedSecret.


        :param api_id: The api_id of this CreateRotatedSecret.  # noqa: E501
        :type: str
        """

        self._api_id = api_id

    @property
    def api_key(self):
        """Gets the api_key of this CreateRotatedSecret.  # noqa: E501


        :return: The api_key of this CreateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this CreateRotatedSecret.


        :param api_key: The api_key of this CreateRotatedSecret.  # noqa: E501
        :type: str
        """

        self._api_key = api_key

    @property
    def auto_rotate(self):
        """Gets the auto_rotate of this CreateRotatedSecret.  # noqa: E501

        Whether to automatically rotate every --rotation-interval days, or disable existing automatic rotation  # noqa: E501

        :return: The auto_rotate of this CreateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._auto_rotate

    @auto_rotate.setter
    def auto_rotate(self, auto_rotate):
        """Sets the auto_rotate of this CreateRotatedSecret.

        Whether to automatically rotate every --rotation-interval days, or disable existing automatic rotation  # noqa: E501

        :param auto_rotate: The auto_rotate of this CreateRotatedSecret.  # noqa: E501
        :type: str
        """

        self._auto_rotate = auto_rotate

    @property
    def key(self):
        """Gets the key of this CreateRotatedSecret.  # noqa: E501

        The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :return: The key of this CreateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CreateRotatedSecret.

        The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :param key: The key of this CreateRotatedSecret.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def metadata(self):
        """Gets the metadata of this CreateRotatedSecret.  # noqa: E501

        Metadata about the secret  # noqa: E501

        :return: The metadata of this CreateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CreateRotatedSecret.

        Metadata about the secret  # noqa: E501

        :param metadata: The metadata of this CreateRotatedSecret.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this CreateRotatedSecret.  # noqa: E501

        Secret name  # noqa: E501

        :return: The name of this CreateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateRotatedSecret.

        Secret name  # noqa: E501

        :param name: The name of this CreateRotatedSecret.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def password(self):
        """Gets the password of this CreateRotatedSecret.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The password of this CreateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateRotatedSecret.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param password: The password of this CreateRotatedSecret.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def rotation_hour(self):
        """Gets the rotation_hour of this CreateRotatedSecret.  # noqa: E501


        :return: The rotation_hour of this CreateRotatedSecret.  # noqa: E501
        :rtype: int
        """
        return self._rotation_hour

    @rotation_hour.setter
    def rotation_hour(self, rotation_hour):
        """Sets the rotation_hour of this CreateRotatedSecret.


        :param rotation_hour: The rotation_hour of this CreateRotatedSecret.  # noqa: E501
        :type: int
        """

        self._rotation_hour = rotation_hour

    @property
    def rotation_interval(self):
        """Gets the rotation_interval of this CreateRotatedSecret.  # noqa: E501

        The number of days to wait between every automatic key rotation (7-365)  # noqa: E501

        :return: The rotation_interval of this CreateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._rotation_interval

    @rotation_interval.setter
    def rotation_interval(self, rotation_interval):
        """Sets the rotation_interval of this CreateRotatedSecret.

        The number of days to wait between every automatic key rotation (7-365)  # noqa: E501

        :param rotation_interval: The rotation_interval of this CreateRotatedSecret.  # noqa: E501
        :type: str
        """

        self._rotation_interval = rotation_interval

    @property
    def rotator_creds_type(self):
        """Gets the rotator_creds_type of this CreateRotatedSecret.  # noqa: E501


        :return: The rotator_creds_type of this CreateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._rotator_creds_type

    @rotator_creds_type.setter
    def rotator_creds_type(self, rotator_creds_type):
        """Sets the rotator_creds_type of this CreateRotatedSecret.


        :param rotator_creds_type: The rotator_creds_type of this CreateRotatedSecret.  # noqa: E501
        :type: str
        """

        self._rotator_creds_type = rotator_creds_type

    @property
    def rotator_type(self):
        """Gets the rotator_type of this CreateRotatedSecret.  # noqa: E501


        :return: The rotator_type of this CreateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._rotator_type

    @rotator_type.setter
    def rotator_type(self, rotator_type):
        """Sets the rotator_type of this CreateRotatedSecret.


        :param rotator_type: The rotator_type of this CreateRotatedSecret.  # noqa: E501
        :type: str
        """

        self._rotator_type = rotator_type

    @property
    def ssh_password(self):
        """Gets the ssh_password of this CreateRotatedSecret.  # noqa: E501


        :return: The ssh_password of this CreateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._ssh_password

    @ssh_password.setter
    def ssh_password(self, ssh_password):
        """Sets the ssh_password of this CreateRotatedSecret.


        :param ssh_password: The ssh_password of this CreateRotatedSecret.  # noqa: E501
        :type: str
        """

        self._ssh_password = ssh_password

    @property
    def ssh_username(self):
        """Gets the ssh_username of this CreateRotatedSecret.  # noqa: E501


        :return: The ssh_username of this CreateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._ssh_username

    @ssh_username.setter
    def ssh_username(self, ssh_username):
        """Sets the ssh_username of this CreateRotatedSecret.


        :param ssh_username: The ssh_username of this CreateRotatedSecret.  # noqa: E501
        :type: str
        """

        self._ssh_username = ssh_username

    @property
    def tags(self):
        """Gets the tags of this CreateRotatedSecret.  # noqa: E501

        List of the tags attached to this secret  # noqa: E501

        :return: The tags of this CreateRotatedSecret.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateRotatedSecret.

        List of the tags attached to this secret  # noqa: E501

        :param tags: The tags of this CreateRotatedSecret.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def target_name(self):
        """Gets the target_name of this CreateRotatedSecret.  # noqa: E501


        :return: The target_name of this CreateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """Sets the target_name of this CreateRotatedSecret.


        :param target_name: The target_name of this CreateRotatedSecret.  # noqa: E501
        :type: str
        """

        self._target_name = target_name

    @property
    def token(self):
        """Gets the token of this CreateRotatedSecret.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this CreateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this CreateRotatedSecret.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this CreateRotatedSecret.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this CreateRotatedSecret.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this CreateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this CreateRotatedSecret.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this CreateRotatedSecret.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def username(self):
        """Gets the username of this CreateRotatedSecret.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The username of this CreateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this CreateRotatedSecret.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param username: The username of this CreateRotatedSecret.  # noqa: E501
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
        if not isinstance(other, CreateRotatedSecret):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateRotatedSecret):
            return True

        return self.to_dict() != other.to_dict()
