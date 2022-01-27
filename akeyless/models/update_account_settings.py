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
        'jwt_ttl_default': 'int',
        'jwt_ttl_max': 'int',
        'jwt_ttl_min': 'int',
        'password': 'str',
        'phone': 'str',
        'postal_code': 'str',
        'token': 'str',
        'uid_token': 'str',
        'username': 'str'
    }

    attribute_map = {
        'address': 'address',
        'city': 'city',
        'company_name': 'company-name',
        'country': 'country',
        'jwt_ttl_default': 'jwt-ttl-default',
        'jwt_ttl_max': 'jwt-ttl-max',
        'jwt_ttl_min': 'jwt-ttl-min',
        'password': 'password',
        'phone': 'phone',
        'postal_code': 'postal-code',
        'token': 'token',
        'uid_token': 'uid-token',
        'username': 'username'
    }

    def __init__(self, address=None, city=None, company_name=None, country=None, jwt_ttl_default=None, jwt_ttl_max=None, jwt_ttl_min=None, password=None, phone=None, postal_code=None, token=None, uid_token=None, username=None, local_vars_configuration=None):  # noqa: E501
        """UpdateAccountSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._address = None
        self._city = None
        self._company_name = None
        self._country = None
        self._jwt_ttl_default = None
        self._jwt_ttl_max = None
        self._jwt_ttl_min = None
        self._password = None
        self._phone = None
        self._postal_code = None
        self._token = None
        self._uid_token = None
        self._username = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if city is not None:
            self.city = city
        if company_name is not None:
            self.company_name = company_name
        if country is not None:
            self.country = country
        if jwt_ttl_default is not None:
            self.jwt_ttl_default = jwt_ttl_default
        if jwt_ttl_max is not None:
            self.jwt_ttl_max = jwt_ttl_max
        if jwt_ttl_min is not None:
            self.jwt_ttl_min = jwt_ttl_min
        if password is not None:
            self.password = password
        if phone is not None:
            self.phone = phone
        if postal_code is not None:
            self.postal_code = postal_code
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if username is not None:
            self.username = username

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
    def password(self):
        """Gets the password of this UpdateAccountSettings.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The password of this UpdateAccountSettings.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UpdateAccountSettings.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param password: The password of this UpdateAccountSettings.  # noqa: E501
        :type: str
        """

        self._password = password

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
    def username(self):
        """Gets the username of this UpdateAccountSettings.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The username of this UpdateAccountSettings.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UpdateAccountSettings.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param username: The username of this UpdateAccountSettings.  # noqa: E501
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
        if not isinstance(other, UpdateAccountSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateAccountSettings):
            return True

        return self.to_dict() != other.to_dict()
