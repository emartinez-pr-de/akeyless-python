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


class RotatedSecretCreateOracledb(object):
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
        'authentication_credentials': 'str',
        'auto_rotate': 'str',
        'delete_protection': 'str',
        'description': 'str',
        'json': 'bool',
        'key': 'str',
        'name': 'str',
        'password_length': 'str',
        'rotate_after_disconnect': 'str',
        'rotated_password': 'str',
        'rotated_username': 'str',
        'rotation_hour': 'int',
        'rotation_interval': 'str',
        'rotator_type': 'str',
        'secure_access_db_name': 'str',
        'secure_access_enable': 'str',
        'secure_access_host': 'list[str]',
        'secure_access_web': 'bool',
        'tags': 'list[str]',
        'target_name': 'str',
        'token': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'authentication_credentials': 'authentication-credentials',
        'auto_rotate': 'auto-rotate',
        'delete_protection': 'delete_protection',
        'description': 'description',
        'json': 'json',
        'key': 'key',
        'name': 'name',
        'password_length': 'password-length',
        'rotate_after_disconnect': 'rotate-after-disconnect',
        'rotated_password': 'rotated-password',
        'rotated_username': 'rotated-username',
        'rotation_hour': 'rotation-hour',
        'rotation_interval': 'rotation-interval',
        'rotator_type': 'rotator-type',
        'secure_access_db_name': 'secure-access-db-name',
        'secure_access_enable': 'secure-access-enable',
        'secure_access_host': 'secure-access-host',
        'secure_access_web': 'secure-access-web',
        'tags': 'tags',
        'target_name': 'target-name',
        'token': 'token',
        'uid_token': 'uid-token'
    }

    def __init__(self, authentication_credentials='use-user-creds', auto_rotate=None, delete_protection=None, description=None, json=False, key=None, name=None, password_length=None, rotate_after_disconnect='false', rotated_password=None, rotated_username=None, rotation_hour=None, rotation_interval=None, rotator_type=None, secure_access_db_name=None, secure_access_enable=None, secure_access_host=None, secure_access_web=False, tags=None, target_name=None, token=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """RotatedSecretCreateOracledb - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._authentication_credentials = None
        self._auto_rotate = None
        self._delete_protection = None
        self._description = None
        self._json = None
        self._key = None
        self._name = None
        self._password_length = None
        self._rotate_after_disconnect = None
        self._rotated_password = None
        self._rotated_username = None
        self._rotation_hour = None
        self._rotation_interval = None
        self._rotator_type = None
        self._secure_access_db_name = None
        self._secure_access_enable = None
        self._secure_access_host = None
        self._secure_access_web = None
        self._tags = None
        self._target_name = None
        self._token = None
        self._uid_token = None
        self.discriminator = None

        if authentication_credentials is not None:
            self.authentication_credentials = authentication_credentials
        if auto_rotate is not None:
            self.auto_rotate = auto_rotate
        if delete_protection is not None:
            self.delete_protection = delete_protection
        if description is not None:
            self.description = description
        if json is not None:
            self.json = json
        if key is not None:
            self.key = key
        self.name = name
        if password_length is not None:
            self.password_length = password_length
        if rotate_after_disconnect is not None:
            self.rotate_after_disconnect = rotate_after_disconnect
        if rotated_password is not None:
            self.rotated_password = rotated_password
        if rotated_username is not None:
            self.rotated_username = rotated_username
        if rotation_hour is not None:
            self.rotation_hour = rotation_hour
        if rotation_interval is not None:
            self.rotation_interval = rotation_interval
        self.rotator_type = rotator_type
        if secure_access_db_name is not None:
            self.secure_access_db_name = secure_access_db_name
        if secure_access_enable is not None:
            self.secure_access_enable = secure_access_enable
        if secure_access_host is not None:
            self.secure_access_host = secure_access_host
        if secure_access_web is not None:
            self.secure_access_web = secure_access_web
        if tags is not None:
            self.tags = tags
        self.target_name = target_name
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def authentication_credentials(self):
        """Gets the authentication_credentials of this RotatedSecretCreateOracledb.  # noqa: E501

        The credentials to connect with use-user-creds/use-target-creds  # noqa: E501

        :return: The authentication_credentials of this RotatedSecretCreateOracledb.  # noqa: E501
        :rtype: str
        """
        return self._authentication_credentials

    @authentication_credentials.setter
    def authentication_credentials(self, authentication_credentials):
        """Sets the authentication_credentials of this RotatedSecretCreateOracledb.

        The credentials to connect with use-user-creds/use-target-creds  # noqa: E501

        :param authentication_credentials: The authentication_credentials of this RotatedSecretCreateOracledb.  # noqa: E501
        :type: str
        """

        self._authentication_credentials = authentication_credentials

    @property
    def auto_rotate(self):
        """Gets the auto_rotate of this RotatedSecretCreateOracledb.  # noqa: E501

        Whether to automatically rotate every --rotation-interval days, or disable existing automatic rotation [true/false]  # noqa: E501

        :return: The auto_rotate of this RotatedSecretCreateOracledb.  # noqa: E501
        :rtype: str
        """
        return self._auto_rotate

    @auto_rotate.setter
    def auto_rotate(self, auto_rotate):
        """Sets the auto_rotate of this RotatedSecretCreateOracledb.

        Whether to automatically rotate every --rotation-interval days, or disable existing automatic rotation [true/false]  # noqa: E501

        :param auto_rotate: The auto_rotate of this RotatedSecretCreateOracledb.  # noqa: E501
        :type: str
        """

        self._auto_rotate = auto_rotate

    @property
    def delete_protection(self):
        """Gets the delete_protection of this RotatedSecretCreateOracledb.  # noqa: E501

        Protection from accidental deletion of this item [true/false]  # noqa: E501

        :return: The delete_protection of this RotatedSecretCreateOracledb.  # noqa: E501
        :rtype: str
        """
        return self._delete_protection

    @delete_protection.setter
    def delete_protection(self, delete_protection):
        """Sets the delete_protection of this RotatedSecretCreateOracledb.

        Protection from accidental deletion of this item [true/false]  # noqa: E501

        :param delete_protection: The delete_protection of this RotatedSecretCreateOracledb.  # noqa: E501
        :type: str
        """

        self._delete_protection = delete_protection

    @property
    def description(self):
        """Gets the description of this RotatedSecretCreateOracledb.  # noqa: E501

        Description of the object  # noqa: E501

        :return: The description of this RotatedSecretCreateOracledb.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RotatedSecretCreateOracledb.

        Description of the object  # noqa: E501

        :param description: The description of this RotatedSecretCreateOracledb.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def json(self):
        """Gets the json of this RotatedSecretCreateOracledb.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this RotatedSecretCreateOracledb.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this RotatedSecretCreateOracledb.

        Set output format to JSON  # noqa: E501

        :param json: The json of this RotatedSecretCreateOracledb.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def key(self):
        """Gets the key of this RotatedSecretCreateOracledb.  # noqa: E501

        The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :return: The key of this RotatedSecretCreateOracledb.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this RotatedSecretCreateOracledb.

        The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :param key: The key of this RotatedSecretCreateOracledb.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this RotatedSecretCreateOracledb.  # noqa: E501

        Rotated secret name  # noqa: E501

        :return: The name of this RotatedSecretCreateOracledb.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RotatedSecretCreateOracledb.

        Rotated secret name  # noqa: E501

        :param name: The name of this RotatedSecretCreateOracledb.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def password_length(self):
        """Gets the password_length of this RotatedSecretCreateOracledb.  # noqa: E501

        The length of the password to be generated  # noqa: E501

        :return: The password_length of this RotatedSecretCreateOracledb.  # noqa: E501
        :rtype: str
        """
        return self._password_length

    @password_length.setter
    def password_length(self, password_length):
        """Sets the password_length of this RotatedSecretCreateOracledb.

        The length of the password to be generated  # noqa: E501

        :param password_length: The password_length of this RotatedSecretCreateOracledb.  # noqa: E501
        :type: str
        """

        self._password_length = password_length

    @property
    def rotate_after_disconnect(self):
        """Gets the rotate_after_disconnect of this RotatedSecretCreateOracledb.  # noqa: E501

        Rotate the value of the secret after SRA session ends [true/false]  # noqa: E501

        :return: The rotate_after_disconnect of this RotatedSecretCreateOracledb.  # noqa: E501
        :rtype: str
        """
        return self._rotate_after_disconnect

    @rotate_after_disconnect.setter
    def rotate_after_disconnect(self, rotate_after_disconnect):
        """Sets the rotate_after_disconnect of this RotatedSecretCreateOracledb.

        Rotate the value of the secret after SRA session ends [true/false]  # noqa: E501

        :param rotate_after_disconnect: The rotate_after_disconnect of this RotatedSecretCreateOracledb.  # noqa: E501
        :type: str
        """

        self._rotate_after_disconnect = rotate_after_disconnect

    @property
    def rotated_password(self):
        """Gets the rotated_password of this RotatedSecretCreateOracledb.  # noqa: E501

        rotated-username password (relevant only for rotator-type=password)  # noqa: E501

        :return: The rotated_password of this RotatedSecretCreateOracledb.  # noqa: E501
        :rtype: str
        """
        return self._rotated_password

    @rotated_password.setter
    def rotated_password(self, rotated_password):
        """Sets the rotated_password of this RotatedSecretCreateOracledb.

        rotated-username password (relevant only for rotator-type=password)  # noqa: E501

        :param rotated_password: The rotated_password of this RotatedSecretCreateOracledb.  # noqa: E501
        :type: str
        """

        self._rotated_password = rotated_password

    @property
    def rotated_username(self):
        """Gets the rotated_username of this RotatedSecretCreateOracledb.  # noqa: E501

        username to be rotated, if selected use-self-creds at rotator-creds-type, this username will try to rotate it's own password, if use-target-creds is selected, target credentials will be use to rotate the rotated-password (relevant only for rotator-type=password)  # noqa: E501

        :return: The rotated_username of this RotatedSecretCreateOracledb.  # noqa: E501
        :rtype: str
        """
        return self._rotated_username

    @rotated_username.setter
    def rotated_username(self, rotated_username):
        """Sets the rotated_username of this RotatedSecretCreateOracledb.

        username to be rotated, if selected use-self-creds at rotator-creds-type, this username will try to rotate it's own password, if use-target-creds is selected, target credentials will be use to rotate the rotated-password (relevant only for rotator-type=password)  # noqa: E501

        :param rotated_username: The rotated_username of this RotatedSecretCreateOracledb.  # noqa: E501
        :type: str
        """

        self._rotated_username = rotated_username

    @property
    def rotation_hour(self):
        """Gets the rotation_hour of this RotatedSecretCreateOracledb.  # noqa: E501

        The Hour of the rotation in UTC  # noqa: E501

        :return: The rotation_hour of this RotatedSecretCreateOracledb.  # noqa: E501
        :rtype: int
        """
        return self._rotation_hour

    @rotation_hour.setter
    def rotation_hour(self, rotation_hour):
        """Sets the rotation_hour of this RotatedSecretCreateOracledb.

        The Hour of the rotation in UTC  # noqa: E501

        :param rotation_hour: The rotation_hour of this RotatedSecretCreateOracledb.  # noqa: E501
        :type: int
        """

        self._rotation_hour = rotation_hour

    @property
    def rotation_interval(self):
        """Gets the rotation_interval of this RotatedSecretCreateOracledb.  # noqa: E501

        The number of days to wait between every automatic key rotation (1-365)  # noqa: E501

        :return: The rotation_interval of this RotatedSecretCreateOracledb.  # noqa: E501
        :rtype: str
        """
        return self._rotation_interval

    @rotation_interval.setter
    def rotation_interval(self, rotation_interval):
        """Sets the rotation_interval of this RotatedSecretCreateOracledb.

        The number of days to wait between every automatic key rotation (1-365)  # noqa: E501

        :param rotation_interval: The rotation_interval of this RotatedSecretCreateOracledb.  # noqa: E501
        :type: str
        """

        self._rotation_interval = rotation_interval

    @property
    def rotator_type(self):
        """Gets the rotator_type of this RotatedSecretCreateOracledb.  # noqa: E501

        The rotator type. options: [target/password]  # noqa: E501

        :return: The rotator_type of this RotatedSecretCreateOracledb.  # noqa: E501
        :rtype: str
        """
        return self._rotator_type

    @rotator_type.setter
    def rotator_type(self, rotator_type):
        """Sets the rotator_type of this RotatedSecretCreateOracledb.

        The rotator type. options: [target/password]  # noqa: E501

        :param rotator_type: The rotator_type of this RotatedSecretCreateOracledb.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and rotator_type is None:  # noqa: E501
            raise ValueError("Invalid value for `rotator_type`, must not be `None`")  # noqa: E501

        self._rotator_type = rotator_type

    @property
    def secure_access_db_name(self):
        """Gets the secure_access_db_name of this RotatedSecretCreateOracledb.  # noqa: E501

        The DB name (relevant only for DB Dynamic-Secret)  # noqa: E501

        :return: The secure_access_db_name of this RotatedSecretCreateOracledb.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_db_name

    @secure_access_db_name.setter
    def secure_access_db_name(self, secure_access_db_name):
        """Sets the secure_access_db_name of this RotatedSecretCreateOracledb.

        The DB name (relevant only for DB Dynamic-Secret)  # noqa: E501

        :param secure_access_db_name: The secure_access_db_name of this RotatedSecretCreateOracledb.  # noqa: E501
        :type: str
        """

        self._secure_access_db_name = secure_access_db_name

    @property
    def secure_access_enable(self):
        """Gets the secure_access_enable of this RotatedSecretCreateOracledb.  # noqa: E501

        Enable/Disable secure remote access [true/false]  # noqa: E501

        :return: The secure_access_enable of this RotatedSecretCreateOracledb.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_enable

    @secure_access_enable.setter
    def secure_access_enable(self, secure_access_enable):
        """Sets the secure_access_enable of this RotatedSecretCreateOracledb.

        Enable/Disable secure remote access [true/false]  # noqa: E501

        :param secure_access_enable: The secure_access_enable of this RotatedSecretCreateOracledb.  # noqa: E501
        :type: str
        """

        self._secure_access_enable = secure_access_enable

    @property
    def secure_access_host(self):
        """Gets the secure_access_host of this RotatedSecretCreateOracledb.  # noqa: E501

        Target servers for connections (In case of Linked Target association, host(s) will inherit Linked Target hosts - Relevant only for Dynamic Secrets/producers)  # noqa: E501

        :return: The secure_access_host of this RotatedSecretCreateOracledb.  # noqa: E501
        :rtype: list[str]
        """
        return self._secure_access_host

    @secure_access_host.setter
    def secure_access_host(self, secure_access_host):
        """Sets the secure_access_host of this RotatedSecretCreateOracledb.

        Target servers for connections (In case of Linked Target association, host(s) will inherit Linked Target hosts - Relevant only for Dynamic Secrets/producers)  # noqa: E501

        :param secure_access_host: The secure_access_host of this RotatedSecretCreateOracledb.  # noqa: E501
        :type: list[str]
        """

        self._secure_access_host = secure_access_host

    @property
    def secure_access_web(self):
        """Gets the secure_access_web of this RotatedSecretCreateOracledb.  # noqa: E501

        Enable Web Secure Remote Access  # noqa: E501

        :return: The secure_access_web of this RotatedSecretCreateOracledb.  # noqa: E501
        :rtype: bool
        """
        return self._secure_access_web

    @secure_access_web.setter
    def secure_access_web(self, secure_access_web):
        """Sets the secure_access_web of this RotatedSecretCreateOracledb.

        Enable Web Secure Remote Access  # noqa: E501

        :param secure_access_web: The secure_access_web of this RotatedSecretCreateOracledb.  # noqa: E501
        :type: bool
        """

        self._secure_access_web = secure_access_web

    @property
    def tags(self):
        """Gets the tags of this RotatedSecretCreateOracledb.  # noqa: E501

        Add tags attached to this object  # noqa: E501

        :return: The tags of this RotatedSecretCreateOracledb.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this RotatedSecretCreateOracledb.

        Add tags attached to this object  # noqa: E501

        :param tags: The tags of this RotatedSecretCreateOracledb.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def target_name(self):
        """Gets the target_name of this RotatedSecretCreateOracledb.  # noqa: E501

        Target name  # noqa: E501

        :return: The target_name of this RotatedSecretCreateOracledb.  # noqa: E501
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """Sets the target_name of this RotatedSecretCreateOracledb.

        Target name  # noqa: E501

        :param target_name: The target_name of this RotatedSecretCreateOracledb.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and target_name is None:  # noqa: E501
            raise ValueError("Invalid value for `target_name`, must not be `None`")  # noqa: E501

        self._target_name = target_name

    @property
    def token(self):
        """Gets the token of this RotatedSecretCreateOracledb.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this RotatedSecretCreateOracledb.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this RotatedSecretCreateOracledb.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this RotatedSecretCreateOracledb.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this RotatedSecretCreateOracledb.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this RotatedSecretCreateOracledb.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this RotatedSecretCreateOracledb.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this RotatedSecretCreateOracledb.  # noqa: E501
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
        if not isinstance(other, RotatedSecretCreateOracledb):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RotatedSecretCreateOracledb):
            return True

        return self.to_dict() != other.to_dict()
