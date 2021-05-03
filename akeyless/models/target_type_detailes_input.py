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


class TargetTypeDetailesInput(object):
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
        'aws_access_key_id': 'str',
        'aws_region': 'str',
        'aws_secret_access_key': 'str',
        'aws_session_token': 'str',
        'db_host_name': 'str',
        'db_name': 'str',
        'db_port': 'str',
        'db_pwd': 'str',
        'db_server_certificates': 'str',
        'db_server_name': 'str',
        'db_user_name': 'str',
        'host': 'str',
        'mongodb_db_name': 'str',
        'mongodb_uri_connection': 'str',
        'password': 'str',
        'port': 'str',
        'private_key': 'str',
        'private_key_password': 'str',
        'rabbitmq_server_password': 'str',
        'rabbitmq_server_uri': 'str',
        'rabbitmq_server_user': 'str',
        'url': 'str',
        'username': 'str'
    }

    attribute_map = {
        'aws_access_key_id': 'aws_access_key_id',
        'aws_region': 'aws_region',
        'aws_secret_access_key': 'aws_secret_access_key',
        'aws_session_token': 'aws_session_token',
        'db_host_name': 'db_host_name',
        'db_name': 'db_name',
        'db_port': 'db_port',
        'db_pwd': 'db_pwd',
        'db_server_certificates': 'db_server_certificates',
        'db_server_name': 'db_server_name',
        'db_user_name': 'db_user_name',
        'host': 'host',
        'mongodb_db_name': 'mongodb_db_name',
        'mongodb_uri_connection': 'mongodb_uri_connection',
        'password': 'password',
        'port': 'port',
        'private_key': 'private_key',
        'private_key_password': 'private_key_password',
        'rabbitmq_server_password': 'rabbitmq_server_password',
        'rabbitmq_server_uri': 'rabbitmq_server_uri',
        'rabbitmq_server_user': 'rabbitmq_server_user',
        'url': 'url',
        'username': 'username'
    }

    def __init__(self, aws_access_key_id=None, aws_region=None, aws_secret_access_key=None, aws_session_token=None, db_host_name=None, db_name=None, db_port=None, db_pwd=None, db_server_certificates=None, db_server_name=None, db_user_name=None, host=None, mongodb_db_name=None, mongodb_uri_connection=None, password=None, port=None, private_key=None, private_key_password=None, rabbitmq_server_password=None, rabbitmq_server_uri=None, rabbitmq_server_user=None, url=None, username=None, local_vars_configuration=None):  # noqa: E501
        """TargetTypeDetailesInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._aws_access_key_id = None
        self._aws_region = None
        self._aws_secret_access_key = None
        self._aws_session_token = None
        self._db_host_name = None
        self._db_name = None
        self._db_port = None
        self._db_pwd = None
        self._db_server_certificates = None
        self._db_server_name = None
        self._db_user_name = None
        self._host = None
        self._mongodb_db_name = None
        self._mongodb_uri_connection = None
        self._password = None
        self._port = None
        self._private_key = None
        self._private_key_password = None
        self._rabbitmq_server_password = None
        self._rabbitmq_server_uri = None
        self._rabbitmq_server_user = None
        self._url = None
        self._username = None
        self.discriminator = None

        if aws_access_key_id is not None:
            self.aws_access_key_id = aws_access_key_id
        if aws_region is not None:
            self.aws_region = aws_region
        if aws_secret_access_key is not None:
            self.aws_secret_access_key = aws_secret_access_key
        if aws_session_token is not None:
            self.aws_session_token = aws_session_token
        if db_host_name is not None:
            self.db_host_name = db_host_name
        if db_name is not None:
            self.db_name = db_name
        if db_port is not None:
            self.db_port = db_port
        if db_pwd is not None:
            self.db_pwd = db_pwd
        if db_server_certificates is not None:
            self.db_server_certificates = db_server_certificates
        if db_server_name is not None:
            self.db_server_name = db_server_name
        if db_user_name is not None:
            self.db_user_name = db_user_name
        if host is not None:
            self.host = host
        if mongodb_db_name is not None:
            self.mongodb_db_name = mongodb_db_name
        if mongodb_uri_connection is not None:
            self.mongodb_uri_connection = mongodb_uri_connection
        if password is not None:
            self.password = password
        if port is not None:
            self.port = port
        if private_key is not None:
            self.private_key = private_key
        if private_key_password is not None:
            self.private_key_password = private_key_password
        if rabbitmq_server_password is not None:
            self.rabbitmq_server_password = rabbitmq_server_password
        if rabbitmq_server_uri is not None:
            self.rabbitmq_server_uri = rabbitmq_server_uri
        if rabbitmq_server_user is not None:
            self.rabbitmq_server_user = rabbitmq_server_user
        if url is not None:
            self.url = url
        if username is not None:
            self.username = username

    @property
    def aws_access_key_id(self):
        """Gets the aws_access_key_id of this TargetTypeDetailesInput.  # noqa: E501


        :return: The aws_access_key_id of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._aws_access_key_id

    @aws_access_key_id.setter
    def aws_access_key_id(self, aws_access_key_id):
        """Sets the aws_access_key_id of this TargetTypeDetailesInput.


        :param aws_access_key_id: The aws_access_key_id of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._aws_access_key_id = aws_access_key_id

    @property
    def aws_region(self):
        """Gets the aws_region of this TargetTypeDetailesInput.  # noqa: E501


        :return: The aws_region of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._aws_region

    @aws_region.setter
    def aws_region(self, aws_region):
        """Sets the aws_region of this TargetTypeDetailesInput.


        :param aws_region: The aws_region of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._aws_region = aws_region

    @property
    def aws_secret_access_key(self):
        """Gets the aws_secret_access_key of this TargetTypeDetailesInput.  # noqa: E501


        :return: The aws_secret_access_key of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._aws_secret_access_key

    @aws_secret_access_key.setter
    def aws_secret_access_key(self, aws_secret_access_key):
        """Sets the aws_secret_access_key of this TargetTypeDetailesInput.


        :param aws_secret_access_key: The aws_secret_access_key of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._aws_secret_access_key = aws_secret_access_key

    @property
    def aws_session_token(self):
        """Gets the aws_session_token of this TargetTypeDetailesInput.  # noqa: E501


        :return: The aws_session_token of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._aws_session_token

    @aws_session_token.setter
    def aws_session_token(self, aws_session_token):
        """Sets the aws_session_token of this TargetTypeDetailesInput.


        :param aws_session_token: The aws_session_token of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._aws_session_token = aws_session_token

    @property
    def db_host_name(self):
        """Gets the db_host_name of this TargetTypeDetailesInput.  # noqa: E501


        :return: The db_host_name of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._db_host_name

    @db_host_name.setter
    def db_host_name(self, db_host_name):
        """Sets the db_host_name of this TargetTypeDetailesInput.


        :param db_host_name: The db_host_name of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._db_host_name = db_host_name

    @property
    def db_name(self):
        """Gets the db_name of this TargetTypeDetailesInput.  # noqa: E501


        :return: The db_name of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this TargetTypeDetailesInput.


        :param db_name: The db_name of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._db_name = db_name

    @property
    def db_port(self):
        """Gets the db_port of this TargetTypeDetailesInput.  # noqa: E501


        :return: The db_port of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._db_port

    @db_port.setter
    def db_port(self, db_port):
        """Sets the db_port of this TargetTypeDetailesInput.


        :param db_port: The db_port of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._db_port = db_port

    @property
    def db_pwd(self):
        """Gets the db_pwd of this TargetTypeDetailesInput.  # noqa: E501


        :return: The db_pwd of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._db_pwd

    @db_pwd.setter
    def db_pwd(self, db_pwd):
        """Sets the db_pwd of this TargetTypeDetailesInput.


        :param db_pwd: The db_pwd of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._db_pwd = db_pwd

    @property
    def db_server_certificates(self):
        """Gets the db_server_certificates of this TargetTypeDetailesInput.  # noqa: E501

        (Optional) DBServerCertificates defines the set of root certificate authorities that clients use when verifying server certificates. If DBServerCertificates is empty, TLS uses the host's root CA set.  # noqa: E501

        :return: The db_server_certificates of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._db_server_certificates

    @db_server_certificates.setter
    def db_server_certificates(self, db_server_certificates):
        """Sets the db_server_certificates of this TargetTypeDetailesInput.

        (Optional) DBServerCertificates defines the set of root certificate authorities that clients use when verifying server certificates. If DBServerCertificates is empty, TLS uses the host's root CA set.  # noqa: E501

        :param db_server_certificates: The db_server_certificates of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._db_server_certificates = db_server_certificates

    @property
    def db_server_name(self):
        """Gets the db_server_name of this TargetTypeDetailesInput.  # noqa: E501

        (Optional) ServerName is used to verify the hostname on the returned certificates unless InsecureSkipVerify is given. It is also included in the client's handshake to support virtual hosting unless it is an IP address.  # noqa: E501

        :return: The db_server_name of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._db_server_name

    @db_server_name.setter
    def db_server_name(self, db_server_name):
        """Sets the db_server_name of this TargetTypeDetailesInput.

        (Optional) ServerName is used to verify the hostname on the returned certificates unless InsecureSkipVerify is given. It is also included in the client's handshake to support virtual hosting unless it is an IP address.  # noqa: E501

        :param db_server_name: The db_server_name of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._db_server_name = db_server_name

    @property
    def db_user_name(self):
        """Gets the db_user_name of this TargetTypeDetailesInput.  # noqa: E501


        :return: The db_user_name of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._db_user_name

    @db_user_name.setter
    def db_user_name(self, db_user_name):
        """Sets the db_user_name of this TargetTypeDetailesInput.


        :param db_user_name: The db_user_name of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._db_user_name = db_user_name

    @property
    def host(self):
        """Gets the host of this TargetTypeDetailesInput.  # noqa: E501


        :return: The host of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this TargetTypeDetailesInput.


        :param host: The host of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def mongodb_db_name(self):
        """Gets the mongodb_db_name of this TargetTypeDetailesInput.  # noqa: E501


        :return: The mongodb_db_name of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_db_name

    @mongodb_db_name.setter
    def mongodb_db_name(self, mongodb_db_name):
        """Sets the mongodb_db_name of this TargetTypeDetailesInput.


        :param mongodb_db_name: The mongodb_db_name of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._mongodb_db_name = mongodb_db_name

    @property
    def mongodb_uri_connection(self):
        """Gets the mongodb_uri_connection of this TargetTypeDetailesInput.  # noqa: E501


        :return: The mongodb_uri_connection of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._mongodb_uri_connection

    @mongodb_uri_connection.setter
    def mongodb_uri_connection(self, mongodb_uri_connection):
        """Sets the mongodb_uri_connection of this TargetTypeDetailesInput.


        :param mongodb_uri_connection: The mongodb_uri_connection of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._mongodb_uri_connection = mongodb_uri_connection

    @property
    def password(self):
        """Gets the password of this TargetTypeDetailesInput.  # noqa: E501


        :return: The password of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this TargetTypeDetailesInput.


        :param password: The password of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def port(self):
        """Gets the port of this TargetTypeDetailesInput.  # noqa: E501


        :return: The port of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this TargetTypeDetailesInput.


        :param port: The port of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def private_key(self):
        """Gets the private_key of this TargetTypeDetailesInput.  # noqa: E501


        :return: The private_key of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this TargetTypeDetailesInput.


        :param private_key: The private_key of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._private_key = private_key

    @property
    def private_key_password(self):
        """Gets the private_key_password of this TargetTypeDetailesInput.  # noqa: E501


        :return: The private_key_password of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._private_key_password

    @private_key_password.setter
    def private_key_password(self, private_key_password):
        """Sets the private_key_password of this TargetTypeDetailesInput.


        :param private_key_password: The private_key_password of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._private_key_password = private_key_password

    @property
    def rabbitmq_server_password(self):
        """Gets the rabbitmq_server_password of this TargetTypeDetailesInput.  # noqa: E501


        :return: The rabbitmq_server_password of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._rabbitmq_server_password

    @rabbitmq_server_password.setter
    def rabbitmq_server_password(self, rabbitmq_server_password):
        """Sets the rabbitmq_server_password of this TargetTypeDetailesInput.


        :param rabbitmq_server_password: The rabbitmq_server_password of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._rabbitmq_server_password = rabbitmq_server_password

    @property
    def rabbitmq_server_uri(self):
        """Gets the rabbitmq_server_uri of this TargetTypeDetailesInput.  # noqa: E501


        :return: The rabbitmq_server_uri of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._rabbitmq_server_uri

    @rabbitmq_server_uri.setter
    def rabbitmq_server_uri(self, rabbitmq_server_uri):
        """Sets the rabbitmq_server_uri of this TargetTypeDetailesInput.


        :param rabbitmq_server_uri: The rabbitmq_server_uri of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._rabbitmq_server_uri = rabbitmq_server_uri

    @property
    def rabbitmq_server_user(self):
        """Gets the rabbitmq_server_user of this TargetTypeDetailesInput.  # noqa: E501


        :return: The rabbitmq_server_user of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._rabbitmq_server_user

    @rabbitmq_server_user.setter
    def rabbitmq_server_user(self, rabbitmq_server_user):
        """Sets the rabbitmq_server_user of this TargetTypeDetailesInput.


        :param rabbitmq_server_user: The rabbitmq_server_user of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._rabbitmq_server_user = rabbitmq_server_user

    @property
    def url(self):
        """Gets the url of this TargetTypeDetailesInput.  # noqa: E501


        :return: The url of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this TargetTypeDetailesInput.


        :param url: The url of this TargetTypeDetailesInput.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def username(self):
        """Gets the username of this TargetTypeDetailesInput.  # noqa: E501


        :return: The username of this TargetTypeDetailesInput.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this TargetTypeDetailesInput.


        :param username: The username of this TargetTypeDetailesInput.  # noqa: E501
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
        if not isinstance(other, TargetTypeDetailesInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TargetTypeDetailesInput):
            return True

        return self.to_dict() != other.to_dict()
