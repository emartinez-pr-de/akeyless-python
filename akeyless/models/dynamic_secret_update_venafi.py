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


class DynamicSecretUpdateVenafi(object):
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
        'admin_rotation_interval_days': 'int',
        'allow_subdomains': 'bool',
        'allowed_domains': 'list[str]',
        'auto_generated_folder': 'str',
        'delete_protection': 'str',
        'description': 'str',
        'enable_admin_rotation': 'bool',
        'json': 'bool',
        'name': 'str',
        'new_name': 'str',
        'producer_encryption_key_name': 'str',
        'root_first_in_chain': 'bool',
        'sign_using_akeyless_pki': 'bool',
        'signer_key_name': 'str',
        'store_private_key': 'bool',
        'tags': 'list[str]',
        'target_name': 'str',
        'token': 'str',
        'uid_token': 'str',
        'user_ttl': 'str',
        'venafi_access_token': 'str',
        'venafi_api_key': 'str',
        'venafi_baseurl': 'str',
        'venafi_client_id': 'str',
        'venafi_refresh_token': 'str',
        'venafi_use_tpp': 'bool',
        'venafi_zone': 'str'
    }

    attribute_map = {
        'admin_rotation_interval_days': 'admin-rotation-interval-days',
        'allow_subdomains': 'allow-subdomains',
        'allowed_domains': 'allowed-domains',
        'auto_generated_folder': 'auto-generated-folder',
        'delete_protection': 'delete_protection',
        'description': 'description',
        'enable_admin_rotation': 'enable-admin-rotation',
        'json': 'json',
        'name': 'name',
        'new_name': 'new-name',
        'producer_encryption_key_name': 'producer-encryption-key-name',
        'root_first_in_chain': 'root-first-in-chain',
        'sign_using_akeyless_pki': 'sign-using-akeyless-pki',
        'signer_key_name': 'signer-key-name',
        'store_private_key': 'store-private-key',
        'tags': 'tags',
        'target_name': 'target-name',
        'token': 'token',
        'uid_token': 'uid-token',
        'user_ttl': 'user-ttl',
        'venafi_access_token': 'venafi-access-token',
        'venafi_api_key': 'venafi-api-key',
        'venafi_baseurl': 'venafi-baseurl',
        'venafi_client_id': 'venafi-client-id',
        'venafi_refresh_token': 'venafi-refresh-token',
        'venafi_use_tpp': 'venafi-use-tpp',
        'venafi_zone': 'venafi-zone'
    }

    def __init__(self, admin_rotation_interval_days=0, allow_subdomains=None, allowed_domains=None, auto_generated_folder=None, delete_protection=None, description=None, enable_admin_rotation=False, json=False, name=None, new_name=None, producer_encryption_key_name=None, root_first_in_chain=None, sign_using_akeyless_pki=None, signer_key_name=None, store_private_key=None, tags=None, target_name=None, token=None, uid_token=None, user_ttl='2160h', venafi_access_token=None, venafi_api_key=None, venafi_baseurl=None, venafi_client_id='akeyless', venafi_refresh_token=None, venafi_use_tpp=None, venafi_zone=None, local_vars_configuration=None):  # noqa: E501
        """DynamicSecretUpdateVenafi - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._admin_rotation_interval_days = None
        self._allow_subdomains = None
        self._allowed_domains = None
        self._auto_generated_folder = None
        self._delete_protection = None
        self._description = None
        self._enable_admin_rotation = None
        self._json = None
        self._name = None
        self._new_name = None
        self._producer_encryption_key_name = None
        self._root_first_in_chain = None
        self._sign_using_akeyless_pki = None
        self._signer_key_name = None
        self._store_private_key = None
        self._tags = None
        self._target_name = None
        self._token = None
        self._uid_token = None
        self._user_ttl = None
        self._venafi_access_token = None
        self._venafi_api_key = None
        self._venafi_baseurl = None
        self._venafi_client_id = None
        self._venafi_refresh_token = None
        self._venafi_use_tpp = None
        self._venafi_zone = None
        self.discriminator = None

        if admin_rotation_interval_days is not None:
            self.admin_rotation_interval_days = admin_rotation_interval_days
        if allow_subdomains is not None:
            self.allow_subdomains = allow_subdomains
        if allowed_domains is not None:
            self.allowed_domains = allowed_domains
        if auto_generated_folder is not None:
            self.auto_generated_folder = auto_generated_folder
        if delete_protection is not None:
            self.delete_protection = delete_protection
        if description is not None:
            self.description = description
        if enable_admin_rotation is not None:
            self.enable_admin_rotation = enable_admin_rotation
        if json is not None:
            self.json = json
        self.name = name
        if new_name is not None:
            self.new_name = new_name
        if producer_encryption_key_name is not None:
            self.producer_encryption_key_name = producer_encryption_key_name
        if root_first_in_chain is not None:
            self.root_first_in_chain = root_first_in_chain
        if sign_using_akeyless_pki is not None:
            self.sign_using_akeyless_pki = sign_using_akeyless_pki
        if signer_key_name is not None:
            self.signer_key_name = signer_key_name
        if store_private_key is not None:
            self.store_private_key = store_private_key
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
        if venafi_access_token is not None:
            self.venafi_access_token = venafi_access_token
        if venafi_api_key is not None:
            self.venafi_api_key = venafi_api_key
        if venafi_baseurl is not None:
            self.venafi_baseurl = venafi_baseurl
        if venafi_client_id is not None:
            self.venafi_client_id = venafi_client_id
        if venafi_refresh_token is not None:
            self.venafi_refresh_token = venafi_refresh_token
        if venafi_use_tpp is not None:
            self.venafi_use_tpp = venafi_use_tpp
        if venafi_zone is not None:
            self.venafi_zone = venafi_zone

    @property
    def admin_rotation_interval_days(self):
        """Gets the admin_rotation_interval_days of this DynamicSecretUpdateVenafi.  # noqa: E501

        Admin credentials rotation interval (days)  # noqa: E501

        :return: The admin_rotation_interval_days of this DynamicSecretUpdateVenafi.  # noqa: E501
        :rtype: int
        """
        return self._admin_rotation_interval_days

    @admin_rotation_interval_days.setter
    def admin_rotation_interval_days(self, admin_rotation_interval_days):
        """Sets the admin_rotation_interval_days of this DynamicSecretUpdateVenafi.

        Admin credentials rotation interval (days)  # noqa: E501

        :param admin_rotation_interval_days: The admin_rotation_interval_days of this DynamicSecretUpdateVenafi.  # noqa: E501
        :type: int
        """

        self._admin_rotation_interval_days = admin_rotation_interval_days

    @property
    def allow_subdomains(self):
        """Gets the allow_subdomains of this DynamicSecretUpdateVenafi.  # noqa: E501

        Allow subdomains  # noqa: E501

        :return: The allow_subdomains of this DynamicSecretUpdateVenafi.  # noqa: E501
        :rtype: bool
        """
        return self._allow_subdomains

    @allow_subdomains.setter
    def allow_subdomains(self, allow_subdomains):
        """Sets the allow_subdomains of this DynamicSecretUpdateVenafi.

        Allow subdomains  # noqa: E501

        :param allow_subdomains: The allow_subdomains of this DynamicSecretUpdateVenafi.  # noqa: E501
        :type: bool
        """

        self._allow_subdomains = allow_subdomains

    @property
    def allowed_domains(self):
        """Gets the allowed_domains of this DynamicSecretUpdateVenafi.  # noqa: E501

        Allowed domains  # noqa: E501

        :return: The allowed_domains of this DynamicSecretUpdateVenafi.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_domains

    @allowed_domains.setter
    def allowed_domains(self, allowed_domains):
        """Sets the allowed_domains of this DynamicSecretUpdateVenafi.

        Allowed domains  # noqa: E501

        :param allowed_domains: The allowed_domains of this DynamicSecretUpdateVenafi.  # noqa: E501
        :type: list[str]
        """

        self._allowed_domains = allowed_domains

    @property
    def auto_generated_folder(self):
        """Gets the auto_generated_folder of this DynamicSecretUpdateVenafi.  # noqa: E501

        Auto generated folder  # noqa: E501

        :return: The auto_generated_folder of this DynamicSecretUpdateVenafi.  # noqa: E501
        :rtype: str
        """
        return self._auto_generated_folder

    @auto_generated_folder.setter
    def auto_generated_folder(self, auto_generated_folder):
        """Sets the auto_generated_folder of this DynamicSecretUpdateVenafi.

        Auto generated folder  # noqa: E501

        :param auto_generated_folder: The auto_generated_folder of this DynamicSecretUpdateVenafi.  # noqa: E501
        :type: str
        """

        self._auto_generated_folder = auto_generated_folder

    @property
    def delete_protection(self):
        """Gets the delete_protection of this DynamicSecretUpdateVenafi.  # noqa: E501

        Protection from accidental deletion of this item [true/false]  # noqa: E501

        :return: The delete_protection of this DynamicSecretUpdateVenafi.  # noqa: E501
        :rtype: str
        """
        return self._delete_protection

    @delete_protection.setter
    def delete_protection(self, delete_protection):
        """Sets the delete_protection of this DynamicSecretUpdateVenafi.

        Protection from accidental deletion of this item [true/false]  # noqa: E501

        :param delete_protection: The delete_protection of this DynamicSecretUpdateVenafi.  # noqa: E501
        :type: str
        """

        self._delete_protection = delete_protection

    @property
    def description(self):
        """Gets the description of this DynamicSecretUpdateVenafi.  # noqa: E501

        Description of the object  # noqa: E501

        :return: The description of this DynamicSecretUpdateVenafi.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DynamicSecretUpdateVenafi.

        Description of the object  # noqa: E501

        :param description: The description of this DynamicSecretUpdateVenafi.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enable_admin_rotation(self):
        """Gets the enable_admin_rotation of this DynamicSecretUpdateVenafi.  # noqa: E501

        Automatic admin credentials rotation  # noqa: E501

        :return: The enable_admin_rotation of this DynamicSecretUpdateVenafi.  # noqa: E501
        :rtype: bool
        """
        return self._enable_admin_rotation

    @enable_admin_rotation.setter
    def enable_admin_rotation(self, enable_admin_rotation):
        """Sets the enable_admin_rotation of this DynamicSecretUpdateVenafi.

        Automatic admin credentials rotation  # noqa: E501

        :param enable_admin_rotation: The enable_admin_rotation of this DynamicSecretUpdateVenafi.  # noqa: E501
        :type: bool
        """

        self._enable_admin_rotation = enable_admin_rotation

    @property
    def json(self):
        """Gets the json of this DynamicSecretUpdateVenafi.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this DynamicSecretUpdateVenafi.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this DynamicSecretUpdateVenafi.

        Set output format to JSON  # noqa: E501

        :param json: The json of this DynamicSecretUpdateVenafi.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def name(self):
        """Gets the name of this DynamicSecretUpdateVenafi.  # noqa: E501

        Dynamic secret name  # noqa: E501

        :return: The name of this DynamicSecretUpdateVenafi.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DynamicSecretUpdateVenafi.

        Dynamic secret name  # noqa: E501

        :param name: The name of this DynamicSecretUpdateVenafi.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def new_name(self):
        """Gets the new_name of this DynamicSecretUpdateVenafi.  # noqa: E501

        Dynamic secret new name  # noqa: E501

        :return: The new_name of this DynamicSecretUpdateVenafi.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this DynamicSecretUpdateVenafi.

        Dynamic secret new name  # noqa: E501

        :param new_name: The new_name of this DynamicSecretUpdateVenafi.  # noqa: E501
        :type: str
        """

        self._new_name = new_name

    @property
    def producer_encryption_key_name(self):
        """Gets the producer_encryption_key_name of this DynamicSecretUpdateVenafi.  # noqa: E501

        Dynamic producer encryption key  # noqa: E501

        :return: The producer_encryption_key_name of this DynamicSecretUpdateVenafi.  # noqa: E501
        :rtype: str
        """
        return self._producer_encryption_key_name

    @producer_encryption_key_name.setter
    def producer_encryption_key_name(self, producer_encryption_key_name):
        """Sets the producer_encryption_key_name of this DynamicSecretUpdateVenafi.

        Dynamic producer encryption key  # noqa: E501

        :param producer_encryption_key_name: The producer_encryption_key_name of this DynamicSecretUpdateVenafi.  # noqa: E501
        :type: str
        """

        self._producer_encryption_key_name = producer_encryption_key_name

    @property
    def root_first_in_chain(self):
        """Gets the root_first_in_chain of this DynamicSecretUpdateVenafi.  # noqa: E501

        Root first in chain  # noqa: E501

        :return: The root_first_in_chain of this DynamicSecretUpdateVenafi.  # noqa: E501
        :rtype: bool
        """
        return self._root_first_in_chain

    @root_first_in_chain.setter
    def root_first_in_chain(self, root_first_in_chain):
        """Sets the root_first_in_chain of this DynamicSecretUpdateVenafi.

        Root first in chain  # noqa: E501

        :param root_first_in_chain: The root_first_in_chain of this DynamicSecretUpdateVenafi.  # noqa: E501
        :type: bool
        """

        self._root_first_in_chain = root_first_in_chain

    @property
    def sign_using_akeyless_pki(self):
        """Gets the sign_using_akeyless_pki of this DynamicSecretUpdateVenafi.  # noqa: E501

        Use Akeyless PKI issuer or Venafi issuer  # noqa: E501

        :return: The sign_using_akeyless_pki of this DynamicSecretUpdateVenafi.  # noqa: E501
        :rtype: bool
        """
        return self._sign_using_akeyless_pki

    @sign_using_akeyless_pki.setter
    def sign_using_akeyless_pki(self, sign_using_akeyless_pki):
        """Sets the sign_using_akeyless_pki of this DynamicSecretUpdateVenafi.

        Use Akeyless PKI issuer or Venafi issuer  # noqa: E501

        :param sign_using_akeyless_pki: The sign_using_akeyless_pki of this DynamicSecretUpdateVenafi.  # noqa: E501
        :type: bool
        """

        self._sign_using_akeyless_pki = sign_using_akeyless_pki

    @property
    def signer_key_name(self):
        """Gets the signer_key_name of this DynamicSecretUpdateVenafi.  # noqa: E501

        Signer key name  # noqa: E501

        :return: The signer_key_name of this DynamicSecretUpdateVenafi.  # noqa: E501
        :rtype: str
        """
        return self._signer_key_name

    @signer_key_name.setter
    def signer_key_name(self, signer_key_name):
        """Sets the signer_key_name of this DynamicSecretUpdateVenafi.

        Signer key name  # noqa: E501

        :param signer_key_name: The signer_key_name of this DynamicSecretUpdateVenafi.  # noqa: E501
        :type: str
        """

        self._signer_key_name = signer_key_name

    @property
    def store_private_key(self):
        """Gets the store_private_key of this DynamicSecretUpdateVenafi.  # noqa: E501

        Store private key  # noqa: E501

        :return: The store_private_key of this DynamicSecretUpdateVenafi.  # noqa: E501
        :rtype: bool
        """
        return self._store_private_key

    @store_private_key.setter
    def store_private_key(self, store_private_key):
        """Sets the store_private_key of this DynamicSecretUpdateVenafi.

        Store private key  # noqa: E501

        :param store_private_key: The store_private_key of this DynamicSecretUpdateVenafi.  # noqa: E501
        :type: bool
        """

        self._store_private_key = store_private_key

    @property
    def tags(self):
        """Gets the tags of this DynamicSecretUpdateVenafi.  # noqa: E501

        Add tags attached to this object  # noqa: E501

        :return: The tags of this DynamicSecretUpdateVenafi.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DynamicSecretUpdateVenafi.

        Add tags attached to this object  # noqa: E501

        :param tags: The tags of this DynamicSecretUpdateVenafi.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def target_name(self):
        """Gets the target_name of this DynamicSecretUpdateVenafi.  # noqa: E501

        Target name  # noqa: E501

        :return: The target_name of this DynamicSecretUpdateVenafi.  # noqa: E501
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """Sets the target_name of this DynamicSecretUpdateVenafi.

        Target name  # noqa: E501

        :param target_name: The target_name of this DynamicSecretUpdateVenafi.  # noqa: E501
        :type: str
        """

        self._target_name = target_name

    @property
    def token(self):
        """Gets the token of this DynamicSecretUpdateVenafi.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this DynamicSecretUpdateVenafi.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this DynamicSecretUpdateVenafi.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this DynamicSecretUpdateVenafi.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this DynamicSecretUpdateVenafi.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this DynamicSecretUpdateVenafi.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this DynamicSecretUpdateVenafi.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this DynamicSecretUpdateVenafi.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def user_ttl(self):
        """Gets the user_ttl of this DynamicSecretUpdateVenafi.  # noqa: E501

        User TTL in time.Duration format (2160h / 129600m / etc...). When using sign-using-akeyless-pki certificates created will have this validity period, otherwise the user-ttl is taken from the Validity Period field of the Zone's' Issuing Template. When using cert-manager it is advised to have a TTL of above 60 days (1440h). For more information - https://cert-manager.io/docs/usage/certificate/  # noqa: E501

        :return: The user_ttl of this DynamicSecretUpdateVenafi.  # noqa: E501
        :rtype: str
        """
        return self._user_ttl

    @user_ttl.setter
    def user_ttl(self, user_ttl):
        """Sets the user_ttl of this DynamicSecretUpdateVenafi.

        User TTL in time.Duration format (2160h / 129600m / etc...). When using sign-using-akeyless-pki certificates created will have this validity period, otherwise the user-ttl is taken from the Validity Period field of the Zone's' Issuing Template. When using cert-manager it is advised to have a TTL of above 60 days (1440h). For more information - https://cert-manager.io/docs/usage/certificate/  # noqa: E501

        :param user_ttl: The user_ttl of this DynamicSecretUpdateVenafi.  # noqa: E501
        :type: str
        """

        self._user_ttl = user_ttl

    @property
    def venafi_access_token(self):
        """Gets the venafi_access_token of this DynamicSecretUpdateVenafi.  # noqa: E501

        Venafi Access Token to use to access the TPP environment (Relevant when using TPP)  # noqa: E501

        :return: The venafi_access_token of this DynamicSecretUpdateVenafi.  # noqa: E501
        :rtype: str
        """
        return self._venafi_access_token

    @venafi_access_token.setter
    def venafi_access_token(self, venafi_access_token):
        """Sets the venafi_access_token of this DynamicSecretUpdateVenafi.

        Venafi Access Token to use to access the TPP environment (Relevant when using TPP)  # noqa: E501

        :param venafi_access_token: The venafi_access_token of this DynamicSecretUpdateVenafi.  # noqa: E501
        :type: str
        """

        self._venafi_access_token = venafi_access_token

    @property
    def venafi_api_key(self):
        """Gets the venafi_api_key of this DynamicSecretUpdateVenafi.  # noqa: E501

        Venafi API key  # noqa: E501

        :return: The venafi_api_key of this DynamicSecretUpdateVenafi.  # noqa: E501
        :rtype: str
        """
        return self._venafi_api_key

    @venafi_api_key.setter
    def venafi_api_key(self, venafi_api_key):
        """Sets the venafi_api_key of this DynamicSecretUpdateVenafi.

        Venafi API key  # noqa: E501

        :param venafi_api_key: The venafi_api_key of this DynamicSecretUpdateVenafi.  # noqa: E501
        :type: str
        """

        self._venafi_api_key = venafi_api_key

    @property
    def venafi_baseurl(self):
        """Gets the venafi_baseurl of this DynamicSecretUpdateVenafi.  # noqa: E501

        Venafi Baseurl  # noqa: E501

        :return: The venafi_baseurl of this DynamicSecretUpdateVenafi.  # noqa: E501
        :rtype: str
        """
        return self._venafi_baseurl

    @venafi_baseurl.setter
    def venafi_baseurl(self, venafi_baseurl):
        """Sets the venafi_baseurl of this DynamicSecretUpdateVenafi.

        Venafi Baseurl  # noqa: E501

        :param venafi_baseurl: The venafi_baseurl of this DynamicSecretUpdateVenafi.  # noqa: E501
        :type: str
        """

        self._venafi_baseurl = venafi_baseurl

    @property
    def venafi_client_id(self):
        """Gets the venafi_client_id of this DynamicSecretUpdateVenafi.  # noqa: E501

        Venafi Client ID that was used when the access token was generated  # noqa: E501

        :return: The venafi_client_id of this DynamicSecretUpdateVenafi.  # noqa: E501
        :rtype: str
        """
        return self._venafi_client_id

    @venafi_client_id.setter
    def venafi_client_id(self, venafi_client_id):
        """Sets the venafi_client_id of this DynamicSecretUpdateVenafi.

        Venafi Client ID that was used when the access token was generated  # noqa: E501

        :param venafi_client_id: The venafi_client_id of this DynamicSecretUpdateVenafi.  # noqa: E501
        :type: str
        """

        self._venafi_client_id = venafi_client_id

    @property
    def venafi_refresh_token(self):
        """Gets the venafi_refresh_token of this DynamicSecretUpdateVenafi.  # noqa: E501

        Venafi Refresh Token to use when the Access Token is expired (Relevant when using TPP)  # noqa: E501

        :return: The venafi_refresh_token of this DynamicSecretUpdateVenafi.  # noqa: E501
        :rtype: str
        """
        return self._venafi_refresh_token

    @venafi_refresh_token.setter
    def venafi_refresh_token(self, venafi_refresh_token):
        """Sets the venafi_refresh_token of this DynamicSecretUpdateVenafi.

        Venafi Refresh Token to use when the Access Token is expired (Relevant when using TPP)  # noqa: E501

        :param venafi_refresh_token: The venafi_refresh_token of this DynamicSecretUpdateVenafi.  # noqa: E501
        :type: str
        """

        self._venafi_refresh_token = venafi_refresh_token

    @property
    def venafi_use_tpp(self):
        """Gets the venafi_use_tpp of this DynamicSecretUpdateVenafi.  # noqa: E501

        Venafi using TPP  # noqa: E501

        :return: The venafi_use_tpp of this DynamicSecretUpdateVenafi.  # noqa: E501
        :rtype: bool
        """
        return self._venafi_use_tpp

    @venafi_use_tpp.setter
    def venafi_use_tpp(self, venafi_use_tpp):
        """Sets the venafi_use_tpp of this DynamicSecretUpdateVenafi.

        Venafi using TPP  # noqa: E501

        :param venafi_use_tpp: The venafi_use_tpp of this DynamicSecretUpdateVenafi.  # noqa: E501
        :type: bool
        """

        self._venafi_use_tpp = venafi_use_tpp

    @property
    def venafi_zone(self):
        """Gets the venafi_zone of this DynamicSecretUpdateVenafi.  # noqa: E501

        Venafi Zone  # noqa: E501

        :return: The venafi_zone of this DynamicSecretUpdateVenafi.  # noqa: E501
        :rtype: str
        """
        return self._venafi_zone

    @venafi_zone.setter
    def venafi_zone(self, venafi_zone):
        """Sets the venafi_zone of this DynamicSecretUpdateVenafi.

        Venafi Zone  # noqa: E501

        :param venafi_zone: The venafi_zone of this DynamicSecretUpdateVenafi.  # noqa: E501
        :type: str
        """

        self._venafi_zone = venafi_zone

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
        if not isinstance(other, DynamicSecretUpdateVenafi):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DynamicSecretUpdateVenafi):
            return True

        return self.to_dict() != other.to_dict()
