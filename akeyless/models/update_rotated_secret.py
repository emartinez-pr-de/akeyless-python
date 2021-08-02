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


class UpdateRotatedSecret(object):
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
        'add_tag': 'list[str]',
        'api_id': 'str',
        'api_key': 'str',
        'auto_rotate': 'str',
        'key': 'str',
        'name': 'str',
        'new_metadata': 'str',
        'new_name': 'str',
        'new_version': 'bool',
        'password': 'str',
        'rm_tag': 'list[str]',
        'rotated_password': 'str',
        'rotated_username': 'str',
        'rotation_hour': 'int',
        'rotation_interval': 'str',
        'rotator_creds_type': 'str',
        'ssh_password': 'str',
        'ssh_username': 'str',
        'token': 'str',
        'uid_token': 'str',
        'username': 'str'
    }

    attribute_map = {
        'add_tag': 'add-tag',
        'api_id': 'api-id',
        'api_key': 'api-key',
        'auto_rotate': 'auto-rotate',
        'key': 'key',
        'name': 'name',
        'new_metadata': 'new-metadata',
        'new_name': 'new-name',
        'new_version': 'new-version',
        'password': 'password',
        'rm_tag': 'rm-tag',
        'rotated_password': 'rotated-password',
        'rotated_username': 'rotated-username',
        'rotation_hour': 'rotation-hour',
        'rotation_interval': 'rotation-interval',
        'rotator_creds_type': 'rotator-creds-type',
        'ssh_password': 'ssh-password',
        'ssh_username': 'ssh-username',
        'token': 'token',
        'uid_token': 'uid-token',
        'username': 'username'
    }

    def __init__(self, add_tag=None, api_id=None, api_key=None, auto_rotate=None, key=None, name=None, new_metadata='default_metadata', new_name=None, new_version=False, password=None, rm_tag=None, rotated_password=None, rotated_username=None, rotation_hour=None, rotation_interval=None, rotator_creds_type=None, ssh_password=None, ssh_username=None, token=None, uid_token=None, username=None, local_vars_configuration=None):  # noqa: E501
        """UpdateRotatedSecret - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._add_tag = None
        self._api_id = None
        self._api_key = None
        self._auto_rotate = None
        self._key = None
        self._name = None
        self._new_metadata = None
        self._new_name = None
        self._new_version = None
        self._password = None
        self._rm_tag = None
        self._rotated_password = None
        self._rotated_username = None
        self._rotation_hour = None
        self._rotation_interval = None
        self._rotator_creds_type = None
        self._ssh_password = None
        self._ssh_username = None
        self._token = None
        self._uid_token = None
        self._username = None
        self.discriminator = None

        if add_tag is not None:
            self.add_tag = add_tag
        if api_id is not None:
            self.api_id = api_id
        if api_key is not None:
            self.api_key = api_key
        if auto_rotate is not None:
            self.auto_rotate = auto_rotate
        if key is not None:
            self.key = key
        self.name = name
        if new_metadata is not None:
            self.new_metadata = new_metadata
        if new_name is not None:
            self.new_name = new_name
        if new_version is not None:
            self.new_version = new_version
        if password is not None:
            self.password = password
        if rm_tag is not None:
            self.rm_tag = rm_tag
        if rotated_password is not None:
            self.rotated_password = rotated_password
        if rotated_username is not None:
            self.rotated_username = rotated_username
        if rotation_hour is not None:
            self.rotation_hour = rotation_hour
        if rotation_interval is not None:
            self.rotation_interval = rotation_interval
        if rotator_creds_type is not None:
            self.rotator_creds_type = rotator_creds_type
        if ssh_password is not None:
            self.ssh_password = ssh_password
        if ssh_username is not None:
            self.ssh_username = ssh_username
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if username is not None:
            self.username = username

    @property
    def add_tag(self):
        """Gets the add_tag of this UpdateRotatedSecret.  # noqa: E501

        List of the new tags that will be attached to this item  # noqa: E501

        :return: The add_tag of this UpdateRotatedSecret.  # noqa: E501
        :rtype: list[str]
        """
        return self._add_tag

    @add_tag.setter
    def add_tag(self, add_tag):
        """Sets the add_tag of this UpdateRotatedSecret.

        List of the new tags that will be attached to this item  # noqa: E501

        :param add_tag: The add_tag of this UpdateRotatedSecret.  # noqa: E501
        :type: list[str]
        """

        self._add_tag = add_tag

    @property
    def api_id(self):
        """Gets the api_id of this UpdateRotatedSecret.  # noqa: E501


        :return: The api_id of this UpdateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this UpdateRotatedSecret.


        :param api_id: The api_id of this UpdateRotatedSecret.  # noqa: E501
        :type: str
        """

        self._api_id = api_id

    @property
    def api_key(self):
        """Gets the api_key of this UpdateRotatedSecret.  # noqa: E501


        :return: The api_key of this UpdateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this UpdateRotatedSecret.


        :param api_key: The api_key of this UpdateRotatedSecret.  # noqa: E501
        :type: str
        """

        self._api_key = api_key

    @property
    def auto_rotate(self):
        """Gets the auto_rotate of this UpdateRotatedSecret.  # noqa: E501

        Whether to automatically rotate every --rotation-interval days, or disable existing automatic rotation  # noqa: E501

        :return: The auto_rotate of this UpdateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._auto_rotate

    @auto_rotate.setter
    def auto_rotate(self, auto_rotate):
        """Sets the auto_rotate of this UpdateRotatedSecret.

        Whether to automatically rotate every --rotation-interval days, or disable existing automatic rotation  # noqa: E501

        :param auto_rotate: The auto_rotate of this UpdateRotatedSecret.  # noqa: E501
        :type: str
        """

        self._auto_rotate = auto_rotate

    @property
    def key(self):
        """Gets the key of this UpdateRotatedSecret.  # noqa: E501

        The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :return: The key of this UpdateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this UpdateRotatedSecret.

        The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :param key: The key of this UpdateRotatedSecret.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this UpdateRotatedSecret.  # noqa: E501

        Secret name  # noqa: E501

        :return: The name of this UpdateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateRotatedSecret.

        Secret name  # noqa: E501

        :param name: The name of this UpdateRotatedSecret.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def new_metadata(self):
        """Gets the new_metadata of this UpdateRotatedSecret.  # noqa: E501

        New item metadata  # noqa: E501

        :return: The new_metadata of this UpdateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._new_metadata

    @new_metadata.setter
    def new_metadata(self, new_metadata):
        """Sets the new_metadata of this UpdateRotatedSecret.

        New item metadata  # noqa: E501

        :param new_metadata: The new_metadata of this UpdateRotatedSecret.  # noqa: E501
        :type: str
        """

        self._new_metadata = new_metadata

    @property
    def new_name(self):
        """Gets the new_name of this UpdateRotatedSecret.  # noqa: E501

        New item name  # noqa: E501

        :return: The new_name of this UpdateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this UpdateRotatedSecret.

        New item name  # noqa: E501

        :param new_name: The new_name of this UpdateRotatedSecret.  # noqa: E501
        :type: str
        """

        self._new_name = new_name

    @property
    def new_version(self):
        """Gets the new_version of this UpdateRotatedSecret.  # noqa: E501

        Whether to create a new version of not  # noqa: E501

        :return: The new_version of this UpdateRotatedSecret.  # noqa: E501
        :rtype: bool
        """
        return self._new_version

    @new_version.setter
    def new_version(self, new_version):
        """Sets the new_version of this UpdateRotatedSecret.

        Whether to create a new version of not  # noqa: E501

        :param new_version: The new_version of this UpdateRotatedSecret.  # noqa: E501
        :type: bool
        """

        self._new_version = new_version

    @property
    def password(self):
        """Gets the password of this UpdateRotatedSecret.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The password of this UpdateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UpdateRotatedSecret.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param password: The password of this UpdateRotatedSecret.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def rm_tag(self):
        """Gets the rm_tag of this UpdateRotatedSecret.  # noqa: E501

        List of the existent tags that will be removed from this item  # noqa: E501

        :return: The rm_tag of this UpdateRotatedSecret.  # noqa: E501
        :rtype: list[str]
        """
        return self._rm_tag

    @rm_tag.setter
    def rm_tag(self, rm_tag):
        """Sets the rm_tag of this UpdateRotatedSecret.

        List of the existent tags that will be removed from this item  # noqa: E501

        :param rm_tag: The rm_tag of this UpdateRotatedSecret.  # noqa: E501
        :type: list[str]
        """

        self._rm_tag = rm_tag

    @property
    def rotated_password(self):
        """Gets the rotated_password of this UpdateRotatedSecret.  # noqa: E501


        :return: The rotated_password of this UpdateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._rotated_password

    @rotated_password.setter
    def rotated_password(self, rotated_password):
        """Sets the rotated_password of this UpdateRotatedSecret.


        :param rotated_password: The rotated_password of this UpdateRotatedSecret.  # noqa: E501
        :type: str
        """

        self._rotated_password = rotated_password

    @property
    def rotated_username(self):
        """Gets the rotated_username of this UpdateRotatedSecret.  # noqa: E501


        :return: The rotated_username of this UpdateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._rotated_username

    @rotated_username.setter
    def rotated_username(self, rotated_username):
        """Sets the rotated_username of this UpdateRotatedSecret.


        :param rotated_username: The rotated_username of this UpdateRotatedSecret.  # noqa: E501
        :type: str
        """

        self._rotated_username = rotated_username

    @property
    def rotation_hour(self):
        """Gets the rotation_hour of this UpdateRotatedSecret.  # noqa: E501


        :return: The rotation_hour of this UpdateRotatedSecret.  # noqa: E501
        :rtype: int
        """
        return self._rotation_hour

    @rotation_hour.setter
    def rotation_hour(self, rotation_hour):
        """Sets the rotation_hour of this UpdateRotatedSecret.


        :param rotation_hour: The rotation_hour of this UpdateRotatedSecret.  # noqa: E501
        :type: int
        """

        self._rotation_hour = rotation_hour

    @property
    def rotation_interval(self):
        """Gets the rotation_interval of this UpdateRotatedSecret.  # noqa: E501

        The number of days to wait between every automatic key rotation (7-365)  # noqa: E501

        :return: The rotation_interval of this UpdateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._rotation_interval

    @rotation_interval.setter
    def rotation_interval(self, rotation_interval):
        """Sets the rotation_interval of this UpdateRotatedSecret.

        The number of days to wait between every automatic key rotation (7-365)  # noqa: E501

        :param rotation_interval: The rotation_interval of this UpdateRotatedSecret.  # noqa: E501
        :type: str
        """

        self._rotation_interval = rotation_interval

    @property
    def rotator_creds_type(self):
        """Gets the rotator_creds_type of this UpdateRotatedSecret.  # noqa: E501


        :return: The rotator_creds_type of this UpdateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._rotator_creds_type

    @rotator_creds_type.setter
    def rotator_creds_type(self, rotator_creds_type):
        """Sets the rotator_creds_type of this UpdateRotatedSecret.


        :param rotator_creds_type: The rotator_creds_type of this UpdateRotatedSecret.  # noqa: E501
        :type: str
        """

        self._rotator_creds_type = rotator_creds_type

    @property
    def ssh_password(self):
        """Gets the ssh_password of this UpdateRotatedSecret.  # noqa: E501

        Deprecated: use RotatedPassword  # noqa: E501

        :return: The ssh_password of this UpdateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._ssh_password

    @ssh_password.setter
    def ssh_password(self, ssh_password):
        """Sets the ssh_password of this UpdateRotatedSecret.

        Deprecated: use RotatedPassword  # noqa: E501

        :param ssh_password: The ssh_password of this UpdateRotatedSecret.  # noqa: E501
        :type: str
        """

        self._ssh_password = ssh_password

    @property
    def ssh_username(self):
        """Gets the ssh_username of this UpdateRotatedSecret.  # noqa: E501

        Deprecated: use RotatedUser  # noqa: E501

        :return: The ssh_username of this UpdateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._ssh_username

    @ssh_username.setter
    def ssh_username(self, ssh_username):
        """Sets the ssh_username of this UpdateRotatedSecret.

        Deprecated: use RotatedUser  # noqa: E501

        :param ssh_username: The ssh_username of this UpdateRotatedSecret.  # noqa: E501
        :type: str
        """

        self._ssh_username = ssh_username

    @property
    def token(self):
        """Gets the token of this UpdateRotatedSecret.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this UpdateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this UpdateRotatedSecret.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this UpdateRotatedSecret.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this UpdateRotatedSecret.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this UpdateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this UpdateRotatedSecret.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this UpdateRotatedSecret.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def username(self):
        """Gets the username of this UpdateRotatedSecret.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The username of this UpdateRotatedSecret.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UpdateRotatedSecret.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param username: The username of this UpdateRotatedSecret.  # noqa: E501
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
        if not isinstance(other, UpdateRotatedSecret):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateRotatedSecret):
            return True

        return self.to_dict() != other.to_dict()
