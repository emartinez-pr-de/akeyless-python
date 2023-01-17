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


class CreateDBTarget(object):
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
        'db_name': 'str',
        'db_server_certificates': 'str',
        'db_server_name': 'str',
        'db_type': 'str',
        'host': 'str',
        'json': 'bool',
        'key': 'str',
        'mongodb_atlas': 'bool',
        'mongodb_atlas_api_private_key': 'str',
        'mongodb_atlas_api_public_key': 'str',
        'mongodb_atlas_project_id': 'str',
        'mongodb_default_auth_db': 'str',
        'mongodb_uri_options': 'str',
        'name': 'str',
        'oracle_service_name': 'str',
        'port': 'str',
        'pwd': 'str',
        'snowflake_account': 'str',
        'snowflake_api_private_key': 'str',
        'snowflake_api_private_key_password': 'str',
        'ssl': 'bool',
        'ssl_certificate': 'str',
        'token': 'str',
        'uid_token': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'comment': 'comment',
        'db_name': 'db-name',
        'db_server_certificates': 'db-server-certificates',
        'db_server_name': 'db-server-name',
        'db_type': 'db-type',
        'host': 'host',
        'json': 'json',
        'key': 'key',
        'mongodb_atlas': 'mongodb-atlas',
        'mongodb_atlas_api_private_key': 'mongodb-atlas-api-private-key',
        'mongodb_atlas_api_public_key': 'mongodb-atlas-api-public-key',
        'mongodb_atlas_project_id': 'mongodb-atlas-project-id',
        'mongodb_default_auth_db': 'mongodb-default-auth-db',
        'mongodb_uri_options': 'mongodb-uri-options',
        'name': 'name',
        'oracle_service_name': 'oracle-service-name',
        'port': 'port',
        'pwd': 'pwd',
        'snowflake_account': 'snowflake-account',
        'snowflake_api_private_key': 'snowflake-api-private-key',
        'snowflake_api_private_key_password': 'snowflake-api-private-key-password',
        'ssl': 'ssl',
        'ssl_certificate': 'ssl-certificate',
        'token': 'token',
        'uid_token': 'uid-token',
        'user_name': 'user-name'
    }

    def __init__(self, comment=None, db_name=None, db_server_certificates=None, db_server_name=None, db_type=None, host=None, json=None, key=None, mongodb_atlas=None, mongodb_atlas_api_private_key=None, mongodb_atlas_api_public_key=None, mongodb_atlas_project_id=None, mongodb_default_auth_db=None, mongodb_uri_options=None, name=None, oracle_service_name=None, port=None, pwd=None, snowflake_account=None, snowflake_api_private_key=None, snowflake_api_private_key_password=None, ssl=None, ssl_certificate=None, token=None, uid_token=None, user_name=None, local_vars_configuration=None):  # noqa: E501
        """CreateDBTarget - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._comment = None
        self._db_name = None
        self._db_server_certificates = None
        self._db_server_name = None
        self._db_type = None
        self._host = None
        self._json = None
        self._key = None
        self._mongodb_atlas = None
        self._mongodb_atlas_api_private_key = None
        self._mongodb_atlas_api_public_key = None
        self._mongodb_atlas_project_id = None
        self._mongodb_default_auth_db = None
        self._mongodb_uri_options = None
        self._name = None
        self._oracle_service_name = None
        self._port = None
        self._pwd = None
        self._snowflake_account = None
        self._snowflake_api_private_key = None
        self._snowflake_api_private_key_password = None
        self._ssl = None
        self._ssl_certificate = None
        self._token = None
        self._uid_token = None
        self._user_name = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        if db_name is not None:
            self.db_name = db_name
        if db_server_certificates is not None:
            self.db_server_certificates = db_server_certificates
        if db_server_name is not None:
            self.db_server_name = db_server_name
        self.db_type = db_type
        if host is not None:
            self.host = host
        if json is not None:
            self.json = json
        if key is not None:
            self.key = key
        if mongodb_atlas is not None:
            self.mongodb_atlas = mongodb_atlas
        if mongodb_atlas_api_private_key is not None:
            self.mongodb_atlas_api_private_key = mongodb_atlas_api_private_key
        if mongodb_atlas_api_public_key is not None:
            self.mongodb_atlas_api_public_key = mongodb_atlas_api_public_key
        if mongodb_atlas_project_id is not None:
            self.mongodb_atlas_project_id = mongodb_atlas_project_id
        if mongodb_default_auth_db is not None:
            self.mongodb_default_auth_db = mongodb_default_auth_db
        if mongodb_uri_options is not None:
            self.mongodb_uri_options = mongodb_uri_options
        self.name = name
        if oracle_service_name is not None:
            self.oracle_service_name = oracle_service_name
        if port is not None:
            self.port = port
        if pwd is not None:
            self.pwd = pwd
        if snowflake_account is not None:
            self.snowflake_account = snowflake_account
        if snowflake_api_private_key is not None:
            self.snowflake_api_private_key = snowflake_api_private_key
        if snowflake_api_private_key_password is not None:
            self.snowflake_api_private_key_password = snowflake_api_private_key_password
        if ssl is not None:
            self.ssl = ssl
        if ssl_certificate is not None:
            self.ssl_certificate = ssl_certificate
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if user_name is not None:
            self.user_name = user_name

    @property
    def comment(self):
        """Gets the comment of this CreateDBTarget.  # noqa: E501

        Comment about the target  # noqa: E501

        :return: The comment of this CreateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this CreateDBTarget.

        Comment about the target  # noqa: E501

        :param comment: The comment of this CreateDBTarget.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def db_name(self):
        """Gets the db_name of this CreateDBTarget.  # noqa: E501


        :return: The db_name of this CreateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this CreateDBTarget.


        :param db_name: The db_name of this CreateDBTarget.  # noqa: E501
        :type: str
        """

        self._db_name = db_name

    @property
    def db_server_certificates(self):
        """Gets the db_server_certificates of this CreateDBTarget.  # noqa: E501

        (Optional) DB server certificates  # noqa: E501

        :return: The db_server_certificates of this CreateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._db_server_certificates

    @db_server_certificates.setter
    def db_server_certificates(self, db_server_certificates):
        """Sets the db_server_certificates of this CreateDBTarget.

        (Optional) DB server certificates  # noqa: E501

        :param db_server_certificates: The db_server_certificates of this CreateDBTarget.  # noqa: E501
        :type: str
        """

        self._db_server_certificates = db_server_certificates

    @property
    def db_server_name(self):
        """Gets the db_server_name of this CreateDBTarget.  # noqa: E501

        (Optional) Server name for certificate verification  # noqa: E501

        :return: The db_server_name of this CreateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._db_server_name

    @db_server_name.setter
    def db_server_name(self, db_server_name):
        """Sets the db_server_name of this CreateDBTarget.

        (Optional) Server name for certificate verification  # noqa: E501

        :param db_server_name: The db_server_name of this CreateDBTarget.  # noqa: E501
        :type: str
        """

        self._db_server_name = db_server_name

    @property
    def db_type(self):
        """Gets the db_type of this CreateDBTarget.  # noqa: E501


        :return: The db_type of this CreateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._db_type

    @db_type.setter
    def db_type(self, db_type):
        """Sets the db_type of this CreateDBTarget.


        :param db_type: The db_type of this CreateDBTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and db_type is None:  # noqa: E501
            raise ValueError("Invalid value for `db_type`, must not be `None`")  # noqa: E501

        self._db_type = db_type

    @property
    def host(self):
        """Gets the host of this CreateDBTarget.  # noqa: E501


        :return: The host of this CreateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this CreateDBTarget.


        :param host: The host of this CreateDBTarget.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def json(self):
        """Gets the json of this CreateDBTarget.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this CreateDBTarget.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this CreateDBTarget.

        Set output format to JSON  # noqa: E501

        :param json: The json of this CreateDBTarget.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def key(self):
        """Gets the key of this CreateDBTarget.  # noqa: E501

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :return: The key of this CreateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CreateDBTarget.

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :param key: The key of this CreateDBTarget.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def mongodb_atlas(self):
        """Gets the mongodb_atlas of this CreateDBTarget.  # noqa: E501


        :return: The mongodb_atlas of this CreateDBTarget.  # noqa: E501
        :rtype: bool
        """
        return self._mongodb_atlas

    @mongodb_atlas.setter
    def mongodb_atlas(self, mongodb_atlas):
        """Sets the mongodb_atlas of this CreateDBTarget.


        :param mongodb_atlas: The mongodb_atlas of this CreateDBTarget.  # noqa: E501
        :type: bool
        """

        self._mongodb_atlas = mongodb_atlas

    @property
    def mongodb_atlas_api_private_key(self):
        """Gets the mongodb_atlas_api_private_key of this CreateDBTarget.  # noqa: E501

        MongoDB Atlas private key  # noqa: E501

        :return: The mongodb_atlas_api_private_key of this CreateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_atlas_api_private_key

    @mongodb_atlas_api_private_key.setter
    def mongodb_atlas_api_private_key(self, mongodb_atlas_api_private_key):
        """Sets the mongodb_atlas_api_private_key of this CreateDBTarget.

        MongoDB Atlas private key  # noqa: E501

        :param mongodb_atlas_api_private_key: The mongodb_atlas_api_private_key of this CreateDBTarget.  # noqa: E501
        :type: str
        """

        self._mongodb_atlas_api_private_key = mongodb_atlas_api_private_key

    @property
    def mongodb_atlas_api_public_key(self):
        """Gets the mongodb_atlas_api_public_key of this CreateDBTarget.  # noqa: E501

        MongoDB Atlas public key  # noqa: E501

        :return: The mongodb_atlas_api_public_key of this CreateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_atlas_api_public_key

    @mongodb_atlas_api_public_key.setter
    def mongodb_atlas_api_public_key(self, mongodb_atlas_api_public_key):
        """Sets the mongodb_atlas_api_public_key of this CreateDBTarget.

        MongoDB Atlas public key  # noqa: E501

        :param mongodb_atlas_api_public_key: The mongodb_atlas_api_public_key of this CreateDBTarget.  # noqa: E501
        :type: str
        """

        self._mongodb_atlas_api_public_key = mongodb_atlas_api_public_key

    @property
    def mongodb_atlas_project_id(self):
        """Gets the mongodb_atlas_project_id of this CreateDBTarget.  # noqa: E501

        MongoDB Atlas project ID  # noqa: E501

        :return: The mongodb_atlas_project_id of this CreateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_atlas_project_id

    @mongodb_atlas_project_id.setter
    def mongodb_atlas_project_id(self, mongodb_atlas_project_id):
        """Sets the mongodb_atlas_project_id of this CreateDBTarget.

        MongoDB Atlas project ID  # noqa: E501

        :param mongodb_atlas_project_id: The mongodb_atlas_project_id of this CreateDBTarget.  # noqa: E501
        :type: str
        """

        self._mongodb_atlas_project_id = mongodb_atlas_project_id

    @property
    def mongodb_default_auth_db(self):
        """Gets the mongodb_default_auth_db of this CreateDBTarget.  # noqa: E501

        MongoDB server default authentication database  # noqa: E501

        :return: The mongodb_default_auth_db of this CreateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_default_auth_db

    @mongodb_default_auth_db.setter
    def mongodb_default_auth_db(self, mongodb_default_auth_db):
        """Sets the mongodb_default_auth_db of this CreateDBTarget.

        MongoDB server default authentication database  # noqa: E501

        :param mongodb_default_auth_db: The mongodb_default_auth_db of this CreateDBTarget.  # noqa: E501
        :type: str
        """

        self._mongodb_default_auth_db = mongodb_default_auth_db

    @property
    def mongodb_uri_options(self):
        """Gets the mongodb_uri_options of this CreateDBTarget.  # noqa: E501

        MongoDB server URI options  # noqa: E501

        :return: The mongodb_uri_options of this CreateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_uri_options

    @mongodb_uri_options.setter
    def mongodb_uri_options(self, mongodb_uri_options):
        """Sets the mongodb_uri_options of this CreateDBTarget.

        MongoDB server URI options  # noqa: E501

        :param mongodb_uri_options: The mongodb_uri_options of this CreateDBTarget.  # noqa: E501
        :type: str
        """

        self._mongodb_uri_options = mongodb_uri_options

    @property
    def name(self):
        """Gets the name of this CreateDBTarget.  # noqa: E501

        Target name  # noqa: E501

        :return: The name of this CreateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateDBTarget.

        Target name  # noqa: E501

        :param name: The name of this CreateDBTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def oracle_service_name(self):
        """Gets the oracle_service_name of this CreateDBTarget.  # noqa: E501


        :return: The oracle_service_name of this CreateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._oracle_service_name

    @oracle_service_name.setter
    def oracle_service_name(self, oracle_service_name):
        """Sets the oracle_service_name of this CreateDBTarget.


        :param oracle_service_name: The oracle_service_name of this CreateDBTarget.  # noqa: E501
        :type: str
        """

        self._oracle_service_name = oracle_service_name

    @property
    def port(self):
        """Gets the port of this CreateDBTarget.  # noqa: E501


        :return: The port of this CreateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this CreateDBTarget.


        :param port: The port of this CreateDBTarget.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def pwd(self):
        """Gets the pwd of this CreateDBTarget.  # noqa: E501


        :return: The pwd of this CreateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._pwd

    @pwd.setter
    def pwd(self, pwd):
        """Sets the pwd of this CreateDBTarget.


        :param pwd: The pwd of this CreateDBTarget.  # noqa: E501
        :type: str
        """

        self._pwd = pwd

    @property
    def snowflake_account(self):
        """Gets the snowflake_account of this CreateDBTarget.  # noqa: E501


        :return: The snowflake_account of this CreateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._snowflake_account

    @snowflake_account.setter
    def snowflake_account(self, snowflake_account):
        """Sets the snowflake_account of this CreateDBTarget.


        :param snowflake_account: The snowflake_account of this CreateDBTarget.  # noqa: E501
        :type: str
        """

        self._snowflake_account = snowflake_account

    @property
    def snowflake_api_private_key(self):
        """Gets the snowflake_api_private_key of this CreateDBTarget.  # noqa: E501

        RSA Private key (base64 encoded)  # noqa: E501

        :return: The snowflake_api_private_key of this CreateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._snowflake_api_private_key

    @snowflake_api_private_key.setter
    def snowflake_api_private_key(self, snowflake_api_private_key):
        """Sets the snowflake_api_private_key of this CreateDBTarget.

        RSA Private key (base64 encoded)  # noqa: E501

        :param snowflake_api_private_key: The snowflake_api_private_key of this CreateDBTarget.  # noqa: E501
        :type: str
        """

        self._snowflake_api_private_key = snowflake_api_private_key

    @property
    def snowflake_api_private_key_password(self):
        """Gets the snowflake_api_private_key_password of this CreateDBTarget.  # noqa: E501

        The Private key passphrase  # noqa: E501

        :return: The snowflake_api_private_key_password of this CreateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._snowflake_api_private_key_password

    @snowflake_api_private_key_password.setter
    def snowflake_api_private_key_password(self, snowflake_api_private_key_password):
        """Sets the snowflake_api_private_key_password of this CreateDBTarget.

        The Private key passphrase  # noqa: E501

        :param snowflake_api_private_key_password: The snowflake_api_private_key_password of this CreateDBTarget.  # noqa: E501
        :type: str
        """

        self._snowflake_api_private_key_password = snowflake_api_private_key_password

    @property
    def ssl(self):
        """Gets the ssl of this CreateDBTarget.  # noqa: E501

        SSL connection mode  # noqa: E501

        :return: The ssl of this CreateDBTarget.  # noqa: E501
        :rtype: bool
        """
        return self._ssl

    @ssl.setter
    def ssl(self, ssl):
        """Sets the ssl of this CreateDBTarget.

        SSL connection mode  # noqa: E501

        :param ssl: The ssl of this CreateDBTarget.  # noqa: E501
        :type: bool
        """

        self._ssl = ssl

    @property
    def ssl_certificate(self):
        """Gets the ssl_certificate of this CreateDBTarget.  # noqa: E501

        SSL connection certificate  # noqa: E501

        :return: The ssl_certificate of this CreateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._ssl_certificate

    @ssl_certificate.setter
    def ssl_certificate(self, ssl_certificate):
        """Sets the ssl_certificate of this CreateDBTarget.

        SSL connection certificate  # noqa: E501

        :param ssl_certificate: The ssl_certificate of this CreateDBTarget.  # noqa: E501
        :type: str
        """

        self._ssl_certificate = ssl_certificate

    @property
    def token(self):
        """Gets the token of this CreateDBTarget.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this CreateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this CreateDBTarget.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this CreateDBTarget.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this CreateDBTarget.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this CreateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this CreateDBTarget.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this CreateDBTarget.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def user_name(self):
        """Gets the user_name of this CreateDBTarget.  # noqa: E501


        :return: The user_name of this CreateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this CreateDBTarget.


        :param user_name: The user_name of this CreateDBTarget.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

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
        if not isinstance(other, CreateDBTarget):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateDBTarget):
            return True

        return self.to_dict() != other.to_dict()
