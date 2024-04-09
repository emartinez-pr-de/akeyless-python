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


class RotatedSecretUpdateGcp(object):
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
        'authentication_credentials': 'str',
        'auto_rotate': 'str',
        'delete_protection': 'str',
        'description': 'str',
        'gcp_key': 'str',
        'gcp_service_account_email': 'str',
        'gcp_service_account_key_id': 'str',
        'json': 'bool',
        'keep_prev_version': 'str',
        'key': 'str',
        'max_versions': 'str',
        'name': 'str',
        'new_name': 'str',
        'password_length': 'str',
        'rm_tag': 'list[str]',
        'rotation_hour': 'int',
        'rotation_interval': 'str',
        'rotator_type': 'str',
        'token': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'add_tag': 'add-tag',
        'authentication_credentials': 'authentication-credentials',
        'auto_rotate': 'auto-rotate',
        'delete_protection': 'delete_protection',
        'description': 'description',
        'gcp_key': 'gcp-key',
        'gcp_service_account_email': 'gcp-service-account-email',
        'gcp_service_account_key_id': 'gcp-service-account-key-id',
        'json': 'json',
        'keep_prev_version': 'keep-prev-version',
        'key': 'key',
        'max_versions': 'max-versions',
        'name': 'name',
        'new_name': 'new-name',
        'password_length': 'password-length',
        'rm_tag': 'rm-tag',
        'rotation_hour': 'rotation-hour',
        'rotation_interval': 'rotation-interval',
        'rotator_type': 'rotator-type',
        'token': 'token',
        'uid_token': 'uid-token'
    }

    def __init__(self, add_tag=None, authentication_credentials='use-user-creds', auto_rotate=None, delete_protection=None, description='default_metadata', gcp_key=None, gcp_service_account_email=None, gcp_service_account_key_id=None, json=False, keep_prev_version=None, key=None, max_versions=None, name=None, new_name=None, password_length=None, rm_tag=None, rotation_hour=None, rotation_interval=None, rotator_type=None, token=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """RotatedSecretUpdateGcp - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._add_tag = None
        self._authentication_credentials = None
        self._auto_rotate = None
        self._delete_protection = None
        self._description = None
        self._gcp_key = None
        self._gcp_service_account_email = None
        self._gcp_service_account_key_id = None
        self._json = None
        self._keep_prev_version = None
        self._key = None
        self._max_versions = None
        self._name = None
        self._new_name = None
        self._password_length = None
        self._rm_tag = None
        self._rotation_hour = None
        self._rotation_interval = None
        self._rotator_type = None
        self._token = None
        self._uid_token = None
        self.discriminator = None

        if add_tag is not None:
            self.add_tag = add_tag
        if authentication_credentials is not None:
            self.authentication_credentials = authentication_credentials
        if auto_rotate is not None:
            self.auto_rotate = auto_rotate
        if delete_protection is not None:
            self.delete_protection = delete_protection
        if description is not None:
            self.description = description
        if gcp_key is not None:
            self.gcp_key = gcp_key
        if gcp_service_account_email is not None:
            self.gcp_service_account_email = gcp_service_account_email
        if gcp_service_account_key_id is not None:
            self.gcp_service_account_key_id = gcp_service_account_key_id
        if json is not None:
            self.json = json
        if keep_prev_version is not None:
            self.keep_prev_version = keep_prev_version
        if key is not None:
            self.key = key
        if max_versions is not None:
            self.max_versions = max_versions
        self.name = name
        if new_name is not None:
            self.new_name = new_name
        if password_length is not None:
            self.password_length = password_length
        if rm_tag is not None:
            self.rm_tag = rm_tag
        if rotation_hour is not None:
            self.rotation_hour = rotation_hour
        if rotation_interval is not None:
            self.rotation_interval = rotation_interval
        self.rotator_type = rotator_type
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def add_tag(self):
        """Gets the add_tag of this RotatedSecretUpdateGcp.  # noqa: E501

        List of the new tags that will be attached to this item  # noqa: E501

        :return: The add_tag of this RotatedSecretUpdateGcp.  # noqa: E501
        :rtype: list[str]
        """
        return self._add_tag

    @add_tag.setter
    def add_tag(self, add_tag):
        """Sets the add_tag of this RotatedSecretUpdateGcp.

        List of the new tags that will be attached to this item  # noqa: E501

        :param add_tag: The add_tag of this RotatedSecretUpdateGcp.  # noqa: E501
        :type: list[str]
        """

        self._add_tag = add_tag

    @property
    def authentication_credentials(self):
        """Gets the authentication_credentials of this RotatedSecretUpdateGcp.  # noqa: E501

        The credentials to connect with use-user-creds/use-target-creds  # noqa: E501

        :return: The authentication_credentials of this RotatedSecretUpdateGcp.  # noqa: E501
        :rtype: str
        """
        return self._authentication_credentials

    @authentication_credentials.setter
    def authentication_credentials(self, authentication_credentials):
        """Sets the authentication_credentials of this RotatedSecretUpdateGcp.

        The credentials to connect with use-user-creds/use-target-creds  # noqa: E501

        :param authentication_credentials: The authentication_credentials of this RotatedSecretUpdateGcp.  # noqa: E501
        :type: str
        """

        self._authentication_credentials = authentication_credentials

    @property
    def auto_rotate(self):
        """Gets the auto_rotate of this RotatedSecretUpdateGcp.  # noqa: E501

        Whether to automatically rotate every --rotation-interval days, or disable existing automatic rotation [true/false]  # noqa: E501

        :return: The auto_rotate of this RotatedSecretUpdateGcp.  # noqa: E501
        :rtype: str
        """
        return self._auto_rotate

    @auto_rotate.setter
    def auto_rotate(self, auto_rotate):
        """Sets the auto_rotate of this RotatedSecretUpdateGcp.

        Whether to automatically rotate every --rotation-interval days, or disable existing automatic rotation [true/false]  # noqa: E501

        :param auto_rotate: The auto_rotate of this RotatedSecretUpdateGcp.  # noqa: E501
        :type: str
        """

        self._auto_rotate = auto_rotate

    @property
    def delete_protection(self):
        """Gets the delete_protection of this RotatedSecretUpdateGcp.  # noqa: E501

        Protection from accidental deletion of this item [true/false]  # noqa: E501

        :return: The delete_protection of this RotatedSecretUpdateGcp.  # noqa: E501
        :rtype: str
        """
        return self._delete_protection

    @delete_protection.setter
    def delete_protection(self, delete_protection):
        """Sets the delete_protection of this RotatedSecretUpdateGcp.

        Protection from accidental deletion of this item [true/false]  # noqa: E501

        :param delete_protection: The delete_protection of this RotatedSecretUpdateGcp.  # noqa: E501
        :type: str
        """

        self._delete_protection = delete_protection

    @property
    def description(self):
        """Gets the description of this RotatedSecretUpdateGcp.  # noqa: E501

        Description of the object  # noqa: E501

        :return: The description of this RotatedSecretUpdateGcp.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RotatedSecretUpdateGcp.

        Description of the object  # noqa: E501

        :param description: The description of this RotatedSecretUpdateGcp.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def gcp_key(self):
        """Gets the gcp_key of this RotatedSecretUpdateGcp.  # noqa: E501

        Base64-encoded service account private key text  # noqa: E501

        :return: The gcp_key of this RotatedSecretUpdateGcp.  # noqa: E501
        :rtype: str
        """
        return self._gcp_key

    @gcp_key.setter
    def gcp_key(self, gcp_key):
        """Sets the gcp_key of this RotatedSecretUpdateGcp.

        Base64-encoded service account private key text  # noqa: E501

        :param gcp_key: The gcp_key of this RotatedSecretUpdateGcp.  # noqa: E501
        :type: str
        """

        self._gcp_key = gcp_key

    @property
    def gcp_service_account_email(self):
        """Gets the gcp_service_account_email of this RotatedSecretUpdateGcp.  # noqa: E501

        The email of the gcp service account to rotate  # noqa: E501

        :return: The gcp_service_account_email of this RotatedSecretUpdateGcp.  # noqa: E501
        :rtype: str
        """
        return self._gcp_service_account_email

    @gcp_service_account_email.setter
    def gcp_service_account_email(self, gcp_service_account_email):
        """Sets the gcp_service_account_email of this RotatedSecretUpdateGcp.

        The email of the gcp service account to rotate  # noqa: E501

        :param gcp_service_account_email: The gcp_service_account_email of this RotatedSecretUpdateGcp.  # noqa: E501
        :type: str
        """

        self._gcp_service_account_email = gcp_service_account_email

    @property
    def gcp_service_account_key_id(self):
        """Gets the gcp_service_account_key_id of this RotatedSecretUpdateGcp.  # noqa: E501

        The key id of the gcp service account to rotate  # noqa: E501

        :return: The gcp_service_account_key_id of this RotatedSecretUpdateGcp.  # noqa: E501
        :rtype: str
        """
        return self._gcp_service_account_key_id

    @gcp_service_account_key_id.setter
    def gcp_service_account_key_id(self, gcp_service_account_key_id):
        """Sets the gcp_service_account_key_id of this RotatedSecretUpdateGcp.

        The key id of the gcp service account to rotate  # noqa: E501

        :param gcp_service_account_key_id: The gcp_service_account_key_id of this RotatedSecretUpdateGcp.  # noqa: E501
        :type: str
        """

        self._gcp_service_account_key_id = gcp_service_account_key_id

    @property
    def json(self):
        """Gets the json of this RotatedSecretUpdateGcp.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this RotatedSecretUpdateGcp.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this RotatedSecretUpdateGcp.

        Set output format to JSON  # noqa: E501

        :param json: The json of this RotatedSecretUpdateGcp.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def keep_prev_version(self):
        """Gets the keep_prev_version of this RotatedSecretUpdateGcp.  # noqa: E501

        Whether to keep previous version [true/false]. If not set, use default according to account settings  # noqa: E501

        :return: The keep_prev_version of this RotatedSecretUpdateGcp.  # noqa: E501
        :rtype: str
        """
        return self._keep_prev_version

    @keep_prev_version.setter
    def keep_prev_version(self, keep_prev_version):
        """Sets the keep_prev_version of this RotatedSecretUpdateGcp.

        Whether to keep previous version [true/false]. If not set, use default according to account settings  # noqa: E501

        :param keep_prev_version: The keep_prev_version of this RotatedSecretUpdateGcp.  # noqa: E501
        :type: str
        """

        self._keep_prev_version = keep_prev_version

    @property
    def key(self):
        """Gets the key of this RotatedSecretUpdateGcp.  # noqa: E501

        The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :return: The key of this RotatedSecretUpdateGcp.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this RotatedSecretUpdateGcp.

        The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :param key: The key of this RotatedSecretUpdateGcp.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def max_versions(self):
        """Gets the max_versions of this RotatedSecretUpdateGcp.  # noqa: E501

        Set the maximum number of versions, limited by the account settings defaults.  # noqa: E501

        :return: The max_versions of this RotatedSecretUpdateGcp.  # noqa: E501
        :rtype: str
        """
        return self._max_versions

    @max_versions.setter
    def max_versions(self, max_versions):
        """Sets the max_versions of this RotatedSecretUpdateGcp.

        Set the maximum number of versions, limited by the account settings defaults.  # noqa: E501

        :param max_versions: The max_versions of this RotatedSecretUpdateGcp.  # noqa: E501
        :type: str
        """

        self._max_versions = max_versions

    @property
    def name(self):
        """Gets the name of this RotatedSecretUpdateGcp.  # noqa: E501

        Rotated secret name  # noqa: E501

        :return: The name of this RotatedSecretUpdateGcp.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RotatedSecretUpdateGcp.

        Rotated secret name  # noqa: E501

        :param name: The name of this RotatedSecretUpdateGcp.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def new_name(self):
        """Gets the new_name of this RotatedSecretUpdateGcp.  # noqa: E501

        New item name  # noqa: E501

        :return: The new_name of this RotatedSecretUpdateGcp.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this RotatedSecretUpdateGcp.

        New item name  # noqa: E501

        :param new_name: The new_name of this RotatedSecretUpdateGcp.  # noqa: E501
        :type: str
        """

        self._new_name = new_name

    @property
    def password_length(self):
        """Gets the password_length of this RotatedSecretUpdateGcp.  # noqa: E501

        The length of the password to be generated  # noqa: E501

        :return: The password_length of this RotatedSecretUpdateGcp.  # noqa: E501
        :rtype: str
        """
        return self._password_length

    @password_length.setter
    def password_length(self, password_length):
        """Sets the password_length of this RotatedSecretUpdateGcp.

        The length of the password to be generated  # noqa: E501

        :param password_length: The password_length of this RotatedSecretUpdateGcp.  # noqa: E501
        :type: str
        """

        self._password_length = password_length

    @property
    def rm_tag(self):
        """Gets the rm_tag of this RotatedSecretUpdateGcp.  # noqa: E501

        List of the existent tags that will be removed from this item  # noqa: E501

        :return: The rm_tag of this RotatedSecretUpdateGcp.  # noqa: E501
        :rtype: list[str]
        """
        return self._rm_tag

    @rm_tag.setter
    def rm_tag(self, rm_tag):
        """Sets the rm_tag of this RotatedSecretUpdateGcp.

        List of the existent tags that will be removed from this item  # noqa: E501

        :param rm_tag: The rm_tag of this RotatedSecretUpdateGcp.  # noqa: E501
        :type: list[str]
        """

        self._rm_tag = rm_tag

    @property
    def rotation_hour(self):
        """Gets the rotation_hour of this RotatedSecretUpdateGcp.  # noqa: E501

        The Hour of the rotation in UTC  # noqa: E501

        :return: The rotation_hour of this RotatedSecretUpdateGcp.  # noqa: E501
        :rtype: int
        """
        return self._rotation_hour

    @rotation_hour.setter
    def rotation_hour(self, rotation_hour):
        """Sets the rotation_hour of this RotatedSecretUpdateGcp.

        The Hour of the rotation in UTC  # noqa: E501

        :param rotation_hour: The rotation_hour of this RotatedSecretUpdateGcp.  # noqa: E501
        :type: int
        """

        self._rotation_hour = rotation_hour

    @property
    def rotation_interval(self):
        """Gets the rotation_interval of this RotatedSecretUpdateGcp.  # noqa: E501

        The number of days to wait between every automatic key rotation (1-365)  # noqa: E501

        :return: The rotation_interval of this RotatedSecretUpdateGcp.  # noqa: E501
        :rtype: str
        """
        return self._rotation_interval

    @rotation_interval.setter
    def rotation_interval(self, rotation_interval):
        """Sets the rotation_interval of this RotatedSecretUpdateGcp.

        The number of days to wait between every automatic key rotation (1-365)  # noqa: E501

        :param rotation_interval: The rotation_interval of this RotatedSecretUpdateGcp.  # noqa: E501
        :type: str
        """

        self._rotation_interval = rotation_interval

    @property
    def rotator_type(self):
        """Gets the rotator_type of this RotatedSecretUpdateGcp.  # noqa: E501

        The rotator type. options: [target/service-account-rotator]  # noqa: E501

        :return: The rotator_type of this RotatedSecretUpdateGcp.  # noqa: E501
        :rtype: str
        """
        return self._rotator_type

    @rotator_type.setter
    def rotator_type(self, rotator_type):
        """Sets the rotator_type of this RotatedSecretUpdateGcp.

        The rotator type. options: [target/service-account-rotator]  # noqa: E501

        :param rotator_type: The rotator_type of this RotatedSecretUpdateGcp.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and rotator_type is None:  # noqa: E501
            raise ValueError("Invalid value for `rotator_type`, must not be `None`")  # noqa: E501

        self._rotator_type = rotator_type

    @property
    def token(self):
        """Gets the token of this RotatedSecretUpdateGcp.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this RotatedSecretUpdateGcp.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this RotatedSecretUpdateGcp.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this RotatedSecretUpdateGcp.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this RotatedSecretUpdateGcp.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this RotatedSecretUpdateGcp.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this RotatedSecretUpdateGcp.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this RotatedSecretUpdateGcp.  # noqa: E501
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
        if not isinstance(other, RotatedSecretUpdateGcp):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RotatedSecretUpdateGcp):
            return True

        return self.to_dict() != other.to_dict()
