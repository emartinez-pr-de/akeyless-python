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


class UpdateSalesforceTarget(object):
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
        'app_private_key_data': 'str',
        'auth_flow': 'str',
        'ca_cert_data': 'str',
        'ca_cert_name': 'str',
        'client_id': 'str',
        'client_secret': 'str',
        'comment': 'str',
        'email': 'str',
        'keep_prev_version': 'str',
        'key': 'str',
        'name': 'str',
        'new_name': 'str',
        'password': 'str',
        'security_token': 'str',
        'tenant_url': 'str',
        'token': 'str',
        'uid_token': 'str',
        'update_version': 'bool'
    }

    attribute_map = {
        'app_private_key_data': 'app-private-key-data',
        'auth_flow': 'auth-flow',
        'ca_cert_data': 'ca-cert-data',
        'ca_cert_name': 'ca-cert-name',
        'client_id': 'client-id',
        'client_secret': 'client-secret',
        'comment': 'comment',
        'email': 'email',
        'keep_prev_version': 'keep-prev-version',
        'key': 'key',
        'name': 'name',
        'new_name': 'new-name',
        'password': 'password',
        'security_token': 'security-token',
        'tenant_url': 'tenant-url',
        'token': 'token',
        'uid_token': 'uid-token',
        'update_version': 'update-version'
    }

    def __init__(self, app_private_key_data=None, auth_flow=None, ca_cert_data=None, ca_cert_name=None, client_id=None, client_secret=None, comment=None, email=None, keep_prev_version=None, key=None, name=None, new_name=None, password=None, security_token=None, tenant_url=None, token=None, uid_token=None, update_version=None, local_vars_configuration=None):  # noqa: E501
        """UpdateSalesforceTarget - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._app_private_key_data = None
        self._auth_flow = None
        self._ca_cert_data = None
        self._ca_cert_name = None
        self._client_id = None
        self._client_secret = None
        self._comment = None
        self._email = None
        self._keep_prev_version = None
        self._key = None
        self._name = None
        self._new_name = None
        self._password = None
        self._security_token = None
        self._tenant_url = None
        self._token = None
        self._uid_token = None
        self._update_version = None
        self.discriminator = None

        if app_private_key_data is not None:
            self.app_private_key_data = app_private_key_data
        self.auth_flow = auth_flow
        if ca_cert_data is not None:
            self.ca_cert_data = ca_cert_data
        if ca_cert_name is not None:
            self.ca_cert_name = ca_cert_name
        self.client_id = client_id
        if client_secret is not None:
            self.client_secret = client_secret
        if comment is not None:
            self.comment = comment
        self.email = email
        if keep_prev_version is not None:
            self.keep_prev_version = keep_prev_version
        if key is not None:
            self.key = key
        self.name = name
        if new_name is not None:
            self.new_name = new_name
        if password is not None:
            self.password = password
        if security_token is not None:
            self.security_token = security_token
        self.tenant_url = tenant_url
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if update_version is not None:
            self.update_version = update_version

    @property
    def app_private_key_data(self):
        """Gets the app_private_key_data of this UpdateSalesforceTarget.  # noqa: E501

        Base64 encoded PEM of the connected app private key (relevant for JWT auth only)  # noqa: E501

        :return: The app_private_key_data of this UpdateSalesforceTarget.  # noqa: E501
        :rtype: str
        """
        return self._app_private_key_data

    @app_private_key_data.setter
    def app_private_key_data(self, app_private_key_data):
        """Sets the app_private_key_data of this UpdateSalesforceTarget.

        Base64 encoded PEM of the connected app private key (relevant for JWT auth only)  # noqa: E501

        :param app_private_key_data: The app_private_key_data of this UpdateSalesforceTarget.  # noqa: E501
        :type: str
        """

        self._app_private_key_data = app_private_key_data

    @property
    def auth_flow(self):
        """Gets the auth_flow of this UpdateSalesforceTarget.  # noqa: E501

        type of the auth flow ('jwt' / 'user-password')  # noqa: E501

        :return: The auth_flow of this UpdateSalesforceTarget.  # noqa: E501
        :rtype: str
        """
        return self._auth_flow

    @auth_flow.setter
    def auth_flow(self, auth_flow):
        """Sets the auth_flow of this UpdateSalesforceTarget.

        type of the auth flow ('jwt' / 'user-password')  # noqa: E501

        :param auth_flow: The auth_flow of this UpdateSalesforceTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and auth_flow is None:  # noqa: E501
            raise ValueError("Invalid value for `auth_flow`, must not be `None`")  # noqa: E501

        self._auth_flow = auth_flow

    @property
    def ca_cert_data(self):
        """Gets the ca_cert_data of this UpdateSalesforceTarget.  # noqa: E501

        Base64 encoded PEM cert to use when uploading a new key to Salesforce  # noqa: E501

        :return: The ca_cert_data of this UpdateSalesforceTarget.  # noqa: E501
        :rtype: str
        """
        return self._ca_cert_data

    @ca_cert_data.setter
    def ca_cert_data(self, ca_cert_data):
        """Sets the ca_cert_data of this UpdateSalesforceTarget.

        Base64 encoded PEM cert to use when uploading a new key to Salesforce  # noqa: E501

        :param ca_cert_data: The ca_cert_data of this UpdateSalesforceTarget.  # noqa: E501
        :type: str
        """

        self._ca_cert_data = ca_cert_data

    @property
    def ca_cert_name(self):
        """Gets the ca_cert_name of this UpdateSalesforceTarget.  # noqa: E501

        name of the certificate in Salesforce tenant to use when uploading new key  # noqa: E501

        :return: The ca_cert_name of this UpdateSalesforceTarget.  # noqa: E501
        :rtype: str
        """
        return self._ca_cert_name

    @ca_cert_name.setter
    def ca_cert_name(self, ca_cert_name):
        """Sets the ca_cert_name of this UpdateSalesforceTarget.

        name of the certificate in Salesforce tenant to use when uploading new key  # noqa: E501

        :param ca_cert_name: The ca_cert_name of this UpdateSalesforceTarget.  # noqa: E501
        :type: str
        """

        self._ca_cert_name = ca_cert_name

    @property
    def client_id(self):
        """Gets the client_id of this UpdateSalesforceTarget.  # noqa: E501

        Client ID of the oauth2 app to use for connecting to Salesforce  # noqa: E501

        :return: The client_id of this UpdateSalesforceTarget.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this UpdateSalesforceTarget.

        Client ID of the oauth2 app to use for connecting to Salesforce  # noqa: E501

        :param client_id: The client_id of this UpdateSalesforceTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and client_id is None:  # noqa: E501
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def client_secret(self):
        """Gets the client_secret of this UpdateSalesforceTarget.  # noqa: E501

        Client secret of the oauth2 app to use for connecting to Salesforce (required for password flow)  # noqa: E501

        :return: The client_secret of this UpdateSalesforceTarget.  # noqa: E501
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this UpdateSalesforceTarget.

        Client secret of the oauth2 app to use for connecting to Salesforce (required for password flow)  # noqa: E501

        :param client_secret: The client_secret of this UpdateSalesforceTarget.  # noqa: E501
        :type: str
        """

        self._client_secret = client_secret

    @property
    def comment(self):
        """Gets the comment of this UpdateSalesforceTarget.  # noqa: E501

        Comment about the target  # noqa: E501

        :return: The comment of this UpdateSalesforceTarget.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this UpdateSalesforceTarget.

        Comment about the target  # noqa: E501

        :param comment: The comment of this UpdateSalesforceTarget.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def email(self):
        """Gets the email of this UpdateSalesforceTarget.  # noqa: E501

        The email of the user attached to the oauth2 app used for connecting to Salesforce  # noqa: E501

        :return: The email of this UpdateSalesforceTarget.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UpdateSalesforceTarget.

        The email of the user attached to the oauth2 app used for connecting to Salesforce  # noqa: E501

        :param email: The email of this UpdateSalesforceTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def keep_prev_version(self):
        """Gets the keep_prev_version of this UpdateSalesforceTarget.  # noqa: E501


        :return: The keep_prev_version of this UpdateSalesforceTarget.  # noqa: E501
        :rtype: str
        """
        return self._keep_prev_version

    @keep_prev_version.setter
    def keep_prev_version(self, keep_prev_version):
        """Sets the keep_prev_version of this UpdateSalesforceTarget.


        :param keep_prev_version: The keep_prev_version of this UpdateSalesforceTarget.  # noqa: E501
        :type: str
        """

        self._keep_prev_version = keep_prev_version

    @property
    def key(self):
        """Gets the key of this UpdateSalesforceTarget.  # noqa: E501

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :return: The key of this UpdateSalesforceTarget.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this UpdateSalesforceTarget.

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :param key: The key of this UpdateSalesforceTarget.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this UpdateSalesforceTarget.  # noqa: E501

        Target name  # noqa: E501

        :return: The name of this UpdateSalesforceTarget.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateSalesforceTarget.

        Target name  # noqa: E501

        :param name: The name of this UpdateSalesforceTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def new_name(self):
        """Gets the new_name of this UpdateSalesforceTarget.  # noqa: E501

        New target name  # noqa: E501

        :return: The new_name of this UpdateSalesforceTarget.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this UpdateSalesforceTarget.

        New target name  # noqa: E501

        :param new_name: The new_name of this UpdateSalesforceTarget.  # noqa: E501
        :type: str
        """

        self._new_name = new_name

    @property
    def password(self):
        """Gets the password of this UpdateSalesforceTarget.  # noqa: E501

        The password of the user attached to the oauth2 app used for connecting to Salesforce (required for user-password flow)  # noqa: E501

        :return: The password of this UpdateSalesforceTarget.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UpdateSalesforceTarget.

        The password of the user attached to the oauth2 app used for connecting to Salesforce (required for user-password flow)  # noqa: E501

        :param password: The password of this UpdateSalesforceTarget.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def security_token(self):
        """Gets the security_token of this UpdateSalesforceTarget.  # noqa: E501

        The security token of the user attached to the oauth2 app used for connecting to Salesforce  (required for user-password flow)  # noqa: E501

        :return: The security_token of this UpdateSalesforceTarget.  # noqa: E501
        :rtype: str
        """
        return self._security_token

    @security_token.setter
    def security_token(self, security_token):
        """Sets the security_token of this UpdateSalesforceTarget.

        The security token of the user attached to the oauth2 app used for connecting to Salesforce  (required for user-password flow)  # noqa: E501

        :param security_token: The security_token of this UpdateSalesforceTarget.  # noqa: E501
        :type: str
        """

        self._security_token = security_token

    @property
    def tenant_url(self):
        """Gets the tenant_url of this UpdateSalesforceTarget.  # noqa: E501

        Url of the Salesforce tenant  # noqa: E501

        :return: The tenant_url of this UpdateSalesforceTarget.  # noqa: E501
        :rtype: str
        """
        return self._tenant_url

    @tenant_url.setter
    def tenant_url(self, tenant_url):
        """Sets the tenant_url of this UpdateSalesforceTarget.

        Url of the Salesforce tenant  # noqa: E501

        :param tenant_url: The tenant_url of this UpdateSalesforceTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and tenant_url is None:  # noqa: E501
            raise ValueError("Invalid value for `tenant_url`, must not be `None`")  # noqa: E501

        self._tenant_url = tenant_url

    @property
    def token(self):
        """Gets the token of this UpdateSalesforceTarget.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this UpdateSalesforceTarget.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this UpdateSalesforceTarget.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this UpdateSalesforceTarget.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this UpdateSalesforceTarget.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this UpdateSalesforceTarget.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this UpdateSalesforceTarget.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this UpdateSalesforceTarget.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def update_version(self):
        """Gets the update_version of this UpdateSalesforceTarget.  # noqa: E501

        Deprecated  # noqa: E501

        :return: The update_version of this UpdateSalesforceTarget.  # noqa: E501
        :rtype: bool
        """
        return self._update_version

    @update_version.setter
    def update_version(self, update_version):
        """Sets the update_version of this UpdateSalesforceTarget.

        Deprecated  # noqa: E501

        :param update_version: The update_version of this UpdateSalesforceTarget.  # noqa: E501
        :type: bool
        """

        self._update_version = update_version

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
        if not isinstance(other, UpdateSalesforceTarget):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateSalesforceTarget):
            return True

        return self.to_dict() != other.to_dict()
