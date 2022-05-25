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


class GatewayCreateProducerRabbitMQ(object):
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
        'name': 'str',
        'producer_encryption_key_name': 'str',
        'rabbitmq_admin_pwd': 'str',
        'rabbitmq_admin_user': 'str',
        'rabbitmq_server_uri': 'str',
        'rabbitmq_user_conf_permission': 'str',
        'rabbitmq_user_read_permission': 'str',
        'rabbitmq_user_tags': 'str',
        'rabbitmq_user_vhost': 'str',
        'rabbitmq_user_write_permission': 'str',
        'secure_access_enable': 'str',
        'secure_access_url': 'str',
        'secure_access_web': 'bool',
        'secure_access_web_browsing': 'bool',
        'secure_access_web_proxy': 'bool',
        'tags': 'list[str]',
        'target_name': 'str',
        'token': 'str',
        'uid_token': 'str',
        'user_ttl': 'str'
    }

    attribute_map = {
        'name': 'name',
        'producer_encryption_key_name': 'producer-encryption-key-name',
        'rabbitmq_admin_pwd': 'rabbitmq-admin-pwd',
        'rabbitmq_admin_user': 'rabbitmq-admin-user',
        'rabbitmq_server_uri': 'rabbitmq-server-uri',
        'rabbitmq_user_conf_permission': 'rabbitmq-user-conf-permission',
        'rabbitmq_user_read_permission': 'rabbitmq-user-read-permission',
        'rabbitmq_user_tags': 'rabbitmq-user-tags',
        'rabbitmq_user_vhost': 'rabbitmq-user-vhost',
        'rabbitmq_user_write_permission': 'rabbitmq-user-write-permission',
        'secure_access_enable': 'secure-access-enable',
        'secure_access_url': 'secure-access-url',
        'secure_access_web': 'secure-access-web',
        'secure_access_web_browsing': 'secure-access-web-browsing',
        'secure_access_web_proxy': 'secure-access-web-proxy',
        'tags': 'tags',
        'target_name': 'target-name',
        'token': 'token',
        'uid_token': 'uid-token',
        'user_ttl': 'user-ttl'
    }

    def __init__(self, name=None, producer_encryption_key_name=None, rabbitmq_admin_pwd=None, rabbitmq_admin_user=None, rabbitmq_server_uri=None, rabbitmq_user_conf_permission=None, rabbitmq_user_read_permission=None, rabbitmq_user_tags=None, rabbitmq_user_vhost=None, rabbitmq_user_write_permission=None, secure_access_enable=None, secure_access_url=None, secure_access_web=True, secure_access_web_browsing=None, secure_access_web_proxy=None, tags=None, target_name=None, token=None, uid_token=None, user_ttl='60m', local_vars_configuration=None):  # noqa: E501
        """GatewayCreateProducerRabbitMQ - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._producer_encryption_key_name = None
        self._rabbitmq_admin_pwd = None
        self._rabbitmq_admin_user = None
        self._rabbitmq_server_uri = None
        self._rabbitmq_user_conf_permission = None
        self._rabbitmq_user_read_permission = None
        self._rabbitmq_user_tags = None
        self._rabbitmq_user_vhost = None
        self._rabbitmq_user_write_permission = None
        self._secure_access_enable = None
        self._secure_access_url = None
        self._secure_access_web = None
        self._secure_access_web_browsing = None
        self._secure_access_web_proxy = None
        self._tags = None
        self._target_name = None
        self._token = None
        self._uid_token = None
        self._user_ttl = None
        self.discriminator = None

        self.name = name
        if producer_encryption_key_name is not None:
            self.producer_encryption_key_name = producer_encryption_key_name
        if rabbitmq_admin_pwd is not None:
            self.rabbitmq_admin_pwd = rabbitmq_admin_pwd
        if rabbitmq_admin_user is not None:
            self.rabbitmq_admin_user = rabbitmq_admin_user
        if rabbitmq_server_uri is not None:
            self.rabbitmq_server_uri = rabbitmq_server_uri
        if rabbitmq_user_conf_permission is not None:
            self.rabbitmq_user_conf_permission = rabbitmq_user_conf_permission
        if rabbitmq_user_read_permission is not None:
            self.rabbitmq_user_read_permission = rabbitmq_user_read_permission
        if rabbitmq_user_tags is not None:
            self.rabbitmq_user_tags = rabbitmq_user_tags
        if rabbitmq_user_vhost is not None:
            self.rabbitmq_user_vhost = rabbitmq_user_vhost
        if rabbitmq_user_write_permission is not None:
            self.rabbitmq_user_write_permission = rabbitmq_user_write_permission
        if secure_access_enable is not None:
            self.secure_access_enable = secure_access_enable
        if secure_access_url is not None:
            self.secure_access_url = secure_access_url
        if secure_access_web is not None:
            self.secure_access_web = secure_access_web
        if secure_access_web_browsing is not None:
            self.secure_access_web_browsing = secure_access_web_browsing
        if secure_access_web_proxy is not None:
            self.secure_access_web_proxy = secure_access_web_proxy
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
    def name(self):
        """Gets the name of this GatewayCreateProducerRabbitMQ.  # noqa: E501

        Producer name  # noqa: E501

        :return: The name of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GatewayCreateProducerRabbitMQ.

        Producer name  # noqa: E501

        :param name: The name of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def producer_encryption_key_name(self):
        """Gets the producer_encryption_key_name of this GatewayCreateProducerRabbitMQ.  # noqa: E501

        Dynamic producer encryption key  # noqa: E501

        :return: The producer_encryption_key_name of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :rtype: str
        """
        return self._producer_encryption_key_name

    @producer_encryption_key_name.setter
    def producer_encryption_key_name(self, producer_encryption_key_name):
        """Sets the producer_encryption_key_name of this GatewayCreateProducerRabbitMQ.

        Dynamic producer encryption key  # noqa: E501

        :param producer_encryption_key_name: The producer_encryption_key_name of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :type: str
        """

        self._producer_encryption_key_name = producer_encryption_key_name

    @property
    def rabbitmq_admin_pwd(self):
        """Gets the rabbitmq_admin_pwd of this GatewayCreateProducerRabbitMQ.  # noqa: E501

        RabbitMQ Admin password  # noqa: E501

        :return: The rabbitmq_admin_pwd of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :rtype: str
        """
        return self._rabbitmq_admin_pwd

    @rabbitmq_admin_pwd.setter
    def rabbitmq_admin_pwd(self, rabbitmq_admin_pwd):
        """Sets the rabbitmq_admin_pwd of this GatewayCreateProducerRabbitMQ.

        RabbitMQ Admin password  # noqa: E501

        :param rabbitmq_admin_pwd: The rabbitmq_admin_pwd of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :type: str
        """

        self._rabbitmq_admin_pwd = rabbitmq_admin_pwd

    @property
    def rabbitmq_admin_user(self):
        """Gets the rabbitmq_admin_user of this GatewayCreateProducerRabbitMQ.  # noqa: E501

        RabbitMQ Admin User  # noqa: E501

        :return: The rabbitmq_admin_user of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :rtype: str
        """
        return self._rabbitmq_admin_user

    @rabbitmq_admin_user.setter
    def rabbitmq_admin_user(self, rabbitmq_admin_user):
        """Sets the rabbitmq_admin_user of this GatewayCreateProducerRabbitMQ.

        RabbitMQ Admin User  # noqa: E501

        :param rabbitmq_admin_user: The rabbitmq_admin_user of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :type: str
        """

        self._rabbitmq_admin_user = rabbitmq_admin_user

    @property
    def rabbitmq_server_uri(self):
        """Gets the rabbitmq_server_uri of this GatewayCreateProducerRabbitMQ.  # noqa: E501

        Server URI  # noqa: E501

        :return: The rabbitmq_server_uri of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :rtype: str
        """
        return self._rabbitmq_server_uri

    @rabbitmq_server_uri.setter
    def rabbitmq_server_uri(self, rabbitmq_server_uri):
        """Sets the rabbitmq_server_uri of this GatewayCreateProducerRabbitMQ.

        Server URI  # noqa: E501

        :param rabbitmq_server_uri: The rabbitmq_server_uri of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :type: str
        """

        self._rabbitmq_server_uri = rabbitmq_server_uri

    @property
    def rabbitmq_user_conf_permission(self):
        """Gets the rabbitmq_user_conf_permission of this GatewayCreateProducerRabbitMQ.  # noqa: E501

        User configuration permission  # noqa: E501

        :return: The rabbitmq_user_conf_permission of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :rtype: str
        """
        return self._rabbitmq_user_conf_permission

    @rabbitmq_user_conf_permission.setter
    def rabbitmq_user_conf_permission(self, rabbitmq_user_conf_permission):
        """Sets the rabbitmq_user_conf_permission of this GatewayCreateProducerRabbitMQ.

        User configuration permission  # noqa: E501

        :param rabbitmq_user_conf_permission: The rabbitmq_user_conf_permission of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :type: str
        """

        self._rabbitmq_user_conf_permission = rabbitmq_user_conf_permission

    @property
    def rabbitmq_user_read_permission(self):
        """Gets the rabbitmq_user_read_permission of this GatewayCreateProducerRabbitMQ.  # noqa: E501

        User read permission  # noqa: E501

        :return: The rabbitmq_user_read_permission of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :rtype: str
        """
        return self._rabbitmq_user_read_permission

    @rabbitmq_user_read_permission.setter
    def rabbitmq_user_read_permission(self, rabbitmq_user_read_permission):
        """Sets the rabbitmq_user_read_permission of this GatewayCreateProducerRabbitMQ.

        User read permission  # noqa: E501

        :param rabbitmq_user_read_permission: The rabbitmq_user_read_permission of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :type: str
        """

        self._rabbitmq_user_read_permission = rabbitmq_user_read_permission

    @property
    def rabbitmq_user_tags(self):
        """Gets the rabbitmq_user_tags of this GatewayCreateProducerRabbitMQ.  # noqa: E501

        User Tags  # noqa: E501

        :return: The rabbitmq_user_tags of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :rtype: str
        """
        return self._rabbitmq_user_tags

    @rabbitmq_user_tags.setter
    def rabbitmq_user_tags(self, rabbitmq_user_tags):
        """Sets the rabbitmq_user_tags of this GatewayCreateProducerRabbitMQ.

        User Tags  # noqa: E501

        :param rabbitmq_user_tags: The rabbitmq_user_tags of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :type: str
        """

        self._rabbitmq_user_tags = rabbitmq_user_tags

    @property
    def rabbitmq_user_vhost(self):
        """Gets the rabbitmq_user_vhost of this GatewayCreateProducerRabbitMQ.  # noqa: E501

        User Virtual Host  # noqa: E501

        :return: The rabbitmq_user_vhost of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :rtype: str
        """
        return self._rabbitmq_user_vhost

    @rabbitmq_user_vhost.setter
    def rabbitmq_user_vhost(self, rabbitmq_user_vhost):
        """Sets the rabbitmq_user_vhost of this GatewayCreateProducerRabbitMQ.

        User Virtual Host  # noqa: E501

        :param rabbitmq_user_vhost: The rabbitmq_user_vhost of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :type: str
        """

        self._rabbitmq_user_vhost = rabbitmq_user_vhost

    @property
    def rabbitmq_user_write_permission(self):
        """Gets the rabbitmq_user_write_permission of this GatewayCreateProducerRabbitMQ.  # noqa: E501

        User write permission  # noqa: E501

        :return: The rabbitmq_user_write_permission of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :rtype: str
        """
        return self._rabbitmq_user_write_permission

    @rabbitmq_user_write_permission.setter
    def rabbitmq_user_write_permission(self, rabbitmq_user_write_permission):
        """Sets the rabbitmq_user_write_permission of this GatewayCreateProducerRabbitMQ.

        User write permission  # noqa: E501

        :param rabbitmq_user_write_permission: The rabbitmq_user_write_permission of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :type: str
        """

        self._rabbitmq_user_write_permission = rabbitmq_user_write_permission

    @property
    def secure_access_enable(self):
        """Gets the secure_access_enable of this GatewayCreateProducerRabbitMQ.  # noqa: E501


        :return: The secure_access_enable of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_enable

    @secure_access_enable.setter
    def secure_access_enable(self, secure_access_enable):
        """Sets the secure_access_enable of this GatewayCreateProducerRabbitMQ.


        :param secure_access_enable: The secure_access_enable of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :type: str
        """

        self._secure_access_enable = secure_access_enable

    @property
    def secure_access_url(self):
        """Gets the secure_access_url of this GatewayCreateProducerRabbitMQ.  # noqa: E501


        :return: The secure_access_url of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_url

    @secure_access_url.setter
    def secure_access_url(self, secure_access_url):
        """Sets the secure_access_url of this GatewayCreateProducerRabbitMQ.


        :param secure_access_url: The secure_access_url of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :type: str
        """

        self._secure_access_url = secure_access_url

    @property
    def secure_access_web(self):
        """Gets the secure_access_web of this GatewayCreateProducerRabbitMQ.  # noqa: E501

        Secure Access Web Category  # noqa: E501

        :return: The secure_access_web of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :rtype: bool
        """
        return self._secure_access_web

    @secure_access_web.setter
    def secure_access_web(self, secure_access_web):
        """Sets the secure_access_web of this GatewayCreateProducerRabbitMQ.

        Secure Access Web Category  # noqa: E501

        :param secure_access_web: The secure_access_web of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :type: bool
        """

        self._secure_access_web = secure_access_web

    @property
    def secure_access_web_browsing(self):
        """Gets the secure_access_web_browsing of this GatewayCreateProducerRabbitMQ.  # noqa: E501


        :return: The secure_access_web_browsing of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :rtype: bool
        """
        return self._secure_access_web_browsing

    @secure_access_web_browsing.setter
    def secure_access_web_browsing(self, secure_access_web_browsing):
        """Sets the secure_access_web_browsing of this GatewayCreateProducerRabbitMQ.


        :param secure_access_web_browsing: The secure_access_web_browsing of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :type: bool
        """

        self._secure_access_web_browsing = secure_access_web_browsing

    @property
    def secure_access_web_proxy(self):
        """Gets the secure_access_web_proxy of this GatewayCreateProducerRabbitMQ.  # noqa: E501


        :return: The secure_access_web_proxy of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :rtype: bool
        """
        return self._secure_access_web_proxy

    @secure_access_web_proxy.setter
    def secure_access_web_proxy(self, secure_access_web_proxy):
        """Sets the secure_access_web_proxy of this GatewayCreateProducerRabbitMQ.


        :param secure_access_web_proxy: The secure_access_web_proxy of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :type: bool
        """

        self._secure_access_web_proxy = secure_access_web_proxy

    @property
    def tags(self):
        """Gets the tags of this GatewayCreateProducerRabbitMQ.  # noqa: E501

        List of the tags attached to this secret  # noqa: E501

        :return: The tags of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this GatewayCreateProducerRabbitMQ.

        List of the tags attached to this secret  # noqa: E501

        :param tags: The tags of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def target_name(self):
        """Gets the target_name of this GatewayCreateProducerRabbitMQ.  # noqa: E501

        Target name  # noqa: E501

        :return: The target_name of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """Sets the target_name of this GatewayCreateProducerRabbitMQ.

        Target name  # noqa: E501

        :param target_name: The target_name of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :type: str
        """

        self._target_name = target_name

    @property
    def token(self):
        """Gets the token of this GatewayCreateProducerRabbitMQ.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GatewayCreateProducerRabbitMQ.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this GatewayCreateProducerRabbitMQ.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GatewayCreateProducerRabbitMQ.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def user_ttl(self):
        """Gets the user_ttl of this GatewayCreateProducerRabbitMQ.  # noqa: E501

        User TTL  # noqa: E501

        :return: The user_ttl of this GatewayCreateProducerRabbitMQ.  # noqa: E501
        :rtype: str
        """
        return self._user_ttl

    @user_ttl.setter
    def user_ttl(self, user_ttl):
        """Sets the user_ttl of this GatewayCreateProducerRabbitMQ.

        User TTL  # noqa: E501

        :param user_ttl: The user_ttl of this GatewayCreateProducerRabbitMQ.  # noqa: E501
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
        if not isinstance(other, GatewayCreateProducerRabbitMQ):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayCreateProducerRabbitMQ):
            return True

        return self.to_dict() != other.to_dict()
