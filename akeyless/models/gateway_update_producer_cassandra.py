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


class GatewayUpdateProducerCassandra(object):
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
        'cassandra_creation_statements': 'str',
        'cassandra_hosts': 'str',
        'cassandra_password': 'str',
        'cassandra_port': 'str',
        'cassandra_username': 'str',
        'delete_protection': 'str',
        'json': 'bool',
        'name': 'str',
        'new_name': 'str',
        'producer_encryption_key_name': 'str',
        'ssl': 'bool',
        'ssl_certificate': 'str',
        'tags': 'list[str]',
        'target_name': 'str',
        'token': 'str',
        'uid_token': 'str',
        'user_ttl': 'str'
    }

    attribute_map = {
        'cassandra_creation_statements': 'cassandra-creation-statements',
        'cassandra_hosts': 'cassandra-hosts',
        'cassandra_password': 'cassandra-password',
        'cassandra_port': 'cassandra-port',
        'cassandra_username': 'cassandra-username',
        'delete_protection': 'delete_protection',
        'json': 'json',
        'name': 'name',
        'new_name': 'new-name',
        'producer_encryption_key_name': 'producer-encryption-key-name',
        'ssl': 'ssl',
        'ssl_certificate': 'ssl-certificate',
        'tags': 'tags',
        'target_name': 'target-name',
        'token': 'token',
        'uid_token': 'uid-token',
        'user_ttl': 'user-ttl'
    }

    def __init__(self, cassandra_creation_statements=None, cassandra_hosts=None, cassandra_password=None, cassandra_port='9042', cassandra_username=None, delete_protection=None, json=False, name=None, new_name=None, producer_encryption_key_name=None, ssl=False, ssl_certificate=None, tags=None, target_name=None, token=None, uid_token=None, user_ttl='60m', local_vars_configuration=None):  # noqa: E501
        """GatewayUpdateProducerCassandra - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cassandra_creation_statements = None
        self._cassandra_hosts = None
        self._cassandra_password = None
        self._cassandra_port = None
        self._cassandra_username = None
        self._delete_protection = None
        self._json = None
        self._name = None
        self._new_name = None
        self._producer_encryption_key_name = None
        self._ssl = None
        self._ssl_certificate = None
        self._tags = None
        self._target_name = None
        self._token = None
        self._uid_token = None
        self._user_ttl = None
        self.discriminator = None

        if cassandra_creation_statements is not None:
            self.cassandra_creation_statements = cassandra_creation_statements
        if cassandra_hosts is not None:
            self.cassandra_hosts = cassandra_hosts
        if cassandra_password is not None:
            self.cassandra_password = cassandra_password
        if cassandra_port is not None:
            self.cassandra_port = cassandra_port
        if cassandra_username is not None:
            self.cassandra_username = cassandra_username
        if delete_protection is not None:
            self.delete_protection = delete_protection
        if json is not None:
            self.json = json
        self.name = name
        if new_name is not None:
            self.new_name = new_name
        if producer_encryption_key_name is not None:
            self.producer_encryption_key_name = producer_encryption_key_name
        if ssl is not None:
            self.ssl = ssl
        if ssl_certificate is not None:
            self.ssl_certificate = ssl_certificate
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
    def cassandra_creation_statements(self):
        """Gets the cassandra_creation_statements of this GatewayUpdateProducerCassandra.  # noqa: E501

        Cassandra creation statements  # noqa: E501

        :return: The cassandra_creation_statements of this GatewayUpdateProducerCassandra.  # noqa: E501
        :rtype: str
        """
        return self._cassandra_creation_statements

    @cassandra_creation_statements.setter
    def cassandra_creation_statements(self, cassandra_creation_statements):
        """Sets the cassandra_creation_statements of this GatewayUpdateProducerCassandra.

        Cassandra creation statements  # noqa: E501

        :param cassandra_creation_statements: The cassandra_creation_statements of this GatewayUpdateProducerCassandra.  # noqa: E501
        :type: str
        """

        self._cassandra_creation_statements = cassandra_creation_statements

    @property
    def cassandra_hosts(self):
        """Gets the cassandra_hosts of this GatewayUpdateProducerCassandra.  # noqa: E501

        Cassandra hosts IP or addresses, comma separated  # noqa: E501

        :return: The cassandra_hosts of this GatewayUpdateProducerCassandra.  # noqa: E501
        :rtype: str
        """
        return self._cassandra_hosts

    @cassandra_hosts.setter
    def cassandra_hosts(self, cassandra_hosts):
        """Sets the cassandra_hosts of this GatewayUpdateProducerCassandra.

        Cassandra hosts IP or addresses, comma separated  # noqa: E501

        :param cassandra_hosts: The cassandra_hosts of this GatewayUpdateProducerCassandra.  # noqa: E501
        :type: str
        """

        self._cassandra_hosts = cassandra_hosts

    @property
    def cassandra_password(self):
        """Gets the cassandra_password of this GatewayUpdateProducerCassandra.  # noqa: E501

        Cassandra superuser password  # noqa: E501

        :return: The cassandra_password of this GatewayUpdateProducerCassandra.  # noqa: E501
        :rtype: str
        """
        return self._cassandra_password

    @cassandra_password.setter
    def cassandra_password(self, cassandra_password):
        """Sets the cassandra_password of this GatewayUpdateProducerCassandra.

        Cassandra superuser password  # noqa: E501

        :param cassandra_password: The cassandra_password of this GatewayUpdateProducerCassandra.  # noqa: E501
        :type: str
        """

        self._cassandra_password = cassandra_password

    @property
    def cassandra_port(self):
        """Gets the cassandra_port of this GatewayUpdateProducerCassandra.  # noqa: E501

        Cassandra port  # noqa: E501

        :return: The cassandra_port of this GatewayUpdateProducerCassandra.  # noqa: E501
        :rtype: str
        """
        return self._cassandra_port

    @cassandra_port.setter
    def cassandra_port(self, cassandra_port):
        """Sets the cassandra_port of this GatewayUpdateProducerCassandra.

        Cassandra port  # noqa: E501

        :param cassandra_port: The cassandra_port of this GatewayUpdateProducerCassandra.  # noqa: E501
        :type: str
        """

        self._cassandra_port = cassandra_port

    @property
    def cassandra_username(self):
        """Gets the cassandra_username of this GatewayUpdateProducerCassandra.  # noqa: E501

        Cassandra superuser username  # noqa: E501

        :return: The cassandra_username of this GatewayUpdateProducerCassandra.  # noqa: E501
        :rtype: str
        """
        return self._cassandra_username

    @cassandra_username.setter
    def cassandra_username(self, cassandra_username):
        """Sets the cassandra_username of this GatewayUpdateProducerCassandra.

        Cassandra superuser username  # noqa: E501

        :param cassandra_username: The cassandra_username of this GatewayUpdateProducerCassandra.  # noqa: E501
        :type: str
        """

        self._cassandra_username = cassandra_username

    @property
    def delete_protection(self):
        """Gets the delete_protection of this GatewayUpdateProducerCassandra.  # noqa: E501

        Protection from accidental deletion of this item [true/false]  # noqa: E501

        :return: The delete_protection of this GatewayUpdateProducerCassandra.  # noqa: E501
        :rtype: str
        """
        return self._delete_protection

    @delete_protection.setter
    def delete_protection(self, delete_protection):
        """Sets the delete_protection of this GatewayUpdateProducerCassandra.

        Protection from accidental deletion of this item [true/false]  # noqa: E501

        :param delete_protection: The delete_protection of this GatewayUpdateProducerCassandra.  # noqa: E501
        :type: str
        """

        self._delete_protection = delete_protection

    @property
    def json(self):
        """Gets the json of this GatewayUpdateProducerCassandra.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this GatewayUpdateProducerCassandra.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this GatewayUpdateProducerCassandra.

        Set output format to JSON  # noqa: E501

        :param json: The json of this GatewayUpdateProducerCassandra.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def name(self):
        """Gets the name of this GatewayUpdateProducerCassandra.  # noqa: E501

        Producer name  # noqa: E501

        :return: The name of this GatewayUpdateProducerCassandra.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GatewayUpdateProducerCassandra.

        Producer name  # noqa: E501

        :param name: The name of this GatewayUpdateProducerCassandra.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def new_name(self):
        """Gets the new_name of this GatewayUpdateProducerCassandra.  # noqa: E501

        Producer name  # noqa: E501

        :return: The new_name of this GatewayUpdateProducerCassandra.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this GatewayUpdateProducerCassandra.

        Producer name  # noqa: E501

        :param new_name: The new_name of this GatewayUpdateProducerCassandra.  # noqa: E501
        :type: str
        """

        self._new_name = new_name

    @property
    def producer_encryption_key_name(self):
        """Gets the producer_encryption_key_name of this GatewayUpdateProducerCassandra.  # noqa: E501

        Dynamic producer encryption key  # noqa: E501

        :return: The producer_encryption_key_name of this GatewayUpdateProducerCassandra.  # noqa: E501
        :rtype: str
        """
        return self._producer_encryption_key_name

    @producer_encryption_key_name.setter
    def producer_encryption_key_name(self, producer_encryption_key_name):
        """Sets the producer_encryption_key_name of this GatewayUpdateProducerCassandra.

        Dynamic producer encryption key  # noqa: E501

        :param producer_encryption_key_name: The producer_encryption_key_name of this GatewayUpdateProducerCassandra.  # noqa: E501
        :type: str
        """

        self._producer_encryption_key_name = producer_encryption_key_name

    @property
    def ssl(self):
        """Gets the ssl of this GatewayUpdateProducerCassandra.  # noqa: E501

        Enable/Disable SSL [true/false]  # noqa: E501

        :return: The ssl of this GatewayUpdateProducerCassandra.  # noqa: E501
        :rtype: bool
        """
        return self._ssl

    @ssl.setter
    def ssl(self, ssl):
        """Sets the ssl of this GatewayUpdateProducerCassandra.

        Enable/Disable SSL [true/false]  # noqa: E501

        :param ssl: The ssl of this GatewayUpdateProducerCassandra.  # noqa: E501
        :type: bool
        """

        self._ssl = ssl

    @property
    def ssl_certificate(self):
        """Gets the ssl_certificate of this GatewayUpdateProducerCassandra.  # noqa: E501

        SSL CA certificate in base64 encoding generated from a trusted Certificate Authority (CA)  # noqa: E501

        :return: The ssl_certificate of this GatewayUpdateProducerCassandra.  # noqa: E501
        :rtype: str
        """
        return self._ssl_certificate

    @ssl_certificate.setter
    def ssl_certificate(self, ssl_certificate):
        """Sets the ssl_certificate of this GatewayUpdateProducerCassandra.

        SSL CA certificate in base64 encoding generated from a trusted Certificate Authority (CA)  # noqa: E501

        :param ssl_certificate: The ssl_certificate of this GatewayUpdateProducerCassandra.  # noqa: E501
        :type: str
        """

        self._ssl_certificate = ssl_certificate

    @property
    def tags(self):
        """Gets the tags of this GatewayUpdateProducerCassandra.  # noqa: E501

        Add tags attached to this object  # noqa: E501

        :return: The tags of this GatewayUpdateProducerCassandra.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this GatewayUpdateProducerCassandra.

        Add tags attached to this object  # noqa: E501

        :param tags: The tags of this GatewayUpdateProducerCassandra.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def target_name(self):
        """Gets the target_name of this GatewayUpdateProducerCassandra.  # noqa: E501

        Target name  # noqa: E501

        :return: The target_name of this GatewayUpdateProducerCassandra.  # noqa: E501
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """Sets the target_name of this GatewayUpdateProducerCassandra.

        Target name  # noqa: E501

        :param target_name: The target_name of this GatewayUpdateProducerCassandra.  # noqa: E501
        :type: str
        """

        self._target_name = target_name

    @property
    def token(self):
        """Gets the token of this GatewayUpdateProducerCassandra.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GatewayUpdateProducerCassandra.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GatewayUpdateProducerCassandra.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GatewayUpdateProducerCassandra.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this GatewayUpdateProducerCassandra.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GatewayUpdateProducerCassandra.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GatewayUpdateProducerCassandra.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GatewayUpdateProducerCassandra.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def user_ttl(self):
        """Gets the user_ttl of this GatewayUpdateProducerCassandra.  # noqa: E501

        User TTL  # noqa: E501

        :return: The user_ttl of this GatewayUpdateProducerCassandra.  # noqa: E501
        :rtype: str
        """
        return self._user_ttl

    @user_ttl.setter
    def user_ttl(self, user_ttl):
        """Sets the user_ttl of this GatewayUpdateProducerCassandra.

        User TTL  # noqa: E501

        :param user_ttl: The user_ttl of this GatewayUpdateProducerCassandra.  # noqa: E501
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
        if not isinstance(other, GatewayUpdateProducerCassandra):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayUpdateProducerCassandra):
            return True

        return self.to_dict() != other.to_dict()
