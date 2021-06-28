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


class GatewayCreateProducerEks(object):
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
        'eks_access_key_id': 'str',
        'eks_assume_role': 'str',
        'eks_cluster_cert': 'str',
        'eks_cluster_endpoint': 'str',
        'eks_cluster_name': 'str',
        'eks_region': 'str',
        'eks_secret_access_key': 'str',
        'name': 'str',
        'password': 'str',
        'producer_encryption_key_name': 'str',
        'token': 'str',
        'uid_token': 'str',
        'user_ttl': 'str',
        'username': 'str'
    }

    attribute_map = {
        'eks_access_key_id': 'eks-access-key-id',
        'eks_assume_role': 'eks-assume-role',
        'eks_cluster_cert': 'eks-cluster-cert',
        'eks_cluster_endpoint': 'eks-cluster-endpoint',
        'eks_cluster_name': 'eks-cluster-name',
        'eks_region': 'eks-region',
        'eks_secret_access_key': 'eks-secret-access-key',
        'name': 'name',
        'password': 'password',
        'producer_encryption_key_name': 'producer-encryption-key-name',
        'token': 'token',
        'uid_token': 'uid-token',
        'user_ttl': 'user-ttl',
        'username': 'username'
    }

    def __init__(self, eks_access_key_id=None, eks_assume_role=None, eks_cluster_cert=None, eks_cluster_endpoint=None, eks_cluster_name=None, eks_region='us-east-2', eks_secret_access_key=None, name=None, password=None, producer_encryption_key_name=None, token=None, uid_token=None, user_ttl='60m', username=None, local_vars_configuration=None):  # noqa: E501
        """GatewayCreateProducerEks - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._eks_access_key_id = None
        self._eks_assume_role = None
        self._eks_cluster_cert = None
        self._eks_cluster_endpoint = None
        self._eks_cluster_name = None
        self._eks_region = None
        self._eks_secret_access_key = None
        self._name = None
        self._password = None
        self._producer_encryption_key_name = None
        self._token = None
        self._uid_token = None
        self._user_ttl = None
        self._username = None
        self.discriminator = None

        self.eks_access_key_id = eks_access_key_id
        if eks_assume_role is not None:
            self.eks_assume_role = eks_assume_role
        self.eks_cluster_cert = eks_cluster_cert
        self.eks_cluster_endpoint = eks_cluster_endpoint
        self.eks_cluster_name = eks_cluster_name
        if eks_region is not None:
            self.eks_region = eks_region
        self.eks_secret_access_key = eks_secret_access_key
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
    def eks_access_key_id(self):
        """Gets the eks_access_key_id of this GatewayCreateProducerEks.  # noqa: E501

        Access Key ID  # noqa: E501

        :return: The eks_access_key_id of this GatewayCreateProducerEks.  # noqa: E501
        :rtype: str
        """
        return self._eks_access_key_id

    @eks_access_key_id.setter
    def eks_access_key_id(self, eks_access_key_id):
        """Sets the eks_access_key_id of this GatewayCreateProducerEks.

        Access Key ID  # noqa: E501

        :param eks_access_key_id: The eks_access_key_id of this GatewayCreateProducerEks.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and eks_access_key_id is None:  # noqa: E501
            raise ValueError("Invalid value for `eks_access_key_id`, must not be `None`")  # noqa: E501

        self._eks_access_key_id = eks_access_key_id

    @property
    def eks_assume_role(self):
        """Gets the eks_assume_role of this GatewayCreateProducerEks.  # noqa: E501

        IAM assume role  # noqa: E501

        :return: The eks_assume_role of this GatewayCreateProducerEks.  # noqa: E501
        :rtype: str
        """
        return self._eks_assume_role

    @eks_assume_role.setter
    def eks_assume_role(self, eks_assume_role):
        """Sets the eks_assume_role of this GatewayCreateProducerEks.

        IAM assume role  # noqa: E501

        :param eks_assume_role: The eks_assume_role of this GatewayCreateProducerEks.  # noqa: E501
        :type: str
        """

        self._eks_assume_role = eks_assume_role

    @property
    def eks_cluster_cert(self):
        """Gets the eks_cluster_cert of this GatewayCreateProducerEks.  # noqa: E501

        EKS cluster CA certificate  # noqa: E501

        :return: The eks_cluster_cert of this GatewayCreateProducerEks.  # noqa: E501
        :rtype: str
        """
        return self._eks_cluster_cert

    @eks_cluster_cert.setter
    def eks_cluster_cert(self, eks_cluster_cert):
        """Sets the eks_cluster_cert of this GatewayCreateProducerEks.

        EKS cluster CA certificate  # noqa: E501

        :param eks_cluster_cert: The eks_cluster_cert of this GatewayCreateProducerEks.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and eks_cluster_cert is None:  # noqa: E501
            raise ValueError("Invalid value for `eks_cluster_cert`, must not be `None`")  # noqa: E501

        self._eks_cluster_cert = eks_cluster_cert

    @property
    def eks_cluster_endpoint(self):
        """Gets the eks_cluster_endpoint of this GatewayCreateProducerEks.  # noqa: E501

        EKS cluster URL endpoint  # noqa: E501

        :return: The eks_cluster_endpoint of this GatewayCreateProducerEks.  # noqa: E501
        :rtype: str
        """
        return self._eks_cluster_endpoint

    @eks_cluster_endpoint.setter
    def eks_cluster_endpoint(self, eks_cluster_endpoint):
        """Sets the eks_cluster_endpoint of this GatewayCreateProducerEks.

        EKS cluster URL endpoint  # noqa: E501

        :param eks_cluster_endpoint: The eks_cluster_endpoint of this GatewayCreateProducerEks.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and eks_cluster_endpoint is None:  # noqa: E501
            raise ValueError("Invalid value for `eks_cluster_endpoint`, must not be `None`")  # noqa: E501

        self._eks_cluster_endpoint = eks_cluster_endpoint

    @property
    def eks_cluster_name(self):
        """Gets the eks_cluster_name of this GatewayCreateProducerEks.  # noqa: E501

        EKS cluster name  # noqa: E501

        :return: The eks_cluster_name of this GatewayCreateProducerEks.  # noqa: E501
        :rtype: str
        """
        return self._eks_cluster_name

    @eks_cluster_name.setter
    def eks_cluster_name(self, eks_cluster_name):
        """Sets the eks_cluster_name of this GatewayCreateProducerEks.

        EKS cluster name  # noqa: E501

        :param eks_cluster_name: The eks_cluster_name of this GatewayCreateProducerEks.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and eks_cluster_name is None:  # noqa: E501
            raise ValueError("Invalid value for `eks_cluster_name`, must not be `None`")  # noqa: E501

        self._eks_cluster_name = eks_cluster_name

    @property
    def eks_region(self):
        """Gets the eks_region of this GatewayCreateProducerEks.  # noqa: E501

        Region  # noqa: E501

        :return: The eks_region of this GatewayCreateProducerEks.  # noqa: E501
        :rtype: str
        """
        return self._eks_region

    @eks_region.setter
    def eks_region(self, eks_region):
        """Sets the eks_region of this GatewayCreateProducerEks.

        Region  # noqa: E501

        :param eks_region: The eks_region of this GatewayCreateProducerEks.  # noqa: E501
        :type: str
        """

        self._eks_region = eks_region

    @property
    def eks_secret_access_key(self):
        """Gets the eks_secret_access_key of this GatewayCreateProducerEks.  # noqa: E501

        Secret Access Key  # noqa: E501

        :return: The eks_secret_access_key of this GatewayCreateProducerEks.  # noqa: E501
        :rtype: str
        """
        return self._eks_secret_access_key

    @eks_secret_access_key.setter
    def eks_secret_access_key(self, eks_secret_access_key):
        """Sets the eks_secret_access_key of this GatewayCreateProducerEks.

        Secret Access Key  # noqa: E501

        :param eks_secret_access_key: The eks_secret_access_key of this GatewayCreateProducerEks.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and eks_secret_access_key is None:  # noqa: E501
            raise ValueError("Invalid value for `eks_secret_access_key`, must not be `None`")  # noqa: E501

        self._eks_secret_access_key = eks_secret_access_key

    @property
    def name(self):
        """Gets the name of this GatewayCreateProducerEks.  # noqa: E501

        Producer name  # noqa: E501

        :return: The name of this GatewayCreateProducerEks.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GatewayCreateProducerEks.

        Producer name  # noqa: E501

        :param name: The name of this GatewayCreateProducerEks.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def password(self):
        """Gets the password of this GatewayCreateProducerEks.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The password of this GatewayCreateProducerEks.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this GatewayCreateProducerEks.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param password: The password of this GatewayCreateProducerEks.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def producer_encryption_key_name(self):
        """Gets the producer_encryption_key_name of this GatewayCreateProducerEks.  # noqa: E501

        Dynamic producer encryption key  # noqa: E501

        :return: The producer_encryption_key_name of this GatewayCreateProducerEks.  # noqa: E501
        :rtype: str
        """
        return self._producer_encryption_key_name

    @producer_encryption_key_name.setter
    def producer_encryption_key_name(self, producer_encryption_key_name):
        """Sets the producer_encryption_key_name of this GatewayCreateProducerEks.

        Dynamic producer encryption key  # noqa: E501

        :param producer_encryption_key_name: The producer_encryption_key_name of this GatewayCreateProducerEks.  # noqa: E501
        :type: str
        """

        self._producer_encryption_key_name = producer_encryption_key_name

    @property
    def token(self):
        """Gets the token of this GatewayCreateProducerEks.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GatewayCreateProducerEks.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GatewayCreateProducerEks.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GatewayCreateProducerEks.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this GatewayCreateProducerEks.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GatewayCreateProducerEks.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GatewayCreateProducerEks.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GatewayCreateProducerEks.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def user_ttl(self):
        """Gets the user_ttl of this GatewayCreateProducerEks.  # noqa: E501

        User TTL  # noqa: E501

        :return: The user_ttl of this GatewayCreateProducerEks.  # noqa: E501
        :rtype: str
        """
        return self._user_ttl

    @user_ttl.setter
    def user_ttl(self, user_ttl):
        """Sets the user_ttl of this GatewayCreateProducerEks.

        User TTL  # noqa: E501

        :param user_ttl: The user_ttl of this GatewayCreateProducerEks.  # noqa: E501
        :type: str
        """

        self._user_ttl = user_ttl

    @property
    def username(self):
        """Gets the username of this GatewayCreateProducerEks.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The username of this GatewayCreateProducerEks.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this GatewayCreateProducerEks.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param username: The username of this GatewayCreateProducerEks.  # noqa: E501
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
        if not isinstance(other, GatewayCreateProducerEks):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayCreateProducerEks):
            return True

        return self.to_dict() != other.to_dict()
