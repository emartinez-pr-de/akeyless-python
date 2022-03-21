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


class GatewayUpdateProducerCustom(object):
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
        'create_sync_url': 'str',
        'name': 'str',
        'new_name': 'str',
        'payload': 'str',
        'producer_encryption_key_name': 'str',
        'revoke_sync_url': 'str',
        'rotate_sync_url': 'str',
        'tags': 'list[str]',
        'timeout_sec': 'int',
        'token': 'str',
        'uid_token': 'str',
        'user_ttl': 'str'
    }

    attribute_map = {
        'create_sync_url': 'create-sync-url',
        'name': 'name',
        'new_name': 'new-name',
        'payload': 'payload',
        'producer_encryption_key_name': 'producer-encryption-key-name',
        'revoke_sync_url': 'revoke-sync-url',
        'rotate_sync_url': 'rotate-sync-url',
        'tags': 'tags',
        'timeout_sec': 'timeout-sec',
        'token': 'token',
        'uid_token': 'uid-token',
        'user_ttl': 'user-ttl'
    }

    def __init__(self, create_sync_url=None, name=None, new_name=None, payload=None, producer_encryption_key_name=None, revoke_sync_url=None, rotate_sync_url=None, tags=None, timeout_sec=60, token=None, uid_token=None, user_ttl='60m', local_vars_configuration=None):  # noqa: E501
        """GatewayUpdateProducerCustom - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._create_sync_url = None
        self._name = None
        self._new_name = None
        self._payload = None
        self._producer_encryption_key_name = None
        self._revoke_sync_url = None
        self._rotate_sync_url = None
        self._tags = None
        self._timeout_sec = None
        self._token = None
        self._uid_token = None
        self._user_ttl = None
        self.discriminator = None

        self.create_sync_url = create_sync_url
        self.name = name
        if new_name is not None:
            self.new_name = new_name
        if payload is not None:
            self.payload = payload
        if producer_encryption_key_name is not None:
            self.producer_encryption_key_name = producer_encryption_key_name
        self.revoke_sync_url = revoke_sync_url
        if rotate_sync_url is not None:
            self.rotate_sync_url = rotate_sync_url
        if tags is not None:
            self.tags = tags
        if timeout_sec is not None:
            self.timeout_sec = timeout_sec
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if user_ttl is not None:
            self.user_ttl = user_ttl

    @property
    def create_sync_url(self):
        """Gets the create_sync_url of this GatewayUpdateProducerCustom.  # noqa: E501

        URL of an endpoint that implements /sync/create method, for example https://webhook.example.com/sync/create  # noqa: E501

        :return: The create_sync_url of this GatewayUpdateProducerCustom.  # noqa: E501
        :rtype: str
        """
        return self._create_sync_url

    @create_sync_url.setter
    def create_sync_url(self, create_sync_url):
        """Sets the create_sync_url of this GatewayUpdateProducerCustom.

        URL of an endpoint that implements /sync/create method, for example https://webhook.example.com/sync/create  # noqa: E501

        :param create_sync_url: The create_sync_url of this GatewayUpdateProducerCustom.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and create_sync_url is None:  # noqa: E501
            raise ValueError("Invalid value for `create_sync_url`, must not be `None`")  # noqa: E501

        self._create_sync_url = create_sync_url

    @property
    def name(self):
        """Gets the name of this GatewayUpdateProducerCustom.  # noqa: E501

        Producer name  # noqa: E501

        :return: The name of this GatewayUpdateProducerCustom.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GatewayUpdateProducerCustom.

        Producer name  # noqa: E501

        :param name: The name of this GatewayUpdateProducerCustom.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def new_name(self):
        """Gets the new_name of this GatewayUpdateProducerCustom.  # noqa: E501

        Producer name  # noqa: E501

        :return: The new_name of this GatewayUpdateProducerCustom.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this GatewayUpdateProducerCustom.

        Producer name  # noqa: E501

        :param new_name: The new_name of this GatewayUpdateProducerCustom.  # noqa: E501
        :type: str
        """

        self._new_name = new_name

    @property
    def payload(self):
        """Gets the payload of this GatewayUpdateProducerCustom.  # noqa: E501

        Secret payload to be sent with each create/revoke webhook request  # noqa: E501

        :return: The payload of this GatewayUpdateProducerCustom.  # noqa: E501
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this GatewayUpdateProducerCustom.

        Secret payload to be sent with each create/revoke webhook request  # noqa: E501

        :param payload: The payload of this GatewayUpdateProducerCustom.  # noqa: E501
        :type: str
        """

        self._payload = payload

    @property
    def producer_encryption_key_name(self):
        """Gets the producer_encryption_key_name of this GatewayUpdateProducerCustom.  # noqa: E501

        Dynamic producer encryption key  # noqa: E501

        :return: The producer_encryption_key_name of this GatewayUpdateProducerCustom.  # noqa: E501
        :rtype: str
        """
        return self._producer_encryption_key_name

    @producer_encryption_key_name.setter
    def producer_encryption_key_name(self, producer_encryption_key_name):
        """Sets the producer_encryption_key_name of this GatewayUpdateProducerCustom.

        Dynamic producer encryption key  # noqa: E501

        :param producer_encryption_key_name: The producer_encryption_key_name of this GatewayUpdateProducerCustom.  # noqa: E501
        :type: str
        """

        self._producer_encryption_key_name = producer_encryption_key_name

    @property
    def revoke_sync_url(self):
        """Gets the revoke_sync_url of this GatewayUpdateProducerCustom.  # noqa: E501

        URL of an endpoint that implements /sync/revoke method, for example https://webhook.example.com/sync/revoke  # noqa: E501

        :return: The revoke_sync_url of this GatewayUpdateProducerCustom.  # noqa: E501
        :rtype: str
        """
        return self._revoke_sync_url

    @revoke_sync_url.setter
    def revoke_sync_url(self, revoke_sync_url):
        """Sets the revoke_sync_url of this GatewayUpdateProducerCustom.

        URL of an endpoint that implements /sync/revoke method, for example https://webhook.example.com/sync/revoke  # noqa: E501

        :param revoke_sync_url: The revoke_sync_url of this GatewayUpdateProducerCustom.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and revoke_sync_url is None:  # noqa: E501
            raise ValueError("Invalid value for `revoke_sync_url`, must not be `None`")  # noqa: E501

        self._revoke_sync_url = revoke_sync_url

    @property
    def rotate_sync_url(self):
        """Gets the rotate_sync_url of this GatewayUpdateProducerCustom.  # noqa: E501

        URL of an endpoint that implements /sync/rotate method, for example https://webhook.example.com/sync/rotate  # noqa: E501

        :return: The rotate_sync_url of this GatewayUpdateProducerCustom.  # noqa: E501
        :rtype: str
        """
        return self._rotate_sync_url

    @rotate_sync_url.setter
    def rotate_sync_url(self, rotate_sync_url):
        """Sets the rotate_sync_url of this GatewayUpdateProducerCustom.

        URL of an endpoint that implements /sync/rotate method, for example https://webhook.example.com/sync/rotate  # noqa: E501

        :param rotate_sync_url: The rotate_sync_url of this GatewayUpdateProducerCustom.  # noqa: E501
        :type: str
        """

        self._rotate_sync_url = rotate_sync_url

    @property
    def tags(self):
        """Gets the tags of this GatewayUpdateProducerCustom.  # noqa: E501

        List of the tags attached to this secret  # noqa: E501

        :return: The tags of this GatewayUpdateProducerCustom.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this GatewayUpdateProducerCustom.

        List of the tags attached to this secret  # noqa: E501

        :param tags: The tags of this GatewayUpdateProducerCustom.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def timeout_sec(self):
        """Gets the timeout_sec of this GatewayUpdateProducerCustom.  # noqa: E501

        Maximum allowed time in seconds for the webhook to return the results  # noqa: E501

        :return: The timeout_sec of this GatewayUpdateProducerCustom.  # noqa: E501
        :rtype: int
        """
        return self._timeout_sec

    @timeout_sec.setter
    def timeout_sec(self, timeout_sec):
        """Sets the timeout_sec of this GatewayUpdateProducerCustom.

        Maximum allowed time in seconds for the webhook to return the results  # noqa: E501

        :param timeout_sec: The timeout_sec of this GatewayUpdateProducerCustom.  # noqa: E501
        :type: int
        """

        self._timeout_sec = timeout_sec

    @property
    def token(self):
        """Gets the token of this GatewayUpdateProducerCustom.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GatewayUpdateProducerCustom.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GatewayUpdateProducerCustom.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GatewayUpdateProducerCustom.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this GatewayUpdateProducerCustom.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GatewayUpdateProducerCustom.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GatewayUpdateProducerCustom.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GatewayUpdateProducerCustom.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def user_ttl(self):
        """Gets the user_ttl of this GatewayUpdateProducerCustom.  # noqa: E501

        User TTL  # noqa: E501

        :return: The user_ttl of this GatewayUpdateProducerCustom.  # noqa: E501
        :rtype: str
        """
        return self._user_ttl

    @user_ttl.setter
    def user_ttl(self, user_ttl):
        """Sets the user_ttl of this GatewayUpdateProducerCustom.

        User TTL  # noqa: E501

        :param user_ttl: The user_ttl of this GatewayUpdateProducerCustom.  # noqa: E501
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
        if not isinstance(other, GatewayUpdateProducerCustom):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayUpdateProducerCustom):
            return True

        return self.to_dict() != other.to_dict()
