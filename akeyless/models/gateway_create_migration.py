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


class GatewayCreateMigration(object):
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
        'aws_key': 'str',
        'aws_key_id': 'str',
        'aws_region': 'str',
        'azure_client_id': 'str',
        'azure_kv_name': 'str',
        'azure_secret': 'str',
        'azure_tenant_id': 'str',
        'gcp_key': 'str',
        'hashi_json': 'str',
        'hashi_ns': 'list[str]',
        'hashi_token': 'str',
        'hashi_url': 'str',
        'k8s_ca_certificate': 'list[int]',
        'k8s_client_certificate': 'list[int]',
        'k8s_client_key': 'list[int]',
        'k8s_namespace': 'str',
        'k8s_password': 'str',
        'k8s_skip_system': 'bool',
        'k8s_token': 'str',
        'k8s_url': 'str',
        'k8s_username': 'str',
        'name': 'str',
        'protection_key': 'str',
        'target_location': 'str',
        'token': 'str',
        'type': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'aws_key': 'aws-key',
        'aws_key_id': 'aws-key-id',
        'aws_region': 'aws-region',
        'azure_client_id': 'azure-client-id',
        'azure_kv_name': 'azure-kv-name',
        'azure_secret': 'azure-secret',
        'azure_tenant_id': 'azure-tenant-id',
        'gcp_key': 'gcp-key',
        'hashi_json': 'hashi-json',
        'hashi_ns': 'hashi-ns',
        'hashi_token': 'hashi-token',
        'hashi_url': 'hashi-url',
        'k8s_ca_certificate': 'k8s-ca-certificate',
        'k8s_client_certificate': 'k8s-client-certificate',
        'k8s_client_key': 'k8s-client-key',
        'k8s_namespace': 'k8s-namespace',
        'k8s_password': 'k8s-password',
        'k8s_skip_system': 'k8s-skip-system',
        'k8s_token': 'k8s-token',
        'k8s_url': 'k8s-url',
        'k8s_username': 'k8s-username',
        'name': 'name',
        'protection_key': 'protection-key',
        'target_location': 'target-location',
        'token': 'token',
        'type': 'type',
        'uid_token': 'uid-token'
    }

    def __init__(self, aws_key=None, aws_key_id=None, aws_region=None, azure_client_id=None, azure_kv_name=None, azure_secret=None, azure_tenant_id=None, gcp_key=None, hashi_json=None, hashi_ns=None, hashi_token=None, hashi_url=None, k8s_ca_certificate=None, k8s_client_certificate=None, k8s_client_key=None, k8s_namespace=None, k8s_password=None, k8s_skip_system=None, k8s_token=None, k8s_url=None, k8s_username=None, name=None, protection_key=None, target_location=None, token=None, type=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """GatewayCreateMigration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._aws_key = None
        self._aws_key_id = None
        self._aws_region = None
        self._azure_client_id = None
        self._azure_kv_name = None
        self._azure_secret = None
        self._azure_tenant_id = None
        self._gcp_key = None
        self._hashi_json = None
        self._hashi_ns = None
        self._hashi_token = None
        self._hashi_url = None
        self._k8s_ca_certificate = None
        self._k8s_client_certificate = None
        self._k8s_client_key = None
        self._k8s_namespace = None
        self._k8s_password = None
        self._k8s_skip_system = None
        self._k8s_token = None
        self._k8s_url = None
        self._k8s_username = None
        self._name = None
        self._protection_key = None
        self._target_location = None
        self._token = None
        self._type = None
        self._uid_token = None
        self.discriminator = None

        if aws_key is not None:
            self.aws_key = aws_key
        if aws_key_id is not None:
            self.aws_key_id = aws_key_id
        if aws_region is not None:
            self.aws_region = aws_region
        if azure_client_id is not None:
            self.azure_client_id = azure_client_id
        if azure_kv_name is not None:
            self.azure_kv_name = azure_kv_name
        if azure_secret is not None:
            self.azure_secret = azure_secret
        if azure_tenant_id is not None:
            self.azure_tenant_id = azure_tenant_id
        if gcp_key is not None:
            self.gcp_key = gcp_key
        if hashi_json is not None:
            self.hashi_json = hashi_json
        if hashi_ns is not None:
            self.hashi_ns = hashi_ns
        if hashi_token is not None:
            self.hashi_token = hashi_token
        if hashi_url is not None:
            self.hashi_url = hashi_url
        if k8s_ca_certificate is not None:
            self.k8s_ca_certificate = k8s_ca_certificate
        if k8s_client_certificate is not None:
            self.k8s_client_certificate = k8s_client_certificate
        if k8s_client_key is not None:
            self.k8s_client_key = k8s_client_key
        if k8s_namespace is not None:
            self.k8s_namespace = k8s_namespace
        if k8s_password is not None:
            self.k8s_password = k8s_password
        if k8s_skip_system is not None:
            self.k8s_skip_system = k8s_skip_system
        if k8s_token is not None:
            self.k8s_token = k8s_token
        if k8s_url is not None:
            self.k8s_url = k8s_url
        if k8s_username is not None:
            self.k8s_username = k8s_username
        self.name = name
        if protection_key is not None:
            self.protection_key = protection_key
        if target_location is not None:
            self.target_location = target_location
        if token is not None:
            self.token = token
        if type is not None:
            self.type = type
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def aws_key(self):
        """Gets the aws_key of this GatewayCreateMigration.  # noqa: E501

        AWS Secret Access Key (relevant only for AWS migration)  # noqa: E501

        :return: The aws_key of this GatewayCreateMigration.  # noqa: E501
        :rtype: str
        """
        return self._aws_key

    @aws_key.setter
    def aws_key(self, aws_key):
        """Sets the aws_key of this GatewayCreateMigration.

        AWS Secret Access Key (relevant only for AWS migration)  # noqa: E501

        :param aws_key: The aws_key of this GatewayCreateMigration.  # noqa: E501
        :type: str
        """

        self._aws_key = aws_key

    @property
    def aws_key_id(self):
        """Gets the aws_key_id of this GatewayCreateMigration.  # noqa: E501

        AWS Access Key ID with sufficient permissions to get all secrets, e.g. 'arn:aws:secretsmanager:[Region]:[AccountId]:secret:[/path/to/secrets/*]' (relevant only for AWS migration)  # noqa: E501

        :return: The aws_key_id of this GatewayCreateMigration.  # noqa: E501
        :rtype: str
        """
        return self._aws_key_id

    @aws_key_id.setter
    def aws_key_id(self, aws_key_id):
        """Sets the aws_key_id of this GatewayCreateMigration.

        AWS Access Key ID with sufficient permissions to get all secrets, e.g. 'arn:aws:secretsmanager:[Region]:[AccountId]:secret:[/path/to/secrets/*]' (relevant only for AWS migration)  # noqa: E501

        :param aws_key_id: The aws_key_id of this GatewayCreateMigration.  # noqa: E501
        :type: str
        """

        self._aws_key_id = aws_key_id

    @property
    def aws_region(self):
        """Gets the aws_region of this GatewayCreateMigration.  # noqa: E501

        AWS region of the required Secrets Manager (relevant only for AWS migration)  # noqa: E501

        :return: The aws_region of this GatewayCreateMigration.  # noqa: E501
        :rtype: str
        """
        return self._aws_region

    @aws_region.setter
    def aws_region(self, aws_region):
        """Sets the aws_region of this GatewayCreateMigration.

        AWS region of the required Secrets Manager (relevant only for AWS migration)  # noqa: E501

        :param aws_region: The aws_region of this GatewayCreateMigration.  # noqa: E501
        :type: str
        """

        self._aws_region = aws_region

    @property
    def azure_client_id(self):
        """Gets the azure_client_id of this GatewayCreateMigration.  # noqa: E501

        Azure Key Vault Access client ID, should be Azure AD App with a service principal (relevant only for Azure Key Vault migration)  # noqa: E501

        :return: The azure_client_id of this GatewayCreateMigration.  # noqa: E501
        :rtype: str
        """
        return self._azure_client_id

    @azure_client_id.setter
    def azure_client_id(self, azure_client_id):
        """Sets the azure_client_id of this GatewayCreateMigration.

        Azure Key Vault Access client ID, should be Azure AD App with a service principal (relevant only for Azure Key Vault migration)  # noqa: E501

        :param azure_client_id: The azure_client_id of this GatewayCreateMigration.  # noqa: E501
        :type: str
        """

        self._azure_client_id = azure_client_id

    @property
    def azure_kv_name(self):
        """Gets the azure_kv_name of this GatewayCreateMigration.  # noqa: E501

        Azure Key Vault Name (relevant only for Azure Key Vault migration)  # noqa: E501

        :return: The azure_kv_name of this GatewayCreateMigration.  # noqa: E501
        :rtype: str
        """
        return self._azure_kv_name

    @azure_kv_name.setter
    def azure_kv_name(self, azure_kv_name):
        """Sets the azure_kv_name of this GatewayCreateMigration.

        Azure Key Vault Name (relevant only for Azure Key Vault migration)  # noqa: E501

        :param azure_kv_name: The azure_kv_name of this GatewayCreateMigration.  # noqa: E501
        :type: str
        """

        self._azure_kv_name = azure_kv_name

    @property
    def azure_secret(self):
        """Gets the azure_secret of this GatewayCreateMigration.  # noqa: E501

        Azure Key Vault secret (relevant only for Azure Key Vault migration)  # noqa: E501

        :return: The azure_secret of this GatewayCreateMigration.  # noqa: E501
        :rtype: str
        """
        return self._azure_secret

    @azure_secret.setter
    def azure_secret(self, azure_secret):
        """Sets the azure_secret of this GatewayCreateMigration.

        Azure Key Vault secret (relevant only for Azure Key Vault migration)  # noqa: E501

        :param azure_secret: The azure_secret of this GatewayCreateMigration.  # noqa: E501
        :type: str
        """

        self._azure_secret = azure_secret

    @property
    def azure_tenant_id(self):
        """Gets the azure_tenant_id of this GatewayCreateMigration.  # noqa: E501

        Azure Key Vault Access tenant ID (relevant only for Azure Key Vault migration)  # noqa: E501

        :return: The azure_tenant_id of this GatewayCreateMigration.  # noqa: E501
        :rtype: str
        """
        return self._azure_tenant_id

    @azure_tenant_id.setter
    def azure_tenant_id(self, azure_tenant_id):
        """Sets the azure_tenant_id of this GatewayCreateMigration.

        Azure Key Vault Access tenant ID (relevant only for Azure Key Vault migration)  # noqa: E501

        :param azure_tenant_id: The azure_tenant_id of this GatewayCreateMigration.  # noqa: E501
        :type: str
        """

        self._azure_tenant_id = azure_tenant_id

    @property
    def gcp_key(self):
        """Gets the gcp_key of this GatewayCreateMigration.  # noqa: E501

        Base64-encoded GCP Service Account private key text with sufficient permissions to Secrets Manager, Minimum required permission is Secret Manager Secret Accessor, e.g. 'roles/secretmanager.secretAccessor' (relevant only for GCP migration)  # noqa: E501

        :return: The gcp_key of this GatewayCreateMigration.  # noqa: E501
        :rtype: str
        """
        return self._gcp_key

    @gcp_key.setter
    def gcp_key(self, gcp_key):
        """Sets the gcp_key of this GatewayCreateMigration.

        Base64-encoded GCP Service Account private key text with sufficient permissions to Secrets Manager, Minimum required permission is Secret Manager Secret Accessor, e.g. 'roles/secretmanager.secretAccessor' (relevant only for GCP migration)  # noqa: E501

        :param gcp_key: The gcp_key of this GatewayCreateMigration.  # noqa: E501
        :type: str
        """

        self._gcp_key = gcp_key

    @property
    def hashi_json(self):
        """Gets the hashi_json of this GatewayCreateMigration.  # noqa: E501

        Import secret key as json value or independent secrets (relevant only for HasiCorp Vault migration)  # noqa: E501

        :return: The hashi_json of this GatewayCreateMigration.  # noqa: E501
        :rtype: str
        """
        return self._hashi_json

    @hashi_json.setter
    def hashi_json(self, hashi_json):
        """Sets the hashi_json of this GatewayCreateMigration.

        Import secret key as json value or independent secrets (relevant only for HasiCorp Vault migration)  # noqa: E501

        :param hashi_json: The hashi_json of this GatewayCreateMigration.  # noqa: E501
        :type: str
        """

        self._hashi_json = hashi_json

    @property
    def hashi_ns(self):
        """Gets the hashi_ns of this GatewayCreateMigration.  # noqa: E501

        HashiCorp Vault Namespaces is a comma-separated list of namespaces which need to be imported into Akeyless Vault. For every provided namespace, all its child namespaces are imported as well, e.g. nmsp/subnmsp1/subnmsp2,nmsp/anothernmsp. By default, import all namespaces (relevant only for HasiCorp Vault migration)  # noqa: E501

        :return: The hashi_ns of this GatewayCreateMigration.  # noqa: E501
        :rtype: list[str]
        """
        return self._hashi_ns

    @hashi_ns.setter
    def hashi_ns(self, hashi_ns):
        """Sets the hashi_ns of this GatewayCreateMigration.

        HashiCorp Vault Namespaces is a comma-separated list of namespaces which need to be imported into Akeyless Vault. For every provided namespace, all its child namespaces are imported as well, e.g. nmsp/subnmsp1/subnmsp2,nmsp/anothernmsp. By default, import all namespaces (relevant only for HasiCorp Vault migration)  # noqa: E501

        :param hashi_ns: The hashi_ns of this GatewayCreateMigration.  # noqa: E501
        :type: list[str]
        """

        self._hashi_ns = hashi_ns

    @property
    def hashi_token(self):
        """Gets the hashi_token of this GatewayCreateMigration.  # noqa: E501

        HashiCorp Vault access token with sufficient permissions to preform list & read operations on secrets objects (relevant only for HasiCorp Vault migration)  # noqa: E501

        :return: The hashi_token of this GatewayCreateMigration.  # noqa: E501
        :rtype: str
        """
        return self._hashi_token

    @hashi_token.setter
    def hashi_token(self, hashi_token):
        """Sets the hashi_token of this GatewayCreateMigration.

        HashiCorp Vault access token with sufficient permissions to preform list & read operations on secrets objects (relevant only for HasiCorp Vault migration)  # noqa: E501

        :param hashi_token: The hashi_token of this GatewayCreateMigration.  # noqa: E501
        :type: str
        """

        self._hashi_token = hashi_token

    @property
    def hashi_url(self):
        """Gets the hashi_url of this GatewayCreateMigration.  # noqa: E501

        HashiCorp Vault API URL, e.g. https://vault-mgr01:8200 (relevant only for HasiCorp Vault migration)  # noqa: E501

        :return: The hashi_url of this GatewayCreateMigration.  # noqa: E501
        :rtype: str
        """
        return self._hashi_url

    @hashi_url.setter
    def hashi_url(self, hashi_url):
        """Sets the hashi_url of this GatewayCreateMigration.

        HashiCorp Vault API URL, e.g. https://vault-mgr01:8200 (relevant only for HasiCorp Vault migration)  # noqa: E501

        :param hashi_url: The hashi_url of this GatewayCreateMigration.  # noqa: E501
        :type: str
        """

        self._hashi_url = hashi_url

    @property
    def k8s_ca_certificate(self):
        """Gets the k8s_ca_certificate of this GatewayCreateMigration.  # noqa: E501

        For Certificate Authentication method K8s Cluster CA certificate (relevant only for K8s migration with Certificate Authentication method)  # noqa: E501

        :return: The k8s_ca_certificate of this GatewayCreateMigration.  # noqa: E501
        :rtype: list[int]
        """
        return self._k8s_ca_certificate

    @k8s_ca_certificate.setter
    def k8s_ca_certificate(self, k8s_ca_certificate):
        """Sets the k8s_ca_certificate of this GatewayCreateMigration.

        For Certificate Authentication method K8s Cluster CA certificate (relevant only for K8s migration with Certificate Authentication method)  # noqa: E501

        :param k8s_ca_certificate: The k8s_ca_certificate of this GatewayCreateMigration.  # noqa: E501
        :type: list[int]
        """

        self._k8s_ca_certificate = k8s_ca_certificate

    @property
    def k8s_client_certificate(self):
        """Gets the k8s_client_certificate of this GatewayCreateMigration.  # noqa: E501

        K8s Client certificate with sufficient permission to list and get secrets in the namespace(s) you selected (relevant only for K8s migration with Certificate Authentication method)  # noqa: E501

        :return: The k8s_client_certificate of this GatewayCreateMigration.  # noqa: E501
        :rtype: list[int]
        """
        return self._k8s_client_certificate

    @k8s_client_certificate.setter
    def k8s_client_certificate(self, k8s_client_certificate):
        """Sets the k8s_client_certificate of this GatewayCreateMigration.

        K8s Client certificate with sufficient permission to list and get secrets in the namespace(s) you selected (relevant only for K8s migration with Certificate Authentication method)  # noqa: E501

        :param k8s_client_certificate: The k8s_client_certificate of this GatewayCreateMigration.  # noqa: E501
        :type: list[int]
        """

        self._k8s_client_certificate = k8s_client_certificate

    @property
    def k8s_client_key(self):
        """Gets the k8s_client_key of this GatewayCreateMigration.  # noqa: E501

        K8s Client key (relevant only for K8s migration with Certificate Authentication method)  # noqa: E501

        :return: The k8s_client_key of this GatewayCreateMigration.  # noqa: E501
        :rtype: list[int]
        """
        return self._k8s_client_key

    @k8s_client_key.setter
    def k8s_client_key(self, k8s_client_key):
        """Sets the k8s_client_key of this GatewayCreateMigration.

        K8s Client key (relevant only for K8s migration with Certificate Authentication method)  # noqa: E501

        :param k8s_client_key: The k8s_client_key of this GatewayCreateMigration.  # noqa: E501
        :type: list[int]
        """

        self._k8s_client_key = k8s_client_key

    @property
    def k8s_namespace(self):
        """Gets the k8s_namespace of this GatewayCreateMigration.  # noqa: E501

        K8s Namespace, Use this field to import secrets from a particular namespace only. By default, the secrets are imported from all namespaces (relevant only for K8s migration)  # noqa: E501

        :return: The k8s_namespace of this GatewayCreateMigration.  # noqa: E501
        :rtype: str
        """
        return self._k8s_namespace

    @k8s_namespace.setter
    def k8s_namespace(self, k8s_namespace):
        """Sets the k8s_namespace of this GatewayCreateMigration.

        K8s Namespace, Use this field to import secrets from a particular namespace only. By default, the secrets are imported from all namespaces (relevant only for K8s migration)  # noqa: E501

        :param k8s_namespace: The k8s_namespace of this GatewayCreateMigration.  # noqa: E501
        :type: str
        """

        self._k8s_namespace = k8s_namespace

    @property
    def k8s_password(self):
        """Gets the k8s_password of this GatewayCreateMigration.  # noqa: E501

        K8s Client password (relevant only for K8s migration with Password Authentication method)  # noqa: E501

        :return: The k8s_password of this GatewayCreateMigration.  # noqa: E501
        :rtype: str
        """
        return self._k8s_password

    @k8s_password.setter
    def k8s_password(self, k8s_password):
        """Sets the k8s_password of this GatewayCreateMigration.

        K8s Client password (relevant only for K8s migration with Password Authentication method)  # noqa: E501

        :param k8s_password: The k8s_password of this GatewayCreateMigration.  # noqa: E501
        :type: str
        """

        self._k8s_password = k8s_password

    @property
    def k8s_skip_system(self):
        """Gets the k8s_skip_system of this GatewayCreateMigration.  # noqa: E501

        K8s Skip Control Plane Secrets, This option allows to avoid importing secrets from system namespaces (relevant only for K8s migration)  # noqa: E501

        :return: The k8s_skip_system of this GatewayCreateMigration.  # noqa: E501
        :rtype: bool
        """
        return self._k8s_skip_system

    @k8s_skip_system.setter
    def k8s_skip_system(self, k8s_skip_system):
        """Sets the k8s_skip_system of this GatewayCreateMigration.

        K8s Skip Control Plane Secrets, This option allows to avoid importing secrets from system namespaces (relevant only for K8s migration)  # noqa: E501

        :param k8s_skip_system: The k8s_skip_system of this GatewayCreateMigration.  # noqa: E501
        :type: bool
        """

        self._k8s_skip_system = k8s_skip_system

    @property
    def k8s_token(self):
        """Gets the k8s_token of this GatewayCreateMigration.  # noqa: E501

        For Token Authentication method K8s Bearer Token with sufficient permission to list and get secrets in the namespace(s) you selected (relevant only for K8s migration with Token Authentication method)  # noqa: E501

        :return: The k8s_token of this GatewayCreateMigration.  # noqa: E501
        :rtype: str
        """
        return self._k8s_token

    @k8s_token.setter
    def k8s_token(self, k8s_token):
        """Sets the k8s_token of this GatewayCreateMigration.

        For Token Authentication method K8s Bearer Token with sufficient permission to list and get secrets in the namespace(s) you selected (relevant only for K8s migration with Token Authentication method)  # noqa: E501

        :param k8s_token: The k8s_token of this GatewayCreateMigration.  # noqa: E501
        :type: str
        """

        self._k8s_token = k8s_token

    @property
    def k8s_url(self):
        """Gets the k8s_url of this GatewayCreateMigration.  # noqa: E501

        K8s API Server URL, e.g. https://k8s-api.mycompany.com:6443 (relevant only for K8s migration)  # noqa: E501

        :return: The k8s_url of this GatewayCreateMigration.  # noqa: E501
        :rtype: str
        """
        return self._k8s_url

    @k8s_url.setter
    def k8s_url(self, k8s_url):
        """Sets the k8s_url of this GatewayCreateMigration.

        K8s API Server URL, e.g. https://k8s-api.mycompany.com:6443 (relevant only for K8s migration)  # noqa: E501

        :param k8s_url: The k8s_url of this GatewayCreateMigration.  # noqa: E501
        :type: str
        """

        self._k8s_url = k8s_url

    @property
    def k8s_username(self):
        """Gets the k8s_username of this GatewayCreateMigration.  # noqa: E501

        For Password Authentication method K8s Client username with sufficient permission to list and get secrets in the namespace(s) you selected (relevant only for K8s migration with Password Authentication method)  # noqa: E501

        :return: The k8s_username of this GatewayCreateMigration.  # noqa: E501
        :rtype: str
        """
        return self._k8s_username

    @k8s_username.setter
    def k8s_username(self, k8s_username):
        """Sets the k8s_username of this GatewayCreateMigration.

        For Password Authentication method K8s Client username with sufficient permission to list and get secrets in the namespace(s) you selected (relevant only for K8s migration with Password Authentication method)  # noqa: E501

        :param k8s_username: The k8s_username of this GatewayCreateMigration.  # noqa: E501
        :type: str
        """

        self._k8s_username = k8s_username

    @property
    def name(self):
        """Gets the name of this GatewayCreateMigration.  # noqa: E501

        Migration name  # noqa: E501

        :return: The name of this GatewayCreateMigration.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GatewayCreateMigration.

        Migration name  # noqa: E501

        :param name: The name of this GatewayCreateMigration.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def protection_key(self):
        """Gets the protection_key of this GatewayCreateMigration.  # noqa: E501

        The name of the key that protects the classic key value (if empty, the account default key will be used)  # noqa: E501

        :return: The protection_key of this GatewayCreateMigration.  # noqa: E501
        :rtype: str
        """
        return self._protection_key

    @protection_key.setter
    def protection_key(self, protection_key):
        """Sets the protection_key of this GatewayCreateMigration.

        The name of the key that protects the classic key value (if empty, the account default key will be used)  # noqa: E501

        :param protection_key: The protection_key of this GatewayCreateMigration.  # noqa: E501
        :type: str
        """

        self._protection_key = protection_key

    @property
    def target_location(self):
        """Gets the target_location of this GatewayCreateMigration.  # noqa: E501

        Target location in Akeyless for imported secrets  # noqa: E501

        :return: The target_location of this GatewayCreateMigration.  # noqa: E501
        :rtype: str
        """
        return self._target_location

    @target_location.setter
    def target_location(self, target_location):
        """Sets the target_location of this GatewayCreateMigration.

        Target location in Akeyless for imported secrets  # noqa: E501

        :param target_location: The target_location of this GatewayCreateMigration.  # noqa: E501
        :type: str
        """

        self._target_location = target_location

    @property
    def token(self):
        """Gets the token of this GatewayCreateMigration.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GatewayCreateMigration.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GatewayCreateMigration.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GatewayCreateMigration.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def type(self):
        """Gets the type of this GatewayCreateMigration.  # noqa: E501

        Migration type (hashi/aws/gcp/k8s/azure_kv)  # noqa: E501

        :return: The type of this GatewayCreateMigration.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GatewayCreateMigration.

        Migration type (hashi/aws/gcp/k8s/azure_kv)  # noqa: E501

        :param type: The type of this GatewayCreateMigration.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def uid_token(self):
        """Gets the uid_token of this GatewayCreateMigration.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GatewayCreateMigration.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GatewayCreateMigration.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GatewayCreateMigration.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

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
        if not isinstance(other, GatewayCreateMigration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayCreateMigration):
            return True

        return self.to_dict() != other.to_dict()
