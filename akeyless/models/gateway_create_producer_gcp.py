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


class GatewayCreateProducerGcp(object):
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
        'gcp_cred_type': 'str',
        'gcp_key': 'str',
        'gcp_key_algo': 'str',
        'gcp_sa_email': 'str',
        'gcp_token_scopes': 'str',
        'json': 'bool',
        'name': 'str',
        'producer_encryption_key_name': 'str',
        'role_binding': 'str',
        'service_account_type': 'str',
        'tags': 'list[str]',
        'target_name': 'str',
        'token': 'str',
        'uid_token': 'str',
        'user_ttl': 'str'
    }

    attribute_map = {
        'delete_protection': 'delete_protection',
        'gcp_cred_type': 'gcp-cred-type',
        'gcp_key': 'gcp-key',
        'gcp_key_algo': 'gcp-key-algo',
        'gcp_sa_email': 'gcp-sa-email',
        'gcp_token_scopes': 'gcp-token-scopes',
        'json': 'json',
        'name': 'name',
        'producer_encryption_key_name': 'producer-encryption-key-name',
        'role_binding': 'role-binding',
        'service_account_type': 'service-account-type',
        'tags': 'tags',
        'target_name': 'target-name',
        'token': 'token',
        'uid_token': 'uid-token',
        'user_ttl': 'user-ttl'
    }

    def __init__(self, delete_protection=None, gcp_cred_type=None, gcp_key=None, gcp_key_algo=None, gcp_sa_email=None, gcp_token_scopes=None, json=False, name=None, producer_encryption_key_name=None, role_binding=None, service_account_type='fixed', tags=None, target_name=None, token=None, uid_token=None, user_ttl='60m', local_vars_configuration=None):  # noqa: E501
        """GatewayCreateProducerGcp - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._delete_protection = None
        self._gcp_cred_type = None
        self._gcp_key = None
        self._gcp_key_algo = None
        self._gcp_sa_email = None
        self._gcp_token_scopes = None
        self._json = None
        self._name = None
        self._producer_encryption_key_name = None
        self._role_binding = None
        self._service_account_type = None
        self._tags = None
        self._target_name = None
        self._token = None
        self._uid_token = None
        self._user_ttl = None
        self.discriminator = None

        if delete_protection is not None:
            self.delete_protection = delete_protection
        if gcp_cred_type is not None:
            self.gcp_cred_type = gcp_cred_type
        if gcp_key is not None:
            self.gcp_key = gcp_key
        if gcp_key_algo is not None:
            self.gcp_key_algo = gcp_key_algo
        if gcp_sa_email is not None:
            self.gcp_sa_email = gcp_sa_email
        if gcp_token_scopes is not None:
            self.gcp_token_scopes = gcp_token_scopes
        if json is not None:
            self.json = json
        self.name = name
        if producer_encryption_key_name is not None:
            self.producer_encryption_key_name = producer_encryption_key_name
        if role_binding is not None:
            self.role_binding = role_binding
        self.service_account_type = service_account_type
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
        """Gets the delete_protection of this GatewayCreateProducerGcp.  # noqa: E501

        Protection from accidental deletion of this item [true/false]  # noqa: E501

        :return: The delete_protection of this GatewayCreateProducerGcp.  # noqa: E501
        :rtype: str
        """
        return self._delete_protection

    @delete_protection.setter
    def delete_protection(self, delete_protection):
        """Sets the delete_protection of this GatewayCreateProducerGcp.

        Protection from accidental deletion of this item [true/false]  # noqa: E501

        :param delete_protection: The delete_protection of this GatewayCreateProducerGcp.  # noqa: E501
        :type: str
        """

        self._delete_protection = delete_protection

    @property
    def gcp_cred_type(self):
        """Gets the gcp_cred_type of this GatewayCreateProducerGcp.  # noqa: E501


        :return: The gcp_cred_type of this GatewayCreateProducerGcp.  # noqa: E501
        :rtype: str
        """
        return self._gcp_cred_type

    @gcp_cred_type.setter
    def gcp_cred_type(self, gcp_cred_type):
        """Sets the gcp_cred_type of this GatewayCreateProducerGcp.


        :param gcp_cred_type: The gcp_cred_type of this GatewayCreateProducerGcp.  # noqa: E501
        :type: str
        """

        self._gcp_cred_type = gcp_cred_type

    @property
    def gcp_key(self):
        """Gets the gcp_key of this GatewayCreateProducerGcp.  # noqa: E501

        Base64-encoded service account private key text  # noqa: E501

        :return: The gcp_key of this GatewayCreateProducerGcp.  # noqa: E501
        :rtype: str
        """
        return self._gcp_key

    @gcp_key.setter
    def gcp_key(self, gcp_key):
        """Sets the gcp_key of this GatewayCreateProducerGcp.

        Base64-encoded service account private key text  # noqa: E501

        :param gcp_key: The gcp_key of this GatewayCreateProducerGcp.  # noqa: E501
        :type: str
        """

        self._gcp_key = gcp_key

    @property
    def gcp_key_algo(self):
        """Gets the gcp_key_algo of this GatewayCreateProducerGcp.  # noqa: E501

        Service account key algorithm, e.g. KEY_ALG_RSA_1024  # noqa: E501

        :return: The gcp_key_algo of this GatewayCreateProducerGcp.  # noqa: E501
        :rtype: str
        """
        return self._gcp_key_algo

    @gcp_key_algo.setter
    def gcp_key_algo(self, gcp_key_algo):
        """Sets the gcp_key_algo of this GatewayCreateProducerGcp.

        Service account key algorithm, e.g. KEY_ALG_RSA_1024  # noqa: E501

        :param gcp_key_algo: The gcp_key_algo of this GatewayCreateProducerGcp.  # noqa: E501
        :type: str
        """

        self._gcp_key_algo = gcp_key_algo

    @property
    def gcp_sa_email(self):
        """Gets the gcp_sa_email of this GatewayCreateProducerGcp.  # noqa: E501

        The email of the fixed service acocunt to generate keys or tokens for. (revelant for service-account-type=fixed)  # noqa: E501

        :return: The gcp_sa_email of this GatewayCreateProducerGcp.  # noqa: E501
        :rtype: str
        """
        return self._gcp_sa_email

    @gcp_sa_email.setter
    def gcp_sa_email(self, gcp_sa_email):
        """Sets the gcp_sa_email of this GatewayCreateProducerGcp.

        The email of the fixed service acocunt to generate keys or tokens for. (revelant for service-account-type=fixed)  # noqa: E501

        :param gcp_sa_email: The gcp_sa_email of this GatewayCreateProducerGcp.  # noqa: E501
        :type: str
        """

        self._gcp_sa_email = gcp_sa_email

    @property
    def gcp_token_scopes(self):
        """Gets the gcp_token_scopes of this GatewayCreateProducerGcp.  # noqa: E501

        Access token scopes list, e.g. scope1,scope2  # noqa: E501

        :return: The gcp_token_scopes of this GatewayCreateProducerGcp.  # noqa: E501
        :rtype: str
        """
        return self._gcp_token_scopes

    @gcp_token_scopes.setter
    def gcp_token_scopes(self, gcp_token_scopes):
        """Sets the gcp_token_scopes of this GatewayCreateProducerGcp.

        Access token scopes list, e.g. scope1,scope2  # noqa: E501

        :param gcp_token_scopes: The gcp_token_scopes of this GatewayCreateProducerGcp.  # noqa: E501
        :type: str
        """

        self._gcp_token_scopes = gcp_token_scopes

    @property
    def json(self):
        """Gets the json of this GatewayCreateProducerGcp.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this GatewayCreateProducerGcp.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this GatewayCreateProducerGcp.

        Set output format to JSON  # noqa: E501

        :param json: The json of this GatewayCreateProducerGcp.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def name(self):
        """Gets the name of this GatewayCreateProducerGcp.  # noqa: E501

        Dynamic secret name  # noqa: E501

        :return: The name of this GatewayCreateProducerGcp.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GatewayCreateProducerGcp.

        Dynamic secret name  # noqa: E501

        :param name: The name of this GatewayCreateProducerGcp.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def producer_encryption_key_name(self):
        """Gets the producer_encryption_key_name of this GatewayCreateProducerGcp.  # noqa: E501

        Dynamic producer encryption key  # noqa: E501

        :return: The producer_encryption_key_name of this GatewayCreateProducerGcp.  # noqa: E501
        :rtype: str
        """
        return self._producer_encryption_key_name

    @producer_encryption_key_name.setter
    def producer_encryption_key_name(self, producer_encryption_key_name):
        """Sets the producer_encryption_key_name of this GatewayCreateProducerGcp.

        Dynamic producer encryption key  # noqa: E501

        :param producer_encryption_key_name: The producer_encryption_key_name of this GatewayCreateProducerGcp.  # noqa: E501
        :type: str
        """

        self._producer_encryption_key_name = producer_encryption_key_name

    @property
    def role_binding(self):
        """Gets the role_binding of this GatewayCreateProducerGcp.  # noqa: E501

        Role binding definitions in json format  # noqa: E501

        :return: The role_binding of this GatewayCreateProducerGcp.  # noqa: E501
        :rtype: str
        """
        return self._role_binding

    @role_binding.setter
    def role_binding(self, role_binding):
        """Sets the role_binding of this GatewayCreateProducerGcp.

        Role binding definitions in json format  # noqa: E501

        :param role_binding: The role_binding of this GatewayCreateProducerGcp.  # noqa: E501
        :type: str
        """

        self._role_binding = role_binding

    @property
    def service_account_type(self):
        """Gets the service_account_type of this GatewayCreateProducerGcp.  # noqa: E501

        The type of the gcp dynamic secret. Options[fixed, dynamic]  # noqa: E501

        :return: The service_account_type of this GatewayCreateProducerGcp.  # noqa: E501
        :rtype: str
        """
        return self._service_account_type

    @service_account_type.setter
    def service_account_type(self, service_account_type):
        """Sets the service_account_type of this GatewayCreateProducerGcp.

        The type of the gcp dynamic secret. Options[fixed, dynamic]  # noqa: E501

        :param service_account_type: The service_account_type of this GatewayCreateProducerGcp.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and service_account_type is None:  # noqa: E501
            raise ValueError("Invalid value for `service_account_type`, must not be `None`")  # noqa: E501

        self._service_account_type = service_account_type

    @property
    def tags(self):
        """Gets the tags of this GatewayCreateProducerGcp.  # noqa: E501

        Add tags attached to this object  # noqa: E501

        :return: The tags of this GatewayCreateProducerGcp.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this GatewayCreateProducerGcp.

        Add tags attached to this object  # noqa: E501

        :param tags: The tags of this GatewayCreateProducerGcp.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def target_name(self):
        """Gets the target_name of this GatewayCreateProducerGcp.  # noqa: E501

        Target name  # noqa: E501

        :return: The target_name of this GatewayCreateProducerGcp.  # noqa: E501
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """Sets the target_name of this GatewayCreateProducerGcp.

        Target name  # noqa: E501

        :param target_name: The target_name of this GatewayCreateProducerGcp.  # noqa: E501
        :type: str
        """

        self._target_name = target_name

    @property
    def token(self):
        """Gets the token of this GatewayCreateProducerGcp.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GatewayCreateProducerGcp.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GatewayCreateProducerGcp.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GatewayCreateProducerGcp.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this GatewayCreateProducerGcp.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GatewayCreateProducerGcp.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GatewayCreateProducerGcp.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GatewayCreateProducerGcp.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def user_ttl(self):
        """Gets the user_ttl of this GatewayCreateProducerGcp.  # noqa: E501

        User TTL  # noqa: E501

        :return: The user_ttl of this GatewayCreateProducerGcp.  # noqa: E501
        :rtype: str
        """
        return self._user_ttl

    @user_ttl.setter
    def user_ttl(self, user_ttl):
        """Sets the user_ttl of this GatewayCreateProducerGcp.

        User TTL  # noqa: E501

        :param user_ttl: The user_ttl of this GatewayCreateProducerGcp.  # noqa: E501
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
        if not isinstance(other, GatewayCreateProducerGcp):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayCreateProducerGcp):
            return True

        return self.to_dict() != other.to_dict()
