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


class SalesforceTargetDetails(object):
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
        'app_private_key': 'list[int]',
        'auth_flow': 'str',
        'ca_cert_data': 'list[int]',
        'ca_cert_name': 'str',
        'client_id': 'str',
        'client_secret': 'str',
        'password': 'str',
        'security_token': 'str',
        'tenant_url': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'app_private_key': 'app_private_key',
        'auth_flow': 'auth_flow',
        'ca_cert_data': 'ca_cert_data',
        'ca_cert_name': 'ca_cert_name',
        'client_id': 'client_id',
        'client_secret': 'client_secret',
        'password': 'password',
        'security_token': 'security_token',
        'tenant_url': 'tenant_url',
        'user_name': 'user_name'
    }

    def __init__(self, app_private_key=None, auth_flow=None, ca_cert_data=None, ca_cert_name=None, client_id=None, client_secret=None, password=None, security_token=None, tenant_url=None, user_name=None, local_vars_configuration=None):  # noqa: E501
        """SalesforceTargetDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._app_private_key = None
        self._auth_flow = None
        self._ca_cert_data = None
        self._ca_cert_name = None
        self._client_id = None
        self._client_secret = None
        self._password = None
        self._security_token = None
        self._tenant_url = None
        self._user_name = None
        self.discriminator = None

        if app_private_key is not None:
            self.app_private_key = app_private_key
        if auth_flow is not None:
            self.auth_flow = auth_flow
        if ca_cert_data is not None:
            self.ca_cert_data = ca_cert_data
        if ca_cert_name is not None:
            self.ca_cert_name = ca_cert_name
        if client_id is not None:
            self.client_id = client_id
        if client_secret is not None:
            self.client_secret = client_secret
        if password is not None:
            self.password = password
        if security_token is not None:
            self.security_token = security_token
        if tenant_url is not None:
            self.tenant_url = tenant_url
        if user_name is not None:
            self.user_name = user_name

    @property
    def app_private_key(self):
        """Gets the app_private_key of this SalesforceTargetDetails.  # noqa: E501

        params needed for jwt auth AppPrivateKey is the rsa private key in PEM format  # noqa: E501

        :return: The app_private_key of this SalesforceTargetDetails.  # noqa: E501
        :rtype: list[int]
        """
        return self._app_private_key

    @app_private_key.setter
    def app_private_key(self, app_private_key):
        """Sets the app_private_key of this SalesforceTargetDetails.

        params needed for jwt auth AppPrivateKey is the rsa private key in PEM format  # noqa: E501

        :param app_private_key: The app_private_key of this SalesforceTargetDetails.  # noqa: E501
        :type: list[int]
        """

        self._app_private_key = app_private_key

    @property
    def auth_flow(self):
        """Gets the auth_flow of this SalesforceTargetDetails.  # noqa: E501


        :return: The auth_flow of this SalesforceTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._auth_flow

    @auth_flow.setter
    def auth_flow(self, auth_flow):
        """Sets the auth_flow of this SalesforceTargetDetails.


        :param auth_flow: The auth_flow of this SalesforceTargetDetails.  # noqa: E501
        :type: str
        """

        self._auth_flow = auth_flow

    @property
    def ca_cert_data(self):
        """Gets the ca_cert_data of this SalesforceTargetDetails.  # noqa: E501

        CACertData is the rsa 4096 certificate data in PEM format  # noqa: E501

        :return: The ca_cert_data of this SalesforceTargetDetails.  # noqa: E501
        :rtype: list[int]
        """
        return self._ca_cert_data

    @ca_cert_data.setter
    def ca_cert_data(self, ca_cert_data):
        """Sets the ca_cert_data of this SalesforceTargetDetails.

        CACertData is the rsa 4096 certificate data in PEM format  # noqa: E501

        :param ca_cert_data: The ca_cert_data of this SalesforceTargetDetails.  # noqa: E501
        :type: list[int]
        """

        self._ca_cert_data = ca_cert_data

    @property
    def ca_cert_name(self):
        """Gets the ca_cert_name of this SalesforceTargetDetails.  # noqa: E501

        CACertName is the name of the certificate in SalesForce tenant  # noqa: E501

        :return: The ca_cert_name of this SalesforceTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._ca_cert_name

    @ca_cert_name.setter
    def ca_cert_name(self, ca_cert_name):
        """Sets the ca_cert_name of this SalesforceTargetDetails.

        CACertName is the name of the certificate in SalesForce tenant  # noqa: E501

        :param ca_cert_name: The ca_cert_name of this SalesforceTargetDetails.  # noqa: E501
        :type: str
        """

        self._ca_cert_name = ca_cert_name

    @property
    def client_id(self):
        """Gets the client_id of this SalesforceTargetDetails.  # noqa: E501


        :return: The client_id of this SalesforceTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this SalesforceTargetDetails.


        :param client_id: The client_id of this SalesforceTargetDetails.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def client_secret(self):
        """Gets the client_secret of this SalesforceTargetDetails.  # noqa: E501

        params needed for password auth  # noqa: E501

        :return: The client_secret of this SalesforceTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this SalesforceTargetDetails.

        params needed for password auth  # noqa: E501

        :param client_secret: The client_secret of this SalesforceTargetDetails.  # noqa: E501
        :type: str
        """

        self._client_secret = client_secret

    @property
    def password(self):
        """Gets the password of this SalesforceTargetDetails.  # noqa: E501


        :return: The password of this SalesforceTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this SalesforceTargetDetails.


        :param password: The password of this SalesforceTargetDetails.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def security_token(self):
        """Gets the security_token of this SalesforceTargetDetails.  # noqa: E501


        :return: The security_token of this SalesforceTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._security_token

    @security_token.setter
    def security_token(self, security_token):
        """Sets the security_token of this SalesforceTargetDetails.


        :param security_token: The security_token of this SalesforceTargetDetails.  # noqa: E501
        :type: str
        """

        self._security_token = security_token

    @property
    def tenant_url(self):
        """Gets the tenant_url of this SalesforceTargetDetails.  # noqa: E501


        :return: The tenant_url of this SalesforceTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._tenant_url

    @tenant_url.setter
    def tenant_url(self, tenant_url):
        """Sets the tenant_url of this SalesforceTargetDetails.


        :param tenant_url: The tenant_url of this SalesforceTargetDetails.  # noqa: E501
        :type: str
        """

        self._tenant_url = tenant_url

    @property
    def user_name(self):
        """Gets the user_name of this SalesforceTargetDetails.  # noqa: E501


        :return: The user_name of this SalesforceTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this SalesforceTargetDetails.


        :param user_name: The user_name of this SalesforceTargetDetails.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

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
        if not isinstance(other, SalesforceTargetDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SalesforceTargetDetails):
            return True

        return self.to_dict() != other.to_dict()
