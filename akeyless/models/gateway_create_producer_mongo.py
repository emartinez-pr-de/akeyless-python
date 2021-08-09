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


class GatewayCreateProducerMongo(object):
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
        'mongodb_atlas_api_private_key': 'str',
        'mongodb_atlas_api_public_key': 'str',
        'mongodb_atlas_project_id': 'str',
        'mongodb_default_auth_db': 'str',
        'mongodb_host_port': 'str',
        'mongodb_name': 'str',
        'mongodb_password': 'str',
        'mongodb_roles': 'str',
        'mongodb_server_uri': 'str',
        'mongodb_uri_options': 'str',
        'mongodb_username': 'str',
        'name': 'str',
        'password': 'str',
        'producer_encryption_key_name': 'str',
        'secure_access_bastion_issuer': 'str',
        'secure_access_enable': 'str',
        'secure_access_host': 'list[str]',
        'target_name': 'str',
        'token': 'str',
        'uid_token': 'str',
        'user_ttl': 'str',
        'username': 'str'
    }

    attribute_map = {
        'mongodb_atlas_api_private_key': 'mongodb-atlas-api-private-key',
        'mongodb_atlas_api_public_key': 'mongodb-atlas-api-public-key',
        'mongodb_atlas_project_id': 'mongodb-atlas-project-id',
        'mongodb_default_auth_db': 'mongodb-default-auth-db',
        'mongodb_host_port': 'mongodb-host-port',
        'mongodb_name': 'mongodb-name',
        'mongodb_password': 'mongodb-password',
        'mongodb_roles': 'mongodb-roles',
        'mongodb_server_uri': 'mongodb-server-uri',
        'mongodb_uri_options': 'mongodb-uri-options',
        'mongodb_username': 'mongodb-username',
        'name': 'name',
        'password': 'password',
        'producer_encryption_key_name': 'producer-encryption-key-name',
        'secure_access_bastion_issuer': 'secure-access-bastion-issuer',
        'secure_access_enable': 'secure-access-enable',
        'secure_access_host': 'secure-access-host',
        'target_name': 'target-name',
        'token': 'token',
        'uid_token': 'uid-token',
        'user_ttl': 'user-ttl',
        'username': 'username'
    }

    def __init__(self, mongodb_atlas_api_private_key=None, mongodb_atlas_api_public_key=None, mongodb_atlas_project_id=None, mongodb_default_auth_db=None, mongodb_host_port=None, mongodb_name=None, mongodb_password=None, mongodb_roles='[]', mongodb_server_uri=None, mongodb_uri_options=None, mongodb_username=None, name=None, password=None, producer_encryption_key_name=None, secure_access_bastion_issuer=None, secure_access_enable=None, secure_access_host=None, target_name=None, token=None, uid_token=None, user_ttl='60m', username=None, local_vars_configuration=None):  # noqa: E501
        """GatewayCreateProducerMongo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._mongodb_atlas_api_private_key = None
        self._mongodb_atlas_api_public_key = None
        self._mongodb_atlas_project_id = None
        self._mongodb_default_auth_db = None
        self._mongodb_host_port = None
        self._mongodb_name = None
        self._mongodb_password = None
        self._mongodb_roles = None
        self._mongodb_server_uri = None
        self._mongodb_uri_options = None
        self._mongodb_username = None
        self._name = None
        self._password = None
        self._producer_encryption_key_name = None
        self._secure_access_bastion_issuer = None
        self._secure_access_enable = None
        self._secure_access_host = None
        self._target_name = None
        self._token = None
        self._uid_token = None
        self._user_ttl = None
        self._username = None
        self.discriminator = None

        if mongodb_atlas_api_private_key is not None:
            self.mongodb_atlas_api_private_key = mongodb_atlas_api_private_key
        if mongodb_atlas_api_public_key is not None:
            self.mongodb_atlas_api_public_key = mongodb_atlas_api_public_key
        if mongodb_atlas_project_id is not None:
            self.mongodb_atlas_project_id = mongodb_atlas_project_id
        if mongodb_default_auth_db is not None:
            self.mongodb_default_auth_db = mongodb_default_auth_db
        if mongodb_host_port is not None:
            self.mongodb_host_port = mongodb_host_port
        if mongodb_name is not None:
            self.mongodb_name = mongodb_name
        if mongodb_password is not None:
            self.mongodb_password = mongodb_password
        if mongodb_roles is not None:
            self.mongodb_roles = mongodb_roles
        if mongodb_server_uri is not None:
            self.mongodb_server_uri = mongodb_server_uri
        if mongodb_uri_options is not None:
            self.mongodb_uri_options = mongodb_uri_options
        if mongodb_username is not None:
            self.mongodb_username = mongodb_username
        self.name = name
        if password is not None:
            self.password = password
        if producer_encryption_key_name is not None:
            self.producer_encryption_key_name = producer_encryption_key_name
        if secure_access_bastion_issuer is not None:
            self.secure_access_bastion_issuer = secure_access_bastion_issuer
        if secure_access_enable is not None:
            self.secure_access_enable = secure_access_enable
        if secure_access_host is not None:
            self.secure_access_host = secure_access_host
        if target_name is not None:
            self.target_name = target_name
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if user_ttl is not None:
            self.user_ttl = user_ttl
        if username is not None:
            self.username = username

    @property
    def mongodb_atlas_api_private_key(self):
        """Gets the mongodb_atlas_api_private_key of this GatewayCreateProducerMongo.  # noqa: E501

        MongoDB Atlas private key  # noqa: E501

        :return: The mongodb_atlas_api_private_key of this GatewayCreateProducerMongo.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_atlas_api_private_key

    @mongodb_atlas_api_private_key.setter
    def mongodb_atlas_api_private_key(self, mongodb_atlas_api_private_key):
        """Sets the mongodb_atlas_api_private_key of this GatewayCreateProducerMongo.

        MongoDB Atlas private key  # noqa: E501

        :param mongodb_atlas_api_private_key: The mongodb_atlas_api_private_key of this GatewayCreateProducerMongo.  # noqa: E501
        :type: str
        """

        self._mongodb_atlas_api_private_key = mongodb_atlas_api_private_key

    @property
    def mongodb_atlas_api_public_key(self):
        """Gets the mongodb_atlas_api_public_key of this GatewayCreateProducerMongo.  # noqa: E501

        MongoDB Atlas public key  # noqa: E501

        :return: The mongodb_atlas_api_public_key of this GatewayCreateProducerMongo.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_atlas_api_public_key

    @mongodb_atlas_api_public_key.setter
    def mongodb_atlas_api_public_key(self, mongodb_atlas_api_public_key):
        """Sets the mongodb_atlas_api_public_key of this GatewayCreateProducerMongo.

        MongoDB Atlas public key  # noqa: E501

        :param mongodb_atlas_api_public_key: The mongodb_atlas_api_public_key of this GatewayCreateProducerMongo.  # noqa: E501
        :type: str
        """

        self._mongodb_atlas_api_public_key = mongodb_atlas_api_public_key

    @property
    def mongodb_atlas_project_id(self):
        """Gets the mongodb_atlas_project_id of this GatewayCreateProducerMongo.  # noqa: E501

        MongoDB Atlas project ID  # noqa: E501

        :return: The mongodb_atlas_project_id of this GatewayCreateProducerMongo.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_atlas_project_id

    @mongodb_atlas_project_id.setter
    def mongodb_atlas_project_id(self, mongodb_atlas_project_id):
        """Sets the mongodb_atlas_project_id of this GatewayCreateProducerMongo.

        MongoDB Atlas project ID  # noqa: E501

        :param mongodb_atlas_project_id: The mongodb_atlas_project_id of this GatewayCreateProducerMongo.  # noqa: E501
        :type: str
        """

        self._mongodb_atlas_project_id = mongodb_atlas_project_id

    @property
    def mongodb_default_auth_db(self):
        """Gets the mongodb_default_auth_db of this GatewayCreateProducerMongo.  # noqa: E501

        MongoDB server default authentication database  # noqa: E501

        :return: The mongodb_default_auth_db of this GatewayCreateProducerMongo.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_default_auth_db

    @mongodb_default_auth_db.setter
    def mongodb_default_auth_db(self, mongodb_default_auth_db):
        """Sets the mongodb_default_auth_db of this GatewayCreateProducerMongo.

        MongoDB server default authentication database  # noqa: E501

        :param mongodb_default_auth_db: The mongodb_default_auth_db of this GatewayCreateProducerMongo.  # noqa: E501
        :type: str
        """

        self._mongodb_default_auth_db = mongodb_default_auth_db

    @property
    def mongodb_host_port(self):
        """Gets the mongodb_host_port of this GatewayCreateProducerMongo.  # noqa: E501

        MongoDB server host and port  # noqa: E501

        :return: The mongodb_host_port of this GatewayCreateProducerMongo.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_host_port

    @mongodb_host_port.setter
    def mongodb_host_port(self, mongodb_host_port):
        """Sets the mongodb_host_port of this GatewayCreateProducerMongo.

        MongoDB server host and port  # noqa: E501

        :param mongodb_host_port: The mongodb_host_port of this GatewayCreateProducerMongo.  # noqa: E501
        :type: str
        """

        self._mongodb_host_port = mongodb_host_port

    @property
    def mongodb_name(self):
        """Gets the mongodb_name of this GatewayCreateProducerMongo.  # noqa: E501

        MongoDB Name  # noqa: E501

        :return: The mongodb_name of this GatewayCreateProducerMongo.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_name

    @mongodb_name.setter
    def mongodb_name(self, mongodb_name):
        """Sets the mongodb_name of this GatewayCreateProducerMongo.

        MongoDB Name  # noqa: E501

        :param mongodb_name: The mongodb_name of this GatewayCreateProducerMongo.  # noqa: E501
        :type: str
        """

        self._mongodb_name = mongodb_name

    @property
    def mongodb_password(self):
        """Gets the mongodb_password of this GatewayCreateProducerMongo.  # noqa: E501

        MongoDB server password. You will prompted to provide a password if it will not appear in CLI parameters  # noqa: E501

        :return: The mongodb_password of this GatewayCreateProducerMongo.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_password

    @mongodb_password.setter
    def mongodb_password(self, mongodb_password):
        """Sets the mongodb_password of this GatewayCreateProducerMongo.

        MongoDB server password. You will prompted to provide a password if it will not appear in CLI parameters  # noqa: E501

        :param mongodb_password: The mongodb_password of this GatewayCreateProducerMongo.  # noqa: E501
        :type: str
        """

        self._mongodb_password = mongodb_password

    @property
    def mongodb_roles(self):
        """Gets the mongodb_roles of this GatewayCreateProducerMongo.  # noqa: E501

        MongoDB Roles  # noqa: E501

        :return: The mongodb_roles of this GatewayCreateProducerMongo.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_roles

    @mongodb_roles.setter
    def mongodb_roles(self, mongodb_roles):
        """Sets the mongodb_roles of this GatewayCreateProducerMongo.

        MongoDB Roles  # noqa: E501

        :param mongodb_roles: The mongodb_roles of this GatewayCreateProducerMongo.  # noqa: E501
        :type: str
        """

        self._mongodb_roles = mongodb_roles

    @property
    def mongodb_server_uri(self):
        """Gets the mongodb_server_uri of this GatewayCreateProducerMongo.  # noqa: E501

        MongoDB server URI  # noqa: E501

        :return: The mongodb_server_uri of this GatewayCreateProducerMongo.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_server_uri

    @mongodb_server_uri.setter
    def mongodb_server_uri(self, mongodb_server_uri):
        """Sets the mongodb_server_uri of this GatewayCreateProducerMongo.

        MongoDB server URI  # noqa: E501

        :param mongodb_server_uri: The mongodb_server_uri of this GatewayCreateProducerMongo.  # noqa: E501
        :type: str
        """

        self._mongodb_server_uri = mongodb_server_uri

    @property
    def mongodb_uri_options(self):
        """Gets the mongodb_uri_options of this GatewayCreateProducerMongo.  # noqa: E501

        MongoDB server URI options  # noqa: E501

        :return: The mongodb_uri_options of this GatewayCreateProducerMongo.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_uri_options

    @mongodb_uri_options.setter
    def mongodb_uri_options(self, mongodb_uri_options):
        """Sets the mongodb_uri_options of this GatewayCreateProducerMongo.

        MongoDB server URI options  # noqa: E501

        :param mongodb_uri_options: The mongodb_uri_options of this GatewayCreateProducerMongo.  # noqa: E501
        :type: str
        """

        self._mongodb_uri_options = mongodb_uri_options

    @property
    def mongodb_username(self):
        """Gets the mongodb_username of this GatewayCreateProducerMongo.  # noqa: E501

        MongoDB server username  # noqa: E501

        :return: The mongodb_username of this GatewayCreateProducerMongo.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_username

    @mongodb_username.setter
    def mongodb_username(self, mongodb_username):
        """Sets the mongodb_username of this GatewayCreateProducerMongo.

        MongoDB server username  # noqa: E501

        :param mongodb_username: The mongodb_username of this GatewayCreateProducerMongo.  # noqa: E501
        :type: str
        """

        self._mongodb_username = mongodb_username

    @property
    def name(self):
        """Gets the name of this GatewayCreateProducerMongo.  # noqa: E501

        Producer name  # noqa: E501

        :return: The name of this GatewayCreateProducerMongo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GatewayCreateProducerMongo.

        Producer name  # noqa: E501

        :param name: The name of this GatewayCreateProducerMongo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def password(self):
        """Gets the password of this GatewayCreateProducerMongo.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The password of this GatewayCreateProducerMongo.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this GatewayCreateProducerMongo.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param password: The password of this GatewayCreateProducerMongo.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def producer_encryption_key_name(self):
        """Gets the producer_encryption_key_name of this GatewayCreateProducerMongo.  # noqa: E501

        Encrypt producer with following key  # noqa: E501

        :return: The producer_encryption_key_name of this GatewayCreateProducerMongo.  # noqa: E501
        :rtype: str
        """
        return self._producer_encryption_key_name

    @producer_encryption_key_name.setter
    def producer_encryption_key_name(self, producer_encryption_key_name):
        """Sets the producer_encryption_key_name of this GatewayCreateProducerMongo.

        Encrypt producer with following key  # noqa: E501

        :param producer_encryption_key_name: The producer_encryption_key_name of this GatewayCreateProducerMongo.  # noqa: E501
        :type: str
        """

        self._producer_encryption_key_name = producer_encryption_key_name

    @property
    def secure_access_bastion_issuer(self):
        """Gets the secure_access_bastion_issuer of this GatewayCreateProducerMongo.  # noqa: E501


        :return: The secure_access_bastion_issuer of this GatewayCreateProducerMongo.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_bastion_issuer

    @secure_access_bastion_issuer.setter
    def secure_access_bastion_issuer(self, secure_access_bastion_issuer):
        """Sets the secure_access_bastion_issuer of this GatewayCreateProducerMongo.


        :param secure_access_bastion_issuer: The secure_access_bastion_issuer of this GatewayCreateProducerMongo.  # noqa: E501
        :type: str
        """

        self._secure_access_bastion_issuer = secure_access_bastion_issuer

    @property
    def secure_access_enable(self):
        """Gets the secure_access_enable of this GatewayCreateProducerMongo.  # noqa: E501


        :return: The secure_access_enable of this GatewayCreateProducerMongo.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_enable

    @secure_access_enable.setter
    def secure_access_enable(self, secure_access_enable):
        """Sets the secure_access_enable of this GatewayCreateProducerMongo.


        :param secure_access_enable: The secure_access_enable of this GatewayCreateProducerMongo.  # noqa: E501
        :type: str
        """

        self._secure_access_enable = secure_access_enable

    @property
    def secure_access_host(self):
        """Gets the secure_access_host of this GatewayCreateProducerMongo.  # noqa: E501


        :return: The secure_access_host of this GatewayCreateProducerMongo.  # noqa: E501
        :rtype: list[str]
        """
        return self._secure_access_host

    @secure_access_host.setter
    def secure_access_host(self, secure_access_host):
        """Sets the secure_access_host of this GatewayCreateProducerMongo.


        :param secure_access_host: The secure_access_host of this GatewayCreateProducerMongo.  # noqa: E501
        :type: list[str]
        """

        self._secure_access_host = secure_access_host

    @property
    def target_name(self):
        """Gets the target_name of this GatewayCreateProducerMongo.  # noqa: E501

        Target name  # noqa: E501

        :return: The target_name of this GatewayCreateProducerMongo.  # noqa: E501
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """Sets the target_name of this GatewayCreateProducerMongo.

        Target name  # noqa: E501

        :param target_name: The target_name of this GatewayCreateProducerMongo.  # noqa: E501
        :type: str
        """

        self._target_name = target_name

    @property
    def token(self):
        """Gets the token of this GatewayCreateProducerMongo.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GatewayCreateProducerMongo.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GatewayCreateProducerMongo.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GatewayCreateProducerMongo.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this GatewayCreateProducerMongo.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GatewayCreateProducerMongo.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GatewayCreateProducerMongo.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GatewayCreateProducerMongo.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def user_ttl(self):
        """Gets the user_ttl of this GatewayCreateProducerMongo.  # noqa: E501

        User TTL  # noqa: E501

        :return: The user_ttl of this GatewayCreateProducerMongo.  # noqa: E501
        :rtype: str
        """
        return self._user_ttl

    @user_ttl.setter
    def user_ttl(self, user_ttl):
        """Sets the user_ttl of this GatewayCreateProducerMongo.

        User TTL  # noqa: E501

        :param user_ttl: The user_ttl of this GatewayCreateProducerMongo.  # noqa: E501
        :type: str
        """

        self._user_ttl = user_ttl

    @property
    def username(self):
        """Gets the username of this GatewayCreateProducerMongo.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The username of this GatewayCreateProducerMongo.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this GatewayCreateProducerMongo.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param username: The username of this GatewayCreateProducerMongo.  # noqa: E501
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
        if not isinstance(other, GatewayCreateProducerMongo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayCreateProducerMongo):
            return True

        return self.to_dict() != other.to_dict()
