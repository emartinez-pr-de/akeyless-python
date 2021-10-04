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


class CreateSSHCertIssuer(object):
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
        'allowed_users': 'str',
        'extensions': 'dict(str, str)',
        'metadata': 'str',
        'name': 'str',
        'password': 'str',
        'principals': 'str',
        'secure_access_bastion_api': 'str',
        'secure_access_bastion_ssh': 'str',
        'secure_access_enable': 'str',
        'secure_access_host': 'list[str]',
        'secure_access_ssh_creds_user': 'str',
        'secure_access_use_internal_bastion': 'bool',
        'signer_key_name': 'str',
        'token': 'str',
        'ttl': 'int',
        'uid_token': 'str',
        'username': 'str'
    }

    attribute_map = {
        'allowed_users': 'allowed-users',
        'extensions': 'extensions',
        'metadata': 'metadata',
        'name': 'name',
        'password': 'password',
        'principals': 'principals',
        'secure_access_bastion_api': 'secure-access-bastion-api',
        'secure_access_bastion_ssh': 'secure-access-bastion-ssh',
        'secure_access_enable': 'secure-access-enable',
        'secure_access_host': 'secure-access-host',
        'secure_access_ssh_creds_user': 'secure-access-ssh-creds-user',
        'secure_access_use_internal_bastion': 'secure-access-use-internal-bastion',
        'signer_key_name': 'signer-key-name',
        'token': 'token',
        'ttl': 'ttl',
        'uid_token': 'uid-token',
        'username': 'username'
    }

    def __init__(self, allowed_users=None, extensions=None, metadata=None, name=None, password=None, principals=None, secure_access_bastion_api=None, secure_access_bastion_ssh=None, secure_access_enable=None, secure_access_host=None, secure_access_ssh_creds_user=None, secure_access_use_internal_bastion=None, signer_key_name=None, token=None, ttl=None, uid_token=None, username=None, local_vars_configuration=None):  # noqa: E501
        """CreateSSHCertIssuer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._allowed_users = None
        self._extensions = None
        self._metadata = None
        self._name = None
        self._password = None
        self._principals = None
        self._secure_access_bastion_api = None
        self._secure_access_bastion_ssh = None
        self._secure_access_enable = None
        self._secure_access_host = None
        self._secure_access_ssh_creds_user = None
        self._secure_access_use_internal_bastion = None
        self._signer_key_name = None
        self._token = None
        self._ttl = None
        self._uid_token = None
        self._username = None
        self.discriminator = None

        self.allowed_users = allowed_users
        if extensions is not None:
            self.extensions = extensions
        if metadata is not None:
            self.metadata = metadata
        self.name = name
        if password is not None:
            self.password = password
        if principals is not None:
            self.principals = principals
        if secure_access_bastion_api is not None:
            self.secure_access_bastion_api = secure_access_bastion_api
        if secure_access_bastion_ssh is not None:
            self.secure_access_bastion_ssh = secure_access_bastion_ssh
        if secure_access_enable is not None:
            self.secure_access_enable = secure_access_enable
        if secure_access_host is not None:
            self.secure_access_host = secure_access_host
        if secure_access_ssh_creds_user is not None:
            self.secure_access_ssh_creds_user = secure_access_ssh_creds_user
        if secure_access_use_internal_bastion is not None:
            self.secure_access_use_internal_bastion = secure_access_use_internal_bastion
        self.signer_key_name = signer_key_name
        if token is not None:
            self.token = token
        self.ttl = ttl
        if uid_token is not None:
            self.uid_token = uid_token
        if username is not None:
            self.username = username

    @property
    def allowed_users(self):
        """Gets the allowed_users of this CreateSSHCertIssuer.  # noqa: E501

        Users allowed to fetch the certificate, e.g root,ubuntu  # noqa: E501

        :return: The allowed_users of this CreateSSHCertIssuer.  # noqa: E501
        :rtype: str
        """
        return self._allowed_users

    @allowed_users.setter
    def allowed_users(self, allowed_users):
        """Sets the allowed_users of this CreateSSHCertIssuer.

        Users allowed to fetch the certificate, e.g root,ubuntu  # noqa: E501

        :param allowed_users: The allowed_users of this CreateSSHCertIssuer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and allowed_users is None:  # noqa: E501
            raise ValueError("Invalid value for `allowed_users`, must not be `None`")  # noqa: E501

        self._allowed_users = allowed_users

    @property
    def extensions(self):
        """Gets the extensions of this CreateSSHCertIssuer.  # noqa: E501

        Signed certificates with extensions, e.g permit-port-forwarding=\\\"\\\"  # noqa: E501

        :return: The extensions of this CreateSSHCertIssuer.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions):
        """Sets the extensions of this CreateSSHCertIssuer.

        Signed certificates with extensions, e.g permit-port-forwarding=\\\"\\\"  # noqa: E501

        :param extensions: The extensions of this CreateSSHCertIssuer.  # noqa: E501
        :type: dict(str, str)
        """

        self._extensions = extensions

    @property
    def metadata(self):
        """Gets the metadata of this CreateSSHCertIssuer.  # noqa: E501

        A metadata about the issuer  # noqa: E501

        :return: The metadata of this CreateSSHCertIssuer.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CreateSSHCertIssuer.

        A metadata about the issuer  # noqa: E501

        :param metadata: The metadata of this CreateSSHCertIssuer.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this CreateSSHCertIssuer.  # noqa: E501

        SSH certificate issuer name  # noqa: E501

        :return: The name of this CreateSSHCertIssuer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateSSHCertIssuer.

        SSH certificate issuer name  # noqa: E501

        :param name: The name of this CreateSSHCertIssuer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def password(self):
        """Gets the password of this CreateSSHCertIssuer.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The password of this CreateSSHCertIssuer.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateSSHCertIssuer.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param password: The password of this CreateSSHCertIssuer.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def principals(self):
        """Gets the principals of this CreateSSHCertIssuer.  # noqa: E501

        Signed certificates with principal, e.g example_role1,example_role2  # noqa: E501

        :return: The principals of this CreateSSHCertIssuer.  # noqa: E501
        :rtype: str
        """
        return self._principals

    @principals.setter
    def principals(self, principals):
        """Sets the principals of this CreateSSHCertIssuer.

        Signed certificates with principal, e.g example_role1,example_role2  # noqa: E501

        :param principals: The principals of this CreateSSHCertIssuer.  # noqa: E501
        :type: str
        """

        self._principals = principals

    @property
    def secure_access_bastion_api(self):
        """Gets the secure_access_bastion_api of this CreateSSHCertIssuer.  # noqa: E501


        :return: The secure_access_bastion_api of this CreateSSHCertIssuer.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_bastion_api

    @secure_access_bastion_api.setter
    def secure_access_bastion_api(self, secure_access_bastion_api):
        """Sets the secure_access_bastion_api of this CreateSSHCertIssuer.


        :param secure_access_bastion_api: The secure_access_bastion_api of this CreateSSHCertIssuer.  # noqa: E501
        :type: str
        """

        self._secure_access_bastion_api = secure_access_bastion_api

    @property
    def secure_access_bastion_ssh(self):
        """Gets the secure_access_bastion_ssh of this CreateSSHCertIssuer.  # noqa: E501


        :return: The secure_access_bastion_ssh of this CreateSSHCertIssuer.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_bastion_ssh

    @secure_access_bastion_ssh.setter
    def secure_access_bastion_ssh(self, secure_access_bastion_ssh):
        """Sets the secure_access_bastion_ssh of this CreateSSHCertIssuer.


        :param secure_access_bastion_ssh: The secure_access_bastion_ssh of this CreateSSHCertIssuer.  # noqa: E501
        :type: str
        """

        self._secure_access_bastion_ssh = secure_access_bastion_ssh

    @property
    def secure_access_enable(self):
        """Gets the secure_access_enable of this CreateSSHCertIssuer.  # noqa: E501


        :return: The secure_access_enable of this CreateSSHCertIssuer.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_enable

    @secure_access_enable.setter
    def secure_access_enable(self, secure_access_enable):
        """Sets the secure_access_enable of this CreateSSHCertIssuer.


        :param secure_access_enable: The secure_access_enable of this CreateSSHCertIssuer.  # noqa: E501
        :type: str
        """

        self._secure_access_enable = secure_access_enable

    @property
    def secure_access_host(self):
        """Gets the secure_access_host of this CreateSSHCertIssuer.  # noqa: E501


        :return: The secure_access_host of this CreateSSHCertIssuer.  # noqa: E501
        :rtype: list[str]
        """
        return self._secure_access_host

    @secure_access_host.setter
    def secure_access_host(self, secure_access_host):
        """Sets the secure_access_host of this CreateSSHCertIssuer.


        :param secure_access_host: The secure_access_host of this CreateSSHCertIssuer.  # noqa: E501
        :type: list[str]
        """

        self._secure_access_host = secure_access_host

    @property
    def secure_access_ssh_creds_user(self):
        """Gets the secure_access_ssh_creds_user of this CreateSSHCertIssuer.  # noqa: E501


        :return: The secure_access_ssh_creds_user of this CreateSSHCertIssuer.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_ssh_creds_user

    @secure_access_ssh_creds_user.setter
    def secure_access_ssh_creds_user(self, secure_access_ssh_creds_user):
        """Sets the secure_access_ssh_creds_user of this CreateSSHCertIssuer.


        :param secure_access_ssh_creds_user: The secure_access_ssh_creds_user of this CreateSSHCertIssuer.  # noqa: E501
        :type: str
        """

        self._secure_access_ssh_creds_user = secure_access_ssh_creds_user

    @property
    def secure_access_use_internal_bastion(self):
        """Gets the secure_access_use_internal_bastion of this CreateSSHCertIssuer.  # noqa: E501


        :return: The secure_access_use_internal_bastion of this CreateSSHCertIssuer.  # noqa: E501
        :rtype: bool
        """
        return self._secure_access_use_internal_bastion

    @secure_access_use_internal_bastion.setter
    def secure_access_use_internal_bastion(self, secure_access_use_internal_bastion):
        """Sets the secure_access_use_internal_bastion of this CreateSSHCertIssuer.


        :param secure_access_use_internal_bastion: The secure_access_use_internal_bastion of this CreateSSHCertIssuer.  # noqa: E501
        :type: bool
        """

        self._secure_access_use_internal_bastion = secure_access_use_internal_bastion

    @property
    def signer_key_name(self):
        """Gets the signer_key_name of this CreateSSHCertIssuer.  # noqa: E501

        A key to sign the certificate with  # noqa: E501

        :return: The signer_key_name of this CreateSSHCertIssuer.  # noqa: E501
        :rtype: str
        """
        return self._signer_key_name

    @signer_key_name.setter
    def signer_key_name(self, signer_key_name):
        """Sets the signer_key_name of this CreateSSHCertIssuer.

        A key to sign the certificate with  # noqa: E501

        :param signer_key_name: The signer_key_name of this CreateSSHCertIssuer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and signer_key_name is None:  # noqa: E501
            raise ValueError("Invalid value for `signer_key_name`, must not be `None`")  # noqa: E501

        self._signer_key_name = signer_key_name

    @property
    def token(self):
        """Gets the token of this CreateSSHCertIssuer.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this CreateSSHCertIssuer.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this CreateSSHCertIssuer.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this CreateSSHCertIssuer.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def ttl(self):
        """Gets the ttl of this CreateSSHCertIssuer.  # noqa: E501

        he requested Time To Live for the certificate, in seconds  # noqa: E501

        :return: The ttl of this CreateSSHCertIssuer.  # noqa: E501
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this CreateSSHCertIssuer.

        he requested Time To Live for the certificate, in seconds  # noqa: E501

        :param ttl: The ttl of this CreateSSHCertIssuer.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and ttl is None:  # noqa: E501
            raise ValueError("Invalid value for `ttl`, must not be `None`")  # noqa: E501

        self._ttl = ttl

    @property
    def uid_token(self):
        """Gets the uid_token of this CreateSSHCertIssuer.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this CreateSSHCertIssuer.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this CreateSSHCertIssuer.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this CreateSSHCertIssuer.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def username(self):
        """Gets the username of this CreateSSHCertIssuer.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The username of this CreateSSHCertIssuer.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this CreateSSHCertIssuer.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param username: The username of this CreateSSHCertIssuer.  # noqa: E501
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
        if not isinstance(other, CreateSSHCertIssuer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateSSHCertIssuer):
            return True

        return self.to_dict() != other.to_dict()
