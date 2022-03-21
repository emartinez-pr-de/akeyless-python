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


class GatewayUpdateProducerNativeK8S(object):
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
        'k8s_cluster_ca_cert': 'str',
        'k8s_cluster_endpoint': 'str',
        'k8s_cluster_token': 'str',
        'k8s_namespace': 'str',
        'k8s_service_account': 'str',
        'name': 'str',
        'new_name': 'str',
        'producer_encryption_key_name': 'str',
        'secure_access_allow_port_forwading': 'bool',
        'secure_access_bastion_issuer': 'str',
        'secure_access_cluster_endpoint': 'str',
        'secure_access_dashboard_url': 'str',
        'secure_access_enable': 'str',
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
        'k8s_cluster_ca_cert': 'k8s-cluster-ca-cert',
        'k8s_cluster_endpoint': 'k8s-cluster-endpoint',
        'k8s_cluster_token': 'k8s-cluster-token',
        'k8s_namespace': 'k8s-namespace',
        'k8s_service_account': 'k8s-service-account',
        'name': 'name',
        'new_name': 'new-name',
        'producer_encryption_key_name': 'producer-encryption-key-name',
        'secure_access_allow_port_forwading': 'secure-access-allow-port-forwading',
        'secure_access_bastion_issuer': 'secure-access-bastion-issuer',
        'secure_access_cluster_endpoint': 'secure-access-cluster-endpoint',
        'secure_access_dashboard_url': 'secure-access-dashboard-url',
        'secure_access_enable': 'secure-access-enable',
        'secure_access_web': 'secure-access-web',
        'secure_access_web_browsing': 'secure-access-web-browsing',
        'secure_access_web_proxy': 'secure-access-web-proxy',
        'tags': 'tags',
        'target_name': 'target-name',
        'token': 'token',
        'uid_token': 'uid-token',
        'user_ttl': 'user-ttl'
    }

    def __init__(self, k8s_cluster_ca_cert=None, k8s_cluster_endpoint=None, k8s_cluster_token=None, k8s_namespace=None, k8s_service_account=None, name=None, new_name=None, producer_encryption_key_name=None, secure_access_allow_port_forwading=None, secure_access_bastion_issuer=None, secure_access_cluster_endpoint=None, secure_access_dashboard_url=None, secure_access_enable=None, secure_access_web=None, secure_access_web_browsing=None, secure_access_web_proxy=None, tags=None, target_name=None, token=None, uid_token=None, user_ttl='60m', local_vars_configuration=None):  # noqa: E501
        """GatewayUpdateProducerNativeK8S - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._k8s_cluster_ca_cert = None
        self._k8s_cluster_endpoint = None
        self._k8s_cluster_token = None
        self._k8s_namespace = None
        self._k8s_service_account = None
        self._name = None
        self._new_name = None
        self._producer_encryption_key_name = None
        self._secure_access_allow_port_forwading = None
        self._secure_access_bastion_issuer = None
        self._secure_access_cluster_endpoint = None
        self._secure_access_dashboard_url = None
        self._secure_access_enable = None
        self._secure_access_web = None
        self._secure_access_web_browsing = None
        self._secure_access_web_proxy = None
        self._tags = None
        self._target_name = None
        self._token = None
        self._uid_token = None
        self._user_ttl = None
        self.discriminator = None

        if k8s_cluster_ca_cert is not None:
            self.k8s_cluster_ca_cert = k8s_cluster_ca_cert
        if k8s_cluster_endpoint is not None:
            self.k8s_cluster_endpoint = k8s_cluster_endpoint
        if k8s_cluster_token is not None:
            self.k8s_cluster_token = k8s_cluster_token
        if k8s_namespace is not None:
            self.k8s_namespace = k8s_namespace
        if k8s_service_account is not None:
            self.k8s_service_account = k8s_service_account
        self.name = name
        if new_name is not None:
            self.new_name = new_name
        if producer_encryption_key_name is not None:
            self.producer_encryption_key_name = producer_encryption_key_name
        if secure_access_allow_port_forwading is not None:
            self.secure_access_allow_port_forwading = secure_access_allow_port_forwading
        if secure_access_bastion_issuer is not None:
            self.secure_access_bastion_issuer = secure_access_bastion_issuer
        if secure_access_cluster_endpoint is not None:
            self.secure_access_cluster_endpoint = secure_access_cluster_endpoint
        if secure_access_dashboard_url is not None:
            self.secure_access_dashboard_url = secure_access_dashboard_url
        if secure_access_enable is not None:
            self.secure_access_enable = secure_access_enable
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
    def k8s_cluster_ca_cert(self):
        """Gets the k8s_cluster_ca_cert of this GatewayUpdateProducerNativeK8S.  # noqa: E501

        K8S cluster CA certificate  # noqa: E501

        :return: The k8s_cluster_ca_cert of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :rtype: str
        """
        return self._k8s_cluster_ca_cert

    @k8s_cluster_ca_cert.setter
    def k8s_cluster_ca_cert(self, k8s_cluster_ca_cert):
        """Sets the k8s_cluster_ca_cert of this GatewayUpdateProducerNativeK8S.

        K8S cluster CA certificate  # noqa: E501

        :param k8s_cluster_ca_cert: The k8s_cluster_ca_cert of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :type: str
        """

        self._k8s_cluster_ca_cert = k8s_cluster_ca_cert

    @property
    def k8s_cluster_endpoint(self):
        """Gets the k8s_cluster_endpoint of this GatewayUpdateProducerNativeK8S.  # noqa: E501

        K8S cluster URL endpoint  # noqa: E501

        :return: The k8s_cluster_endpoint of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :rtype: str
        """
        return self._k8s_cluster_endpoint

    @k8s_cluster_endpoint.setter
    def k8s_cluster_endpoint(self, k8s_cluster_endpoint):
        """Sets the k8s_cluster_endpoint of this GatewayUpdateProducerNativeK8S.

        K8S cluster URL endpoint  # noqa: E501

        :param k8s_cluster_endpoint: The k8s_cluster_endpoint of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :type: str
        """

        self._k8s_cluster_endpoint = k8s_cluster_endpoint

    @property
    def k8s_cluster_token(self):
        """Gets the k8s_cluster_token of this GatewayUpdateProducerNativeK8S.  # noqa: E501

        K8S cluster Bearer token  # noqa: E501

        :return: The k8s_cluster_token of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :rtype: str
        """
        return self._k8s_cluster_token

    @k8s_cluster_token.setter
    def k8s_cluster_token(self, k8s_cluster_token):
        """Sets the k8s_cluster_token of this GatewayUpdateProducerNativeK8S.

        K8S cluster Bearer token  # noqa: E501

        :param k8s_cluster_token: The k8s_cluster_token of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :type: str
        """

        self._k8s_cluster_token = k8s_cluster_token

    @property
    def k8s_namespace(self):
        """Gets the k8s_namespace of this GatewayUpdateProducerNativeK8S.  # noqa: E501

        K8S namespace  # noqa: E501

        :return: The k8s_namespace of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :rtype: str
        """
        return self._k8s_namespace

    @k8s_namespace.setter
    def k8s_namespace(self, k8s_namespace):
        """Sets the k8s_namespace of this GatewayUpdateProducerNativeK8S.

        K8S namespace  # noqa: E501

        :param k8s_namespace: The k8s_namespace of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :type: str
        """

        self._k8s_namespace = k8s_namespace

    @property
    def k8s_service_account(self):
        """Gets the k8s_service_account of this GatewayUpdateProducerNativeK8S.  # noqa: E501

        K8S service account  # noqa: E501

        :return: The k8s_service_account of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :rtype: str
        """
        return self._k8s_service_account

    @k8s_service_account.setter
    def k8s_service_account(self, k8s_service_account):
        """Sets the k8s_service_account of this GatewayUpdateProducerNativeK8S.

        K8S service account  # noqa: E501

        :param k8s_service_account: The k8s_service_account of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :type: str
        """

        self._k8s_service_account = k8s_service_account

    @property
    def name(self):
        """Gets the name of this GatewayUpdateProducerNativeK8S.  # noqa: E501

        Producer name  # noqa: E501

        :return: The name of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GatewayUpdateProducerNativeK8S.

        Producer name  # noqa: E501

        :param name: The name of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def new_name(self):
        """Gets the new_name of this GatewayUpdateProducerNativeK8S.  # noqa: E501

        Producer name  # noqa: E501

        :return: The new_name of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this GatewayUpdateProducerNativeK8S.

        Producer name  # noqa: E501

        :param new_name: The new_name of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :type: str
        """

        self._new_name = new_name

    @property
    def producer_encryption_key_name(self):
        """Gets the producer_encryption_key_name of this GatewayUpdateProducerNativeK8S.  # noqa: E501

        Dynamic producer encryption key  # noqa: E501

        :return: The producer_encryption_key_name of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :rtype: str
        """
        return self._producer_encryption_key_name

    @producer_encryption_key_name.setter
    def producer_encryption_key_name(self, producer_encryption_key_name):
        """Sets the producer_encryption_key_name of this GatewayUpdateProducerNativeK8S.

        Dynamic producer encryption key  # noqa: E501

        :param producer_encryption_key_name: The producer_encryption_key_name of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :type: str
        """

        self._producer_encryption_key_name = producer_encryption_key_name

    @property
    def secure_access_allow_port_forwading(self):
        """Gets the secure_access_allow_port_forwading of this GatewayUpdateProducerNativeK8S.  # noqa: E501


        :return: The secure_access_allow_port_forwading of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :rtype: bool
        """
        return self._secure_access_allow_port_forwading

    @secure_access_allow_port_forwading.setter
    def secure_access_allow_port_forwading(self, secure_access_allow_port_forwading):
        """Sets the secure_access_allow_port_forwading of this GatewayUpdateProducerNativeK8S.


        :param secure_access_allow_port_forwading: The secure_access_allow_port_forwading of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :type: bool
        """

        self._secure_access_allow_port_forwading = secure_access_allow_port_forwading

    @property
    def secure_access_bastion_issuer(self):
        """Gets the secure_access_bastion_issuer of this GatewayUpdateProducerNativeK8S.  # noqa: E501


        :return: The secure_access_bastion_issuer of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_bastion_issuer

    @secure_access_bastion_issuer.setter
    def secure_access_bastion_issuer(self, secure_access_bastion_issuer):
        """Sets the secure_access_bastion_issuer of this GatewayUpdateProducerNativeK8S.


        :param secure_access_bastion_issuer: The secure_access_bastion_issuer of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :type: str
        """

        self._secure_access_bastion_issuer = secure_access_bastion_issuer

    @property
    def secure_access_cluster_endpoint(self):
        """Gets the secure_access_cluster_endpoint of this GatewayUpdateProducerNativeK8S.  # noqa: E501


        :return: The secure_access_cluster_endpoint of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_cluster_endpoint

    @secure_access_cluster_endpoint.setter
    def secure_access_cluster_endpoint(self, secure_access_cluster_endpoint):
        """Sets the secure_access_cluster_endpoint of this GatewayUpdateProducerNativeK8S.


        :param secure_access_cluster_endpoint: The secure_access_cluster_endpoint of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :type: str
        """

        self._secure_access_cluster_endpoint = secure_access_cluster_endpoint

    @property
    def secure_access_dashboard_url(self):
        """Gets the secure_access_dashboard_url of this GatewayUpdateProducerNativeK8S.  # noqa: E501


        :return: The secure_access_dashboard_url of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_dashboard_url

    @secure_access_dashboard_url.setter
    def secure_access_dashboard_url(self, secure_access_dashboard_url):
        """Sets the secure_access_dashboard_url of this GatewayUpdateProducerNativeK8S.


        :param secure_access_dashboard_url: The secure_access_dashboard_url of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :type: str
        """

        self._secure_access_dashboard_url = secure_access_dashboard_url

    @property
    def secure_access_enable(self):
        """Gets the secure_access_enable of this GatewayUpdateProducerNativeK8S.  # noqa: E501


        :return: The secure_access_enable of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_enable

    @secure_access_enable.setter
    def secure_access_enable(self, secure_access_enable):
        """Sets the secure_access_enable of this GatewayUpdateProducerNativeK8S.


        :param secure_access_enable: The secure_access_enable of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :type: str
        """

        self._secure_access_enable = secure_access_enable

    @property
    def secure_access_web(self):
        """Gets the secure_access_web of this GatewayUpdateProducerNativeK8S.  # noqa: E501


        :return: The secure_access_web of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :rtype: bool
        """
        return self._secure_access_web

    @secure_access_web.setter
    def secure_access_web(self, secure_access_web):
        """Sets the secure_access_web of this GatewayUpdateProducerNativeK8S.


        :param secure_access_web: The secure_access_web of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :type: bool
        """

        self._secure_access_web = secure_access_web

    @property
    def secure_access_web_browsing(self):
        """Gets the secure_access_web_browsing of this GatewayUpdateProducerNativeK8S.  # noqa: E501


        :return: The secure_access_web_browsing of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :rtype: bool
        """
        return self._secure_access_web_browsing

    @secure_access_web_browsing.setter
    def secure_access_web_browsing(self, secure_access_web_browsing):
        """Sets the secure_access_web_browsing of this GatewayUpdateProducerNativeK8S.


        :param secure_access_web_browsing: The secure_access_web_browsing of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :type: bool
        """

        self._secure_access_web_browsing = secure_access_web_browsing

    @property
    def secure_access_web_proxy(self):
        """Gets the secure_access_web_proxy of this GatewayUpdateProducerNativeK8S.  # noqa: E501


        :return: The secure_access_web_proxy of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :rtype: bool
        """
        return self._secure_access_web_proxy

    @secure_access_web_proxy.setter
    def secure_access_web_proxy(self, secure_access_web_proxy):
        """Sets the secure_access_web_proxy of this GatewayUpdateProducerNativeK8S.


        :param secure_access_web_proxy: The secure_access_web_proxy of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :type: bool
        """

        self._secure_access_web_proxy = secure_access_web_proxy

    @property
    def tags(self):
        """Gets the tags of this GatewayUpdateProducerNativeK8S.  # noqa: E501

        List of the tags attached to this secret  # noqa: E501

        :return: The tags of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this GatewayUpdateProducerNativeK8S.

        List of the tags attached to this secret  # noqa: E501

        :param tags: The tags of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def target_name(self):
        """Gets the target_name of this GatewayUpdateProducerNativeK8S.  # noqa: E501

        Target name  # noqa: E501

        :return: The target_name of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """Sets the target_name of this GatewayUpdateProducerNativeK8S.

        Target name  # noqa: E501

        :param target_name: The target_name of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :type: str
        """

        self._target_name = target_name

    @property
    def token(self):
        """Gets the token of this GatewayUpdateProducerNativeK8S.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GatewayUpdateProducerNativeK8S.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this GatewayUpdateProducerNativeK8S.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GatewayUpdateProducerNativeK8S.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def user_ttl(self):
        """Gets the user_ttl of this GatewayUpdateProducerNativeK8S.  # noqa: E501

        User TTL  # noqa: E501

        :return: The user_ttl of this GatewayUpdateProducerNativeK8S.  # noqa: E501
        :rtype: str
        """
        return self._user_ttl

    @user_ttl.setter
    def user_ttl(self, user_ttl):
        """Sets the user_ttl of this GatewayUpdateProducerNativeK8S.

        User TTL  # noqa: E501

        :param user_ttl: The user_ttl of this GatewayUpdateProducerNativeK8S.  # noqa: E501
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
        if not isinstance(other, GatewayUpdateProducerNativeK8S):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayUpdateProducerNativeK8S):
            return True

        return self.to_dict() != other.to_dict()
