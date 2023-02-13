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


class GatewayCreateProducerSnowflake(object):
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
        'account': 'str',
        'account_password': 'str',
        'account_username': 'str',
        'db_name': 'str',
        'delete_protection': 'str',
        'json': 'bool',
        'name': 'str',
        'private_key': 'str',
        'private_key_passphrase': 'str',
        'role': 'str',
        'tags': 'list[str]',
        'target_name': 'str',
        'token': 'str',
        'uid_token': 'str',
        'user_ttl': 'str',
        'warehouse': 'str'
    }

    attribute_map = {
        'account': 'account',
        'account_password': 'account-password',
        'account_username': 'account-username',
        'db_name': 'db-name',
        'delete_protection': 'delete_protection',
        'json': 'json',
        'name': 'name',
        'private_key': 'private-key',
        'private_key_passphrase': 'private-key-passphrase',
        'role': 'role',
        'tags': 'tags',
        'target_name': 'target-name',
        'token': 'token',
        'uid_token': 'uid-token',
        'user_ttl': 'user-ttl',
        'warehouse': 'warehouse'
    }

    def __init__(self, account=None, account_password=None, account_username=None, db_name=None, delete_protection=None, json=False, name=None, private_key=None, private_key_passphrase=None, role=None, tags=None, target_name=None, token=None, uid_token=None, user_ttl='24h', warehouse=None, local_vars_configuration=None):  # noqa: E501
        """GatewayCreateProducerSnowflake - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account = None
        self._account_password = None
        self._account_username = None
        self._db_name = None
        self._delete_protection = None
        self._json = None
        self._name = None
        self._private_key = None
        self._private_key_passphrase = None
        self._role = None
        self._tags = None
        self._target_name = None
        self._token = None
        self._uid_token = None
        self._user_ttl = None
        self._warehouse = None
        self.discriminator = None

        if account is not None:
            self.account = account
        if account_password is not None:
            self.account_password = account_password
        if account_username is not None:
            self.account_username = account_username
        if db_name is not None:
            self.db_name = db_name
        if delete_protection is not None:
            self.delete_protection = delete_protection
        if json is not None:
            self.json = json
        self.name = name
        if private_key is not None:
            self.private_key = private_key
        if private_key_passphrase is not None:
            self.private_key_passphrase = private_key_passphrase
        if role is not None:
            self.role = role
        if tags is not None:
            self.tags = tags
        if target_name is not None:
            self.target_name = target_name
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if user_ttl is not None:
            self.user_ttl = user_ttl
        if warehouse is not None:
            self.warehouse = warehouse

    @property
    def account(self):
        """Gets the account of this GatewayCreateProducerSnowflake.  # noqa: E501

        Account name  # noqa: E501

        :return: The account of this GatewayCreateProducerSnowflake.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this GatewayCreateProducerSnowflake.

        Account name  # noqa: E501

        :param account: The account of this GatewayCreateProducerSnowflake.  # noqa: E501
        :type: str
        """

        self._account = account

    @property
    def account_password(self):
        """Gets the account_password of this GatewayCreateProducerSnowflake.  # noqa: E501

        Database Password  # noqa: E501

        :return: The account_password of this GatewayCreateProducerSnowflake.  # noqa: E501
        :rtype: str
        """
        return self._account_password

    @account_password.setter
    def account_password(self, account_password):
        """Sets the account_password of this GatewayCreateProducerSnowflake.

        Database Password  # noqa: E501

        :param account_password: The account_password of this GatewayCreateProducerSnowflake.  # noqa: E501
        :type: str
        """

        self._account_password = account_password

    @property
    def account_username(self):
        """Gets the account_username of this GatewayCreateProducerSnowflake.  # noqa: E501

        Database Username  # noqa: E501

        :return: The account_username of this GatewayCreateProducerSnowflake.  # noqa: E501
        :rtype: str
        """
        return self._account_username

    @account_username.setter
    def account_username(self, account_username):
        """Sets the account_username of this GatewayCreateProducerSnowflake.

        Database Username  # noqa: E501

        :param account_username: The account_username of this GatewayCreateProducerSnowflake.  # noqa: E501
        :type: str
        """

        self._account_username = account_username

    @property
    def db_name(self):
        """Gets the db_name of this GatewayCreateProducerSnowflake.  # noqa: E501

        Database name  # noqa: E501

        :return: The db_name of this GatewayCreateProducerSnowflake.  # noqa: E501
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this GatewayCreateProducerSnowflake.

        Database name  # noqa: E501

        :param db_name: The db_name of this GatewayCreateProducerSnowflake.  # noqa: E501
        :type: str
        """

        self._db_name = db_name

    @property
    def delete_protection(self):
        """Gets the delete_protection of this GatewayCreateProducerSnowflake.  # noqa: E501

        Protection from accidental deletion of this item [true/false]  # noqa: E501

        :return: The delete_protection of this GatewayCreateProducerSnowflake.  # noqa: E501
        :rtype: str
        """
        return self._delete_protection

    @delete_protection.setter
    def delete_protection(self, delete_protection):
        """Sets the delete_protection of this GatewayCreateProducerSnowflake.

        Protection from accidental deletion of this item [true/false]  # noqa: E501

        :param delete_protection: The delete_protection of this GatewayCreateProducerSnowflake.  # noqa: E501
        :type: str
        """

        self._delete_protection = delete_protection

    @property
    def json(self):
        """Gets the json of this GatewayCreateProducerSnowflake.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this GatewayCreateProducerSnowflake.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this GatewayCreateProducerSnowflake.

        Set output format to JSON  # noqa: E501

        :param json: The json of this GatewayCreateProducerSnowflake.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def name(self):
        """Gets the name of this GatewayCreateProducerSnowflake.  # noqa: E501

        Producer name  # noqa: E501

        :return: The name of this GatewayCreateProducerSnowflake.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GatewayCreateProducerSnowflake.

        Producer name  # noqa: E501

        :param name: The name of this GatewayCreateProducerSnowflake.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def private_key(self):
        """Gets the private_key of this GatewayCreateProducerSnowflake.  # noqa: E501

        RSA Private key (base64 encoded)  # noqa: E501

        :return: The private_key of this GatewayCreateProducerSnowflake.  # noqa: E501
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this GatewayCreateProducerSnowflake.

        RSA Private key (base64 encoded)  # noqa: E501

        :param private_key: The private_key of this GatewayCreateProducerSnowflake.  # noqa: E501
        :type: str
        """

        self._private_key = private_key

    @property
    def private_key_passphrase(self):
        """Gets the private_key_passphrase of this GatewayCreateProducerSnowflake.  # noqa: E501

        The Private key passphrase  # noqa: E501

        :return: The private_key_passphrase of this GatewayCreateProducerSnowflake.  # noqa: E501
        :rtype: str
        """
        return self._private_key_passphrase

    @private_key_passphrase.setter
    def private_key_passphrase(self, private_key_passphrase):
        """Sets the private_key_passphrase of this GatewayCreateProducerSnowflake.

        The Private key passphrase  # noqa: E501

        :param private_key_passphrase: The private_key_passphrase of this GatewayCreateProducerSnowflake.  # noqa: E501
        :type: str
        """

        self._private_key_passphrase = private_key_passphrase

    @property
    def role(self):
        """Gets the role of this GatewayCreateProducerSnowflake.  # noqa: E501

        User role  # noqa: E501

        :return: The role of this GatewayCreateProducerSnowflake.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this GatewayCreateProducerSnowflake.

        User role  # noqa: E501

        :param role: The role of this GatewayCreateProducerSnowflake.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def tags(self):
        """Gets the tags of this GatewayCreateProducerSnowflake.  # noqa: E501

        List of the tags attached to this secret  # noqa: E501

        :return: The tags of this GatewayCreateProducerSnowflake.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this GatewayCreateProducerSnowflake.

        List of the tags attached to this secret  # noqa: E501

        :param tags: The tags of this GatewayCreateProducerSnowflake.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def target_name(self):
        """Gets the target_name of this GatewayCreateProducerSnowflake.  # noqa: E501

        Target name  # noqa: E501

        :return: The target_name of this GatewayCreateProducerSnowflake.  # noqa: E501
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """Sets the target_name of this GatewayCreateProducerSnowflake.

        Target name  # noqa: E501

        :param target_name: The target_name of this GatewayCreateProducerSnowflake.  # noqa: E501
        :type: str
        """

        self._target_name = target_name

    @property
    def token(self):
        """Gets the token of this GatewayCreateProducerSnowflake.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GatewayCreateProducerSnowflake.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GatewayCreateProducerSnowflake.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GatewayCreateProducerSnowflake.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this GatewayCreateProducerSnowflake.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GatewayCreateProducerSnowflake.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GatewayCreateProducerSnowflake.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GatewayCreateProducerSnowflake.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def user_ttl(self):
        """Gets the user_ttl of this GatewayCreateProducerSnowflake.  # noqa: E501

        User TTL  # noqa: E501

        :return: The user_ttl of this GatewayCreateProducerSnowflake.  # noqa: E501
        :rtype: str
        """
        return self._user_ttl

    @user_ttl.setter
    def user_ttl(self, user_ttl):
        """Sets the user_ttl of this GatewayCreateProducerSnowflake.

        User TTL  # noqa: E501

        :param user_ttl: The user_ttl of this GatewayCreateProducerSnowflake.  # noqa: E501
        :type: str
        """

        self._user_ttl = user_ttl

    @property
    def warehouse(self):
        """Gets the warehouse of this GatewayCreateProducerSnowflake.  # noqa: E501

        Warehouse name  # noqa: E501

        :return: The warehouse of this GatewayCreateProducerSnowflake.  # noqa: E501
        :rtype: str
        """
        return self._warehouse

    @warehouse.setter
    def warehouse(self, warehouse):
        """Sets the warehouse of this GatewayCreateProducerSnowflake.

        Warehouse name  # noqa: E501

        :param warehouse: The warehouse of this GatewayCreateProducerSnowflake.  # noqa: E501
        :type: str
        """

        self._warehouse = warehouse

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
        if not isinstance(other, GatewayCreateProducerSnowflake):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayCreateProducerSnowflake):
            return True

        return self.to_dict() != other.to_dict()
