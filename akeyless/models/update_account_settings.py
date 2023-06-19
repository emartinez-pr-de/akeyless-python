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


class UpdateAccountSettings(object):
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
        'address': 'str',
        'city': 'str',
        'company_name': 'str',
        'country': 'str',
        'default_share_link_ttl_minutes': 'str',
        'default_versioning': 'str',
        'dp_enable_classic_key_protection': 'str',
        'item_type': 'str',
        'items_deletion_protection': 'str',
        'json': 'bool',
        'jwt_ttl_default': 'int',
        'jwt_ttl_max': 'int',
        'jwt_ttl_min': 'int',
        'max_versions': 'str',
        'password_length': 'int',
        'phone': 'str',
        'postal_code': 'str',
        'token': 'str',
        'uid_token': 'str',
        'use_lower_letters': 'str',
        'use_numbers': 'str',
        'use_special_characters': 'str',
        'use_capital_letters': 'str'
    }

    attribute_map = {
        'address': 'address',
        'city': 'city',
        'company_name': 'company-name',
        'country': 'country',
        'default_share_link_ttl_minutes': 'default-share-link-ttl-minutes',
        'default_versioning': 'default-versioning',
        'dp_enable_classic_key_protection': 'dp-enable-classic-key-protection',
        'item_type': 'item-type',
        'items_deletion_protection': 'items-deletion-protection',
        'json': 'json',
        'jwt_ttl_default': 'jwt-ttl-default',
        'jwt_ttl_max': 'jwt-ttl-max',
        'jwt_ttl_min': 'jwt-ttl-min',
        'max_versions': 'max-versions',
        'password_length': 'password-length',
        'phone': 'phone',
        'postal_code': 'postal-code',
        'token': 'token',
        'uid_token': 'uid-token',
        'use_lower_letters': 'use-lower-letters',
        'use_numbers': 'use-numbers',
        'use_special_characters': 'use-special-characters',
        'use_capital_letters': 'use_capital-letters'
    }

    def __init__(self, address=None, city=None, company_name=None, country=None, default_share_link_ttl_minutes=None, default_versioning=None, dp_enable_classic_key_protection=None, item_type=None, items_deletion_protection=None, json=False, jwt_ttl_default=None, jwt_ttl_max=None, jwt_ttl_min=None, max_versions=None, password_length=None, phone=None, postal_code=None, token=None, uid_token=None, use_lower_letters=None, use_numbers=None, use_special_characters=None, use_capital_letters=None, local_vars_configuration=None):  # noqa: E501
        """UpdateAccountSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._address = None
        self._city = None
        self._company_name = None
        self._country = None
        self._default_share_link_ttl_minutes = None
        self._default_versioning = None
        self._dp_enable_classic_key_protection = None
        self._item_type = None
        self._items_deletion_protection = None
        self._json = None
        self._jwt_ttl_default = None
        self._jwt_ttl_max = None
        self._jwt_ttl_min = None
        self._max_versions = None
        self._password_length = None
        self._phone = None
        self._postal_code = None
        self._token = None
        self._uid_token = None
        self._use_lower_letters = None
        self._use_numbers = None
        self._use_special_characters = None
        self._use_capital_letters = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if city is not None:
            self.city = city
        if company_name is not None:
            self.company_name = company_name
        if country is not None:
            self.country = country
        if default_share_link_ttl_minutes is not None:
            self.default_share_link_ttl_minutes = default_share_link_ttl_minutes
        if default_versioning is not None:
            self.default_versioning = default_versioning
        if dp_enable_classic_key_protection is not None:
            self.dp_enable_classic_key_protection = dp_enable_classic_key_protection
        if item_type is not None:
            self.item_type = item_type
        if items_deletion_protection is not None:
            self.items_deletion_protection = items_deletion_protection
        if json is not None:
            self.json = json
        if jwt_ttl_default is not None:
            self.jwt_ttl_default = jwt_ttl_default
        if jwt_ttl_max is not None:
            self.jwt_ttl_max = jwt_ttl_max
        if jwt_ttl_min is not None:
            self.jwt_ttl_min = jwt_ttl_min
        if max_versions is not None:
            self.max_versions = max_versions
        if password_length is not None:
            self.password_length = password_length
        if phone is not None:
            self.phone = phone
        if postal_code is not None:
            self.postal_code = postal_code
        if token is not None:
            self.token = token
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

    @property
    def address(self):
        """Gets the address of this UpdateAccountSettings.  # noqa: E501

        Address  # noqa: E501

        :return: The address of this UpdateAccountSettings.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this UpdateAccountSettings.

        Address  # noqa: E501

        :param address: The address of this UpdateAccountSettings.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def city(self):
        """Gets the city of this UpdateAccountSettings.  # noqa: E501

        City  # noqa: E501

        :return: The city of this UpdateAccountSettings.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this UpdateAccountSettings.

        City  # noqa: E501

        :param city: The city of this UpdateAccountSettings.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def company_name(self):
        """Gets the company_name of this UpdateAccountSettings.  # noqa: E501

        Company name  # noqa: E501

        :return: The company_name of this UpdateAccountSettings.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this UpdateAccountSettings.

        Company name  # noqa: E501

        :param company_name: The company_name of this UpdateAccountSettings.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def country(self):
        """Gets the country of this UpdateAccountSettings.  # noqa: E501

        Country  # noqa: E501

        :return: The country of this UpdateAccountSettings.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this UpdateAccountSettings.

        Country  # noqa: E501

        :param country: The country of this UpdateAccountSettings.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def default_share_link_ttl_minutes(self):
        """Gets the default_share_link_ttl_minutes of this UpdateAccountSettings.  # noqa: E501

        Set the default ttl in minutes for sharing item number between 60 and 43200  # noqa: E501

        :return: The default_share_link_ttl_minutes of this UpdateAccountSettings.  # noqa: E501
        :rtype: str
        """
        return self._default_share_link_ttl_minutes

    @default_share_link_ttl_minutes.setter
    def default_share_link_ttl_minutes(self, default_share_link_ttl_minutes):
        """Sets the default_share_link_ttl_minutes of this UpdateAccountSettings.

        Set the default ttl in minutes for sharing item number between 60 and 43200  # noqa: E501

        :param default_share_link_ttl_minutes: The default_share_link_ttl_minutes of this UpdateAccountSettings.  # noqa: E501
        :type: str
        """

        self._default_share_link_ttl_minutes = default_share_link_ttl_minutes

    @property
    def default_versioning(self):
        """Gets the default_versioning of this UpdateAccountSettings.  # noqa: E501

        If set to true, new item version will be created on each update [true/false]  # noqa: E501

        :return: The default_versioning of this UpdateAccountSettings.  # noqa: E501
        :rtype: str
        """
        return self._default_versioning

    @default_versioning.setter
    def default_versioning(self, default_versioning):
        """Sets the default_versioning of this UpdateAccountSettings.

        If set to true, new item version will be created on each update [true/false]  # noqa: E501

        :param default_versioning: The default_versioning of this UpdateAccountSettings.  # noqa: E501
        :type: str
        """

        self._default_versioning = default_versioning

    @property
    def dp_enable_classic_key_protection(self):
        """Gets the dp_enable_classic_key_protection of this UpdateAccountSettings.  # noqa: E501

        Set to update protection with classic keys state [true/false]  # noqa: E501

        :return: The dp_enable_classic_key_protection of this UpdateAccountSettings.  # noqa: E501
        :rtype: str
        """
        return self._dp_enable_classic_key_protection

    @dp_enable_classic_key_protection.setter
    def dp_enable_classic_key_protection(self, dp_enable_classic_key_protection):
        """Sets the dp_enable_classic_key_protection of this UpdateAccountSettings.

        Set to update protection with classic keys state [true/false]  # noqa: E501

        :param dp_enable_classic_key_protection: The dp_enable_classic_key_protection of this UpdateAccountSettings.  # noqa: E501
        :type: str
        """

        self._dp_enable_classic_key_protection = dp_enable_classic_key_protection

    @property
    def item_type(self):
        """Gets the item_type of this UpdateAccountSettings.  # noqa: E501

        VersionSettingsObjectType defines object types for account version settings  # noqa: E501

        :return: The item_type of this UpdateAccountSettings.  # noqa: E501
        :rtype: str
        """
        return self._item_type

    @item_type.setter
    def item_type(self, item_type):
        """Sets the item_type of this UpdateAccountSettings.

        VersionSettingsObjectType defines object types for account version settings  # noqa: E501

        :param item_type: The item_type of this UpdateAccountSettings.  # noqa: E501
        :type: str
        """

        self._item_type = item_type

    @property
    def items_deletion_protection(self):
        """Gets the items_deletion_protection of this UpdateAccountSettings.  # noqa: E501

        Set or unset the default behaviour of items deletion protection [true/false]  # noqa: E501

        :return: The items_deletion_protection of this UpdateAccountSettings.  # noqa: E501
        :rtype: str
        """
        return self._items_deletion_protection

    @items_deletion_protection.setter
    def items_deletion_protection(self, items_deletion_protection):
        """Sets the items_deletion_protection of this UpdateAccountSettings.

        Set or unset the default behaviour of items deletion protection [true/false]  # noqa: E501

        :param items_deletion_protection: The items_deletion_protection of this UpdateAccountSettings.  # noqa: E501
        :type: str
        """

        self._items_deletion_protection = items_deletion_protection

    @property
    def json(self):
        """Gets the json of this UpdateAccountSettings.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this UpdateAccountSettings.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this UpdateAccountSettings.

        Set output format to JSON  # noqa: E501

        :param json: The json of this UpdateAccountSettings.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def jwt_ttl_default(self):
        """Gets the jwt_ttl_default of this UpdateAccountSettings.  # noqa: E501

        Default ttl  # noqa: E501

        :return: The jwt_ttl_default of this UpdateAccountSettings.  # noqa: E501
        :rtype: int
        """
        return self._jwt_ttl_default

    @jwt_ttl_default.setter
    def jwt_ttl_default(self, jwt_ttl_default):
        """Sets the jwt_ttl_default of this UpdateAccountSettings.

        Default ttl  # noqa: E501

        :param jwt_ttl_default: The jwt_ttl_default of this UpdateAccountSettings.  # noqa: E501
        :type: int
        """

        self._jwt_ttl_default = jwt_ttl_default

    @property
    def jwt_ttl_max(self):
        """Gets the jwt_ttl_max of this UpdateAccountSettings.  # noqa: E501

        Maximum ttl  # noqa: E501

        :return: The jwt_ttl_max of this UpdateAccountSettings.  # noqa: E501
        :rtype: int
        """
        return self._jwt_ttl_max

    @jwt_ttl_max.setter
    def jwt_ttl_max(self, jwt_ttl_max):
        """Sets the jwt_ttl_max of this UpdateAccountSettings.

        Maximum ttl  # noqa: E501

        :param jwt_ttl_max: The jwt_ttl_max of this UpdateAccountSettings.  # noqa: E501
        :type: int
        """

        self._jwt_ttl_max = jwt_ttl_max

    @property
    def jwt_ttl_min(self):
        """Gets the jwt_ttl_min of this UpdateAccountSettings.  # noqa: E501

        Minimum ttl  # noqa: E501

        :return: The jwt_ttl_min of this UpdateAccountSettings.  # noqa: E501
        :rtype: int
        """
        return self._jwt_ttl_min

    @jwt_ttl_min.setter
    def jwt_ttl_min(self, jwt_ttl_min):
        """Sets the jwt_ttl_min of this UpdateAccountSettings.

        Minimum ttl  # noqa: E501

        :param jwt_ttl_min: The jwt_ttl_min of this UpdateAccountSettings.  # noqa: E501
        :type: int
        """

        self._jwt_ttl_min = jwt_ttl_min

    @property
    def max_versions(self):
        """Gets the max_versions of this UpdateAccountSettings.  # noqa: E501

        Max versions  # noqa: E501

        :return: The max_versions of this UpdateAccountSettings.  # noqa: E501
        :rtype: str
        """
        return self._max_versions

    @max_versions.setter
    def max_versions(self, max_versions):
        """Sets the max_versions of this UpdateAccountSettings.

        Max versions  # noqa: E501

        :param max_versions: The max_versions of this UpdateAccountSettings.  # noqa: E501
        :type: str
        """

        self._max_versions = max_versions

    @property
    def password_length(self):
        """Gets the password_length of this UpdateAccountSettings.  # noqa: E501

        Password length between 5 - to 50 characters  # noqa: E501

        :return: The password_length of this UpdateAccountSettings.  # noqa: E501
        :rtype: int
        """
        return self._password_length

    @password_length.setter
    def password_length(self, password_length):
        """Sets the password_length of this UpdateAccountSettings.

        Password length between 5 - to 50 characters  # noqa: E501

        :param password_length: The password_length of this UpdateAccountSettings.  # noqa: E501
        :type: int
        """

        self._password_length = password_length

    @property
    def phone(self):
        """Gets the phone of this UpdateAccountSettings.  # noqa: E501

        Phone number  # noqa: E501

        :return: The phone of this UpdateAccountSettings.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this UpdateAccountSettings.

        Phone number  # noqa: E501

        :param phone: The phone of this UpdateAccountSettings.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def postal_code(self):
        """Gets the postal_code of this UpdateAccountSettings.  # noqa: E501

        Postal code  # noqa: E501

        :return: The postal_code of this UpdateAccountSettings.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this UpdateAccountSettings.

        Postal code  # noqa: E501

        :param postal_code: The postal_code of this UpdateAccountSettings.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def token(self):
        """Gets the token of this UpdateAccountSettings.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this UpdateAccountSettings.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this UpdateAccountSettings.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this UpdateAccountSettings.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this UpdateAccountSettings.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this UpdateAccountSettings.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this UpdateAccountSettings.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this UpdateAccountSettings.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def use_lower_letters(self):
        """Gets the use_lower_letters of this UpdateAccountSettings.  # noqa: E501

        Password must contain lower case letters [true/false]  # noqa: E501

        :return: The use_lower_letters of this UpdateAccountSettings.  # noqa: E501
        :rtype: str
        """
        return self._use_lower_letters

    @use_lower_letters.setter
    def use_lower_letters(self, use_lower_letters):
        """Sets the use_lower_letters of this UpdateAccountSettings.

        Password must contain lower case letters [true/false]  # noqa: E501

        :param use_lower_letters: The use_lower_letters of this UpdateAccountSettings.  # noqa: E501
        :type: str
        """

        self._use_lower_letters = use_lower_letters

    @property
    def use_numbers(self):
        """Gets the use_numbers of this UpdateAccountSettings.  # noqa: E501

        Password must contain numbers [true/false]  # noqa: E501

        :return: The use_numbers of this UpdateAccountSettings.  # noqa: E501
        :rtype: str
        """
        return self._use_numbers

    @use_numbers.setter
    def use_numbers(self, use_numbers):
        """Sets the use_numbers of this UpdateAccountSettings.

        Password must contain numbers [true/false]  # noqa: E501

        :param use_numbers: The use_numbers of this UpdateAccountSettings.  # noqa: E501
        :type: str
        """

        self._use_numbers = use_numbers

    @property
    def use_special_characters(self):
        """Gets the use_special_characters of this UpdateAccountSettings.  # noqa: E501

        Password must contain special characters [true/false]  # noqa: E501

        :return: The use_special_characters of this UpdateAccountSettings.  # noqa: E501
        :rtype: str
        """
        return self._use_special_characters

    @use_special_characters.setter
    def use_special_characters(self, use_special_characters):
        """Sets the use_special_characters of this UpdateAccountSettings.

        Password must contain special characters [true/false]  # noqa: E501

        :param use_special_characters: The use_special_characters of this UpdateAccountSettings.  # noqa: E501
        :type: str
        """

        self._use_special_characters = use_special_characters

    @property
    def use_capital_letters(self):
        """Gets the use_capital_letters of this UpdateAccountSettings.  # noqa: E501

        Password must contain capital letters [true/false]  # noqa: E501

        :return: The use_capital_letters of this UpdateAccountSettings.  # noqa: E501
        :rtype: str
        """
        return self._use_capital_letters

    @use_capital_letters.setter
    def use_capital_letters(self, use_capital_letters):
        """Sets the use_capital_letters of this UpdateAccountSettings.

        Password must contain capital letters [true/false]  # noqa: E501

        :param use_capital_letters: The use_capital_letters of this UpdateAccountSettings.  # noqa: E501
        :type: str
        """

        self._use_capital_letters = use_capital_letters

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
        if not isinstance(other, UpdateAccountSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateAccountSettings):
            return True

        return self.to_dict() != other.to_dict()
