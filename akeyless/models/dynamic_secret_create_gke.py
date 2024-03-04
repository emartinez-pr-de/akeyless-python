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


class DynamicSecretCreateGke(object):
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
        'delete_protection': 'str',
        'description': 'str',
        'gke_account_key': 'str',
        'gke_cluster_cert': 'str',
        'gke_cluster_endpoint': 'str',
        'gke_cluster_name': 'str',
        'gke_service_account_email': 'str',
        'json': 'bool',
        'name': 'str',
        'producer_encryption_key_name': 'str',
        'secure_access_allow_port_forwading': 'bool',
        'secure_access_bastion_issuer': 'str',
        'secure_access_cluster_endpoint': 'str',
        'secure_access_enable': 'str',
        'secure_access_web': 'bool',
        'tags': 'list[str]',
        'target_name': 'str',
        'token': 'str',
        'uid_token': 'str',
        'user_ttl': 'str'
    }

    attribute_map = {
        'delete_protection': 'delete_protection',
        'description': 'description',
        'gke_account_key': 'gke-account-key',
        'gke_cluster_cert': 'gke-cluster-cert',
        'gke_cluster_endpoint': 'gke-cluster-endpoint',
        'gke_cluster_name': 'gke-cluster-name',
        'gke_service_account_email': 'gke-service-account-email',
        'json': 'json',
        'name': 'name',
        'producer_encryption_key_name': 'producer-encryption-key-name',
        'secure_access_allow_port_forwading': 'secure-access-allow-port-forwading',
        'secure_access_bastion_issuer': 'secure-access-bastion-issuer',
        'secure_access_cluster_endpoint': 'secure-access-cluster-endpoint',
        'secure_access_enable': 'secure-access-enable',
        'secure_access_web': 'secure-access-web',
        'tags': 'tags',
        'target_name': 'target-name',
        'token': 'token',
        'uid_token': 'uid-token',
        'user_ttl': 'user-ttl'
    }

    def __init__(self, delete_protection=None, description=None, gke_account_key=None, gke_cluster_cert=None, gke_cluster_endpoint=None, gke_cluster_name=None, gke_service_account_email=None, json=False, name=None, producer_encryption_key_name=None, secure_access_allow_port_forwading=None, secure_access_bastion_issuer=None, secure_access_cluster_endpoint=None, secure_access_enable=None, secure_access_web=False, tags=None, target_name=None, token=None, uid_token=None, user_ttl='60m', local_vars_configuration=None):  # noqa: E501
        """DynamicSecretCreateGke - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._delete_protection = None
        self._description = None
        self._gke_account_key = None
        self._gke_cluster_cert = None
        self._gke_cluster_endpoint = None
        self._gke_cluster_name = None
        self._gke_service_account_email = None
        self._json = None
        self._name = None
        self._producer_encryption_key_name = None
        self._secure_access_allow_port_forwading = None
        self._secure_access_bastion_issuer = None
        self._secure_access_cluster_endpoint = None
        self._secure_access_enable = None
        self._secure_access_web = None
        self._tags = None
        self._target_name = None
        self._token = None
        self._uid_token = None
        self._user_ttl = None
        self.discriminator = None

        if delete_protection is not None:
            self.delete_protection = delete_protection
        if description is not None:
            self.description = description
        if gke_account_key is not None:
            self.gke_account_key = gke_account_key
        if gke_cluster_cert is not None:
            self.gke_cluster_cert = gke_cluster_cert
        if gke_cluster_endpoint is not None:
            self.gke_cluster_endpoint = gke_cluster_endpoint
        if gke_cluster_name is not None:
            self.gke_cluster_name = gke_cluster_name
        if gke_service_account_email is not None:
            self.gke_service_account_email = gke_service_account_email
        if json is not None:
            self.json = json
        self.name = name
        if producer_encryption_key_name is not None:
            self.producer_encryption_key_name = producer_encryption_key_name
        if secure_access_allow_port_forwading is not None:
            self.secure_access_allow_port_forwading = secure_access_allow_port_forwading
        if secure_access_bastion_issuer is not None:
            self.secure_access_bastion_issuer = secure_access_bastion_issuer
        if secure_access_cluster_endpoint is not None:
            self.secure_access_cluster_endpoint = secure_access_cluster_endpoint
        if secure_access_enable is not None:
            self.secure_access_enable = secure_access_enable
        if secure_access_web is not None:
            self.secure_access_web = secure_access_web
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
    def delete_protection(self):
        """Gets the delete_protection of this DynamicSecretCreateGke.  # noqa: E501

        Protection from accidental deletion of this item [true/false]  # noqa: E501

        :return: The delete_protection of this DynamicSecretCreateGke.  # noqa: E501
        :rtype: str
        """
        return self._delete_protection

    @delete_protection.setter
    def delete_protection(self, delete_protection):
        """Sets the delete_protection of this DynamicSecretCreateGke.

        Protection from accidental deletion of this item [true/false]  # noqa: E501

        :param delete_protection: The delete_protection of this DynamicSecretCreateGke.  # noqa: E501
        :type: str
        """

        self._delete_protection = delete_protection

    @property
    def description(self):
        """Gets the description of this DynamicSecretCreateGke.  # noqa: E501

        Description of the object  # noqa: E501

        :return: The description of this DynamicSecretCreateGke.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DynamicSecretCreateGke.

        Description of the object  # noqa: E501

        :param description: The description of this DynamicSecretCreateGke.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def gke_account_key(self):
        """Gets the gke_account_key of this DynamicSecretCreateGke.  # noqa: E501

        GKE Service Account key file path  # noqa: E501

        :return: The gke_account_key of this DynamicSecretCreateGke.  # noqa: E501
        :rtype: str
        """
        return self._gke_account_key

    @gke_account_key.setter
    def gke_account_key(self, gke_account_key):
        """Sets the gke_account_key of this DynamicSecretCreateGke.

        GKE Service Account key file path  # noqa: E501

        :param gke_account_key: The gke_account_key of this DynamicSecretCreateGke.  # noqa: E501
        :type: str
        """

        self._gke_account_key = gke_account_key

    @property
    def gke_cluster_cert(self):
        """Gets the gke_cluster_cert of this DynamicSecretCreateGke.  # noqa: E501

        GKE cluster CA certificate  # noqa: E501

        :return: The gke_cluster_cert of this DynamicSecretCreateGke.  # noqa: E501
        :rtype: str
        """
        return self._gke_cluster_cert

    @gke_cluster_cert.setter
    def gke_cluster_cert(self, gke_cluster_cert):
        """Sets the gke_cluster_cert of this DynamicSecretCreateGke.

        GKE cluster CA certificate  # noqa: E501

        :param gke_cluster_cert: The gke_cluster_cert of this DynamicSecretCreateGke.  # noqa: E501
        :type: str
        """

        self._gke_cluster_cert = gke_cluster_cert

    @property
    def gke_cluster_endpoint(self):
        """Gets the gke_cluster_endpoint of this DynamicSecretCreateGke.  # noqa: E501

        GKE cluster URL endpoint  # noqa: E501

        :return: The gke_cluster_endpoint of this DynamicSecretCreateGke.  # noqa: E501
        :rtype: str
        """
        return self._gke_cluster_endpoint

    @gke_cluster_endpoint.setter
    def gke_cluster_endpoint(self, gke_cluster_endpoint):
        """Sets the gke_cluster_endpoint of this DynamicSecretCreateGke.

        GKE cluster URL endpoint  # noqa: E501

        :param gke_cluster_endpoint: The gke_cluster_endpoint of this DynamicSecretCreateGke.  # noqa: E501
        :type: str
        """

        self._gke_cluster_endpoint = gke_cluster_endpoint

    @property
    def gke_cluster_name(self):
        """Gets the gke_cluster_name of this DynamicSecretCreateGke.  # noqa: E501

        GKE cluster name  # noqa: E501

        :return: The gke_cluster_name of this DynamicSecretCreateGke.  # noqa: E501
        :rtype: str
        """
        return self._gke_cluster_name

    @gke_cluster_name.setter
    def gke_cluster_name(self, gke_cluster_name):
        """Sets the gke_cluster_name of this DynamicSecretCreateGke.

        GKE cluster name  # noqa: E501

        :param gke_cluster_name: The gke_cluster_name of this DynamicSecretCreateGke.  # noqa: E501
        :type: str
        """

        self._gke_cluster_name = gke_cluster_name

    @property
    def gke_service_account_email(self):
        """Gets the gke_service_account_email of this DynamicSecretCreateGke.  # noqa: E501

        GKE service account email  # noqa: E501

        :return: The gke_service_account_email of this DynamicSecretCreateGke.  # noqa: E501
        :rtype: str
        """
        return self._gke_service_account_email

    @gke_service_account_email.setter
    def gke_service_account_email(self, gke_service_account_email):
        """Sets the gke_service_account_email of this DynamicSecretCreateGke.

        GKE service account email  # noqa: E501

        :param gke_service_account_email: The gke_service_account_email of this DynamicSecretCreateGke.  # noqa: E501
        :type: str
        """

        self._gke_service_account_email = gke_service_account_email

    @property
    def json(self):
        """Gets the json of this DynamicSecretCreateGke.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this DynamicSecretCreateGke.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this DynamicSecretCreateGke.

        Set output format to JSON  # noqa: E501

        :param json: The json of this DynamicSecretCreateGke.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def name(self):
        """Gets the name of this DynamicSecretCreateGke.  # noqa: E501

        Dynamic secret name  # noqa: E501

        :return: The name of this DynamicSecretCreateGke.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DynamicSecretCreateGke.

        Dynamic secret name  # noqa: E501

        :param name: The name of this DynamicSecretCreateGke.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def producer_encryption_key_name(self):
        """Gets the producer_encryption_key_name of this DynamicSecretCreateGke.  # noqa: E501

        Dynamic producer encryption key  # noqa: E501

        :return: The producer_encryption_key_name of this DynamicSecretCreateGke.  # noqa: E501
        :rtype: str
        """
        return self._producer_encryption_key_name

    @producer_encryption_key_name.setter
    def producer_encryption_key_name(self, producer_encryption_key_name):
        """Sets the producer_encryption_key_name of this DynamicSecretCreateGke.

        Dynamic producer encryption key  # noqa: E501

        :param producer_encryption_key_name: The producer_encryption_key_name of this DynamicSecretCreateGke.  # noqa: E501
        :type: str
        """

        self._producer_encryption_key_name = producer_encryption_key_name

    @property
    def secure_access_allow_port_forwading(self):
        """Gets the secure_access_allow_port_forwading of this DynamicSecretCreateGke.  # noqa: E501

        Enable Port forwarding while using CLI access  # noqa: E501

        :return: The secure_access_allow_port_forwading of this DynamicSecretCreateGke.  # noqa: E501
        :rtype: bool
        """
        return self._secure_access_allow_port_forwading

    @secure_access_allow_port_forwading.setter
    def secure_access_allow_port_forwading(self, secure_access_allow_port_forwading):
        """Sets the secure_access_allow_port_forwading of this DynamicSecretCreateGke.

        Enable Port forwarding while using CLI access  # noqa: E501

        :param secure_access_allow_port_forwading: The secure_access_allow_port_forwading of this DynamicSecretCreateGke.  # noqa: E501
        :type: bool
        """

        self._secure_access_allow_port_forwading = secure_access_allow_port_forwading

    @property
    def secure_access_bastion_issuer(self):
        """Gets the secure_access_bastion_issuer of this DynamicSecretCreateGke.  # noqa: E501

        Path to the SSH Certificate Issuer for your Akeyless Bastion  # noqa: E501

        :return: The secure_access_bastion_issuer of this DynamicSecretCreateGke.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_bastion_issuer

    @secure_access_bastion_issuer.setter
    def secure_access_bastion_issuer(self, secure_access_bastion_issuer):
        """Sets the secure_access_bastion_issuer of this DynamicSecretCreateGke.

        Path to the SSH Certificate Issuer for your Akeyless Bastion  # noqa: E501

        :param secure_access_bastion_issuer: The secure_access_bastion_issuer of this DynamicSecretCreateGke.  # noqa: E501
        :type: str
        """

        self._secure_access_bastion_issuer = secure_access_bastion_issuer

    @property
    def secure_access_cluster_endpoint(self):
        """Gets the secure_access_cluster_endpoint of this DynamicSecretCreateGke.  # noqa: E501

        The K8s cluster endpoint URL  # noqa: E501

        :return: The secure_access_cluster_endpoint of this DynamicSecretCreateGke.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_cluster_endpoint

    @secure_access_cluster_endpoint.setter
    def secure_access_cluster_endpoint(self, secure_access_cluster_endpoint):
        """Sets the secure_access_cluster_endpoint of this DynamicSecretCreateGke.

        The K8s cluster endpoint URL  # noqa: E501

        :param secure_access_cluster_endpoint: The secure_access_cluster_endpoint of this DynamicSecretCreateGke.  # noqa: E501
        :type: str
        """

        self._secure_access_cluster_endpoint = secure_access_cluster_endpoint

    @property
    def secure_access_enable(self):
        """Gets the secure_access_enable of this DynamicSecretCreateGke.  # noqa: E501

        Enable/Disable secure remote access [true/false]  # noqa: E501

        :return: The secure_access_enable of this DynamicSecretCreateGke.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_enable

    @secure_access_enable.setter
    def secure_access_enable(self, secure_access_enable):
        """Sets the secure_access_enable of this DynamicSecretCreateGke.

        Enable/Disable secure remote access [true/false]  # noqa: E501

        :param secure_access_enable: The secure_access_enable of this DynamicSecretCreateGke.  # noqa: E501
        :type: str
        """

        self._secure_access_enable = secure_access_enable

    @property
    def secure_access_web(self):
        """Gets the secure_access_web of this DynamicSecretCreateGke.  # noqa: E501

        Enable Web Secure Remote Access  # noqa: E501

        :return: The secure_access_web of this DynamicSecretCreateGke.  # noqa: E501
        :rtype: bool
        """
        return self._secure_access_web

    @secure_access_web.setter
    def secure_access_web(self, secure_access_web):
        """Sets the secure_access_web of this DynamicSecretCreateGke.

        Enable Web Secure Remote Access  # noqa: E501

        :param secure_access_web: The secure_access_web of this DynamicSecretCreateGke.  # noqa: E501
        :type: bool
        """

        self._secure_access_web = secure_access_web

    @property
    def tags(self):
        """Gets the tags of this DynamicSecretCreateGke.  # noqa: E501

        Add tags attached to this object  # noqa: E501

        :return: The tags of this DynamicSecretCreateGke.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DynamicSecretCreateGke.

        Add tags attached to this object  # noqa: E501

        :param tags: The tags of this DynamicSecretCreateGke.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def target_name(self):
        """Gets the target_name of this DynamicSecretCreateGke.  # noqa: E501

        Target name  # noqa: E501

        :return: The target_name of this DynamicSecretCreateGke.  # noqa: E501
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """Sets the target_name of this DynamicSecretCreateGke.

        Target name  # noqa: E501

        :param target_name: The target_name of this DynamicSecretCreateGke.  # noqa: E501
        :type: str
        """

        self._target_name = target_name

    @property
    def token(self):
        """Gets the token of this DynamicSecretCreateGke.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this DynamicSecretCreateGke.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this DynamicSecretCreateGke.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this DynamicSecretCreateGke.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this DynamicSecretCreateGke.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this DynamicSecretCreateGke.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this DynamicSecretCreateGke.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this DynamicSecretCreateGke.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def user_ttl(self):
        """Gets the user_ttl of this DynamicSecretCreateGke.  # noqa: E501

        User TTL  # noqa: E501

        :return: The user_ttl of this DynamicSecretCreateGke.  # noqa: E501
        :rtype: str
        """
        return self._user_ttl

    @user_ttl.setter
    def user_ttl(self, user_ttl):
        """Sets the user_ttl of this DynamicSecretCreateGke.

        User TTL  # noqa: E501

        :param user_ttl: The user_ttl of this DynamicSecretCreateGke.  # noqa: E501
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
        if not isinstance(other, DynamicSecretCreateGke):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DynamicSecretCreateGke):
            return True

        return self.to_dict() != other.to_dict()
