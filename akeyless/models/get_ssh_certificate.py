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


class GetSSHCertificate(object):
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
        'cert_issuer_name': 'str',
        'cert_username': 'str',
        'password': 'str',
        'public_key_data': 'str',
        'token': 'str',
        'uid_token': 'str',
        'username': 'str'
    }

    attribute_map = {
        'cert_issuer_name': 'cert-issuer-name',
        'cert_username': 'cert-username',
        'password': 'password',
        'public_key_data': 'public-key-data',
        'token': 'token',
        'uid_token': 'uid-token',
        'username': 'username'
    }

    def __init__(self, cert_issuer_name=None, cert_username=None, password=None, public_key_data=None, token=None, uid_token=None, username=None, local_vars_configuration=None):  # noqa: E501
        """GetSSHCertificate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cert_issuer_name = None
        self._cert_username = None
        self._password = None
        self._public_key_data = None
        self._token = None
        self._uid_token = None
        self._username = None
        self.discriminator = None

        self.cert_issuer_name = cert_issuer_name
        self.cert_username = cert_username
        if password is not None:
            self.password = password
        if public_key_data is not None:
            self.public_key_data = public_key_data
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if username is not None:
            self.username = username

    @property
    def cert_issuer_name(self):
        """Gets the cert_issuer_name of this GetSSHCertificate.  # noqa: E501

        The name of the SSH certificate issuer  # noqa: E501

        :return: The cert_issuer_name of this GetSSHCertificate.  # noqa: E501
        :rtype: str
        """
        return self._cert_issuer_name

    @cert_issuer_name.setter
    def cert_issuer_name(self, cert_issuer_name):
        """Sets the cert_issuer_name of this GetSSHCertificate.

        The name of the SSH certificate issuer  # noqa: E501

        :param cert_issuer_name: The cert_issuer_name of this GetSSHCertificate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and cert_issuer_name is None:  # noqa: E501
            raise ValueError("Invalid value for `cert_issuer_name`, must not be `None`")  # noqa: E501

        self._cert_issuer_name = cert_issuer_name

    @property
    def cert_username(self):
        """Gets the cert_username of this GetSSHCertificate.  # noqa: E501

        The username to sign in the SSH certificate  # noqa: E501

        :return: The cert_username of this GetSSHCertificate.  # noqa: E501
        :rtype: str
        """
        return self._cert_username

    @cert_username.setter
    def cert_username(self, cert_username):
        """Sets the cert_username of this GetSSHCertificate.

        The username to sign in the SSH certificate  # noqa: E501

        :param cert_username: The cert_username of this GetSSHCertificate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and cert_username is None:  # noqa: E501
            raise ValueError("Invalid value for `cert_username`, must not be `None`")  # noqa: E501

        self._cert_username = cert_username

    @property
    def password(self):
        """Gets the password of this GetSSHCertificate.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The password of this GetSSHCertificate.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this GetSSHCertificate.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param password: The password of this GetSSHCertificate.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def public_key_data(self):
        """Gets the public_key_data of this GetSSHCertificate.  # noqa: E501

        SSH public key file contents. If this option is used, the certificate will be printed to stdout  # noqa: E501

        :return: The public_key_data of this GetSSHCertificate.  # noqa: E501
        :rtype: str
        """
        return self._public_key_data

    @public_key_data.setter
    def public_key_data(self, public_key_data):
        """Sets the public_key_data of this GetSSHCertificate.

        SSH public key file contents. If this option is used, the certificate will be printed to stdout  # noqa: E501

        :param public_key_data: The public_key_data of this GetSSHCertificate.  # noqa: E501
        :type: str
        """

        self._public_key_data = public_key_data

    @property
    def token(self):
        """Gets the token of this GetSSHCertificate.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GetSSHCertificate.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GetSSHCertificate.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GetSSHCertificate.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this GetSSHCertificate.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GetSSHCertificate.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GetSSHCertificate.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GetSSHCertificate.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def username(self):
        """Gets the username of this GetSSHCertificate.  # noqa: E501

        Required only when the authentication process requires a username and password  # noqa: E501

        :return: The username of this GetSSHCertificate.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this GetSSHCertificate.

        Required only when the authentication process requires a username and password  # noqa: E501

        :param username: The username of this GetSSHCertificate.  # noqa: E501
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
        if not isinstance(other, GetSSHCertificate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetSSHCertificate):
            return True

        return self.to_dict() != other.to_dict()
