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


class GatewayCreateProducerGke(object):
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
        'gateway_url': 'str',
        'gke_cluster_cert': 'str',
        'gke_cluster_endpoint': 'str',
        'gke_cluster_name': 'str',
        'gke_service_account_email': 'str',
        'name': 'str',
        'password': 'str',
        'producer_encryption_key_name': 'str',
        'token': 'str',
        'uid_token': 'str',
        'user_ttl': 'str',
        'username': 'str'
    }

    attribute_map = {
        'gateway_url': 'gateway-url',
        'gke_cluster_cert': 'gke-cluster-cert',
        'gke_cluster_endpoint': 'gke-cluster-endpoint',
        'gke_cluster_name': 'gke-cluster-name',
        'gke_service_account_email': 'gke-service-account-email',
        'name': 'name',
        'password': 'password',
        'producer_encryption_key_name': 'producer-encryption-key-name',
        'token': 'token',
        'uid_token': 'uid-token',
        'user_ttl': 'user-ttl',
        'username': 'username'
    }

    def __init__(self, gateway_url='http://localhost:8000', gke_cluster_cert=None, gke_cluster_endpoint=None, gke_cluster_name=None, gke_service_account_email=None, name=None, password=None, producer_encryption_key_name=None, token=None, uid_token=None, user_ttl='60m', username=None, local_vars_configuration=None):  # noqa: E501
        """GatewayCreateProducerGke - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._gateway_url = None
        self._gke_cluster_cert = None
        self._gke_cluster_endpoint = None
        self._gke_cluster_name = None
        self._gke_service_account_email = None
        self._name = None
        self._password = None
        self._producer_encryption_key_name = None
        self._token = None
        self._uid_token = None
        self._user_ttl = None
        self._username = None
        self.discriminator = None

        if gateway_url is not None:
            self.gateway_url = gateway_url
        self.gke_cluster_cert = gke_cluster_cert
        self.gke_cluster_endpoint = gke_cluster_endpoint
        self.gke_cluster_name = gke_cluster_name
        self.gke_service_account_email = gke_service_account_email
        self.name = name
        if password is not None:
            self.password = password
        if producer_encryption_key_name is not None:
            self.producer_encryption_key_name = producer_encryption_key_name
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if user_ttl is not None:
            self.user_ttl = user_ttl
        if username is not None:
            self.username = username

    @property
    def gateway_url(self):
        """Gets the gateway_url of this GatewayCreateProducerGke.  # noqa: E501

        Gateway url  # noqa: E501

        :return: The gateway_url of this GatewayCreateProducerGke.  # noqa: E501
        :rtype: str
        """
        return self._gateway_url

    @gateway_url.setter
    def gateway_url(self, gateway_url):
        """Sets the gateway_url of this GatewayCreateProducerGke.

        Gateway url  # noqa: E501

        :param gateway_url: The gateway_url of this GatewayCreateProducerGke.  # noqa: E501
        :type: str
        """

        self._gateway_url = gateway_url

    @property
    def gke_cluster_cert(self):
        """Gets the gke_cluster_cert of this GatewayCreateProducerGke.  # noqa: E501

        GKE cluster CA certificate  # noqa: E501

        :return: The gke_cluster_cert of this GatewayCreateProducerGke.  # noqa: E501
        :rtype: str
        """
        return self._gke_cluster_cert

    @gke_cluster_cert.setter
    def gke_cluster_cert(self, gke_cluster_cert):
        """Sets the gke_cluster_cert of this GatewayCreateProducerGke.

        GKE cluster CA certificate  # noqa: E501

        :param gke_cluster_cert: The gke_cluster_cert of this GatewayCreateProducerGke.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and gke_cluster_cert is None:  # noqa: E501
            raise ValueError("Invalid value for `gke_cluster_cert`, must not be `None`")  # noqa: E501

        self._gke_cluster_cert = gke_cluster_cert

    @property
    def gke_cluster_endpoint(self):
        """Gets the gke_cluster_endpoint of this GatewayCreateProducerGke.  # noqa: E501

        GKE cluster URL endpoint  # noqa: E501

        :return: The gke_cluster_endpoint of this GatewayCreateProducerGke.  # noqa: E501
        :rtype: str
        """
        return self._gke_cluster_endpoint

    @gke_cluster_endpoint.setter
    def gke_cluster_endpoint(self, gke_cluster_endpoint):
        """Sets the gke_cluster_endpoint of this GatewayCreateProducerGke.

        GKE cluster URL endpoint  # noqa: E501

        :param gke_cluster_endpoint: The gke_cluster_endpoint of this GatewayCreateProducerGke.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and gke_cluster_endpoint is None:  # noqa: E501
            raise ValueError("Invalid value for `gke_cluster_endpoint`, must not be `None`")  # noqa: E501

        self._gke_cluster_endpoint = gke_cluster_endpoint

    @property
    def gke_cluster_name(self):
        """Gets the gke_cluster_name of this GatewayCreateProducerGke.  # noqa: E501

        GKE cluster name  # noqa: E501

        :return: The gke_cluster_name of this GatewayCreateProducerGke.  # noqa: E501
        :rtype: str
        """
        return self._gke_cluster_name

    @gke_cluster_name.setter
    def gke_cluster_name(self, gke_cluster_name):
        """Sets the gke_cluster_name of this GatewayCreateProducerGke.

        GKE cluster name  # noqa: E501

        :param gke_cluster_name: The gke_cluster_name of this GatewayCreateProducerGke.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and gke_cluster_name is None:  # noqa: E501
            raise ValueError("Invalid value for `gke_cluster_name`, must not be `None`")  # noqa: E501

        self._gke_cluster_name = gke_cluster_name

    @property
    def gke_service_account_email(self):
        """Gets the gke_service_account_email of this GatewayCreateProducerGke.  # noqa: E501

        GKE service account email  # noqa: E501

        :return: The gke_service_account_email of this GatewayCreateProducerGke.  # noqa: E501
        :rtype: str
        """
        return self._gke_service_account_email

    @gke_service_account_email.setter
    def gke_service_account_email(self, gke_service_account_email):
        """Sets the gke_service_account_email of this GatewayCreateProducerGke.

        GKE service account email  # noqa: E501

        :param gke_service_account_email: The gke_service_account_email of this GatewayCreateProducerGke.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and gke_service_account_email is None:  # noqa: E501
            raise ValueError("Invalid value for `gke_service_account_email`, must not be `None`")  # noqa: E501

        self._gke_service_account_email = gke_service_account_email

    @property
    def name(self):
        """Gets the name of this GatewayCreateProducerGke.  # noqa: E501

        Producer name  # noqa: E501

        :return: The name of this GatewayCreateProducerGke.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GatewayCreateProducerGke.

        Producer name  # noqa: E501

        :param name: The name of this GatewayCreateProducerGke.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def password(self):
        """Gets the password of this GatewayCreateProducerGke.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The password of this GatewayCreateProducerGke.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this GatewayCreateProducerGke.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param password: The password of this GatewayCreateProducerGke.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def producer_encryption_key_name(self):
        """Gets the producer_encryption_key_name of this GatewayCreateProducerGke.  # noqa: E501

        Dynamic producer encryption key  # noqa: E501

        :return: The producer_encryption_key_name of this GatewayCreateProducerGke.  # noqa: E501
        :rtype: str
        """
        return self._producer_encryption_key_name

    @producer_encryption_key_name.setter
    def producer_encryption_key_name(self, producer_encryption_key_name):
        """Sets the producer_encryption_key_name of this GatewayCreateProducerGke.

        Dynamic producer encryption key  # noqa: E501

        :param producer_encryption_key_name: The producer_encryption_key_name of this GatewayCreateProducerGke.  # noqa: E501
        :type: str
        """

        self._producer_encryption_key_name = producer_encryption_key_name

    @property
    def token(self):
        """Gets the token of this GatewayCreateProducerGke.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GatewayCreateProducerGke.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GatewayCreateProducerGke.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GatewayCreateProducerGke.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this GatewayCreateProducerGke.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GatewayCreateProducerGke.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GatewayCreateProducerGke.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GatewayCreateProducerGke.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def user_ttl(self):
        """Gets the user_ttl of this GatewayCreateProducerGke.  # noqa: E501

        User TTL  # noqa: E501

        :return: The user_ttl of this GatewayCreateProducerGke.  # noqa: E501
        :rtype: str
        """
        return self._user_ttl

    @user_ttl.setter
    def user_ttl(self, user_ttl):
        """Sets the user_ttl of this GatewayCreateProducerGke.

        User TTL  # noqa: E501

        :param user_ttl: The user_ttl of this GatewayCreateProducerGke.  # noqa: E501
        :type: str
        """

        self._user_ttl = user_ttl

    @property
    def username(self):
        """Gets the username of this GatewayCreateProducerGke.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The username of this GatewayCreateProducerGke.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this GatewayCreateProducerGke.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param username: The username of this GatewayCreateProducerGke.  # noqa: E501
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
        if not isinstance(other, GatewayCreateProducerGke):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayCreateProducerGke):
            return True

        return self.to_dict() != other.to_dict()
