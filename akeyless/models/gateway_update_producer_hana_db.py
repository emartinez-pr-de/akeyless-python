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


class GatewayUpdateProducerHanaDb(object):
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
        'hana_dbname': 'str',
        'hanadb_create_statements': 'str',
        'hanadb_host': 'str',
        'hanadb_password': 'str',
        'hanadb_port': 'str',
        'hanadb_revocation_statements': 'str',
        'hanadb_username': 'str',
        'name': 'str',
        'new_name': 'str',
        'producer_encryption_key_name': 'str',
        'secure_access_bastion_issuer': 'str',
        'secure_access_db_schema': 'str',
        'secure_access_enable': 'str',
        'secure_access_host': 'list[str]',
        'secure_access_web': 'bool',
        'tags': 'list[str]',
        'target_name': 'str',
        'token': 'str',
        'uid_token': 'str',
        'user_ttl': 'str'
    }

    attribute_map = {
        'hana_dbname': 'hana-dbname',
        'hanadb_create_statements': 'hanadb-create-statements',
        'hanadb_host': 'hanadb-host',
        'hanadb_password': 'hanadb-password',
        'hanadb_port': 'hanadb-port',
        'hanadb_revocation_statements': 'hanadb-revocation-statements',
        'hanadb_username': 'hanadb-username',
        'name': 'name',
        'new_name': 'new-name',
        'producer_encryption_key_name': 'producer-encryption-key-name',
        'secure_access_bastion_issuer': 'secure-access-bastion-issuer',
        'secure_access_db_schema': 'secure-access-db-schema',
        'secure_access_enable': 'secure-access-enable',
        'secure_access_host': 'secure-access-host',
        'secure_access_web': 'secure-access-web',
        'tags': 'tags',
        'target_name': 'target-name',
        'token': 'token',
        'uid_token': 'uid-token',
        'user_ttl': 'user-ttl'
    }

    def __init__(self, hana_dbname=None, hanadb_create_statements=None, hanadb_host='127.0.0.1', hanadb_password=None, hanadb_port='443', hanadb_revocation_statements=None, hanadb_username=None, name=None, new_name=None, producer_encryption_key_name=None, secure_access_bastion_issuer=None, secure_access_db_schema=None, secure_access_enable=None, secure_access_host=None, secure_access_web=None, tags=None, target_name=None, token=None, uid_token=None, user_ttl='60m', local_vars_configuration=None):  # noqa: E501
        """GatewayUpdateProducerHanaDb - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._hana_dbname = None
        self._hanadb_create_statements = None
        self._hanadb_host = None
        self._hanadb_password = None
        self._hanadb_port = None
        self._hanadb_revocation_statements = None
        self._hanadb_username = None
        self._name = None
        self._new_name = None
        self._producer_encryption_key_name = None
        self._secure_access_bastion_issuer = None
        self._secure_access_db_schema = None
        self._secure_access_enable = None
        self._secure_access_host = None
        self._secure_access_web = None
        self._tags = None
        self._target_name = None
        self._token = None
        self._uid_token = None
        self._user_ttl = None
        self.discriminator = None

        if hana_dbname is not None:
            self.hana_dbname = hana_dbname
        if hanadb_create_statements is not None:
            self.hanadb_create_statements = hanadb_create_statements
        if hanadb_host is not None:
            self.hanadb_host = hanadb_host
        if hanadb_password is not None:
            self.hanadb_password = hanadb_password
        if hanadb_port is not None:
            self.hanadb_port = hanadb_port
        if hanadb_revocation_statements is not None:
            self.hanadb_revocation_statements = hanadb_revocation_statements
        if hanadb_username is not None:
            self.hanadb_username = hanadb_username
        self.name = name
        if new_name is not None:
            self.new_name = new_name
        if producer_encryption_key_name is not None:
            self.producer_encryption_key_name = producer_encryption_key_name
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
    def hana_dbname(self):
        """Gets the hana_dbname of this GatewayUpdateProducerHanaDb.  # noqa: E501

        HanaDb Name  # noqa: E501

        :return: The hana_dbname of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :rtype: str
        """
        return self._hana_dbname

    @hana_dbname.setter
    def hana_dbname(self, hana_dbname):
        """Sets the hana_dbname of this GatewayUpdateProducerHanaDb.

        HanaDb Name  # noqa: E501

        :param hana_dbname: The hana_dbname of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :type: str
        """

        self._hana_dbname = hana_dbname

    @property
    def hanadb_create_statements(self):
        """Gets the hanadb_create_statements of this GatewayUpdateProducerHanaDb.  # noqa: E501

        HanaDb Creation statements  # noqa: E501

        :return: The hanadb_create_statements of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :rtype: str
        """
        return self._hanadb_create_statements

    @hanadb_create_statements.setter
    def hanadb_create_statements(self, hanadb_create_statements):
        """Sets the hanadb_create_statements of this GatewayUpdateProducerHanaDb.

        HanaDb Creation statements  # noqa: E501

        :param hanadb_create_statements: The hanadb_create_statements of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :type: str
        """

        self._hanadb_create_statements = hanadb_create_statements

    @property
    def hanadb_host(self):
        """Gets the hanadb_host of this GatewayUpdateProducerHanaDb.  # noqa: E501

        HanaDb Host  # noqa: E501

        :return: The hanadb_host of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :rtype: str
        """
        return self._hanadb_host

    @hanadb_host.setter
    def hanadb_host(self, hanadb_host):
        """Sets the hanadb_host of this GatewayUpdateProducerHanaDb.

        HanaDb Host  # noqa: E501

        :param hanadb_host: The hanadb_host of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :type: str
        """

        self._hanadb_host = hanadb_host

    @property
    def hanadb_password(self):
        """Gets the hanadb_password of this GatewayUpdateProducerHanaDb.  # noqa: E501

        HanaDb Password  # noqa: E501

        :return: The hanadb_password of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :rtype: str
        """
        return self._hanadb_password

    @hanadb_password.setter
    def hanadb_password(self, hanadb_password):
        """Sets the hanadb_password of this GatewayUpdateProducerHanaDb.

        HanaDb Password  # noqa: E501

        :param hanadb_password: The hanadb_password of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :type: str
        """

        self._hanadb_password = hanadb_password

    @property
    def hanadb_port(self):
        """Gets the hanadb_port of this GatewayUpdateProducerHanaDb.  # noqa: E501

        HanaDb Port  # noqa: E501

        :return: The hanadb_port of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :rtype: str
        """
        return self._hanadb_port

    @hanadb_port.setter
    def hanadb_port(self, hanadb_port):
        """Sets the hanadb_port of this GatewayUpdateProducerHanaDb.

        HanaDb Port  # noqa: E501

        :param hanadb_port: The hanadb_port of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :type: str
        """

        self._hanadb_port = hanadb_port

    @property
    def hanadb_revocation_statements(self):
        """Gets the hanadb_revocation_statements of this GatewayUpdateProducerHanaDb.  # noqa: E501

        HanaDb Revocation statements  # noqa: E501

        :return: The hanadb_revocation_statements of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :rtype: str
        """
        return self._hanadb_revocation_statements

    @hanadb_revocation_statements.setter
    def hanadb_revocation_statements(self, hanadb_revocation_statements):
        """Sets the hanadb_revocation_statements of this GatewayUpdateProducerHanaDb.

        HanaDb Revocation statements  # noqa: E501

        :param hanadb_revocation_statements: The hanadb_revocation_statements of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :type: str
        """

        self._hanadb_revocation_statements = hanadb_revocation_statements

    @property
    def hanadb_username(self):
        """Gets the hanadb_username of this GatewayUpdateProducerHanaDb.  # noqa: E501

        HanaDb Username  # noqa: E501

        :return: The hanadb_username of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :rtype: str
        """
        return self._hanadb_username

    @hanadb_username.setter
    def hanadb_username(self, hanadb_username):
        """Sets the hanadb_username of this GatewayUpdateProducerHanaDb.

        HanaDb Username  # noqa: E501

        :param hanadb_username: The hanadb_username of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :type: str
        """

        self._hanadb_username = hanadb_username

    @property
    def name(self):
        """Gets the name of this GatewayUpdateProducerHanaDb.  # noqa: E501

        Producer name  # noqa: E501

        :return: The name of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GatewayUpdateProducerHanaDb.

        Producer name  # noqa: E501

        :param name: The name of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def new_name(self):
        """Gets the new_name of this GatewayUpdateProducerHanaDb.  # noqa: E501

        Producer name  # noqa: E501

        :return: The new_name of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this GatewayUpdateProducerHanaDb.

        Producer name  # noqa: E501

        :param new_name: The new_name of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :type: str
        """

        self._new_name = new_name

    @property
    def producer_encryption_key_name(self):
        """Gets the producer_encryption_key_name of this GatewayUpdateProducerHanaDb.  # noqa: E501

        Dynamic producer encryption key  # noqa: E501

        :return: The producer_encryption_key_name of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :rtype: str
        """
        return self._producer_encryption_key_name

    @producer_encryption_key_name.setter
    def producer_encryption_key_name(self, producer_encryption_key_name):
        """Sets the producer_encryption_key_name of this GatewayUpdateProducerHanaDb.

        Dynamic producer encryption key  # noqa: E501

        :param producer_encryption_key_name: The producer_encryption_key_name of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :type: str
        """

        self._producer_encryption_key_name = producer_encryption_key_name

    @property
    def secure_access_bastion_issuer(self):
        """Gets the secure_access_bastion_issuer of this GatewayUpdateProducerHanaDb.  # noqa: E501


        :return: The secure_access_bastion_issuer of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_bastion_issuer

    @secure_access_bastion_issuer.setter
    def secure_access_bastion_issuer(self, secure_access_bastion_issuer):
        """Sets the secure_access_bastion_issuer of this GatewayUpdateProducerHanaDb.


        :param secure_access_bastion_issuer: The secure_access_bastion_issuer of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :type: str
        """

        self._secure_access_bastion_issuer = secure_access_bastion_issuer

    @property
    def secure_access_db_schema(self):
        """Gets the secure_access_db_schema of this GatewayUpdateProducerHanaDb.  # noqa: E501


        :return: The secure_access_db_schema of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_db_schema

    @secure_access_db_schema.setter
    def secure_access_db_schema(self, secure_access_db_schema):
        """Sets the secure_access_db_schema of this GatewayUpdateProducerHanaDb.


        :param secure_access_db_schema: The secure_access_db_schema of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :type: str
        """

        self._secure_access_db_schema = secure_access_db_schema

    @property
    def secure_access_enable(self):
        """Gets the secure_access_enable of this GatewayUpdateProducerHanaDb.  # noqa: E501


        :return: The secure_access_enable of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_enable

    @secure_access_enable.setter
    def secure_access_enable(self, secure_access_enable):
        """Sets the secure_access_enable of this GatewayUpdateProducerHanaDb.


        :param secure_access_enable: The secure_access_enable of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :type: str
        """

        self._secure_access_enable = secure_access_enable

    @property
    def secure_access_host(self):
        """Gets the secure_access_host of this GatewayUpdateProducerHanaDb.  # noqa: E501


        :return: The secure_access_host of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :rtype: list[str]
        """
        return self._secure_access_host

    @secure_access_host.setter
    def secure_access_host(self, secure_access_host):
        """Sets the secure_access_host of this GatewayUpdateProducerHanaDb.


        :param secure_access_host: The secure_access_host of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :type: list[str]
        """

        self._secure_access_host = secure_access_host

    @property
    def secure_access_web(self):
        """Gets the secure_access_web of this GatewayUpdateProducerHanaDb.  # noqa: E501


        :return: The secure_access_web of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :rtype: bool
        """
        return self._secure_access_web

    @secure_access_web.setter
    def secure_access_web(self, secure_access_web):
        """Sets the secure_access_web of this GatewayUpdateProducerHanaDb.


        :param secure_access_web: The secure_access_web of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :type: bool
        """

        self._secure_access_web = secure_access_web

    @property
    def tags(self):
        """Gets the tags of this GatewayUpdateProducerHanaDb.  # noqa: E501

        List of the tags attached to this secret  # noqa: E501

        :return: The tags of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this GatewayUpdateProducerHanaDb.

        List of the tags attached to this secret  # noqa: E501

        :param tags: The tags of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def target_name(self):
        """Gets the target_name of this GatewayUpdateProducerHanaDb.  # noqa: E501

        Target name  # noqa: E501

        :return: The target_name of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """Sets the target_name of this GatewayUpdateProducerHanaDb.

        Target name  # noqa: E501

        :param target_name: The target_name of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :type: str
        """

        self._target_name = target_name

    @property
    def token(self):
        """Gets the token of this GatewayUpdateProducerHanaDb.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GatewayUpdateProducerHanaDb.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this GatewayUpdateProducerHanaDb.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GatewayUpdateProducerHanaDb.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def user_ttl(self):
        """Gets the user_ttl of this GatewayUpdateProducerHanaDb.  # noqa: E501

        User TTL  # noqa: E501

        :return: The user_ttl of this GatewayUpdateProducerHanaDb.  # noqa: E501
        :rtype: str
        """
        return self._user_ttl

    @user_ttl.setter
    def user_ttl(self, user_ttl):
        """Sets the user_ttl of this GatewayUpdateProducerHanaDb.

        User TTL  # noqa: E501

        :param user_ttl: The user_ttl of this GatewayUpdateProducerHanaDb.  # noqa: E501
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
        if not isinstance(other, GatewayUpdateProducerHanaDb):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayUpdateProducerHanaDb):
            return True

        return self.to_dict() != other.to_dict()