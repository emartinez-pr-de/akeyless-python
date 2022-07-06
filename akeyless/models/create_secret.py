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


class CreateSecret(object):
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
        'custom_fields': 'dict(str, str)',
        'delete_protection': 'str',
        'item_accessibility': 'str',
        'metadata': 'str',
        'multiline_value': 'bool',
        'name': 'str',
        'password_length': 'int',
        'protection_key': 'str',
        'secure_access_bastion_issuer': 'str',
        'secure_access_enable': 'str',
        'secure_access_host': 'list[str]',
        'secure_access_ssh_creds': 'str',
        'secure_access_ssh_user': 'str',
        'secure_access_url': 'str',
        'secure_access_web_browsing': 'bool',
        'secure_access_web_proxy': 'bool',
        'tags': 'list[str]',
        'token': 'str',
        'type': 'str',
        'uid_token': 'str',
        'use_lower_letters': 'str',
        'use_numbers': 'str',
        'use_special_characters': 'str',
        'use_capital_letters': 'str',
        'username': 'str',
        'value': 'str',
        'website': 'str'
    }

    attribute_map = {
        'custom_fields': 'custom-fields',
        'delete_protection': 'delete_protection',
        'item_accessibility': 'item-accessibility',
        'metadata': 'metadata',
        'multiline_value': 'multiline_value',
        'name': 'name',
        'password_length': 'password-length',
        'protection_key': 'protection_key',
        'secure_access_bastion_issuer': 'secure-access-bastion-issuer',
        'secure_access_enable': 'secure-access-enable',
        'secure_access_host': 'secure-access-host',
        'secure_access_ssh_creds': 'secure-access-ssh-creds',
        'secure_access_ssh_user': 'secure-access-ssh-user',
        'secure_access_url': 'secure-access-url',
        'secure_access_web_browsing': 'secure-access-web-browsing',
        'secure_access_web_proxy': 'secure-access-web-proxy',
        'tags': 'tags',
        'token': 'token',
        'type': 'type',
        'uid_token': 'uid-token',
        'use_lower_letters': 'use-lower-letters',
        'use_numbers': 'use-numbers',
        'use_special_characters': 'use-special-characters',
        'use_capital_letters': 'use_capital-letters',
        'username': 'username',
        'value': 'value',
        'website': 'website'
    }

    def __init__(self, custom_fields=None, delete_protection=None, item_accessibility=None, metadata=None, multiline_value=None, name=None, password_length=None, protection_key=None, secure_access_bastion_issuer=None, secure_access_enable=None, secure_access_host=None, secure_access_ssh_creds=None, secure_access_ssh_user=None, secure_access_url=None, secure_access_web_browsing=None, secure_access_web_proxy=None, tags=None, token=None, type=None, uid_token=None, use_lower_letters=None, use_numbers=None, use_special_characters=None, use_capital_letters=None, username=None, value=None, website=None, local_vars_configuration=None):  # noqa: E501
        """CreateSecret - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._custom_fields = None
        self._delete_protection = None
        self._item_accessibility = None
        self._metadata = None
        self._multiline_value = None
        self._name = None
        self._password_length = None
        self._protection_key = None
        self._secure_access_bastion_issuer = None
        self._secure_access_enable = None
        self._secure_access_host = None
        self._secure_access_ssh_creds = None
        self._secure_access_ssh_user = None
        self._secure_access_url = None
        self._secure_access_web_browsing = None
        self._secure_access_web_proxy = None
        self._tags = None
        self._token = None
        self._type = None
        self._uid_token = None
        self._use_lower_letters = None
        self._use_numbers = None
        self._use_special_characters = None
        self._use_capital_letters = None
        self._username = None
        self._value = None
        self._website = None
        self.discriminator = None

        if custom_fields is not None:
            self.custom_fields = custom_fields
        if delete_protection is not None:
            self.delete_protection = delete_protection
        if item_accessibility is not None:
            self.item_accessibility = item_accessibility
        if metadata is not None:
            self.metadata = metadata
        if multiline_value is not None:
            self.multiline_value = multiline_value
        self.name = name
        if password_length is not None:
            self.password_length = password_length
        if protection_key is not None:
            self.protection_key = protection_key
        if secure_access_bastion_issuer is not None:
            self.secure_access_bastion_issuer = secure_access_bastion_issuer
        if secure_access_enable is not None:
            self.secure_access_enable = secure_access_enable
        if secure_access_host is not None:
            self.secure_access_host = secure_access_host
        if secure_access_ssh_creds is not None:
            self.secure_access_ssh_creds = secure_access_ssh_creds
        if secure_access_ssh_user is not None:
            self.secure_access_ssh_user = secure_access_ssh_user
        if secure_access_url is not None:
            self.secure_access_url = secure_access_url
        if secure_access_web_browsing is not None:
            self.secure_access_web_browsing = secure_access_web_browsing
        if secure_access_web_proxy is not None:
            self.secure_access_web_proxy = secure_access_web_proxy
        if tags is not None:
            self.tags = tags
        if token is not None:
            self.token = token
        if type is not None:
            self.type = type
        if uid_token is not None:
            self.uid_token = uid_token
        if use_lower_letters is not None:
            self.use_lower_letters = use_lower_letters
        if use_numbers is not None:
            self.use_numbers = use_numbers
        if use_special_characters is not None:
            self.use_special_characters = use_special_characters
        if use_capital_letters is not None:
            self.use_capital_letters = use_capital_letters
        if username is not None:
            self.username = username
        self.value = value
        if website is not None:
            self.website = website

    @property
    def custom_fields(self):
        """Gets the custom_fields of this CreateSecret.  # noqa: E501

        For Password Management use, additional fields  # noqa: E501

        :return: The custom_fields of this CreateSecret.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this CreateSecret.

        For Password Management use, additional fields  # noqa: E501

        :param custom_fields: The custom_fields of this CreateSecret.  # noqa: E501
        :type: dict(str, str)
        """

        self._custom_fields = custom_fields

    @property
    def delete_protection(self):
        """Gets the delete_protection of this CreateSecret.  # noqa: E501

        Protection from accidental deletion of this item  # noqa: E501

        :return: The delete_protection of this CreateSecret.  # noqa: E501
        :rtype: str
        """
        return self._delete_protection

    @delete_protection.setter
    def delete_protection(self, delete_protection):
        """Sets the delete_protection of this CreateSecret.

        Protection from accidental deletion of this item  # noqa: E501

        :param delete_protection: The delete_protection of this CreateSecret.  # noqa: E501
        :type: str
        """

        self._delete_protection = delete_protection

    @property
    def item_accessibility(self):
        """Gets the item_accessibility of this CreateSecret.  # noqa: E501

        for personal password manager  # noqa: E501

        :return: The item_accessibility of this CreateSecret.  # noqa: E501
        :rtype: str
        """
        return self._item_accessibility

    @item_accessibility.setter
    def item_accessibility(self, item_accessibility):
        """Sets the item_accessibility of this CreateSecret.

        for personal password manager  # noqa: E501

        :param item_accessibility: The item_accessibility of this CreateSecret.  # noqa: E501
        :type: str
        """

        self._item_accessibility = item_accessibility

    @property
    def metadata(self):
        """Gets the metadata of this CreateSecret.  # noqa: E501

        Metadata about the secret  # noqa: E501

        :return: The metadata of this CreateSecret.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CreateSecret.

        Metadata about the secret  # noqa: E501

        :param metadata: The metadata of this CreateSecret.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def multiline_value(self):
        """Gets the multiline_value of this CreateSecret.  # noqa: E501

        The provided value is a multiline value (separated by '\\n')  # noqa: E501

        :return: The multiline_value of this CreateSecret.  # noqa: E501
        :rtype: bool
        """
        return self._multiline_value

    @multiline_value.setter
    def multiline_value(self, multiline_value):
        """Sets the multiline_value of this CreateSecret.

        The provided value is a multiline value (separated by '\\n')  # noqa: E501

        :param multiline_value: The multiline_value of this CreateSecret.  # noqa: E501
        :type: bool
        """

        self._multiline_value = multiline_value

    @property
    def name(self):
        """Gets the name of this CreateSecret.  # noqa: E501

        Secret name  # noqa: E501

        :return: The name of this CreateSecret.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateSecret.

        Secret name  # noqa: E501

        :param name: The name of this CreateSecret.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def password_length(self):
        """Gets the password_length of this CreateSecret.  # noqa: E501

        For PasswordPolicy use  # noqa: E501

        :return: The password_length of this CreateSecret.  # noqa: E501
        :rtype: int
        """
        return self._password_length

    @password_length.setter
    def password_length(self, password_length):
        """Sets the password_length of this CreateSecret.

        For PasswordPolicy use  # noqa: E501

        :param password_length: The password_length of this CreateSecret.  # noqa: E501
        :type: int
        """

        self._password_length = password_length

    @property
    def protection_key(self):
        """Gets the protection_key of this CreateSecret.  # noqa: E501

        The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :return: The protection_key of this CreateSecret.  # noqa: E501
        :rtype: str
        """
        return self._protection_key

    @protection_key.setter
    def protection_key(self, protection_key):
        """Sets the protection_key of this CreateSecret.

        The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :param protection_key: The protection_key of this CreateSecret.  # noqa: E501
        :type: str
        """

        self._protection_key = protection_key

    @property
    def secure_access_bastion_issuer(self):
        """Gets the secure_access_bastion_issuer of this CreateSecret.  # noqa: E501


        :return: The secure_access_bastion_issuer of this CreateSecret.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_bastion_issuer

    @secure_access_bastion_issuer.setter
    def secure_access_bastion_issuer(self, secure_access_bastion_issuer):
        """Sets the secure_access_bastion_issuer of this CreateSecret.


        :param secure_access_bastion_issuer: The secure_access_bastion_issuer of this CreateSecret.  # noqa: E501
        :type: str
        """

        self._secure_access_bastion_issuer = secure_access_bastion_issuer

    @property
    def secure_access_enable(self):
        """Gets the secure_access_enable of this CreateSecret.  # noqa: E501


        :return: The secure_access_enable of this CreateSecret.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_enable

    @secure_access_enable.setter
    def secure_access_enable(self, secure_access_enable):
        """Sets the secure_access_enable of this CreateSecret.


        :param secure_access_enable: The secure_access_enable of this CreateSecret.  # noqa: E501
        :type: str
        """

        self._secure_access_enable = secure_access_enable

    @property
    def secure_access_host(self):
        """Gets the secure_access_host of this CreateSecret.  # noqa: E501


        :return: The secure_access_host of this CreateSecret.  # noqa: E501
        :rtype: list[str]
        """
        return self._secure_access_host

    @secure_access_host.setter
    def secure_access_host(self, secure_access_host):
        """Sets the secure_access_host of this CreateSecret.


        :param secure_access_host: The secure_access_host of this CreateSecret.  # noqa: E501
        :type: list[str]
        """

        self._secure_access_host = secure_access_host

    @property
    def secure_access_ssh_creds(self):
        """Gets the secure_access_ssh_creds of this CreateSecret.  # noqa: E501


        :return: The secure_access_ssh_creds of this CreateSecret.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_ssh_creds

    @secure_access_ssh_creds.setter
    def secure_access_ssh_creds(self, secure_access_ssh_creds):
        """Sets the secure_access_ssh_creds of this CreateSecret.


        :param secure_access_ssh_creds: The secure_access_ssh_creds of this CreateSecret.  # noqa: E501
        :type: str
        """

        self._secure_access_ssh_creds = secure_access_ssh_creds

    @property
    def secure_access_ssh_user(self):
        """Gets the secure_access_ssh_user of this CreateSecret.  # noqa: E501


        :return: The secure_access_ssh_user of this CreateSecret.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_ssh_user

    @secure_access_ssh_user.setter
    def secure_access_ssh_user(self, secure_access_ssh_user):
        """Sets the secure_access_ssh_user of this CreateSecret.


        :param secure_access_ssh_user: The secure_access_ssh_user of this CreateSecret.  # noqa: E501
        :type: str
        """

        self._secure_access_ssh_user = secure_access_ssh_user

    @property
    def secure_access_url(self):
        """Gets the secure_access_url of this CreateSecret.  # noqa: E501


        :return: The secure_access_url of this CreateSecret.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_url

    @secure_access_url.setter
    def secure_access_url(self, secure_access_url):
        """Sets the secure_access_url of this CreateSecret.


        :param secure_access_url: The secure_access_url of this CreateSecret.  # noqa: E501
        :type: str
        """

        self._secure_access_url = secure_access_url

    @property
    def secure_access_web_browsing(self):
        """Gets the secure_access_web_browsing of this CreateSecret.  # noqa: E501


        :return: The secure_access_web_browsing of this CreateSecret.  # noqa: E501
        :rtype: bool
        """
        return self._secure_access_web_browsing

    @secure_access_web_browsing.setter
    def secure_access_web_browsing(self, secure_access_web_browsing):
        """Sets the secure_access_web_browsing of this CreateSecret.


        :param secure_access_web_browsing: The secure_access_web_browsing of this CreateSecret.  # noqa: E501
        :type: bool
        """

        self._secure_access_web_browsing = secure_access_web_browsing

    @property
    def secure_access_web_proxy(self):
        """Gets the secure_access_web_proxy of this CreateSecret.  # noqa: E501


        :return: The secure_access_web_proxy of this CreateSecret.  # noqa: E501
        :rtype: bool
        """
        return self._secure_access_web_proxy

    @secure_access_web_proxy.setter
    def secure_access_web_proxy(self, secure_access_web_proxy):
        """Sets the secure_access_web_proxy of this CreateSecret.


        :param secure_access_web_proxy: The secure_access_web_proxy of this CreateSecret.  # noqa: E501
        :type: bool
        """

        self._secure_access_web_proxy = secure_access_web_proxy

    @property
    def tags(self):
        """Gets the tags of this CreateSecret.  # noqa: E501

        List of the tags attached to this secret  # noqa: E501

        :return: The tags of this CreateSecret.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateSecret.

        List of the tags attached to this secret  # noqa: E501

        :param tags: The tags of this CreateSecret.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def token(self):
        """Gets the token of this CreateSecret.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this CreateSecret.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this CreateSecret.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this CreateSecret.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def type(self):
        """Gets the type of this CreateSecret.  # noqa: E501

        For Password Management use, reflect the website context  # noqa: E501

        :return: The type of this CreateSecret.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateSecret.

        For Password Management use, reflect the website context  # noqa: E501

        :param type: The type of this CreateSecret.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def uid_token(self):
        """Gets the uid_token of this CreateSecret.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this CreateSecret.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this CreateSecret.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this CreateSecret.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def use_lower_letters(self):
        """Gets the use_lower_letters of this CreateSecret.  # noqa: E501

        For PasswordPolicy use  # noqa: E501

        :return: The use_lower_letters of this CreateSecret.  # noqa: E501
        :rtype: str
        """
        return self._use_lower_letters

    @use_lower_letters.setter
    def use_lower_letters(self, use_lower_letters):
        """Sets the use_lower_letters of this CreateSecret.

        For PasswordPolicy use  # noqa: E501

        :param use_lower_letters: The use_lower_letters of this CreateSecret.  # noqa: E501
        :type: str
        """

        self._use_lower_letters = use_lower_letters

    @property
    def use_numbers(self):
        """Gets the use_numbers of this CreateSecret.  # noqa: E501

        For PasswordPolicy use  # noqa: E501

        :return: The use_numbers of this CreateSecret.  # noqa: E501
        :rtype: str
        """
        return self._use_numbers

    @use_numbers.setter
    def use_numbers(self, use_numbers):
        """Sets the use_numbers of this CreateSecret.

        For PasswordPolicy use  # noqa: E501

        :param use_numbers: The use_numbers of this CreateSecret.  # noqa: E501
        :type: str
        """

        self._use_numbers = use_numbers

    @property
    def use_special_characters(self):
        """Gets the use_special_characters of this CreateSecret.  # noqa: E501

        For PasswordPolicy use  # noqa: E501

        :return: The use_special_characters of this CreateSecret.  # noqa: E501
        :rtype: str
        """
        return self._use_special_characters

    @use_special_characters.setter
    def use_special_characters(self, use_special_characters):
        """Sets the use_special_characters of this CreateSecret.

        For PasswordPolicy use  # noqa: E501

        :param use_special_characters: The use_special_characters of this CreateSecret.  # noqa: E501
        :type: str
        """

        self._use_special_characters = use_special_characters

    @property
    def use_capital_letters(self):
        """Gets the use_capital_letters of this CreateSecret.  # noqa: E501

        For PasswordPolicy use  # noqa: E501

        :return: The use_capital_letters of this CreateSecret.  # noqa: E501
        :rtype: str
        """
        return self._use_capital_letters

    @use_capital_letters.setter
    def use_capital_letters(self, use_capital_letters):
        """Sets the use_capital_letters of this CreateSecret.

        For PasswordPolicy use  # noqa: E501

        :param use_capital_letters: The use_capital_letters of this CreateSecret.  # noqa: E501
        :type: str
        """

        self._use_capital_letters = use_capital_letters

    @property
    def username(self):
        """Gets the username of this CreateSecret.  # noqa: E501

        For Password Management use  # noqa: E501

        :return: The username of this CreateSecret.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this CreateSecret.

        For Password Management use  # noqa: E501

        :param username: The username of this CreateSecret.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def value(self):
        """Gets the value of this CreateSecret.  # noqa: E501

        The secret value  # noqa: E501

        :return: The value of this CreateSecret.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CreateSecret.

        The secret value  # noqa: E501

        :param value: The value of this CreateSecret.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def website(self):
        """Gets the website of this CreateSecret.  # noqa: E501

        For Password Management use, reflect the website context  # noqa: E501

        :return: The website of this CreateSecret.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this CreateSecret.

        For Password Management use, reflect the website context  # noqa: E501

        :param website: The website of this CreateSecret.  # noqa: E501
        :type: str
        """

        self._website = website

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
        if not isinstance(other, CreateSecret):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateSecret):
            return True

        return self.to_dict() != other.to_dict()
