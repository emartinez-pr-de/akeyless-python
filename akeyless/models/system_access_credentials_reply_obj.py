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


class SystemAccessCredentialsReplyObj(object):
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
        'auth_creds': 'str',
        'expiry': 'int',
        'kfm_creds': 'str',
        'required_mfa': 'str',
        'token': 'str',
        'uam_creds': 'str'
    }

    attribute_map = {
        'auth_creds': 'auth_creds',
        'expiry': 'expiry',
        'kfm_creds': 'kfm_creds',
        'required_mfa': 'required_mfa',
        'token': 'token',
        'uam_creds': 'uam_creds'
    }

    def __init__(self, auth_creds=None, expiry=None, kfm_creds=None, required_mfa=None, token=None, uam_creds=None, local_vars_configuration=None):  # noqa: E501
        """SystemAccessCredentialsReplyObj - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._auth_creds = None
        self._expiry = None
        self._kfm_creds = None
        self._required_mfa = None
        self._token = None
        self._uam_creds = None
        self.discriminator = None

        if auth_creds is not None:
            self.auth_creds = auth_creds
        if expiry is not None:
            self.expiry = expiry
        if kfm_creds is not None:
            self.kfm_creds = kfm_creds
        if required_mfa is not None:
            self.required_mfa = required_mfa
        if token is not None:
            self.token = token
        if uam_creds is not None:
            self.uam_creds = uam_creds

    @property
    def auth_creds(self):
        """Gets the auth_creds of this SystemAccessCredentialsReplyObj.  # noqa: E501

        Temporary credentials for accessing Auth  # noqa: E501

        :return: The auth_creds of this SystemAccessCredentialsReplyObj.  # noqa: E501
        :rtype: str
        """
        return self._auth_creds

    @auth_creds.setter
    def auth_creds(self, auth_creds):
        """Sets the auth_creds of this SystemAccessCredentialsReplyObj.

        Temporary credentials for accessing Auth  # noqa: E501

        :param auth_creds: The auth_creds of this SystemAccessCredentialsReplyObj.  # noqa: E501
        :type: str
        """

        self._auth_creds = auth_creds

    @property
    def expiry(self):
        """Gets the expiry of this SystemAccessCredentialsReplyObj.  # noqa: E501

        Credentials expiration date  # noqa: E501

        :return: The expiry of this SystemAccessCredentialsReplyObj.  # noqa: E501
        :rtype: int
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """Sets the expiry of this SystemAccessCredentialsReplyObj.

        Credentials expiration date  # noqa: E501

        :param expiry: The expiry of this SystemAccessCredentialsReplyObj.  # noqa: E501
        :type: int
        """

        self._expiry = expiry

    @property
    def kfm_creds(self):
        """Gets the kfm_creds of this SystemAccessCredentialsReplyObj.  # noqa: E501

        Temporary credentials for accessing the KFMs instances  # noqa: E501

        :return: The kfm_creds of this SystemAccessCredentialsReplyObj.  # noqa: E501
        :rtype: str
        """
        return self._kfm_creds

    @kfm_creds.setter
    def kfm_creds(self, kfm_creds):
        """Sets the kfm_creds of this SystemAccessCredentialsReplyObj.

        Temporary credentials for accessing the KFMs instances  # noqa: E501

        :param kfm_creds: The kfm_creds of this SystemAccessCredentialsReplyObj.  # noqa: E501
        :type: str
        """

        self._kfm_creds = kfm_creds

    @property
    def required_mfa(self):
        """Gets the required_mfa of this SystemAccessCredentialsReplyObj.  # noqa: E501


        :return: The required_mfa of this SystemAccessCredentialsReplyObj.  # noqa: E501
        :rtype: str
        """
        return self._required_mfa

    @required_mfa.setter
    def required_mfa(self, required_mfa):
        """Sets the required_mfa of this SystemAccessCredentialsReplyObj.


        :param required_mfa: The required_mfa of this SystemAccessCredentialsReplyObj.  # noqa: E501
        :type: str
        """

        self._required_mfa = required_mfa

    @property
    def token(self):
        """Gets the token of this SystemAccessCredentialsReplyObj.  # noqa: E501

        Credentials tmp token  # noqa: E501

        :return: The token of this SystemAccessCredentialsReplyObj.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this SystemAccessCredentialsReplyObj.

        Credentials tmp token  # noqa: E501

        :param token: The token of this SystemAccessCredentialsReplyObj.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uam_creds(self):
        """Gets the uam_creds of this SystemAccessCredentialsReplyObj.  # noqa: E501

        Temporary credentials for accessing the UAM service  # noqa: E501

        :return: The uam_creds of this SystemAccessCredentialsReplyObj.  # noqa: E501
        :rtype: str
        """
        return self._uam_creds

    @uam_creds.setter
    def uam_creds(self, uam_creds):
        """Sets the uam_creds of this SystemAccessCredentialsReplyObj.

        Temporary credentials for accessing the UAM service  # noqa: E501

        :param uam_creds: The uam_creds of this SystemAccessCredentialsReplyObj.  # noqa: E501
        :type: str
        """

        self._uam_creds = uam_creds

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
        if not isinstance(other, SystemAccessCredentialsReplyObj):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SystemAccessCredentialsReplyObj):
            return True

        return self.to_dict() != other.to_dict()
