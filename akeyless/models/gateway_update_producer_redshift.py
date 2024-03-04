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


class GatewayUpdateProducerRedshift(object):
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
        'json': 'bool',
        'name': 'str',
        'new_name': 'str',
        'password_length': 'str',
        'producer_encryption_key': 'str',
        'redshift_db_name': 'str',
        'redshift_host': 'str',
        'redshift_password': 'str',
        'redshift_port': 'str',
        'redshift_username': 'str',
        'secure_access_enable': 'str',
        'secure_access_host': 'list[str]',
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
        'json': 'json',
        'name': 'name',
        'new_name': 'new-name',
        'password_length': 'password-length',
        'producer_encryption_key': 'producer-encryption-key',
        'redshift_db_name': 'redshift-db-name',
        'redshift_host': 'redshift-host',
        'redshift_password': 'redshift-password',
        'redshift_port': 'redshift-port',
        'redshift_username': 'redshift-username',
        'secure_access_enable': 'secure-access-enable',
        'secure_access_host': 'secure-access-host',
        'ssl': 'ssl',
        'tags': 'tags',
        'target_name': 'target-name',
        'token': 'token',
        'uid_token': 'uid-token',
        'user_ttl': 'user-ttl'
    }

    def __init__(self, creation_statements=None, delete_protection=None, json=False, name=None, new_name=None, password_length=None, producer_encryption_key=None, redshift_db_name=None, redshift_host='127.0.0.1', redshift_password=None, redshift_port='5439', redshift_username=None, secure_access_enable=None, secure_access_host=None, ssl=False, tags=None, target_name=None, token=None, uid_token=None, user_ttl='60m', local_vars_configuration=None):  # noqa: E501
        """GatewayUpdateProducerRedshift - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._creation_statements = None
        self._delete_protection = None
        self._json = None
        self._name = None
        self._new_name = None
        self._password_length = None
        self._producer_encryption_key = None
        self._redshift_db_name = None
        self._redshift_host = None
        self._redshift_password = None
        self._redshift_port = None
        self._redshift_username = None
        self._secure_access_enable = None
        self._secure_access_host = None
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
        if json is not None:
            self.json = json
        self.name = name
        if new_name is not None:
            self.new_name = new_name
        if password_length is not None:
            self.password_length = password_length
        if producer_encryption_key is not None:
            self.producer_encryption_key = producer_encryption_key
        if redshift_db_name is not None:
            self.redshift_db_name = redshift_db_name
        if redshift_host is not None:
            self.redshift_host = redshift_host
        if redshift_password is not None:
            self.redshift_password = redshift_password
        if redshift_port is not None:
            self.redshift_port = redshift_port
        if redshift_username is not None:
            self.redshift_username = redshift_username
        if secure_access_enable is not None:
            self.secure_access_enable = secure_access_enable
        if secure_access_host is not None:
            self.secure_access_host = secure_access_host
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
        """Gets the creation_statements of this GatewayUpdateProducerRedshift.  # noqa: E501

        Redshift Creation statements  # noqa: E501

        :return: The creation_statements of this GatewayUpdateProducerRedshift.  # noqa: E501
        :rtype: str
        """
        return self._creation_statements

    @creation_statements.setter
    def creation_statements(self, creation_statements):
        """Sets the creation_statements of this GatewayUpdateProducerRedshift.

        Redshift Creation statements  # noqa: E501

        :param creation_statements: The creation_statements of this GatewayUpdateProducerRedshift.  # noqa: E501
        :type: str
        """

        self._creation_statements = creation_statements

    @property
    def delete_protection(self):
        """Gets the delete_protection of this GatewayUpdateProducerRedshift.  # noqa: E501

        Protection from accidental deletion of this item [true/false]  # noqa: E501

        :return: The delete_protection of this GatewayUpdateProducerRedshift.  # noqa: E501
        :rtype: str
        """
        return self._delete_protection

    @delete_protection.setter
    def delete_protection(self, delete_protection):
        """Sets the delete_protection of this GatewayUpdateProducerRedshift.

        Protection from accidental deletion of this item [true/false]  # noqa: E501

        :param delete_protection: The delete_protection of this GatewayUpdateProducerRedshift.  # noqa: E501
        :type: str
        """

        self._delete_protection = delete_protection

    @property
    def json(self):
        """Gets the json of this GatewayUpdateProducerRedshift.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this GatewayUpdateProducerRedshift.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this GatewayUpdateProducerRedshift.

        Set output format to JSON  # noqa: E501

        :param json: The json of this GatewayUpdateProducerRedshift.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def name(self):
        """Gets the name of this GatewayUpdateProducerRedshift.  # noqa: E501

        Dynamic secret name  # noqa: E501

        :return: The name of this GatewayUpdateProducerRedshift.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GatewayUpdateProducerRedshift.

        Dynamic secret name  # noqa: E501

        :param name: The name of this GatewayUpdateProducerRedshift.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def new_name(self):
        """Gets the new_name of this GatewayUpdateProducerRedshift.  # noqa: E501

        Dynamic secret name  # noqa: E501

        :return: The new_name of this GatewayUpdateProducerRedshift.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this GatewayUpdateProducerRedshift.

        Dynamic secret name  # noqa: E501

        :param new_name: The new_name of this GatewayUpdateProducerRedshift.  # noqa: E501
        :type: str
        """

        self._new_name = new_name

    @property
    def password_length(self):
        """Gets the password_length of this GatewayUpdateProducerRedshift.  # noqa: E501

        The length of the password to be generated  # noqa: E501

        :return: The password_length of this GatewayUpdateProducerRedshift.  # noqa: E501
        :rtype: str
        """
        return self._password_length

    @password_length.setter
    def password_length(self, password_length):
        """Sets the password_length of this GatewayUpdateProducerRedshift.

        The length of the password to be generated  # noqa: E501

        :param password_length: The password_length of this GatewayUpdateProducerRedshift.  # noqa: E501
        :type: str
        """

        self._password_length = password_length

    @property
    def producer_encryption_key(self):
        """Gets the producer_encryption_key of this GatewayUpdateProducerRedshift.  # noqa: E501

        Dynamic producer encryption key  # noqa: E501

        :return: The producer_encryption_key of this GatewayUpdateProducerRedshift.  # noqa: E501
        :rtype: str
        """
        return self._producer_encryption_key

    @producer_encryption_key.setter
    def producer_encryption_key(self, producer_encryption_key):
        """Sets the producer_encryption_key of this GatewayUpdateProducerRedshift.

        Dynamic producer encryption key  # noqa: E501

        :param producer_encryption_key: The producer_encryption_key of this GatewayUpdateProducerRedshift.  # noqa: E501
        :type: str
        """

        self._producer_encryption_key = producer_encryption_key

    @property
    def redshift_db_name(self):
        """Gets the redshift_db_name of this GatewayUpdateProducerRedshift.  # noqa: E501

        Redshift DB Name  # noqa: E501

        :return: The redshift_db_name of this GatewayUpdateProducerRedshift.  # noqa: E501
        :rtype: str
        """
        return self._redshift_db_name

    @redshift_db_name.setter
    def redshift_db_name(self, redshift_db_name):
        """Sets the redshift_db_name of this GatewayUpdateProducerRedshift.

        Redshift DB Name  # noqa: E501

        :param redshift_db_name: The redshift_db_name of this GatewayUpdateProducerRedshift.  # noqa: E501
        :type: str
        """

        self._redshift_db_name = redshift_db_name

    @property
    def redshift_host(self):
        """Gets the redshift_host of this GatewayUpdateProducerRedshift.  # noqa: E501

        Redshift Host  # noqa: E501

        :return: The redshift_host of this GatewayUpdateProducerRedshift.  # noqa: E501
        :rtype: str
        """
        return self._redshift_host

    @redshift_host.setter
    def redshift_host(self, redshift_host):
        """Sets the redshift_host of this GatewayUpdateProducerRedshift.

        Redshift Host  # noqa: E501

        :param redshift_host: The redshift_host of this GatewayUpdateProducerRedshift.  # noqa: E501
        :type: str
        """

        self._redshift_host = redshift_host

    @property
    def redshift_password(self):
        """Gets the redshift_password of this GatewayUpdateProducerRedshift.  # noqa: E501

        Redshift Password  # noqa: E501

        :return: The redshift_password of this GatewayUpdateProducerRedshift.  # noqa: E501
        :rtype: str
        """
        return self._redshift_password

    @redshift_password.setter
    def redshift_password(self, redshift_password):
        """Sets the redshift_password of this GatewayUpdateProducerRedshift.

        Redshift Password  # noqa: E501

        :param redshift_password: The redshift_password of this GatewayUpdateProducerRedshift.  # noqa: E501
        :type: str
        """

        self._redshift_password = redshift_password

    @property
    def redshift_port(self):
        """Gets the redshift_port of this GatewayUpdateProducerRedshift.  # noqa: E501

        Redshift Port  # noqa: E501

        :return: The redshift_port of this GatewayUpdateProducerRedshift.  # noqa: E501
        :rtype: str
        """
        return self._redshift_port

    @redshift_port.setter
    def redshift_port(self, redshift_port):
        """Sets the redshift_port of this GatewayUpdateProducerRedshift.

        Redshift Port  # noqa: E501

        :param redshift_port: The redshift_port of this GatewayUpdateProducerRedshift.  # noqa: E501
        :type: str
        """

        self._redshift_port = redshift_port

    @property
    def redshift_username(self):
        """Gets the redshift_username of this GatewayUpdateProducerRedshift.  # noqa: E501

        Redshift Username  # noqa: E501

        :return: The redshift_username of this GatewayUpdateProducerRedshift.  # noqa: E501
        :rtype: str
        """
        return self._redshift_username

    @redshift_username.setter
    def redshift_username(self, redshift_username):
        """Sets the redshift_username of this GatewayUpdateProducerRedshift.

        Redshift Username  # noqa: E501

        :param redshift_username: The redshift_username of this GatewayUpdateProducerRedshift.  # noqa: E501
        :type: str
        """

        self._redshift_username = redshift_username

    @property
    def secure_access_enable(self):
        """Gets the secure_access_enable of this GatewayUpdateProducerRedshift.  # noqa: E501

        Enable/Disable secure remote access [true/false]  # noqa: E501

        :return: The secure_access_enable of this GatewayUpdateProducerRedshift.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_enable

    @secure_access_enable.setter
    def secure_access_enable(self, secure_access_enable):
        """Sets the secure_access_enable of this GatewayUpdateProducerRedshift.

        Enable/Disable secure remote access [true/false]  # noqa: E501

        :param secure_access_enable: The secure_access_enable of this GatewayUpdateProducerRedshift.  # noqa: E501
        :type: str
        """

        self._secure_access_enable = secure_access_enable

    @property
    def secure_access_host(self):
        """Gets the secure_access_host of this GatewayUpdateProducerRedshift.  # noqa: E501

        Target DB servers for connections (In case of Linked Target association, host(s) will inherit Linked Target hosts)  # noqa: E501

        :return: The secure_access_host of this GatewayUpdateProducerRedshift.  # noqa: E501
        :rtype: list[str]
        """
        return self._secure_access_host

    @secure_access_host.setter
    def secure_access_host(self, secure_access_host):
        """Sets the secure_access_host of this GatewayUpdateProducerRedshift.

        Target DB servers for connections (In case of Linked Target association, host(s) will inherit Linked Target hosts)  # noqa: E501

        :param secure_access_host: The secure_access_host of this GatewayUpdateProducerRedshift.  # noqa: E501
        :type: list[str]
        """

        self._secure_access_host = secure_access_host

    @property
    def ssl(self):
        """Gets the ssl of this GatewayUpdateProducerRedshift.  # noqa: E501

        Enable/Disable SSL [true/false]  # noqa: E501

        :return: The ssl of this GatewayUpdateProducerRedshift.  # noqa: E501
        :rtype: bool
        """
        return self._ssl

    @ssl.setter
    def ssl(self, ssl):
        """Sets the ssl of this GatewayUpdateProducerRedshift.

        Enable/Disable SSL [true/false]  # noqa: E501

        :param ssl: The ssl of this GatewayUpdateProducerRedshift.  # noqa: E501
        :type: bool
        """

        self._ssl = ssl

    @property
    def tags(self):
        """Gets the tags of this GatewayUpdateProducerRedshift.  # noqa: E501

        Add tags attached to this object  # noqa: E501

        :return: The tags of this GatewayUpdateProducerRedshift.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this GatewayUpdateProducerRedshift.

        Add tags attached to this object  # noqa: E501

        :param tags: The tags of this GatewayUpdateProducerRedshift.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def target_name(self):
        """Gets the target_name of this GatewayUpdateProducerRedshift.  # noqa: E501

        Target name  # noqa: E501

        :return: The target_name of this GatewayUpdateProducerRedshift.  # noqa: E501
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """Sets the target_name of this GatewayUpdateProducerRedshift.

        Target name  # noqa: E501

        :param target_name: The target_name of this GatewayUpdateProducerRedshift.  # noqa: E501
        :type: str
        """

        self._target_name = target_name

    @property
    def token(self):
        """Gets the token of this GatewayUpdateProducerRedshift.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GatewayUpdateProducerRedshift.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GatewayUpdateProducerRedshift.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GatewayUpdateProducerRedshift.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this GatewayUpdateProducerRedshift.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GatewayUpdateProducerRedshift.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GatewayUpdateProducerRedshift.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GatewayUpdateProducerRedshift.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def user_ttl(self):
        """Gets the user_ttl of this GatewayUpdateProducerRedshift.  # noqa: E501

        User TTL  # noqa: E501

        :return: The user_ttl of this GatewayUpdateProducerRedshift.  # noqa: E501
        :rtype: str
        """
        return self._user_ttl

    @user_ttl.setter
    def user_ttl(self, user_ttl):
        """Sets the user_ttl of this GatewayUpdateProducerRedshift.

        User TTL  # noqa: E501

        :param user_ttl: The user_ttl of this GatewayUpdateProducerRedshift.  # noqa: E501
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
        if not isinstance(other, GatewayUpdateProducerRedshift):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayUpdateProducerRedshift):
            return True

        return self.to_dict() != other.to_dict()
