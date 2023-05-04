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


class CreateZeroSSLTarget(object):
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
        'api_key': 'str',
        'comment': 'str',
        'description': 'str',
        'imap_fqdn': 'str',
        'imap_password': 'str',
        'imap_port': 'str',
        'imap_target_email': 'str',
        'imap_username': 'str',
        'json': 'bool',
        'key': 'str',
        'name': 'str',
        'timeout': 'str',
        'token': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'api_key': 'api-key',
        'comment': 'comment',
        'description': 'description',
        'imap_fqdn': 'imap-fqdn',
        'imap_password': 'imap-password',
        'imap_port': 'imap-port',
        'imap_target_email': 'imap-target-email',
        'imap_username': 'imap-username',
        'json': 'json',
        'key': 'key',
        'name': 'name',
        'timeout': 'timeout',
        'token': 'token',
        'uid_token': 'uid-token'
    }

    def __init__(self, api_key=None, comment=None, description=None, imap_fqdn=None, imap_password=None, imap_port='993', imap_target_email=None, imap_username=None, json=False, key=None, name=None, timeout='5m', token=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """CreateZeroSSLTarget - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._api_key = None
        self._comment = None
        self._description = None
        self._imap_fqdn = None
        self._imap_password = None
        self._imap_port = None
        self._imap_target_email = None
        self._imap_username = None
        self._json = None
        self._key = None
        self._name = None
        self._timeout = None
        self._token = None
        self._uid_token = None
        self.discriminator = None

        self.api_key = api_key
        if comment is not None:
            self.comment = comment
        if description is not None:
            self.description = description
        self.imap_fqdn = imap_fqdn
        self.imap_password = imap_password
        if imap_port is not None:
            self.imap_port = imap_port
        if imap_target_email is not None:
            self.imap_target_email = imap_target_email
        self.imap_username = imap_username
        if json is not None:
            self.json = json
        if key is not None:
            self.key = key
        self.name = name
        if timeout is not None:
            self.timeout = timeout
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def api_key(self):
        """Gets the api_key of this CreateZeroSSLTarget.  # noqa: E501

        API Key of the ZeroSSLTarget account  # noqa: E501

        :return: The api_key of this CreateZeroSSLTarget.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this CreateZeroSSLTarget.

        API Key of the ZeroSSLTarget account  # noqa: E501

        :param api_key: The api_key of this CreateZeroSSLTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and api_key is None:  # noqa: E501
            raise ValueError("Invalid value for `api_key`, must not be `None`")  # noqa: E501

        self._api_key = api_key

    @property
    def comment(self):
        """Gets the comment of this CreateZeroSSLTarget.  # noqa: E501

        Deprecated - use description  # noqa: E501

        :return: The comment of this CreateZeroSSLTarget.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this CreateZeroSSLTarget.

        Deprecated - use description  # noqa: E501

        :param comment: The comment of this CreateZeroSSLTarget.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def description(self):
        """Gets the description of this CreateZeroSSLTarget.  # noqa: E501

        Description of the object  # noqa: E501

        :return: The description of this CreateZeroSSLTarget.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateZeroSSLTarget.

        Description of the object  # noqa: E501

        :param description: The description of this CreateZeroSSLTarget.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def imap_fqdn(self):
        """Gets the imap_fqdn of this CreateZeroSSLTarget.  # noqa: E501

        ImapFQDN of the IMAP service, FQDN or IPv4 address. Must be FQDN if the IMAP is using TLS  # noqa: E501

        :return: The imap_fqdn of this CreateZeroSSLTarget.  # noqa: E501
        :rtype: str
        """
        return self._imap_fqdn

    @imap_fqdn.setter
    def imap_fqdn(self, imap_fqdn):
        """Sets the imap_fqdn of this CreateZeroSSLTarget.

        ImapFQDN of the IMAP service, FQDN or IPv4 address. Must be FQDN if the IMAP is using TLS  # noqa: E501

        :param imap_fqdn: The imap_fqdn of this CreateZeroSSLTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and imap_fqdn is None:  # noqa: E501
            raise ValueError("Invalid value for `imap_fqdn`, must not be `None`")  # noqa: E501

        self._imap_fqdn = imap_fqdn

    @property
    def imap_password(self):
        """Gets the imap_password of this CreateZeroSSLTarget.  # noqa: E501

        ImapPassword to access the IMAP service  # noqa: E501

        :return: The imap_password of this CreateZeroSSLTarget.  # noqa: E501
        :rtype: str
        """
        return self._imap_password

    @imap_password.setter
    def imap_password(self, imap_password):
        """Sets the imap_password of this CreateZeroSSLTarget.

        ImapPassword to access the IMAP service  # noqa: E501

        :param imap_password: The imap_password of this CreateZeroSSLTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and imap_password is None:  # noqa: E501
            raise ValueError("Invalid value for `imap_password`, must not be `None`")  # noqa: E501

        self._imap_password = imap_password

    @property
    def imap_port(self):
        """Gets the imap_port of this CreateZeroSSLTarget.  # noqa: E501

        ImapPort of the IMAP service  # noqa: E501

        :return: The imap_port of this CreateZeroSSLTarget.  # noqa: E501
        :rtype: str
        """
        return self._imap_port

    @imap_port.setter
    def imap_port(self, imap_port):
        """Sets the imap_port of this CreateZeroSSLTarget.

        ImapPort of the IMAP service  # noqa: E501

        :param imap_port: The imap_port of this CreateZeroSSLTarget.  # noqa: E501
        :type: str
        """

        self._imap_port = imap_port

    @property
    def imap_target_email(self):
        """Gets the imap_target_email of this CreateZeroSSLTarget.  # noqa: E501

        ImapValidationEmail to use when asking ZeroSSL to send a validation email, if empty will user imap-username  # noqa: E501

        :return: The imap_target_email of this CreateZeroSSLTarget.  # noqa: E501
        :rtype: str
        """
        return self._imap_target_email

    @imap_target_email.setter
    def imap_target_email(self, imap_target_email):
        """Sets the imap_target_email of this CreateZeroSSLTarget.

        ImapValidationEmail to use when asking ZeroSSL to send a validation email, if empty will user imap-username  # noqa: E501

        :param imap_target_email: The imap_target_email of this CreateZeroSSLTarget.  # noqa: E501
        :type: str
        """

        self._imap_target_email = imap_target_email

    @property
    def imap_username(self):
        """Gets the imap_username of this CreateZeroSSLTarget.  # noqa: E501

        ImapUsername to access the IMAP service  # noqa: E501

        :return: The imap_username of this CreateZeroSSLTarget.  # noqa: E501
        :rtype: str
        """
        return self._imap_username

    @imap_username.setter
    def imap_username(self, imap_username):
        """Sets the imap_username of this CreateZeroSSLTarget.

        ImapUsername to access the IMAP service  # noqa: E501

        :param imap_username: The imap_username of this CreateZeroSSLTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and imap_username is None:  # noqa: E501
            raise ValueError("Invalid value for `imap_username`, must not be `None`")  # noqa: E501

        self._imap_username = imap_username

    @property
    def json(self):
        """Gets the json of this CreateZeroSSLTarget.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this CreateZeroSSLTarget.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this CreateZeroSSLTarget.

        Set output format to JSON  # noqa: E501

        :param json: The json of this CreateZeroSSLTarget.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def key(self):
        """Gets the key of this CreateZeroSSLTarget.  # noqa: E501

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :return: The key of this CreateZeroSSLTarget.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CreateZeroSSLTarget.

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :param key: The key of this CreateZeroSSLTarget.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this CreateZeroSSLTarget.  # noqa: E501

        Target name  # noqa: E501

        :return: The name of this CreateZeroSSLTarget.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateZeroSSLTarget.

        Target name  # noqa: E501

        :param name: The name of this CreateZeroSSLTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def timeout(self):
        """Gets the timeout of this CreateZeroSSLTarget.  # noqa: E501

        Timeout waiting for certificate validation in Duration format (1h - 1 Hour, 20m - 20 Minutes, 33m3s - 33 Minutes and 3 Seconds), maximum 1h.  # noqa: E501

        :return: The timeout of this CreateZeroSSLTarget.  # noqa: E501
        :rtype: str
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this CreateZeroSSLTarget.

        Timeout waiting for certificate validation in Duration format (1h - 1 Hour, 20m - 20 Minutes, 33m3s - 33 Minutes and 3 Seconds), maximum 1h.  # noqa: E501

        :param timeout: The timeout of this CreateZeroSSLTarget.  # noqa: E501
        :type: str
        """

        self._timeout = timeout

    @property
    def token(self):
        """Gets the token of this CreateZeroSSLTarget.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this CreateZeroSSLTarget.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this CreateZeroSSLTarget.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this CreateZeroSSLTarget.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this CreateZeroSSLTarget.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this CreateZeroSSLTarget.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this CreateZeroSSLTarget.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this CreateZeroSSLTarget.  # noqa: E501
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
        if not isinstance(other, CreateZeroSSLTarget):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateZeroSSLTarget):
            return True

        return self.to_dict() != other.to_dict()
