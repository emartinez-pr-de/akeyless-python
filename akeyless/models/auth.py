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
        'cloud_id': 'str',
        'gcp_audience': 'str',
        'jwt': 'str',
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
        'cloud_id': 'cloud-id',
        'gcp_audience': 'gcp-audience',
        'jwt': 'jwt',
        'ldap_password': 'ldap_password',
        'ldap_username': 'ldap_username',
        'uid_token': 'uid_token'
    }

    def __init__(self, access_id=None, access_key=None, access_type='access_key', admin_email=None, admin_password=None, cloud_id=None, gcp_audience=None, jwt=None, ldap_password=None, ldap_username=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """Auth - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_id = None
        self._access_key = None
        self._access_type = None
        self._admin_email = None
        self._admin_password = None
        self._cloud_id = None
        self._gcp_audience = None
        self._jwt = None
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
        if cloud_id is not None:
            self.cloud_id = cloud_id
        if gcp_audience is not None:
            self.gcp_audience = gcp_audience
        if jwt is not None:
            self.jwt = jwt
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

        Access Type (access_key/password/saml/ldap/azure_ad/aws_iam/universal_identity/jwt/gcp)  # noqa: E501

        :return: The access_type of this Auth.  # noqa: E501
        :rtype: str
        """
        return self._access_type

    @access_type.setter
    def access_type(self, access_type):
        """Sets the access_type of this Auth.

        Access Type (access_key/password/saml/ldap/azure_ad/aws_iam/universal_identity/jwt/gcp)  # noqa: E501

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
