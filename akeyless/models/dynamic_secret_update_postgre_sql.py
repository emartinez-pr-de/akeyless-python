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


class DynamicSecretUpdatePostgreSql(object):
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
        'creation_statements': 'str',
        'delete_protection': 'str',
        'description': 'str',
        'json': 'bool',
        'name': 'str',
        'new_name': 'str',
        'password_length': 'str',
        'postgresql_db_name': 'str',
        'postgresql_host': 'str',
        'postgresql_password': 'str',
        'postgresql_port': 'str',
        'postgresql_username': 'str',
        'producer_encryption_key': 'str',
        'revocation_statement': 'str',
        'secure_access_bastion_issuer': 'str',
        'secure_access_db_schema': 'str',
        'secure_access_enable': 'str',
        'secure_access_host': 'list[str]',
        'secure_access_web': 'bool',
        'ssl': 'bool',
        'tags': 'list[str]',
        'target_name': 'str',
        'token': 'str',
        'uid_token': 'str',
        'user_ttl': 'str'
    }

    attribute_map = {
        'creation_statements': 'creation-statements',
        'delete_protection': 'delete_protection',
        'description': 'description',
        'json': 'json',
        'name': 'name',
        'new_name': 'new-name',
        'password_length': 'password-length',
        'postgresql_db_name': 'postgresql-db-name',
        'postgresql_host': 'postgresql-host',
        'postgresql_password': 'postgresql-password',
        'postgresql_port': 'postgresql-port',
        'postgresql_username': 'postgresql-username',
        'producer_encryption_key': 'producer-encryption-key',
        'revocation_statement': 'revocation-statement',
        'secure_access_bastion_issuer': 'secure-access-bastion-issuer',
        'secure_access_db_schema': 'secure-access-db-schema',
        'secure_access_enable': 'secure-access-enable',
        'secure_access_host': 'secure-access-host',
        'secure_access_web': 'secure-access-web',
        'ssl': 'ssl',
        'tags': 'tags',
        'target_name': 'target-name',
        'token': 'token',
        'uid_token': 'uid-token',
        'user_ttl': 'user-ttl'
    }

    def __init__(self, creation_statements=None, delete_protection=None, description=None, json=False, name=None, new_name=None, password_length=None, postgresql_db_name=None, postgresql_host='127.0.0.1', postgresql_password=None, postgresql_port='5432', postgresql_username=None, producer_encryption_key=None, revocation_statement=None, secure_access_bastion_issuer=None, secure_access_db_schema=None, secure_access_enable=None, secure_access_host=None, secure_access_web=False, ssl=False, tags=None, target_name=None, token=None, uid_token=None, user_ttl='60m', local_vars_configuration=None):  # noqa: E501
        """DynamicSecretUpdatePostgreSql - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._creation_statements = None
        self._delete_protection = None
        self._description = None
        self._json = None
        self._name = None
        self._new_name = None
        self._password_length = None
        self._postgresql_db_name = None
        self._postgresql_host = None
        self._postgresql_password = None
        self._postgresql_port = None
        self._postgresql_username = None
        self._producer_encryption_key = None
        self._revocation_statement = None
        self._secure_access_bastion_issuer = None
        self._secure_access_db_schema = None
        self._secure_access_enable = None
        self._secure_access_host = None
        self._secure_access_web = None
        self._ssl = None
        self._tags = None
        self._target_name = None
        self._token = None
        self._uid_token = None
        self._user_ttl = None
        self.discriminator = None

        if creation_statements is not None:
            self.creation_statements = creation_statements
        if delete_protection is not None:
            self.delete_protection = delete_protection
        if description is not None:
            self.description = description
        if json is not None:
            self.json = json
        self.name = name
        if new_name is not None:
            self.new_name = new_name
        if password_length is not None:
            self.password_length = password_length
        if postgresql_db_name is not None:
            self.postgresql_db_name = postgresql_db_name
        if postgresql_host is not None:
            self.postgresql_host = postgresql_host
        if postgresql_password is not None:
            self.postgresql_password = postgresql_password
        if postgresql_port is not None:
            self.postgresql_port = postgresql_port
        if postgresql_username is not None:
            self.postgresql_username = postgresql_username
        if producer_encryption_key is not None:
            self.producer_encryption_key = producer_encryption_key
        if revocation_statement is not None:
            self.revocation_statement = revocation_statement
        if secure_access_bastion_issuer is not None:
            self.secure_access_bastion_issuer = secure_access_bastion_issuer
        if secure_access_db_schema is not None:
            self.secure_access_db_schema = secure_access_db_schema
        if secure_access_enable is not None:
            self.secure_access_enable = secure_access_enable
        if secure_access_host is not None:
            self.secure_access_host = secure_access_host
        if secure_access_web is not None:
            self.secure_access_web = secure_access_web
        if ssl is not None:
            self.ssl = ssl
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

    @property
    def creation_statements(self):
        """Gets the creation_statements of this DynamicSecretUpdatePostgreSql.  # noqa: E501

        PostgreSQL Creation statements  # noqa: E501

        :return: The creation_statements of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :rtype: str
        """
        return self._creation_statements

    @creation_statements.setter
    def creation_statements(self, creation_statements):
        """Sets the creation_statements of this DynamicSecretUpdatePostgreSql.

        PostgreSQL Creation statements  # noqa: E501

        :param creation_statements: The creation_statements of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :type: str
        """

        self._creation_statements = creation_statements

    @property
    def delete_protection(self):
        """Gets the delete_protection of this DynamicSecretUpdatePostgreSql.  # noqa: E501

        Protection from accidental deletion of this item [true/false]  # noqa: E501

        :return: The delete_protection of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :rtype: str
        """
        return self._delete_protection

    @delete_protection.setter
    def delete_protection(self, delete_protection):
        """Sets the delete_protection of this DynamicSecretUpdatePostgreSql.

        Protection from accidental deletion of this item [true/false]  # noqa: E501

        :param delete_protection: The delete_protection of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :type: str
        """

        self._delete_protection = delete_protection

    @property
    def description(self):
        """Gets the description of this DynamicSecretUpdatePostgreSql.  # noqa: E501

        Description of the object  # noqa: E501

        :return: The description of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DynamicSecretUpdatePostgreSql.

        Description of the object  # noqa: E501

        :param description: The description of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def json(self):
        """Gets the json of this DynamicSecretUpdatePostgreSql.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this DynamicSecretUpdatePostgreSql.

        Set output format to JSON  # noqa: E501

        :param json: The json of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def name(self):
        """Gets the name of this DynamicSecretUpdatePostgreSql.  # noqa: E501

        Dynamic secret name  # noqa: E501

        :return: The name of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DynamicSecretUpdatePostgreSql.

        Dynamic secret name  # noqa: E501

        :param name: The name of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def new_name(self):
        """Gets the new_name of this DynamicSecretUpdatePostgreSql.  # noqa: E501

        Dynamic secret name  # noqa: E501

        :return: The new_name of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this DynamicSecretUpdatePostgreSql.

        Dynamic secret name  # noqa: E501

        :param new_name: The new_name of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :type: str
        """

        self._new_name = new_name

    @property
    def password_length(self):
        """Gets the password_length of this DynamicSecretUpdatePostgreSql.  # noqa: E501

        The length of the password to be generated  # noqa: E501

        :return: The password_length of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :rtype: str
        """
        return self._password_length

    @password_length.setter
    def password_length(self, password_length):
        """Sets the password_length of this DynamicSecretUpdatePostgreSql.

        The length of the password to be generated  # noqa: E501

        :param password_length: The password_length of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :type: str
        """

        self._password_length = password_length

    @property
    def postgresql_db_name(self):
        """Gets the postgresql_db_name of this DynamicSecretUpdatePostgreSql.  # noqa: E501

        PostgreSQL DB Name  # noqa: E501

        :return: The postgresql_db_name of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :rtype: str
        """
        return self._postgresql_db_name

    @postgresql_db_name.setter
    def postgresql_db_name(self, postgresql_db_name):
        """Sets the postgresql_db_name of this DynamicSecretUpdatePostgreSql.

        PostgreSQL DB Name  # noqa: E501

        :param postgresql_db_name: The postgresql_db_name of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :type: str
        """

        self._postgresql_db_name = postgresql_db_name

    @property
    def postgresql_host(self):
        """Gets the postgresql_host of this DynamicSecretUpdatePostgreSql.  # noqa: E501

        PostgreSQL Host  # noqa: E501

        :return: The postgresql_host of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :rtype: str
        """
        return self._postgresql_host

    @postgresql_host.setter
    def postgresql_host(self, postgresql_host):
        """Sets the postgresql_host of this DynamicSecretUpdatePostgreSql.

        PostgreSQL Host  # noqa: E501

        :param postgresql_host: The postgresql_host of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :type: str
        """

        self._postgresql_host = postgresql_host

    @property
    def postgresql_password(self):
        """Gets the postgresql_password of this DynamicSecretUpdatePostgreSql.  # noqa: E501

        PostgreSQL Password  # noqa: E501

        :return: The postgresql_password of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :rtype: str
        """
        return self._postgresql_password

    @postgresql_password.setter
    def postgresql_password(self, postgresql_password):
        """Sets the postgresql_password of this DynamicSecretUpdatePostgreSql.

        PostgreSQL Password  # noqa: E501

        :param postgresql_password: The postgresql_password of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :type: str
        """

        self._postgresql_password = postgresql_password

    @property
    def postgresql_port(self):
        """Gets the postgresql_port of this DynamicSecretUpdatePostgreSql.  # noqa: E501

        PostgreSQL Port  # noqa: E501

        :return: The postgresql_port of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :rtype: str
        """
        return self._postgresql_port

    @postgresql_port.setter
    def postgresql_port(self, postgresql_port):
        """Sets the postgresql_port of this DynamicSecretUpdatePostgreSql.

        PostgreSQL Port  # noqa: E501

        :param postgresql_port: The postgresql_port of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :type: str
        """

        self._postgresql_port = postgresql_port

    @property
    def postgresql_username(self):
        """Gets the postgresql_username of this DynamicSecretUpdatePostgreSql.  # noqa: E501

        PostgreSQL Username  # noqa: E501

        :return: The postgresql_username of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :rtype: str
        """
        return self._postgresql_username

    @postgresql_username.setter
    def postgresql_username(self, postgresql_username):
        """Sets the postgresql_username of this DynamicSecretUpdatePostgreSql.

        PostgreSQL Username  # noqa: E501

        :param postgresql_username: The postgresql_username of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :type: str
        """

        self._postgresql_username = postgresql_username

    @property
    def producer_encryption_key(self):
        """Gets the producer_encryption_key of this DynamicSecretUpdatePostgreSql.  # noqa: E501

        Dynamic producer encryption key  # noqa: E501

        :return: The producer_encryption_key of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :rtype: str
        """
        return self._producer_encryption_key

    @producer_encryption_key.setter
    def producer_encryption_key(self, producer_encryption_key):
        """Sets the producer_encryption_key of this DynamicSecretUpdatePostgreSql.

        Dynamic producer encryption key  # noqa: E501

        :param producer_encryption_key: The producer_encryption_key of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :type: str
        """

        self._producer_encryption_key = producer_encryption_key

    @property
    def revocation_statement(self):
        """Gets the revocation_statement of this DynamicSecretUpdatePostgreSql.  # noqa: E501

        PostgreSQL Revocation statements  # noqa: E501

        :return: The revocation_statement of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :rtype: str
        """
        return self._revocation_statement

    @revocation_statement.setter
    def revocation_statement(self, revocation_statement):
        """Sets the revocation_statement of this DynamicSecretUpdatePostgreSql.

        PostgreSQL Revocation statements  # noqa: E501

        :param revocation_statement: The revocation_statement of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :type: str
        """

        self._revocation_statement = revocation_statement

    @property
    def secure_access_bastion_issuer(self):
        """Gets the secure_access_bastion_issuer of this DynamicSecretUpdatePostgreSql.  # noqa: E501

        Path to the SSH Certificate Issuer for your Akeyless Bastion  # noqa: E501

        :return: The secure_access_bastion_issuer of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_bastion_issuer

    @secure_access_bastion_issuer.setter
    def secure_access_bastion_issuer(self, secure_access_bastion_issuer):
        """Sets the secure_access_bastion_issuer of this DynamicSecretUpdatePostgreSql.

        Path to the SSH Certificate Issuer for your Akeyless Bastion  # noqa: E501

        :param secure_access_bastion_issuer: The secure_access_bastion_issuer of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :type: str
        """

        self._secure_access_bastion_issuer = secure_access_bastion_issuer

    @property
    def secure_access_db_schema(self):
        """Gets the secure_access_db_schema of this DynamicSecretUpdatePostgreSql.  # noqa: E501

        The DB schema  # noqa: E501

        :return: The secure_access_db_schema of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_db_schema

    @secure_access_db_schema.setter
    def secure_access_db_schema(self, secure_access_db_schema):
        """Sets the secure_access_db_schema of this DynamicSecretUpdatePostgreSql.

        The DB schema  # noqa: E501

        :param secure_access_db_schema: The secure_access_db_schema of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :type: str
        """

        self._secure_access_db_schema = secure_access_db_schema

    @property
    def secure_access_enable(self):
        """Gets the secure_access_enable of this DynamicSecretUpdatePostgreSql.  # noqa: E501

        Enable/Disable secure remote access [true/false]  # noqa: E501

        :return: The secure_access_enable of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_enable

    @secure_access_enable.setter
    def secure_access_enable(self, secure_access_enable):
        """Sets the secure_access_enable of this DynamicSecretUpdatePostgreSql.

        Enable/Disable secure remote access [true/false]  # noqa: E501

        :param secure_access_enable: The secure_access_enable of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :type: str
        """

        self._secure_access_enable = secure_access_enable

    @property
    def secure_access_host(self):
        """Gets the secure_access_host of this DynamicSecretUpdatePostgreSql.  # noqa: E501

        Target DB servers for connections (In case of Linked Target association, host(s) will inherit Linked Target hosts)  # noqa: E501

        :return: The secure_access_host of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :rtype: list[str]
        """
        return self._secure_access_host

    @secure_access_host.setter
    def secure_access_host(self, secure_access_host):
        """Sets the secure_access_host of this DynamicSecretUpdatePostgreSql.

        Target DB servers for connections (In case of Linked Target association, host(s) will inherit Linked Target hosts)  # noqa: E501

        :param secure_access_host: The secure_access_host of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :type: list[str]
        """

        self._secure_access_host = secure_access_host

    @property
    def secure_access_web(self):
        """Gets the secure_access_web of this DynamicSecretUpdatePostgreSql.  # noqa: E501

        Enable Web Secure Remote Access  # noqa: E501

        :return: The secure_access_web of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :rtype: bool
        """
        return self._secure_access_web

    @secure_access_web.setter
    def secure_access_web(self, secure_access_web):
        """Sets the secure_access_web of this DynamicSecretUpdatePostgreSql.

        Enable Web Secure Remote Access  # noqa: E501

        :param secure_access_web: The secure_access_web of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :type: bool
        """

        self._secure_access_web = secure_access_web

    @property
    def ssl(self):
        """Gets the ssl of this DynamicSecretUpdatePostgreSql.  # noqa: E501

        Enable/Disable SSL [true/false]  # noqa: E501

        :return: The ssl of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :rtype: bool
        """
        return self._ssl

    @ssl.setter
    def ssl(self, ssl):
        """Sets the ssl of this DynamicSecretUpdatePostgreSql.

        Enable/Disable SSL [true/false]  # noqa: E501

        :param ssl: The ssl of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :type: bool
        """

        self._ssl = ssl

    @property
    def tags(self):
        """Gets the tags of this DynamicSecretUpdatePostgreSql.  # noqa: E501

        Add tags attached to this object  # noqa: E501

        :return: The tags of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DynamicSecretUpdatePostgreSql.

        Add tags attached to this object  # noqa: E501

        :param tags: The tags of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def target_name(self):
        """Gets the target_name of this DynamicSecretUpdatePostgreSql.  # noqa: E501

        Target name  # noqa: E501

        :return: The target_name of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """Sets the target_name of this DynamicSecretUpdatePostgreSql.

        Target name  # noqa: E501

        :param target_name: The target_name of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :type: str
        """

        self._target_name = target_name

    @property
    def token(self):
        """Gets the token of this DynamicSecretUpdatePostgreSql.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this DynamicSecretUpdatePostgreSql.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this DynamicSecretUpdatePostgreSql.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this DynamicSecretUpdatePostgreSql.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def user_ttl(self):
        """Gets the user_ttl of this DynamicSecretUpdatePostgreSql.  # noqa: E501

        User TTL  # noqa: E501

        :return: The user_ttl of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :rtype: str
        """
        return self._user_ttl

    @user_ttl.setter
    def user_ttl(self, user_ttl):
        """Sets the user_ttl of this DynamicSecretUpdatePostgreSql.

        User TTL  # noqa: E501

        :param user_ttl: The user_ttl of this DynamicSecretUpdatePostgreSql.  # noqa: E501
        :type: str
        """

        self._user_ttl = user_ttl

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
        if not isinstance(other, DynamicSecretUpdatePostgreSql):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DynamicSecretUpdatePostgreSql):
            return True

        return self.to_dict() != other.to_dict()
