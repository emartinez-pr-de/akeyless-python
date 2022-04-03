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


class GetAccountSettingsCommandOutput(object):
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
        'account_id': 'str',
        'address': 'CustomerFullAddress',
        'company_name': 'str',
        'email': 'str',
        'object_version_settings': 'AccountObjectVersionSettingsOutput',
        'phone': 'str',
        'secret_management': 'SmInfo',
        'secure_remote_access': 'SraInfo',
        'system_access_creds_settings': 'SystemAccessCredsSettings'
    }

    attribute_map = {
        'account_id': 'account_id',
        'address': 'address',
        'company_name': 'company_name',
        'email': 'email',
        'object_version_settings': 'object_version_settings',
        'phone': 'phone',
        'secret_management': 'secret_management',
        'secure_remote_access': 'secure_remote_access',
        'system_access_creds_settings': 'system_access_creds_settings'
    }

    def __init__(self, account_id=None, address=None, company_name=None, email=None, object_version_settings=None, phone=None, secret_management=None, secure_remote_access=None, system_access_creds_settings=None, local_vars_configuration=None):  # noqa: E501
        """GetAccountSettingsCommandOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._address = None
        self._company_name = None
        self._email = None
        self._object_version_settings = None
        self._phone = None
        self._secret_management = None
        self._secure_remote_access = None
        self._system_access_creds_settings = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if address is not None:
            self.address = address
        if company_name is not None:
            self.company_name = company_name
        if email is not None:
            self.email = email
        if object_version_settings is not None:
            self.object_version_settings = object_version_settings
        if phone is not None:
            self.phone = phone
        if secret_management is not None:
            self.secret_management = secret_management
        if secure_remote_access is not None:
            self.secure_remote_access = secure_remote_access
        if system_access_creds_settings is not None:
            self.system_access_creds_settings = system_access_creds_settings

    @property
    def account_id(self):
        """Gets the account_id of this GetAccountSettingsCommandOutput.  # noqa: E501


        :return: The account_id of this GetAccountSettingsCommandOutput.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this GetAccountSettingsCommandOutput.


        :param account_id: The account_id of this GetAccountSettingsCommandOutput.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def address(self):
        """Gets the address of this GetAccountSettingsCommandOutput.  # noqa: E501


        :return: The address of this GetAccountSettingsCommandOutput.  # noqa: E501
        :rtype: CustomerFullAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this GetAccountSettingsCommandOutput.


        :param address: The address of this GetAccountSettingsCommandOutput.  # noqa: E501
        :type: CustomerFullAddress
        """

        self._address = address

    @property
    def company_name(self):
        """Gets the company_name of this GetAccountSettingsCommandOutput.  # noqa: E501


        :return: The company_name of this GetAccountSettingsCommandOutput.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this GetAccountSettingsCommandOutput.


        :param company_name: The company_name of this GetAccountSettingsCommandOutput.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def email(self):
        """Gets the email of this GetAccountSettingsCommandOutput.  # noqa: E501


        :return: The email of this GetAccountSettingsCommandOutput.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this GetAccountSettingsCommandOutput.


        :param email: The email of this GetAccountSettingsCommandOutput.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def object_version_settings(self):
        """Gets the object_version_settings of this GetAccountSettingsCommandOutput.  # noqa: E501


        :return: The object_version_settings of this GetAccountSettingsCommandOutput.  # noqa: E501
        :rtype: AccountObjectVersionSettingsOutput
        """
        return self._object_version_settings

    @object_version_settings.setter
    def object_version_settings(self, object_version_settings):
        """Sets the object_version_settings of this GetAccountSettingsCommandOutput.


        :param object_version_settings: The object_version_settings of this GetAccountSettingsCommandOutput.  # noqa: E501
        :type: AccountObjectVersionSettingsOutput
        """

        self._object_version_settings = object_version_settings

    @property
    def phone(self):
        """Gets the phone of this GetAccountSettingsCommandOutput.  # noqa: E501


        :return: The phone of this GetAccountSettingsCommandOutput.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this GetAccountSettingsCommandOutput.


        :param phone: The phone of this GetAccountSettingsCommandOutput.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def secret_management(self):
        """Gets the secret_management of this GetAccountSettingsCommandOutput.  # noqa: E501


        :return: The secret_management of this GetAccountSettingsCommandOutput.  # noqa: E501
        :rtype: SmInfo
        """
        return self._secret_management

    @secret_management.setter
    def secret_management(self, secret_management):
        """Sets the secret_management of this GetAccountSettingsCommandOutput.


        :param secret_management: The secret_management of this GetAccountSettingsCommandOutput.  # noqa: E501
        :type: SmInfo
        """

        self._secret_management = secret_management

    @property
    def secure_remote_access(self):
        """Gets the secure_remote_access of this GetAccountSettingsCommandOutput.  # noqa: E501


        :return: The secure_remote_access of this GetAccountSettingsCommandOutput.  # noqa: E501
        :rtype: SraInfo
        """
        return self._secure_remote_access

    @secure_remote_access.setter
    def secure_remote_access(self, secure_remote_access):
        """Sets the secure_remote_access of this GetAccountSettingsCommandOutput.


        :param secure_remote_access: The secure_remote_access of this GetAccountSettingsCommandOutput.  # noqa: E501
        :type: SraInfo
        """

        self._secure_remote_access = secure_remote_access

    @property
    def system_access_creds_settings(self):
        """Gets the system_access_creds_settings of this GetAccountSettingsCommandOutput.  # noqa: E501


        :return: The system_access_creds_settings of this GetAccountSettingsCommandOutput.  # noqa: E501
        :rtype: SystemAccessCredsSettings
        """
        return self._system_access_creds_settings

    @system_access_creds_settings.setter
    def system_access_creds_settings(self, system_access_creds_settings):
        """Sets the system_access_creds_settings of this GetAccountSettingsCommandOutput.


        :param system_access_creds_settings: The system_access_creds_settings of this GetAccountSettingsCommandOutput.  # noqa: E501
        :type: SystemAccessCredsSettings
        """

        self._system_access_creds_settings = system_access_creds_settings

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
        if not isinstance(other, GetAccountSettingsCommandOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetAccountSettingsCommandOutput):
            return True

        return self.to_dict() != other.to_dict()