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


class CreateNativeK8STarget(object):
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
        'description': 'str',
        'json': 'bool',
        'k8s_auth_type': 'str',
        'k8s_client_certificate': 'str',
        'k8s_client_key': 'str',
        'k8s_cluster_ca_cert': 'str',
        'k8s_cluster_endpoint': 'str',
        'k8s_cluster_token': 'str',
        'key': 'str',
        'max_versions': 'str',
        'name': 'str',
        'token': 'str',
        'uid_token': 'str',
        'use_gw_service_account': 'bool'
    }

    attribute_map = {
        'comment': 'comment',
        'description': 'description',
        'json': 'json',
        'k8s_auth_type': 'k8s-auth-type',
        'k8s_client_certificate': 'k8s-client-certificate',
        'k8s_client_key': 'k8s-client-key',
        'k8s_cluster_ca_cert': 'k8s-cluster-ca-cert',
        'k8s_cluster_endpoint': 'k8s-cluster-endpoint',
        'k8s_cluster_token': 'k8s-cluster-token',
        'key': 'key',
        'max_versions': 'max-versions',
        'name': 'name',
        'token': 'token',
        'uid_token': 'uid-token',
        'use_gw_service_account': 'use-gw-service-account'
    }

    def __init__(self, comment=None, description=None, json=False, k8s_auth_type='token', k8s_client_certificate=None, k8s_client_key=None, k8s_cluster_ca_cert='dummy_val', k8s_cluster_endpoint='dummy_val', k8s_cluster_token='dummy_val', key=None, max_versions=None, name=None, token=None, uid_token=None, use_gw_service_account=None, local_vars_configuration=None):  # noqa: E501
        """CreateNativeK8STarget - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._comment = None
        self._description = None
        self._json = None
        self._k8s_auth_type = None
        self._k8s_client_certificate = None
        self._k8s_client_key = None
        self._k8s_cluster_ca_cert = None
        self._k8s_cluster_endpoint = None
        self._k8s_cluster_token = None
        self._key = None
        self._max_versions = None
        self._name = None
        self._token = None
        self._uid_token = None
        self._use_gw_service_account = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        if description is not None:
            self.description = description
        if json is not None:
            self.json = json
        if k8s_auth_type is not None:
            self.k8s_auth_type = k8s_auth_type
        if k8s_client_certificate is not None:
            self.k8s_client_certificate = k8s_client_certificate
        if k8s_client_key is not None:
            self.k8s_client_key = k8s_client_key
        self.k8s_cluster_ca_cert = k8s_cluster_ca_cert
        self.k8s_cluster_endpoint = k8s_cluster_endpoint
        self.k8s_cluster_token = k8s_cluster_token
        if key is not None:
            self.key = key
        if max_versions is not None:
            self.max_versions = max_versions
        self.name = name
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if use_gw_service_account is not None:
            self.use_gw_service_account = use_gw_service_account

    @property
    def comment(self):
        """Gets the comment of this CreateNativeK8STarget.  # noqa: E501

        Deprecated - use description  # noqa: E501

        :return: The comment of this CreateNativeK8STarget.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this CreateNativeK8STarget.

        Deprecated - use description  # noqa: E501

        :param comment: The comment of this CreateNativeK8STarget.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def description(self):
        """Gets the description of this CreateNativeK8STarget.  # noqa: E501

        Description of the object  # noqa: E501

        :return: The description of this CreateNativeK8STarget.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateNativeK8STarget.

        Description of the object  # noqa: E501

        :param description: The description of this CreateNativeK8STarget.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def json(self):
        """Gets the json of this CreateNativeK8STarget.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this CreateNativeK8STarget.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this CreateNativeK8STarget.

        Set output format to JSON  # noqa: E501

        :param json: The json of this CreateNativeK8STarget.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def k8s_auth_type(self):
        """Gets the k8s_auth_type of this CreateNativeK8STarget.  # noqa: E501

        K8S auth type [token/certificate]  # noqa: E501

        :return: The k8s_auth_type of this CreateNativeK8STarget.  # noqa: E501
        :rtype: str
        """
        return self._k8s_auth_type

    @k8s_auth_type.setter
    def k8s_auth_type(self, k8s_auth_type):
        """Sets the k8s_auth_type of this CreateNativeK8STarget.

        K8S auth type [token/certificate]  # noqa: E501

        :param k8s_auth_type: The k8s_auth_type of this CreateNativeK8STarget.  # noqa: E501
        :type: str
        """

        self._k8s_auth_type = k8s_auth_type

    @property
    def k8s_client_certificate(self):
        """Gets the k8s_client_certificate of this CreateNativeK8STarget.  # noqa: E501

        Content of the k8 client certificate (PEM format) in a Base64 format  # noqa: E501

        :return: The k8s_client_certificate of this CreateNativeK8STarget.  # noqa: E501
        :rtype: str
        """
        return self._k8s_client_certificate

    @k8s_client_certificate.setter
    def k8s_client_certificate(self, k8s_client_certificate):
        """Sets the k8s_client_certificate of this CreateNativeK8STarget.

        Content of the k8 client certificate (PEM format) in a Base64 format  # noqa: E501

        :param k8s_client_certificate: The k8s_client_certificate of this CreateNativeK8STarget.  # noqa: E501
        :type: str
        """

        self._k8s_client_certificate = k8s_client_certificate

    @property
    def k8s_client_key(self):
        """Gets the k8s_client_key of this CreateNativeK8STarget.  # noqa: E501

        Content of the k8 client private key (PEM format) in a Base64 format  # noqa: E501

        :return: The k8s_client_key of this CreateNativeK8STarget.  # noqa: E501
        :rtype: str
        """
        return self._k8s_client_key

    @k8s_client_key.setter
    def k8s_client_key(self, k8s_client_key):
        """Sets the k8s_client_key of this CreateNativeK8STarget.

        Content of the k8 client private key (PEM format) in a Base64 format  # noqa: E501

        :param k8s_client_key: The k8s_client_key of this CreateNativeK8STarget.  # noqa: E501
        :type: str
        """

        self._k8s_client_key = k8s_client_key

    @property
    def k8s_cluster_ca_cert(self):
        """Gets the k8s_cluster_ca_cert of this CreateNativeK8STarget.  # noqa: E501

        K8S cluster CA certificate  # noqa: E501

        :return: The k8s_cluster_ca_cert of this CreateNativeK8STarget.  # noqa: E501
        :rtype: str
        """
        return self._k8s_cluster_ca_cert

    @k8s_cluster_ca_cert.setter
    def k8s_cluster_ca_cert(self, k8s_cluster_ca_cert):
        """Sets the k8s_cluster_ca_cert of this CreateNativeK8STarget.

        K8S cluster CA certificate  # noqa: E501

        :param k8s_cluster_ca_cert: The k8s_cluster_ca_cert of this CreateNativeK8STarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and k8s_cluster_ca_cert is None:  # noqa: E501
            raise ValueError("Invalid value for `k8s_cluster_ca_cert`, must not be `None`")  # noqa: E501

        self._k8s_cluster_ca_cert = k8s_cluster_ca_cert

    @property
    def k8s_cluster_endpoint(self):
        """Gets the k8s_cluster_endpoint of this CreateNativeK8STarget.  # noqa: E501

        K8S cluster URL endpoint  # noqa: E501

        :return: The k8s_cluster_endpoint of this CreateNativeK8STarget.  # noqa: E501
        :rtype: str
        """
        return self._k8s_cluster_endpoint

    @k8s_cluster_endpoint.setter
    def k8s_cluster_endpoint(self, k8s_cluster_endpoint):
        """Sets the k8s_cluster_endpoint of this CreateNativeK8STarget.

        K8S cluster URL endpoint  # noqa: E501

        :param k8s_cluster_endpoint: The k8s_cluster_endpoint of this CreateNativeK8STarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and k8s_cluster_endpoint is None:  # noqa: E501
            raise ValueError("Invalid value for `k8s_cluster_endpoint`, must not be `None`")  # noqa: E501

        self._k8s_cluster_endpoint = k8s_cluster_endpoint

    @property
    def k8s_cluster_token(self):
        """Gets the k8s_cluster_token of this CreateNativeK8STarget.  # noqa: E501

        K8S cluster Bearer token  # noqa: E501

        :return: The k8s_cluster_token of this CreateNativeK8STarget.  # noqa: E501
        :rtype: str
        """
        return self._k8s_cluster_token

    @k8s_cluster_token.setter
    def k8s_cluster_token(self, k8s_cluster_token):
        """Sets the k8s_cluster_token of this CreateNativeK8STarget.

        K8S cluster Bearer token  # noqa: E501

        :param k8s_cluster_token: The k8s_cluster_token of this CreateNativeK8STarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and k8s_cluster_token is None:  # noqa: E501
            raise ValueError("Invalid value for `k8s_cluster_token`, must not be `None`")  # noqa: E501

        self._k8s_cluster_token = k8s_cluster_token

    @property
    def key(self):
        """Gets the key of this CreateNativeK8STarget.  # noqa: E501

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :return: The key of this CreateNativeK8STarget.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CreateNativeK8STarget.

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :param key: The key of this CreateNativeK8STarget.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def max_versions(self):
        """Gets the max_versions of this CreateNativeK8STarget.  # noqa: E501

        Set the maximum number of versions, limited by the account settings defaults.  # noqa: E501

        :return: The max_versions of this CreateNativeK8STarget.  # noqa: E501
        :rtype: str
        """
        return self._max_versions

    @max_versions.setter
    def max_versions(self, max_versions):
        """Sets the max_versions of this CreateNativeK8STarget.

        Set the maximum number of versions, limited by the account settings defaults.  # noqa: E501

        :param max_versions: The max_versions of this CreateNativeK8STarget.  # noqa: E501
        :type: str
        """

        self._max_versions = max_versions

    @property
    def name(self):
        """Gets the name of this CreateNativeK8STarget.  # noqa: E501

        Target name  # noqa: E501

        :return: The name of this CreateNativeK8STarget.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateNativeK8STarget.

        Target name  # noqa: E501

        :param name: The name of this CreateNativeK8STarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def token(self):
        """Gets the token of this CreateNativeK8STarget.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this CreateNativeK8STarget.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this CreateNativeK8STarget.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this CreateNativeK8STarget.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this CreateNativeK8STarget.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this CreateNativeK8STarget.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this CreateNativeK8STarget.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this CreateNativeK8STarget.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def use_gw_service_account(self):
        """Gets the use_gw_service_account of this CreateNativeK8STarget.  # noqa: E501

        Use the GW's service account  # noqa: E501

        :return: The use_gw_service_account of this CreateNativeK8STarget.  # noqa: E501
        :rtype: bool
        """
        return self._use_gw_service_account

    @use_gw_service_account.setter
    def use_gw_service_account(self, use_gw_service_account):
        """Sets the use_gw_service_account of this CreateNativeK8STarget.

        Use the GW's service account  # noqa: E501

        :param use_gw_service_account: The use_gw_service_account of this CreateNativeK8STarget.  # noqa: E501
        :type: bool
        """

        self._use_gw_service_account = use_gw_service_account

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
        if not isinstance(other, CreateNativeK8STarget):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateNativeK8STarget):
            return True

        return self.to_dict() != other.to_dict()
