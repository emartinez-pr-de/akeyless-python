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


class GatewayPartialUpdateK8SAuthConfig(object):
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
        'use_default_identity_bool': 'bool',
        'access_id': 'str',
        'config_encryption_key_name': 'str',
        'disable_issuer_validation': 'str',
        'json': 'bool',
        'k8s_auth_type': 'str',
        'k8s_ca_cert': 'str',
        'k8s_client_certificate': 'str',
        'k8s_client_key': 'str',
        'k8s_host': 'str',
        'k8s_issuer': 'str',
        'name': 'str',
        'new_name': 'str',
        'rancher_api_key': 'str',
        'rancher_cluster_id': 'str',
        'signing_key': 'str',
        'token': 'str',
        'token_exp': 'int',
        'token_reviewer_jwt': 'str',
        'uid_token': 'str',
        'use_gw_service_account': 'str'
    }

    attribute_map = {
        'use_default_identity_bool': 'UseDefaultIdentityBool',
        'access_id': 'access-id',
        'config_encryption_key_name': 'config-encryption-key-name',
        'disable_issuer_validation': 'disable-issuer-validation',
        'json': 'json',
        'k8s_auth_type': 'k8s-auth-type',
        'k8s_ca_cert': 'k8s-ca-cert',
        'k8s_client_certificate': 'k8s-client-certificate',
        'k8s_client_key': 'k8s-client-key',
        'k8s_host': 'k8s-host',
        'k8s_issuer': 'k8s-issuer',
        'name': 'name',
        'new_name': 'new-name',
        'rancher_api_key': 'rancher-api-key',
        'rancher_cluster_id': 'rancher-cluster-id',
        'signing_key': 'signing-key',
        'token': 'token',
        'token_exp': 'token-exp',
        'token_reviewer_jwt': 'token-reviewer-jwt',
        'uid_token': 'uid-token',
        'use_gw_service_account': 'use-gw-service-account'
    }

    def __init__(self, use_default_identity_bool=None, access_id=None, config_encryption_key_name=None, disable_issuer_validation=None, json=False, k8s_auth_type='token', k8s_ca_cert=None, k8s_client_certificate=None, k8s_client_key=None, k8s_host=None, k8s_issuer=None, name=None, new_name=None, rancher_api_key=None, rancher_cluster_id=None, signing_key=None, token=None, token_exp=None, token_reviewer_jwt=None, uid_token=None, use_gw_service_account=None, local_vars_configuration=None):  # noqa: E501
        """GatewayPartialUpdateK8SAuthConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._use_default_identity_bool = None
        self._access_id = None
        self._config_encryption_key_name = None
        self._disable_issuer_validation = None
        self._json = None
        self._k8s_auth_type = None
        self._k8s_ca_cert = None
        self._k8s_client_certificate = None
        self._k8s_client_key = None
        self._k8s_host = None
        self._k8s_issuer = None
        self._name = None
        self._new_name = None
        self._rancher_api_key = None
        self._rancher_cluster_id = None
        self._signing_key = None
        self._token = None
        self._token_exp = None
        self._token_reviewer_jwt = None
        self._uid_token = None
        self._use_gw_service_account = None
        self.discriminator = None

        if use_default_identity_bool is not None:
            self.use_default_identity_bool = use_default_identity_bool
        if access_id is not None:
            self.access_id = access_id
        if config_encryption_key_name is not None:
            self.config_encryption_key_name = config_encryption_key_name
        if disable_issuer_validation is not None:
            self.disable_issuer_validation = disable_issuer_validation
        if json is not None:
            self.json = json
        if k8s_auth_type is not None:
            self.k8s_auth_type = k8s_auth_type
        if k8s_ca_cert is not None:
            self.k8s_ca_cert = k8s_ca_cert
        if k8s_client_certificate is not None:
            self.k8s_client_certificate = k8s_client_certificate
        if k8s_client_key is not None:
            self.k8s_client_key = k8s_client_key
        if k8s_host is not None:
            self.k8s_host = k8s_host
        if k8s_issuer is not None:
            self.k8s_issuer = k8s_issuer
        if name is not None:
            self.name = name
        if new_name is not None:
            self.new_name = new_name
        if rancher_api_key is not None:
            self.rancher_api_key = rancher_api_key
        if rancher_cluster_id is not None:
            self.rancher_cluster_id = rancher_cluster_id
        if signing_key is not None:
            self.signing_key = signing_key
        if token is not None:
            self.token = token
        if token_exp is not None:
            self.token_exp = token_exp
        if token_reviewer_jwt is not None:
            self.token_reviewer_jwt = token_reviewer_jwt
        if uid_token is not None:
            self.uid_token = uid_token
        if use_gw_service_account is not None:
            self.use_gw_service_account = use_gw_service_account

    @property
    def use_default_identity_bool(self):
        """Gets the use_default_identity_bool of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501


        :return: The use_default_identity_bool of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :rtype: bool
        """
        return self._use_default_identity_bool

    @use_default_identity_bool.setter
    def use_default_identity_bool(self, use_default_identity_bool):
        """Sets the use_default_identity_bool of this GatewayPartialUpdateK8SAuthConfig.


        :param use_default_identity_bool: The use_default_identity_bool of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :type: bool
        """

        self._use_default_identity_bool = use_default_identity_bool

    @property
    def access_id(self):
        """Gets the access_id of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501

        The access ID of the Kubernetes auth method  # noqa: E501

        :return: The access_id of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._access_id

    @access_id.setter
    def access_id(self, access_id):
        """Sets the access_id of this GatewayPartialUpdateK8SAuthConfig.

        The access ID of the Kubernetes auth method  # noqa: E501

        :param access_id: The access_id of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :type: str
        """

        self._access_id = access_id

    @property
    def config_encryption_key_name(self):
        """Gets the config_encryption_key_name of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501

        Config encryption key  # noqa: E501

        :return: The config_encryption_key_name of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._config_encryption_key_name

    @config_encryption_key_name.setter
    def config_encryption_key_name(self, config_encryption_key_name):
        """Sets the config_encryption_key_name of this GatewayPartialUpdateK8SAuthConfig.

        Config encryption key  # noqa: E501

        :param config_encryption_key_name: The config_encryption_key_name of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :type: str
        """

        self._config_encryption_key_name = config_encryption_key_name

    @property
    def disable_issuer_validation(self):
        """Gets the disable_issuer_validation of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501

        Disable issuer validation [true/false]  # noqa: E501

        :return: The disable_issuer_validation of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._disable_issuer_validation

    @disable_issuer_validation.setter
    def disable_issuer_validation(self, disable_issuer_validation):
        """Sets the disable_issuer_validation of this GatewayPartialUpdateK8SAuthConfig.

        Disable issuer validation [true/false]  # noqa: E501

        :param disable_issuer_validation: The disable_issuer_validation of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :type: str
        """

        self._disable_issuer_validation = disable_issuer_validation

    @property
    def json(self):
        """Gets the json of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this GatewayPartialUpdateK8SAuthConfig.

        Set output format to JSON  # noqa: E501

        :param json: The json of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def k8s_auth_type(self):
        """Gets the k8s_auth_type of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501

        K8S auth type [token/certificate]. (relevant for \"native_k8s\" only)  # noqa: E501

        :return: The k8s_auth_type of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._k8s_auth_type

    @k8s_auth_type.setter
    def k8s_auth_type(self, k8s_auth_type):
        """Sets the k8s_auth_type of this GatewayPartialUpdateK8SAuthConfig.

        K8S auth type [token/certificate]. (relevant for \"native_k8s\" only)  # noqa: E501

        :param k8s_auth_type: The k8s_auth_type of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :type: str
        """

        self._k8s_auth_type = k8s_auth_type

    @property
    def k8s_ca_cert(self):
        """Gets the k8s_ca_cert of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501

        The CA Certificate (base64 encoded) to use to call into the kubernetes API server  # noqa: E501

        :return: The k8s_ca_cert of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._k8s_ca_cert

    @k8s_ca_cert.setter
    def k8s_ca_cert(self, k8s_ca_cert):
        """Sets the k8s_ca_cert of this GatewayPartialUpdateK8SAuthConfig.

        The CA Certificate (base64 encoded) to use to call into the kubernetes API server  # noqa: E501

        :param k8s_ca_cert: The k8s_ca_cert of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :type: str
        """

        self._k8s_ca_cert = k8s_ca_cert

    @property
    def k8s_client_certificate(self):
        """Gets the k8s_client_certificate of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501

        Content of the k8 client certificate (PEM format) in a Base64 format (relevant for \"native_k8s\" only)  # noqa: E501

        :return: The k8s_client_certificate of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._k8s_client_certificate

    @k8s_client_certificate.setter
    def k8s_client_certificate(self, k8s_client_certificate):
        """Sets the k8s_client_certificate of this GatewayPartialUpdateK8SAuthConfig.

        Content of the k8 client certificate (PEM format) in a Base64 format (relevant for \"native_k8s\" only)  # noqa: E501

        :param k8s_client_certificate: The k8s_client_certificate of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :type: str
        """

        self._k8s_client_certificate = k8s_client_certificate

    @property
    def k8s_client_key(self):
        """Gets the k8s_client_key of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501

        Content of the k8 client private key (PEM format) in a Base64 format (relevant for \"native_k8s\" only)  # noqa: E501

        :return: The k8s_client_key of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._k8s_client_key

    @k8s_client_key.setter
    def k8s_client_key(self, k8s_client_key):
        """Sets the k8s_client_key of this GatewayPartialUpdateK8SAuthConfig.

        Content of the k8 client private key (PEM format) in a Base64 format (relevant for \"native_k8s\" only)  # noqa: E501

        :param k8s_client_key: The k8s_client_key of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :type: str
        """

        self._k8s_client_key = k8s_client_key

    @property
    def k8s_host(self):
        """Gets the k8s_host of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501

        The URL of the kubernetes API server  # noqa: E501

        :return: The k8s_host of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._k8s_host

    @k8s_host.setter
    def k8s_host(self, k8s_host):
        """Sets the k8s_host of this GatewayPartialUpdateK8SAuthConfig.

        The URL of the kubernetes API server  # noqa: E501

        :param k8s_host: The k8s_host of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :type: str
        """

        self._k8s_host = k8s_host

    @property
    def k8s_issuer(self):
        """Gets the k8s_issuer of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501

        The Kubernetes JWT issuer name. K8SIssuer is the claim that specifies who issued the Kubernetes token  # noqa: E501

        :return: The k8s_issuer of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._k8s_issuer

    @k8s_issuer.setter
    def k8s_issuer(self, k8s_issuer):
        """Sets the k8s_issuer of this GatewayPartialUpdateK8SAuthConfig.

        The Kubernetes JWT issuer name. K8SIssuer is the claim that specifies who issued the Kubernetes token  # noqa: E501

        :param k8s_issuer: The k8s_issuer of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :type: str
        """

        self._k8s_issuer = k8s_issuer

    @property
    def name(self):
        """Gets the name of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501

        K8S Auth config name  # noqa: E501

        :return: The name of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GatewayPartialUpdateK8SAuthConfig.

        K8S Auth config name  # noqa: E501

        :param name: The name of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def new_name(self):
        """Gets the new_name of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501

        K8S Auth config new name  # noqa: E501

        :return: The new_name of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this GatewayPartialUpdateK8SAuthConfig.

        K8S Auth config new name  # noqa: E501

        :param new_name: The new_name of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :type: str
        """

        self._new_name = new_name

    @property
    def rancher_api_key(self):
        """Gets the rancher_api_key of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501

        The api key used to access the TokenReview API to validate other JWTs (relevant for \"rancher\" only)  # noqa: E501

        :return: The rancher_api_key of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._rancher_api_key

    @rancher_api_key.setter
    def rancher_api_key(self, rancher_api_key):
        """Sets the rancher_api_key of this GatewayPartialUpdateK8SAuthConfig.

        The api key used to access the TokenReview API to validate other JWTs (relevant for \"rancher\" only)  # noqa: E501

        :param rancher_api_key: The rancher_api_key of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :type: str
        """

        self._rancher_api_key = rancher_api_key

    @property
    def rancher_cluster_id(self):
        """Gets the rancher_cluster_id of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501

        The cluster id as define in rancher (relevant for \"rancher\" only)  # noqa: E501

        :return: The rancher_cluster_id of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._rancher_cluster_id

    @rancher_cluster_id.setter
    def rancher_cluster_id(self, rancher_cluster_id):
        """Sets the rancher_cluster_id of this GatewayPartialUpdateK8SAuthConfig.

        The cluster id as define in rancher (relevant for \"rancher\" only)  # noqa: E501

        :param rancher_cluster_id: The rancher_cluster_id of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :type: str
        """

        self._rancher_cluster_id = rancher_cluster_id

    @property
    def signing_key(self):
        """Gets the signing_key of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501

        The private key (base64 encoded) associated with the public key defined in the Kubernetes auth  # noqa: E501

        :return: The signing_key of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._signing_key

    @signing_key.setter
    def signing_key(self, signing_key):
        """Sets the signing_key of this GatewayPartialUpdateK8SAuthConfig.

        The private key (base64 encoded) associated with the public key defined in the Kubernetes auth  # noqa: E501

        :param signing_key: The signing_key of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :type: str
        """

        self._signing_key = signing_key

    @property
    def token(self):
        """Gets the token of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GatewayPartialUpdateK8SAuthConfig.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def token_exp(self):
        """Gets the token_exp of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501

        Time in seconds of expiration of the Akeyless Kube Auth Method token  # noqa: E501

        :return: The token_exp of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :rtype: int
        """
        return self._token_exp

    @token_exp.setter
    def token_exp(self, token_exp):
        """Sets the token_exp of this GatewayPartialUpdateK8SAuthConfig.

        Time in seconds of expiration of the Akeyless Kube Auth Method token  # noqa: E501

        :param token_exp: The token_exp of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :type: int
        """

        self._token_exp = token_exp

    @property
    def token_reviewer_jwt(self):
        """Gets the token_reviewer_jwt of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501

        A Kubernetes service account JWT used to access the TokenReview API to validate other JWTs (relevant for \"native_k8s\" only). If not set, the JWT submitted in the authentication process will be used to access the Kubernetes TokenReview API.  # noqa: E501

        :return: The token_reviewer_jwt of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._token_reviewer_jwt

    @token_reviewer_jwt.setter
    def token_reviewer_jwt(self, token_reviewer_jwt):
        """Sets the token_reviewer_jwt of this GatewayPartialUpdateK8SAuthConfig.

        A Kubernetes service account JWT used to access the TokenReview API to validate other JWTs (relevant for \"native_k8s\" only). If not set, the JWT submitted in the authentication process will be used to access the Kubernetes TokenReview API.  # noqa: E501

        :param token_reviewer_jwt: The token_reviewer_jwt of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :type: str
        """

        self._token_reviewer_jwt = token_reviewer_jwt

    @property
    def uid_token(self):
        """Gets the uid_token of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GatewayPartialUpdateK8SAuthConfig.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def use_gw_service_account(self):
        """Gets the use_gw_service_account of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501

        Use the GW's service account  # noqa: E501

        :return: The use_gw_service_account of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._use_gw_service_account

    @use_gw_service_account.setter
    def use_gw_service_account(self, use_gw_service_account):
        """Sets the use_gw_service_account of this GatewayPartialUpdateK8SAuthConfig.

        Use the GW's service account  # noqa: E501

        :param use_gw_service_account: The use_gw_service_account of this GatewayPartialUpdateK8SAuthConfig.  # noqa: E501
        :type: str
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
        if not isinstance(other, GatewayPartialUpdateK8SAuthConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayPartialUpdateK8SAuthConfig):
            return True

        return self.to_dict() != other.to_dict()
