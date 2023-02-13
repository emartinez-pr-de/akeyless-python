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


class Auth(object):
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
        'access_id': 'str',
        'access_key': 'str',
        'access_type': 'str',
        'admin_email': 'str',
        'admin_password': 'str',
        'cert_data': 'str',
        'cloud_id': 'str',
        'debug': 'bool',
        'gateway_url': 'str',
        'gcp_audience': 'str',
        'json': 'bool',
        'jwt': 'str',
        'k8s_auth_config_name': 'str',
        'k8s_service_account_token': 'str',
        'key_data': 'str',
        'ldap_password': 'str',
        'ldap_username': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'access_id': 'access-id',
        'access_key': 'access-key',
        'access_type': 'access-type',
        'admin_email': 'admin-email',
        'admin_password': 'admin-password',
        'cert_data': 'cert-data',
        'cloud_id': 'cloud-id',
        'debug': 'debug',
        'gateway_url': 'gateway-url',
        'gcp_audience': 'gcp-audience',
        'json': 'json',
        'jwt': 'jwt',
        'k8s_auth_config_name': 'k8s-auth-config-name',
        'k8s_service_account_token': 'k8s-service-account-token',
        'key_data': 'key-data',
        'ldap_password': 'ldap_password',
        'ldap_username': 'ldap_username',
        'uid_token': 'uid_token'
    }

    def __init__(self, access_id=None, access_key=None, access_type='access_key', admin_email=None, admin_password=None, cert_data=None, cloud_id=None, debug=None, gateway_url=None, gcp_audience='akeyless.io', json=False, jwt=None, k8s_auth_config_name=None, k8s_service_account_token=None, key_data=None, ldap_password=None, ldap_username=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """Auth - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_id = None
        self._access_key = None
        self._access_type = None
        self._admin_email = None
        self._admin_password = None
        self._cert_data = None
        self._cloud_id = None
        self._debug = None
        self._gateway_url = None
        self._gcp_audience = None
        self._json = None
        self._jwt = None
        self._k8s_auth_config_name = None
        self._k8s_service_account_token = None
        self._key_data = None
        self._ldap_password = None
        self._ldap_username = None
        self._uid_token = None
        self.discriminator = None

        if access_id is not None:
            self.access_id = access_id
        if access_key is not None:
            self.access_key = access_key
        if access_type is not None:
            self.access_type = access_type
        if admin_email is not None:
            self.admin_email = admin_email
        if admin_password is not None:
            self.admin_password = admin_password
        if cert_data is not None:
            self.cert_data = cert_data
        if cloud_id is not None:
            self.cloud_id = cloud_id
        if debug is not None:
            self.debug = debug
        if gateway_url is not None:
            self.gateway_url = gateway_url
        if gcp_audience is not None:
            self.gcp_audience = gcp_audience
        if json is not None:
            self.json = json
        if jwt is not None:
            self.jwt = jwt
        if k8s_auth_config_name is not None:
            self.k8s_auth_config_name = k8s_auth_config_name
        if k8s_service_account_token is not None:
            self.k8s_service_account_token = k8s_service_account_token
        if key_data is not None:
            self.key_data = key_data
        if ldap_password is not None:
            self.ldap_password = ldap_password
        if ldap_username is not None:
            self.ldap_username = ldap_username
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def access_id(self):
        """Gets the access_id of this Auth.  # noqa: E501

        Access ID  # noqa: E501

        :return: The access_id of this Auth.  # noqa: E501
        :rtype: str
        """
        return self._access_id

    @access_id.setter
    def access_id(self, access_id):
        """Sets the access_id of this Auth.

        Access ID  # noqa: E501

        :param access_id: The access_id of this Auth.  # noqa: E501
        :type: str
        """

        self._access_id = access_id

    @property
    def access_key(self):
        """Gets the access_key of this Auth.  # noqa: E501

        Access key (relevant only for access-type=access_key)  # noqa: E501

        :return: The access_key of this Auth.  # noqa: E501
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this Auth.

        Access key (relevant only for access-type=access_key)  # noqa: E501

        :param access_key: The access_key of this Auth.  # noqa: E501
        :type: str
        """

        self._access_key = access_key

    @property
    def access_type(self):
        """Gets the access_type of this Auth.  # noqa: E501

        Access Type (access_key/password/saml/ldap/k8s/azure_ad/oidc/aws_iam/universal_identity/jwt/gcp/cert)  # noqa: E501

        :return: The access_type of this Auth.  # noqa: E501
        :rtype: str
        """
        return self._access_type

    @access_type.setter
    def access_type(self, access_type):
        """Sets the access_type of this Auth.

        Access Type (access_key/password/saml/ldap/k8s/azure_ad/oidc/aws_iam/universal_identity/jwt/gcp/cert)  # noqa: E501

        :param access_type: The access_type of this Auth.  # noqa: E501
        :type: str
        """

        self._access_type = access_type

    @property
    def admin_email(self):
        """Gets the admin_email of this Auth.  # noqa: E501

        Email (relevant only for access-type=password)  # noqa: E501

        :return: The admin_email of this Auth.  # noqa: E501
        :rtype: str
        """
        return self._admin_email

    @admin_email.setter
    def admin_email(self, admin_email):
        """Sets the admin_email of this Auth.

        Email (relevant only for access-type=password)  # noqa: E501

        :param admin_email: The admin_email of this Auth.  # noqa: E501
        :type: str
        """

        self._admin_email = admin_email

    @property
    def admin_password(self):
        """Gets the admin_password of this Auth.  # noqa: E501

        Password (relevant only for access-type=password)  # noqa: E501

        :return: The admin_password of this Auth.  # noqa: E501
        :rtype: str
        """
        return self._admin_password

    @admin_password.setter
    def admin_password(self, admin_password):
        """Sets the admin_password of this Auth.

        Password (relevant only for access-type=password)  # noqa: E501

        :param admin_password: The admin_password of this Auth.  # noqa: E501
        :type: str
        """

        self._admin_password = admin_password

    @property
    def cert_data(self):
        """Gets the cert_data of this Auth.  # noqa: E501

        Certificate data encoded in base64. Used if file was not provided. (relevant only for access-type=cert)  # noqa: E501

        :return: The cert_data of this Auth.  # noqa: E501
        :rtype: str
        """
        return self._cert_data

    @cert_data.setter
    def cert_data(self, cert_data):
        """Sets the cert_data of this Auth.

        Certificate data encoded in base64. Used if file was not provided. (relevant only for access-type=cert)  # noqa: E501

        :param cert_data: The cert_data of this Auth.  # noqa: E501
        :type: str
        """

        self._cert_data = cert_data

    @property
    def cloud_id(self):
        """Gets the cloud_id of this Auth.  # noqa: E501

        The cloud identity (relevant only for access-type=azure_ad,aws_iam,gcp)  # noqa: E501

        :return: The cloud_id of this Auth.  # noqa: E501
        :rtype: str
        """
        return self._cloud_id

    @cloud_id.setter
    def cloud_id(self, cloud_id):
        """Sets the cloud_id of this Auth.

        The cloud identity (relevant only for access-type=azure_ad,aws_iam,gcp)  # noqa: E501

        :param cloud_id: The cloud_id of this Auth.  # noqa: E501
        :type: str
        """

        self._cloud_id = cloud_id

    @property
    def debug(self):
        """Gets the debug of this Auth.  # noqa: E501


        :return: The debug of this Auth.  # noqa: E501
        :rtype: bool
        """
        return self._debug

    @debug.setter
    def debug(self, debug):
        """Sets the debug of this Auth.


        :param debug: The debug of this Auth.  # noqa: E501
        :type: bool
        """

        self._debug = debug

    @property
    def gateway_url(self):
        """Gets the gateway_url of this Auth.  # noqa: E501

        Gateway URL for the K8S authenticated (relevant only for access-type=k8s)  # noqa: E501

        :return: The gateway_url of this Auth.  # noqa: E501
        :rtype: str
        """
        return self._gateway_url

    @gateway_url.setter
    def gateway_url(self, gateway_url):
        """Sets the gateway_url of this Auth.

        Gateway URL for the K8S authenticated (relevant only for access-type=k8s)  # noqa: E501

        :param gateway_url: The gateway_url of this Auth.  # noqa: E501
        :type: str
        """

        self._gateway_url = gateway_url

    @property
    def gcp_audience(self):
        """Gets the gcp_audience of this Auth.  # noqa: E501

        GCP JWT audience  # noqa: E501

        :return: The gcp_audience of this Auth.  # noqa: E501
        :rtype: str
        """
        return self._gcp_audience

    @gcp_audience.setter
    def gcp_audience(self, gcp_audience):
        """Sets the gcp_audience of this Auth.

        GCP JWT audience  # noqa: E501

        :param gcp_audience: The gcp_audience of this Auth.  # noqa: E501
        :type: str
        """

        self._gcp_audience = gcp_audience

    @property
    def json(self):
        """Gets the json of this Auth.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this Auth.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this Auth.

        Set output format to JSON  # noqa: E501

        :param json: The json of this Auth.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def jwt(self):
        """Gets the jwt of this Auth.  # noqa: E501

        The Json Web Token (relevant only for access-type=jwt/oidc)  # noqa: E501

        :return: The jwt of this Auth.  # noqa: E501
        :rtype: str
        """
        return self._jwt

    @jwt.setter
    def jwt(self, jwt):
        """Sets the jwt of this Auth.

        The Json Web Token (relevant only for access-type=jwt/oidc)  # noqa: E501

        :param jwt: The jwt of this Auth.  # noqa: E501
        :type: str
        """

        self._jwt = jwt

    @property
    def k8s_auth_config_name(self):
        """Gets the k8s_auth_config_name of this Auth.  # noqa: E501

        The K8S Auth config name (relevant only for access-type=k8s)  # noqa: E501

        :return: The k8s_auth_config_name of this Auth.  # noqa: E501
        :rtype: str
        """
        return self._k8s_auth_config_name

    @k8s_auth_config_name.setter
    def k8s_auth_config_name(self, k8s_auth_config_name):
        """Sets the k8s_auth_config_name of this Auth.

        The K8S Auth config name (relevant only for access-type=k8s)  # noqa: E501

        :param k8s_auth_config_name: The k8s_auth_config_name of this Auth.  # noqa: E501
        :type: str
        """

        self._k8s_auth_config_name = k8s_auth_config_name

    @property
    def k8s_service_account_token(self):
        """Gets the k8s_service_account_token of this Auth.  # noqa: E501

        The K8S service account token. (relevant only for access-type=k8s)  # noqa: E501

        :return: The k8s_service_account_token of this Auth.  # noqa: E501
        :rtype: str
        """
        return self._k8s_service_account_token

    @k8s_service_account_token.setter
    def k8s_service_account_token(self, k8s_service_account_token):
        """Sets the k8s_service_account_token of this Auth.

        The K8S service account token. (relevant only for access-type=k8s)  # noqa: E501

        :param k8s_service_account_token: The k8s_service_account_token of this Auth.  # noqa: E501
        :type: str
        """

        self._k8s_service_account_token = k8s_service_account_token

    @property
    def key_data(self):
        """Gets the key_data of this Auth.  # noqa: E501

        Private key data encoded in base64. Used if file was not provided.(relevant only for access-type=cert)  # noqa: E501

        :return: The key_data of this Auth.  # noqa: E501
        :rtype: str
        """
        return self._key_data

    @key_data.setter
    def key_data(self, key_data):
        """Sets the key_data of this Auth.

        Private key data encoded in base64. Used if file was not provided.(relevant only for access-type=cert)  # noqa: E501

        :param key_data: The key_data of this Auth.  # noqa: E501
        :type: str
        """

        self._key_data = key_data

    @property
    def ldap_password(self):
        """Gets the ldap_password of this Auth.  # noqa: E501

        LDAP password (relevant only for access-type=ldap)  # noqa: E501

        :return: The ldap_password of this Auth.  # noqa: E501
        :rtype: str
        """
        return self._ldap_password

    @ldap_password.setter
    def ldap_password(self, ldap_password):
        """Sets the ldap_password of this Auth.

        LDAP password (relevant only for access-type=ldap)  # noqa: E501

        :param ldap_password: The ldap_password of this Auth.  # noqa: E501
        :type: str
        """

        self._ldap_password = ldap_password

    @property
    def ldap_username(self):
        """Gets the ldap_username of this Auth.  # noqa: E501

        LDAP username (relevant only for access-type=ldap)  # noqa: E501

        :return: The ldap_username of this Auth.  # noqa: E501
        :rtype: str
        """
        return self._ldap_username

    @ldap_username.setter
    def ldap_username(self, ldap_username):
        """Sets the ldap_username of this Auth.

        LDAP username (relevant only for access-type=ldap)  # noqa: E501

        :param ldap_username: The ldap_username of this Auth.  # noqa: E501
        :type: str
        """

        self._ldap_username = ldap_username

    @property
    def uid_token(self):
        """Gets the uid_token of this Auth.  # noqa: E501

        The universal_identity token (relevant only for access-type=universal_identity)  # noqa: E501

        :return: The uid_token of this Auth.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this Auth.

        The universal_identity token (relevant only for access-type=universal_identity)  # noqa: E501

        :param uid_token: The uid_token of this Auth.  # noqa: E501
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
        if not isinstance(other, Auth):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Auth):
            return True

        return self.to_dict() != other.to_dict()
