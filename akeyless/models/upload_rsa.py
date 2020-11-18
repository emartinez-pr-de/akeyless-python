# coding: utf-8

"""
    Akeyless API

    The purpose of this application is to provide access to Akeyless API.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: support@akeyless.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from akeyless.configuration import Configuration


class UploadRSA(object):
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
        'alg': 'str',
        'cert': 'str',
        'cert_file_data': 'str',
        'customer_frg_id': 'str',
        'metadata': 'str',
        'name': 'str',
        'rsa_file_data': 'str',
        'rsa_key_file_path': 'str',
        'split_level': 'int',
        'tag': 'list[str]',
        'token': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'alg': 'alg',
        'cert': 'cert',
        'cert_file_data': 'cert-file-data',
        'customer_frg_id': 'customer-frg-id',
        'metadata': 'metadata',
        'name': 'name',
        'rsa_file_data': 'rsa-file-data',
        'rsa_key_file_path': 'rsa-key-file-path',
        'split_level': 'split-level',
        'tag': 'tag',
        'token': 'token',
        'uid_token': 'uid-token'
    }

    def __init__(self, alg=None, cert=None, cert_file_data=None, customer_frg_id=None, metadata=None, name=None, rsa_file_data=None, rsa_key_file_path=None, split_level=2, tag=None, token=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """UploadRSA - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._alg = None
        self._cert = None
        self._cert_file_data = None
        self._customer_frg_id = None
        self._metadata = None
        self._name = None
        self._rsa_file_data = None
        self._rsa_key_file_path = None
        self._split_level = None
        self._tag = None
        self._token = None
        self._uid_token = None
        self.discriminator = None

        self.alg = alg
        if cert is not None:
            self.cert = cert
        if cert_file_data is not None:
            self.cert_file_data = cert_file_data
        if customer_frg_id is not None:
            self.customer_frg_id = customer_frg_id
        if metadata is not None:
            self.metadata = metadata
        self.name = name
        if rsa_file_data is not None:
            self.rsa_file_data = rsa_file_data
        if rsa_key_file_path is not None:
            self.rsa_key_file_path = rsa_key_file_path
        if split_level is not None:
            self.split_level = split_level
        if tag is not None:
            self.tag = tag
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def alg(self):
        """Gets the alg of this UploadRSA.  # noqa: E501

        Key type. options: [RSA1024, RSA2048]  # noqa: E501

        :return: The alg of this UploadRSA.  # noqa: E501
        :rtype: str
        """
        return self._alg

    @alg.setter
    def alg(self, alg):
        """Sets the alg of this UploadRSA.

        Key type. options: [RSA1024, RSA2048]  # noqa: E501

        :param alg: The alg of this UploadRSA.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and alg is None:  # noqa: E501
            raise ValueError("Invalid value for `alg`, must not be `None`")  # noqa: E501

        self._alg = alg

    @property
    def cert(self):
        """Gets the cert of this UploadRSA.  # noqa: E501

        Path to a file that contain the certificate in a PEM format.  # noqa: E501

        :return: The cert of this UploadRSA.  # noqa: E501
        :rtype: str
        """
        return self._cert

    @cert.setter
    def cert(self, cert):
        """Sets the cert of this UploadRSA.

        Path to a file that contain the certificate in a PEM format.  # noqa: E501

        :param cert: The cert of this UploadRSA.  # noqa: E501
        :type: str
        """

        self._cert = cert

    @property
    def cert_file_data(self):
        """Gets the cert_file_data of this UploadRSA.  # noqa: E501

        Certificate in a PEM format.  # noqa: E501

        :return: The cert_file_data of this UploadRSA.  # noqa: E501
        :rtype: str
        """
        return self._cert_file_data

    @cert_file_data.setter
    def cert_file_data(self, cert_file_data):
        """Sets the cert_file_data of this UploadRSA.

        Certificate in a PEM format.  # noqa: E501

        :param cert_file_data: The cert_file_data of this UploadRSA.  # noqa: E501
        :type: str
        """

        self._cert_file_data = cert_file_data

    @property
    def customer_frg_id(self):
        """Gets the customer_frg_id of this UploadRSA.  # noqa: E501

        The customer fragment ID that will be used to split the key (if empty, the key will be created independently of a customer fragment)  # noqa: E501

        :return: The customer_frg_id of this UploadRSA.  # noqa: E501
        :rtype: str
        """
        return self._customer_frg_id

    @customer_frg_id.setter
    def customer_frg_id(self, customer_frg_id):
        """Sets the customer_frg_id of this UploadRSA.

        The customer fragment ID that will be used to split the key (if empty, the key will be created independently of a customer fragment)  # noqa: E501

        :param customer_frg_id: The customer_frg_id of this UploadRSA.  # noqa: E501
        :type: str
        """

        self._customer_frg_id = customer_frg_id

    @property
    def metadata(self):
        """Gets the metadata of this UploadRSA.  # noqa: E501

        A metadata about the key  # noqa: E501

        :return: The metadata of this UploadRSA.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this UploadRSA.

        A metadata about the key  # noqa: E501

        :param metadata: The metadata of this UploadRSA.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this UploadRSA.  # noqa: E501

        Name of key to be created  # noqa: E501

        :return: The name of this UploadRSA.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UploadRSA.

        Name of key to be created  # noqa: E501

        :param name: The name of this UploadRSA.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def rsa_file_data(self):
        """Gets the rsa_file_data of this UploadRSA.  # noqa: E501

        RSA private key data, base64 encoded  # noqa: E501

        :return: The rsa_file_data of this UploadRSA.  # noqa: E501
        :rtype: str
        """
        return self._rsa_file_data

    @rsa_file_data.setter
    def rsa_file_data(self, rsa_file_data):
        """Sets the rsa_file_data of this UploadRSA.

        RSA private key data, base64 encoded  # noqa: E501

        :param rsa_file_data: The rsa_file_data of this UploadRSA.  # noqa: E501
        :type: str
        """

        self._rsa_file_data = rsa_file_data

    @property
    def rsa_key_file_path(self):
        """Gets the rsa_key_file_path of this UploadRSA.  # noqa: E501

        RSA private key file path  # noqa: E501

        :return: The rsa_key_file_path of this UploadRSA.  # noqa: E501
        :rtype: str
        """
        return self._rsa_key_file_path

    @rsa_key_file_path.setter
    def rsa_key_file_path(self, rsa_key_file_path):
        """Sets the rsa_key_file_path of this UploadRSA.

        RSA private key file path  # noqa: E501

        :param rsa_key_file_path: The rsa_key_file_path of this UploadRSA.  # noqa: E501
        :type: str
        """

        self._rsa_key_file_path = rsa_key_file_path

    @property
    def split_level(self):
        """Gets the split_level of this UploadRSA.  # noqa: E501

        The number of fragments that the item will be split into  # noqa: E501

        :return: The split_level of this UploadRSA.  # noqa: E501
        :rtype: int
        """
        return self._split_level

    @split_level.setter
    def split_level(self, split_level):
        """Sets the split_level of this UploadRSA.

        The number of fragments that the item will be split into  # noqa: E501

        :param split_level: The split_level of this UploadRSA.  # noqa: E501
        :type: int
        """

        self._split_level = split_level

    @property
    def tag(self):
        """Gets the tag of this UploadRSA.  # noqa: E501

        List of the tags attached to this key  # noqa: E501

        :return: The tag of this UploadRSA.  # noqa: E501
        :rtype: list[str]
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this UploadRSA.

        List of the tags attached to this key  # noqa: E501

        :param tag: The tag of this UploadRSA.  # noqa: E501
        :type: list[str]
        """

        self._tag = tag

    @property
    def token(self):
        """Gets the token of this UploadRSA.  # noqa: E501

        Use a specific profile from your akeyless/profiles/ folder  # noqa: E501

        :return: The token of this UploadRSA.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this UploadRSA.

        Use a specific profile from your akeyless/profiles/ folder  # noqa: E501

        :param token: The token of this UploadRSA.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this UploadRSA.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this UploadRSA.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this UploadRSA.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this UploadRSA.  # noqa: E501
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
        if not isinstance(other, UploadRSA):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UploadRSA):
            return True

        return self.to_dict() != other.to_dict()
