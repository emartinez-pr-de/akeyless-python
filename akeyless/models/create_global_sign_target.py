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


class CreateGlobalSignTarget(object):
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
        'comment': 'str',
        'contact_email': 'str',
        'contact_first_name': 'str',
        'contact_last_name': 'str',
        'contact_phone': 'str',
        'description': 'str',
        'json': 'bool',
        'key': 'str',
        'max_versions': 'str',
        'name': 'str',
        'password': 'str',
        'profile_id': 'str',
        'timeout': 'str',
        'token': 'str',
        'uid_token': 'str',
        'username': 'str'
    }

    attribute_map = {
        'comment': 'comment',
        'contact_email': 'contact-email',
        'contact_first_name': 'contact-first-name',
        'contact_last_name': 'contact-last-name',
        'contact_phone': 'contact-phone',
        'description': 'description',
        'json': 'json',
        'key': 'key',
        'max_versions': 'max-versions',
        'name': 'name',
        'password': 'password',
        'profile_id': 'profile-id',
        'timeout': 'timeout',
        'token': 'token',
        'uid_token': 'uid-token',
        'username': 'username'
    }

    def __init__(self, comment=None, contact_email=None, contact_first_name=None, contact_last_name=None, contact_phone=None, description=None, json=False, key=None, max_versions=None, name=None, password=None, profile_id=None, timeout='5m', token=None, uid_token=None, username=None, local_vars_configuration=None):  # noqa: E501
        """CreateGlobalSignTarget - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._comment = None
        self._contact_email = None
        self._contact_first_name = None
        self._contact_last_name = None
        self._contact_phone = None
        self._description = None
        self._json = None
        self._key = None
        self._max_versions = None
        self._name = None
        self._password = None
        self._profile_id = None
        self._timeout = None
        self._token = None
        self._uid_token = None
        self._username = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        self.contact_email = contact_email
        self.contact_first_name = contact_first_name
        self.contact_last_name = contact_last_name
        self.contact_phone = contact_phone
        if description is not None:
            self.description = description
        if json is not None:
            self.json = json
        if key is not None:
            self.key = key
        if max_versions is not None:
            self.max_versions = max_versions
        self.name = name
        self.password = password
        self.profile_id = profile_id
        if timeout is not None:
            self.timeout = timeout
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        self.username = username

    @property
    def comment(self):
        """Gets the comment of this CreateGlobalSignTarget.  # noqa: E501

        Deprecated - use description  # noqa: E501

        :return: The comment of this CreateGlobalSignTarget.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this CreateGlobalSignTarget.

        Deprecated - use description  # noqa: E501

        :param comment: The comment of this CreateGlobalSignTarget.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def contact_email(self):
        """Gets the contact_email of this CreateGlobalSignTarget.  # noqa: E501

        Email of the GlobalSign GCC account contact  # noqa: E501

        :return: The contact_email of this CreateGlobalSignTarget.  # noqa: E501
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """Sets the contact_email of this CreateGlobalSignTarget.

        Email of the GlobalSign GCC account contact  # noqa: E501

        :param contact_email: The contact_email of this CreateGlobalSignTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and contact_email is None:  # noqa: E501
            raise ValueError("Invalid value for `contact_email`, must not be `None`")  # noqa: E501

        self._contact_email = contact_email

    @property
    def contact_first_name(self):
        """Gets the contact_first_name of this CreateGlobalSignTarget.  # noqa: E501

        First name of the GlobalSign GCC account contact  # noqa: E501

        :return: The contact_first_name of this CreateGlobalSignTarget.  # noqa: E501
        :rtype: str
        """
        return self._contact_first_name

    @contact_first_name.setter
    def contact_first_name(self, contact_first_name):
        """Sets the contact_first_name of this CreateGlobalSignTarget.

        First name of the GlobalSign GCC account contact  # noqa: E501

        :param contact_first_name: The contact_first_name of this CreateGlobalSignTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and contact_first_name is None:  # noqa: E501
            raise ValueError("Invalid value for `contact_first_name`, must not be `None`")  # noqa: E501

        self._contact_first_name = contact_first_name

    @property
    def contact_last_name(self):
        """Gets the contact_last_name of this CreateGlobalSignTarget.  # noqa: E501

        Last name of the GlobalSign GCC account contact  # noqa: E501

        :return: The contact_last_name of this CreateGlobalSignTarget.  # noqa: E501
        :rtype: str
        """
        return self._contact_last_name

    @contact_last_name.setter
    def contact_last_name(self, contact_last_name):
        """Sets the contact_last_name of this CreateGlobalSignTarget.

        Last name of the GlobalSign GCC account contact  # noqa: E501

        :param contact_last_name: The contact_last_name of this CreateGlobalSignTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and contact_last_name is None:  # noqa: E501
            raise ValueError("Invalid value for `contact_last_name`, must not be `None`")  # noqa: E501

        self._contact_last_name = contact_last_name

    @property
    def contact_phone(self):
        """Gets the contact_phone of this CreateGlobalSignTarget.  # noqa: E501

        Telephone of the GlobalSign GCC account contact  # noqa: E501

        :return: The contact_phone of this CreateGlobalSignTarget.  # noqa: E501
        :rtype: str
        """
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, contact_phone):
        """Sets the contact_phone of this CreateGlobalSignTarget.

        Telephone of the GlobalSign GCC account contact  # noqa: E501

        :param contact_phone: The contact_phone of this CreateGlobalSignTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and contact_phone is None:  # noqa: E501
            raise ValueError("Invalid value for `contact_phone`, must not be `None`")  # noqa: E501

        self._contact_phone = contact_phone

    @property
    def description(self):
        """Gets the description of this CreateGlobalSignTarget.  # noqa: E501

        Description of the object  # noqa: E501

        :return: The description of this CreateGlobalSignTarget.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateGlobalSignTarget.

        Description of the object  # noqa: E501

        :param description: The description of this CreateGlobalSignTarget.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def json(self):
        """Gets the json of this CreateGlobalSignTarget.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this CreateGlobalSignTarget.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this CreateGlobalSignTarget.

        Set output format to JSON  # noqa: E501

        :param json: The json of this CreateGlobalSignTarget.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def key(self):
        """Gets the key of this CreateGlobalSignTarget.  # noqa: E501

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :return: The key of this CreateGlobalSignTarget.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CreateGlobalSignTarget.

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :param key: The key of this CreateGlobalSignTarget.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def max_versions(self):
        """Gets the max_versions of this CreateGlobalSignTarget.  # noqa: E501

        Set the maximum number of versions, limited by the account settings defaults.  # noqa: E501

        :return: The max_versions of this CreateGlobalSignTarget.  # noqa: E501
        :rtype: str
        """
        return self._max_versions

    @max_versions.setter
    def max_versions(self, max_versions):
        """Sets the max_versions of this CreateGlobalSignTarget.

        Set the maximum number of versions, limited by the account settings defaults.  # noqa: E501

        :param max_versions: The max_versions of this CreateGlobalSignTarget.  # noqa: E501
        :type: str
        """

        self._max_versions = max_versions

    @property
    def name(self):
        """Gets the name of this CreateGlobalSignTarget.  # noqa: E501

        Target name  # noqa: E501

        :return: The name of this CreateGlobalSignTarget.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateGlobalSignTarget.

        Target name  # noqa: E501

        :param name: The name of this CreateGlobalSignTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def password(self):
        """Gets the password of this CreateGlobalSignTarget.  # noqa: E501

        Password of the GlobalSign GCC account  # noqa: E501

        :return: The password of this CreateGlobalSignTarget.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateGlobalSignTarget.

        Password of the GlobalSign GCC account  # noqa: E501

        :param password: The password of this CreateGlobalSignTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and password is None:  # noqa: E501
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def profile_id(self):
        """Gets the profile_id of this CreateGlobalSignTarget.  # noqa: E501

        Profile ID of the GlobalSign GCC account  # noqa: E501

        :return: The profile_id of this CreateGlobalSignTarget.  # noqa: E501
        :rtype: str
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """Sets the profile_id of this CreateGlobalSignTarget.

        Profile ID of the GlobalSign GCC account  # noqa: E501

        :param profile_id: The profile_id of this CreateGlobalSignTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and profile_id is None:  # noqa: E501
            raise ValueError("Invalid value for `profile_id`, must not be `None`")  # noqa: E501

        self._profile_id = profile_id

    @property
    def timeout(self):
        """Gets the timeout of this CreateGlobalSignTarget.  # noqa: E501

        Timeout waiting for certificate validation in Duration format (1h - 1 Hour, 20m - 20 Minutes, 33m3s - 33 Minutes and 3 Seconds), maximum 1h.  # noqa: E501

        :return: The timeout of this CreateGlobalSignTarget.  # noqa: E501
        :rtype: str
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this CreateGlobalSignTarget.

        Timeout waiting for certificate validation in Duration format (1h - 1 Hour, 20m - 20 Minutes, 33m3s - 33 Minutes and 3 Seconds), maximum 1h.  # noqa: E501

        :param timeout: The timeout of this CreateGlobalSignTarget.  # noqa: E501
        :type: str
        """

        self._timeout = timeout

    @property
    def token(self):
        """Gets the token of this CreateGlobalSignTarget.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this CreateGlobalSignTarget.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this CreateGlobalSignTarget.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this CreateGlobalSignTarget.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this CreateGlobalSignTarget.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this CreateGlobalSignTarget.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this CreateGlobalSignTarget.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this CreateGlobalSignTarget.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def username(self):
        """Gets the username of this CreateGlobalSignTarget.  # noqa: E501

        Username of the GlobalSign GCC account  # noqa: E501

        :return: The username of this CreateGlobalSignTarget.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this CreateGlobalSignTarget.

        Username of the GlobalSign GCC account  # noqa: E501

        :param username: The username of this CreateGlobalSignTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and username is None:  # noqa: E501
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, CreateGlobalSignTarget):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateGlobalSignTarget):
            return True

        return self.to_dict() != other.to_dict()
