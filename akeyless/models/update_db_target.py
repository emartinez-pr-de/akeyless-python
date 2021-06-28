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


class UpdateDBTarget(object):
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
        'key': 'str',
        'mongodb_atlas': 'bool',
        'mongodb_atlas_api_private_key': 'str',
        'mongodb_atlas_api_public_key': 'str',
        'mongodb_atlas_project_id': 'str',
        'mongodb_default_auth_db': 'str',
        'mongodb_host_port': 'str',
        'mongodb_password': 'str',
        'mongodb_server_uri': 'str',
        'mongodb_uri_options': 'str',
        'mongodb_username': 'str',
        'name': 'str',
        'new_name': 'str',
        'password': 'str',
        'port': 'str',
        'pwd': 'str',
        'snowflake_account': 'str',
        'token': 'str',
        'uid_token': 'str',
        'update_version': 'bool',
        'user_name': 'str',
        'username': 'str'
    }

    attribute_map = {
        'comment': 'comment',
        'db_name': 'db-name',
        'db_server_certificates': 'db-server-certificates',
        'db_server_name': 'db-server-name',
        'db_type': 'db-type',
        'host': 'host',
        'key': 'key',
        'mongodb_atlas': 'mongodb-atlas',
        'mongodb_atlas_api_private_key': 'mongodb-atlas-api-private-key',
        'mongodb_atlas_api_public_key': 'mongodb-atlas-api-public-key',
        'mongodb_atlas_project_id': 'mongodb-atlas-project-id',
        'mongodb_default_auth_db': 'mongodb-default-auth-db',
        'mongodb_host_port': 'mongodb-host-port',
        'mongodb_password': 'mongodb-password',
        'mongodb_server_uri': 'mongodb-server-uri',
        'mongodb_uri_options': 'mongodb-uri-options',
        'mongodb_username': 'mongodb-username',
        'name': 'name',
        'new_name': 'new-name',
        'password': 'password',
        'port': 'port',
        'pwd': 'pwd',
        'snowflake_account': 'snowflake-account',
        'token': 'token',
        'uid_token': 'uid-token',
        'update_version': 'update-version',
        'user_name': 'user-name',
        'username': 'username'
    }

    def __init__(self, comment=None, db_name=None, db_server_certificates=None, db_server_name=None, db_type=None, host=None, key=None, mongodb_atlas=None, mongodb_atlas_api_private_key=None, mongodb_atlas_api_public_key=None, mongodb_atlas_project_id=None, mongodb_default_auth_db=None, mongodb_host_port=None, mongodb_password=None, mongodb_server_uri=None, mongodb_uri_options=None, mongodb_username=None, name=None, new_name=None, password=None, port=None, pwd=None, snowflake_account=None, token=None, uid_token=None, update_version=False, user_name=None, username=None, local_vars_configuration=None):  # noqa: E501
        """UpdateDBTarget - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._comment = None
        self._db_name = None
        self._db_server_certificates = None
        self._db_server_name = None
        self._db_type = None
        self._host = None
        self._key = None
        self._mongodb_atlas = None
        self._mongodb_atlas_api_private_key = None
        self._mongodb_atlas_api_public_key = None
        self._mongodb_atlas_project_id = None
        self._mongodb_default_auth_db = None
        self._mongodb_host_port = None
        self._mongodb_password = None
        self._mongodb_server_uri = None
        self._mongodb_uri_options = None
        self._mongodb_username = None
        self._name = None
        self._new_name = None
        self._password = None
        self._port = None
        self._pwd = None
        self._snowflake_account = None
        self._token = None
        self._uid_token = None
        self._update_version = None
        self._user_name = None
        self._username = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        if db_name is not None:
            self.db_name = db_name
        if db_server_certificates is not None:
            self.db_server_certificates = db_server_certificates
        if db_server_name is not None:
            self.db_server_name = db_server_name
        if db_type is not None:
            self.db_type = db_type
        if host is not None:
            self.host = host
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
        if mongodb_host_port is not None:
            self.mongodb_host_port = mongodb_host_port
        if mongodb_password is not None:
            self.mongodb_password = mongodb_password
        if mongodb_server_uri is not None:
            self.mongodb_server_uri = mongodb_server_uri
        if mongodb_uri_options is not None:
            self.mongodb_uri_options = mongodb_uri_options
        if mongodb_username is not None:
            self.mongodb_username = mongodb_username
        self.name = name
        self.new_name = new_name
        if password is not None:
            self.password = password
        if port is not None:
            self.port = port
        if pwd is not None:
            self.pwd = pwd
        if snowflake_account is not None:
            self.snowflake_account = snowflake_account
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if update_version is not None:
            self.update_version = update_version
        if user_name is not None:
            self.user_name = user_name
        if username is not None:
            self.username = username

    @property
    def comment(self):
        """Gets the comment of this UpdateDBTarget.  # noqa: E501

        Comment about the target  # noqa: E501

        :return: The comment of this UpdateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this UpdateDBTarget.

        Comment about the target  # noqa: E501

        :param comment: The comment of this UpdateDBTarget.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def db_name(self):
        """Gets the db_name of this UpdateDBTarget.  # noqa: E501


        :return: The db_name of this UpdateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this UpdateDBTarget.


        :param db_name: The db_name of this UpdateDBTarget.  # noqa: E501
        :type: str
        """

        self._db_name = db_name

    @property
    def db_server_certificates(self):
        """Gets the db_server_certificates of this UpdateDBTarget.  # noqa: E501

        (Optional) DB server certificates  # noqa: E501

        :return: The db_server_certificates of this UpdateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._db_server_certificates

    @db_server_certificates.setter
    def db_server_certificates(self, db_server_certificates):
        """Sets the db_server_certificates of this UpdateDBTarget.

        (Optional) DB server certificates  # noqa: E501

        :param db_server_certificates: The db_server_certificates of this UpdateDBTarget.  # noqa: E501
        :type: str
        """

        self._db_server_certificates = db_server_certificates

    @property
    def db_server_name(self):
        """Gets the db_server_name of this UpdateDBTarget.  # noqa: E501

        (Optional) Server name for certificate verification  # noqa: E501

        :return: The db_server_name of this UpdateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._db_server_name

    @db_server_name.setter
    def db_server_name(self, db_server_name):
        """Sets the db_server_name of this UpdateDBTarget.

        (Optional) Server name for certificate verification  # noqa: E501

        :param db_server_name: The db_server_name of this UpdateDBTarget.  # noqa: E501
        :type: str
        """

        self._db_server_name = db_server_name

    @property
    def db_type(self):
        """Gets the db_type of this UpdateDBTarget.  # noqa: E501


        :return: The db_type of this UpdateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._db_type

    @db_type.setter
    def db_type(self, db_type):
        """Sets the db_type of this UpdateDBTarget.


        :param db_type: The db_type of this UpdateDBTarget.  # noqa: E501
        :type: str
        """

        self._db_type = db_type

    @property
    def host(self):
        """Gets the host of this UpdateDBTarget.  # noqa: E501


        :return: The host of this UpdateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this UpdateDBTarget.


        :param host: The host of this UpdateDBTarget.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def key(self):
        """Gets the key of this UpdateDBTarget.  # noqa: E501

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :return: The key of this UpdateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this UpdateDBTarget.

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :param key: The key of this UpdateDBTarget.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def mongodb_atlas(self):
        """Gets the mongodb_atlas of this UpdateDBTarget.  # noqa: E501


        :return: The mongodb_atlas of this UpdateDBTarget.  # noqa: E501
        :rtype: bool
        """
        return self._mongodb_atlas

    @mongodb_atlas.setter
    def mongodb_atlas(self, mongodb_atlas):
        """Sets the mongodb_atlas of this UpdateDBTarget.


        :param mongodb_atlas: The mongodb_atlas of this UpdateDBTarget.  # noqa: E501
        :type: bool
        """

        self._mongodb_atlas = mongodb_atlas

    @property
    def mongodb_atlas_api_private_key(self):
        """Gets the mongodb_atlas_api_private_key of this UpdateDBTarget.  # noqa: E501

        MongoDB Atlas private key  # noqa: E501

        :return: The mongodb_atlas_api_private_key of this UpdateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_atlas_api_private_key

    @mongodb_atlas_api_private_key.setter
    def mongodb_atlas_api_private_key(self, mongodb_atlas_api_private_key):
        """Sets the mongodb_atlas_api_private_key of this UpdateDBTarget.

        MongoDB Atlas private key  # noqa: E501

        :param mongodb_atlas_api_private_key: The mongodb_atlas_api_private_key of this UpdateDBTarget.  # noqa: E501
        :type: str
        """

        self._mongodb_atlas_api_private_key = mongodb_atlas_api_private_key

    @property
    def mongodb_atlas_api_public_key(self):
        """Gets the mongodb_atlas_api_public_key of this UpdateDBTarget.  # noqa: E501

        MongoDB Atlas public key  # noqa: E501

        :return: The mongodb_atlas_api_public_key of this UpdateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_atlas_api_public_key

    @mongodb_atlas_api_public_key.setter
    def mongodb_atlas_api_public_key(self, mongodb_atlas_api_public_key):
        """Sets the mongodb_atlas_api_public_key of this UpdateDBTarget.

        MongoDB Atlas public key  # noqa: E501

        :param mongodb_atlas_api_public_key: The mongodb_atlas_api_public_key of this UpdateDBTarget.  # noqa: E501
        :type: str
        """

        self._mongodb_atlas_api_public_key = mongodb_atlas_api_public_key

    @property
    def mongodb_atlas_project_id(self):
        """Gets the mongodb_atlas_project_id of this UpdateDBTarget.  # noqa: E501

        MongoDB Atlas project ID  # noqa: E501

        :return: The mongodb_atlas_project_id of this UpdateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_atlas_project_id

    @mongodb_atlas_project_id.setter
    def mongodb_atlas_project_id(self, mongodb_atlas_project_id):
        """Sets the mongodb_atlas_project_id of this UpdateDBTarget.

        MongoDB Atlas project ID  # noqa: E501

        :param mongodb_atlas_project_id: The mongodb_atlas_project_id of this UpdateDBTarget.  # noqa: E501
        :type: str
        """

        self._mongodb_atlas_project_id = mongodb_atlas_project_id

    @property
    def mongodb_default_auth_db(self):
        """Gets the mongodb_default_auth_db of this UpdateDBTarget.  # noqa: E501

        MongoDB server default authentication database  # noqa: E501

        :return: The mongodb_default_auth_db of this UpdateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_default_auth_db

    @mongodb_default_auth_db.setter
    def mongodb_default_auth_db(self, mongodb_default_auth_db):
        """Sets the mongodb_default_auth_db of this UpdateDBTarget.

        MongoDB server default authentication database  # noqa: E501

        :param mongodb_default_auth_db: The mongodb_default_auth_db of this UpdateDBTarget.  # noqa: E501
        :type: str
        """

        self._mongodb_default_auth_db = mongodb_default_auth_db

    @property
    def mongodb_host_port(self):
        """Gets the mongodb_host_port of this UpdateDBTarget.  # noqa: E501

        MongoDB server host and port  # noqa: E501

        :return: The mongodb_host_port of this UpdateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_host_port

    @mongodb_host_port.setter
    def mongodb_host_port(self, mongodb_host_port):
        """Sets the mongodb_host_port of this UpdateDBTarget.

        MongoDB server host and port  # noqa: E501

        :param mongodb_host_port: The mongodb_host_port of this UpdateDBTarget.  # noqa: E501
        :type: str
        """

        self._mongodb_host_port = mongodb_host_port

    @property
    def mongodb_password(self):
        """Gets the mongodb_password of this UpdateDBTarget.  # noqa: E501

        MongoDB server password. You will prompted to provide a password if it will not appear in CLI parameters  # noqa: E501

        :return: The mongodb_password of this UpdateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_password

    @mongodb_password.setter
    def mongodb_password(self, mongodb_password):
        """Sets the mongodb_password of this UpdateDBTarget.

        MongoDB server password. You will prompted to provide a password if it will not appear in CLI parameters  # noqa: E501

        :param mongodb_password: The mongodb_password of this UpdateDBTarget.  # noqa: E501
        :type: str
        """

        self._mongodb_password = mongodb_password

    @property
    def mongodb_server_uri(self):
        """Gets the mongodb_server_uri of this UpdateDBTarget.  # noqa: E501

        MongoDB server URI  # noqa: E501

        :return: The mongodb_server_uri of this UpdateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_server_uri

    @mongodb_server_uri.setter
    def mongodb_server_uri(self, mongodb_server_uri):
        """Sets the mongodb_server_uri of this UpdateDBTarget.

        MongoDB server URI  # noqa: E501

        :param mongodb_server_uri: The mongodb_server_uri of this UpdateDBTarget.  # noqa: E501
        :type: str
        """

        self._mongodb_server_uri = mongodb_server_uri

    @property
    def mongodb_uri_options(self):
        """Gets the mongodb_uri_options of this UpdateDBTarget.  # noqa: E501

        MongoDB server URI options  # noqa: E501

        :return: The mongodb_uri_options of this UpdateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_uri_options

    @mongodb_uri_options.setter
    def mongodb_uri_options(self, mongodb_uri_options):
        """Sets the mongodb_uri_options of this UpdateDBTarget.

        MongoDB server URI options  # noqa: E501

        :param mongodb_uri_options: The mongodb_uri_options of this UpdateDBTarget.  # noqa: E501
        :type: str
        """

        self._mongodb_uri_options = mongodb_uri_options

    @property
    def mongodb_username(self):
        """Gets the mongodb_username of this UpdateDBTarget.  # noqa: E501

        MongoDB server username  # noqa: E501

        :return: The mongodb_username of this UpdateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_username

    @mongodb_username.setter
    def mongodb_username(self, mongodb_username):
        """Sets the mongodb_username of this UpdateDBTarget.

        MongoDB server username  # noqa: E501

        :param mongodb_username: The mongodb_username of this UpdateDBTarget.  # noqa: E501
        :type: str
        """

        self._mongodb_username = mongodb_username

    @property
    def name(self):
        """Gets the name of this UpdateDBTarget.  # noqa: E501

        Target name  # noqa: E501

        :return: The name of this UpdateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateDBTarget.

        Target name  # noqa: E501

        :param name: The name of this UpdateDBTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def new_name(self):
        """Gets the new_name of this UpdateDBTarget.  # noqa: E501

        New target name  # noqa: E501

        :return: The new_name of this UpdateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this UpdateDBTarget.

        New target name  # noqa: E501

        :param new_name: The new_name of this UpdateDBTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and new_name is None:  # noqa: E501
            raise ValueError("Invalid value for `new_name`, must not be `None`")  # noqa: E501

        self._new_name = new_name

    @property
    def password(self):
        """Gets the password of this UpdateDBTarget.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The password of this UpdateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UpdateDBTarget.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param password: The password of this UpdateDBTarget.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def port(self):
        """Gets the port of this UpdateDBTarget.  # noqa: E501


        :return: The port of this UpdateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this UpdateDBTarget.


        :param port: The port of this UpdateDBTarget.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def pwd(self):
        """Gets the pwd of this UpdateDBTarget.  # noqa: E501


        :return: The pwd of this UpdateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._pwd

    @pwd.setter
    def pwd(self, pwd):
        """Sets the pwd of this UpdateDBTarget.


        :param pwd: The pwd of this UpdateDBTarget.  # noqa: E501
        :type: str
        """

        self._pwd = pwd

    @property
    def snowflake_account(self):
        """Gets the snowflake_account of this UpdateDBTarget.  # noqa: E501


        :return: The snowflake_account of this UpdateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._snowflake_account

    @snowflake_account.setter
    def snowflake_account(self, snowflake_account):
        """Sets the snowflake_account of this UpdateDBTarget.


        :param snowflake_account: The snowflake_account of this UpdateDBTarget.  # noqa: E501
        :type: str
        """

        self._snowflake_account = snowflake_account

    @property
    def token(self):
        """Gets the token of this UpdateDBTarget.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this UpdateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this UpdateDBTarget.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this UpdateDBTarget.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this UpdateDBTarget.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this UpdateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this UpdateDBTarget.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this UpdateDBTarget.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def update_version(self):
        """Gets the update_version of this UpdateDBTarget.  # noqa: E501

        Create new version for the target  # noqa: E501

        :return: The update_version of this UpdateDBTarget.  # noqa: E501
        :rtype: bool
        """
        return self._update_version

    @update_version.setter
    def update_version(self, update_version):
        """Sets the update_version of this UpdateDBTarget.

        Create new version for the target  # noqa: E501

        :param update_version: The update_version of this UpdateDBTarget.  # noqa: E501
        :type: bool
        """

        self._update_version = update_version

    @property
    def user_name(self):
        """Gets the user_name of this UpdateDBTarget.  # noqa: E501


        :return: The user_name of this UpdateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this UpdateDBTarget.


        :param user_name: The user_name of this UpdateDBTarget.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def username(self):
        """Gets the username of this UpdateDBTarget.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The username of this UpdateDBTarget.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UpdateDBTarget.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param username: The username of this UpdateDBTarget.  # noqa: E501
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
        if not isinstance(other, UpdateDBTarget):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateDBTarget):
            return True

        return self.to_dict() != other.to_dict()
