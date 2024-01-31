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


class ImportPasswords(object):
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
        'accessibility': 'str',
        'format': 'str',
        'import_path': 'str',
        'json': 'bool',
        'protection_key': 'str',
        'target_folder': 'str',
        'token': 'str',
        'uid_token': 'str',
        'update_mode': 'str'
    }

    attribute_map = {
        'accessibility': 'accessibility',
        'format': 'format',
        'import_path': 'import-path',
        'json': 'json',
        'protection_key': 'protection_key',
        'target_folder': 'target-folder',
        'token': 'token',
        'uid_token': 'uid-token',
        'update_mode': 'update-mode'
    }

    def __init__(self, accessibility='personal', format='LastPass', import_path=None, json=False, protection_key=None, target_folder='/', token=None, uid_token=None, update_mode=None, local_vars_configuration=None):  # noqa: E501
        """ImportPasswords - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._accessibility = None
        self._format = None
        self._import_path = None
        self._json = None
        self._protection_key = None
        self._target_folder = None
        self._token = None
        self._uid_token = None
        self._update_mode = None
        self.discriminator = None

        if accessibility is not None:
            self.accessibility = accessibility
        if format is not None:
            self.format = format
        self.import_path = import_path
        if json is not None:
            self.json = json
        if protection_key is not None:
            self.protection_key = protection_key
        if target_folder is not None:
            self.target_folder = target_folder
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if update_mode is not None:
            self.update_mode = update_mode

    @property
    def accessibility(self):
        """Gets the accessibility of this ImportPasswords.  # noqa: E501

        for personal password manager  # noqa: E501

        :return: The accessibility of this ImportPasswords.  # noqa: E501
        :rtype: str
        """
        return self._accessibility

    @accessibility.setter
    def accessibility(self, accessibility):
        """Sets the accessibility of this ImportPasswords.

        for personal password manager  # noqa: E501

        :param accessibility: The accessibility of this ImportPasswords.  # noqa: E501
        :type: str
        """

        self._accessibility = accessibility

    @property
    def format(self):
        """Gets the format of this ImportPasswords.  # noqa: E501

        Password format type [LastPass/Chrome/Firefox]  # noqa: E501

        :return: The format of this ImportPasswords.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this ImportPasswords.

        Password format type [LastPass/Chrome/Firefox]  # noqa: E501

        :param format: The format of this ImportPasswords.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def import_path(self):
        """Gets the import_path of this ImportPasswords.  # noqa: E501

        File path  # noqa: E501

        :return: The import_path of this ImportPasswords.  # noqa: E501
        :rtype: str
        """
        return self._import_path

    @import_path.setter
    def import_path(self, import_path):
        """Sets the import_path of this ImportPasswords.

        File path  # noqa: E501

        :param import_path: The import_path of this ImportPasswords.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and import_path is None:  # noqa: E501
            raise ValueError("Invalid value for `import_path`, must not be `None`")  # noqa: E501

        self._import_path = import_path

    @property
    def json(self):
        """Gets the json of this ImportPasswords.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this ImportPasswords.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this ImportPasswords.

        Set output format to JSON  # noqa: E501

        :param json: The json of this ImportPasswords.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def protection_key(self):
        """Gets the protection_key of this ImportPasswords.  # noqa: E501

        The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :return: The protection_key of this ImportPasswords.  # noqa: E501
        :rtype: str
        """
        return self._protection_key

    @protection_key.setter
    def protection_key(self, protection_key):
        """Sets the protection_key of this ImportPasswords.

        The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :param protection_key: The protection_key of this ImportPasswords.  # noqa: E501
        :type: str
        """

        self._protection_key = protection_key

    @property
    def target_folder(self):
        """Gets the target_folder of this ImportPasswords.  # noqa: E501

        Target folder for imported passwords  # noqa: E501

        :return: The target_folder of this ImportPasswords.  # noqa: E501
        :rtype: str
        """
        return self._target_folder

    @target_folder.setter
    def target_folder(self, target_folder):
        """Sets the target_folder of this ImportPasswords.

        Target folder for imported passwords  # noqa: E501

        :param target_folder: The target_folder of this ImportPasswords.  # noqa: E501
        :type: str
        """

        self._target_folder = target_folder

    @property
    def token(self):
        """Gets the token of this ImportPasswords.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this ImportPasswords.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this ImportPasswords.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this ImportPasswords.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this ImportPasswords.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this ImportPasswords.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this ImportPasswords.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this ImportPasswords.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def update_mode(self):
        """Gets the update_mode of this ImportPasswords.  # noqa: E501


        :return: The update_mode of this ImportPasswords.  # noqa: E501
        :rtype: str
        """
        return self._update_mode

    @update_mode.setter
    def update_mode(self, update_mode):
        """Sets the update_mode of this ImportPasswords.


        :param update_mode: The update_mode of this ImportPasswords.  # noqa: E501
        :type: str
        """

        self._update_mode = update_mode

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
        if not isinstance(other, ImportPasswords):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImportPasswords):
            return True

        return self.to_dict() != other.to_dict()
