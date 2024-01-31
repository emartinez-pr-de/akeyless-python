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


class VerifyPKCS1(object):
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
        'display_id': 'str',
        'hash_function': 'str',
        'input_format': 'str',
        'item_id': 'int',
        'json': 'bool',
        'key_name': 'str',
        'message': 'str',
        'prehashed': 'bool',
        'signature': 'str',
        'token': 'str',
        'uid_token': 'str',
        'version': 'int'
    }

    attribute_map = {
        'display_id': 'display-id',
        'hash_function': 'hash-function',
        'input_format': 'input-format',
        'item_id': 'item-id',
        'json': 'json',
        'key_name': 'key-name',
        'message': 'message',
        'prehashed': 'prehashed',
        'signature': 'signature',
        'token': 'token',
        'uid_token': 'uid-token',
        'version': 'version'
    }

    def __init__(self, display_id=None, hash_function=None, input_format=None, item_id=None, json=False, key_name=None, message=None, prehashed=None, signature=None, token=None, uid_token=None, version=None, local_vars_configuration=None):  # noqa: E501
        """VerifyPKCS1 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._display_id = None
        self._hash_function = None
        self._input_format = None
        self._item_id = None
        self._json = None
        self._key_name = None
        self._message = None
        self._prehashed = None
        self._signature = None
        self._token = None
        self._uid_token = None
        self._version = None
        self.discriminator = None

        if display_id is not None:
            self.display_id = display_id
        if hash_function is not None:
            self.hash_function = hash_function
        if input_format is not None:
            self.input_format = input_format
        if item_id is not None:
            self.item_id = item_id
        if json is not None:
            self.json = json
        self.key_name = key_name
        self.message = message
        if prehashed is not None:
            self.prehashed = prehashed
        self.signature = signature
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if version is not None:
            self.version = version

    @property
    def display_id(self):
        """Gets the display_id of this VerifyPKCS1.  # noqa: E501

        The display id of the key to use in the verification process  # noqa: E501

        :return: The display_id of this VerifyPKCS1.  # noqa: E501
        :rtype: str
        """
        return self._display_id

    @display_id.setter
    def display_id(self, display_id):
        """Sets the display_id of this VerifyPKCS1.

        The display id of the key to use in the verification process  # noqa: E501

        :param display_id: The display_id of this VerifyPKCS1.  # noqa: E501
        :type: str
        """

        self._display_id = display_id

    @property
    def hash_function(self):
        """Gets the hash_function of this VerifyPKCS1.  # noqa: E501

        HashFunction defines the hash function (e.g. sha-256)  # noqa: E501

        :return: The hash_function of this VerifyPKCS1.  # noqa: E501
        :rtype: str
        """
        return self._hash_function

    @hash_function.setter
    def hash_function(self, hash_function):
        """Sets the hash_function of this VerifyPKCS1.

        HashFunction defines the hash function (e.g. sha-256)  # noqa: E501

        :param hash_function: The hash_function of this VerifyPKCS1.  # noqa: E501
        :type: str
        """

        self._hash_function = hash_function

    @property
    def input_format(self):
        """Gets the input_format of this VerifyPKCS1.  # noqa: E501

        Select default assumed format for the plaintext message. Currently supported options: [base64]  # noqa: E501

        :return: The input_format of this VerifyPKCS1.  # noqa: E501
        :rtype: str
        """
        return self._input_format

    @input_format.setter
    def input_format(self, input_format):
        """Sets the input_format of this VerifyPKCS1.

        Select default assumed format for the plaintext message. Currently supported options: [base64]  # noqa: E501

        :param input_format: The input_format of this VerifyPKCS1.  # noqa: E501
        :type: str
        """

        self._input_format = input_format

    @property
    def item_id(self):
        """Gets the item_id of this VerifyPKCS1.  # noqa: E501

        The item id of the key to use in the verification process  # noqa: E501

        :return: The item_id of this VerifyPKCS1.  # noqa: E501
        :rtype: int
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this VerifyPKCS1.

        The item id of the key to use in the verification process  # noqa: E501

        :param item_id: The item_id of this VerifyPKCS1.  # noqa: E501
        :type: int
        """

        self._item_id = item_id

    @property
    def json(self):
        """Gets the json of this VerifyPKCS1.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this VerifyPKCS1.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this VerifyPKCS1.

        Set output format to JSON  # noqa: E501

        :param json: The json of this VerifyPKCS1.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def key_name(self):
        """Gets the key_name of this VerifyPKCS1.  # noqa: E501

        The name of the RSA key to use in the verification process  # noqa: E501

        :return: The key_name of this VerifyPKCS1.  # noqa: E501
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this VerifyPKCS1.

        The name of the RSA key to use in the verification process  # noqa: E501

        :param key_name: The key_name of this VerifyPKCS1.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and key_name is None:  # noqa: E501
            raise ValueError("Invalid value for `key_name`, must not be `None`")  # noqa: E501

        self._key_name = key_name

    @property
    def message(self):
        """Gets the message of this VerifyPKCS1.  # noqa: E501

        The message to be verified  # noqa: E501

        :return: The message of this VerifyPKCS1.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this VerifyPKCS1.

        The message to be verified  # noqa: E501

        :param message: The message of this VerifyPKCS1.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def prehashed(self):
        """Gets the prehashed of this VerifyPKCS1.  # noqa: E501

        Markes that the message is already hashed  # noqa: E501

        :return: The prehashed of this VerifyPKCS1.  # noqa: E501
        :rtype: bool
        """
        return self._prehashed

    @prehashed.setter
    def prehashed(self, prehashed):
        """Sets the prehashed of this VerifyPKCS1.

        Markes that the message is already hashed  # noqa: E501

        :param prehashed: The prehashed of this VerifyPKCS1.  # noqa: E501
        :type: bool
        """

        self._prehashed = prehashed

    @property
    def signature(self):
        """Gets the signature of this VerifyPKCS1.  # noqa: E501

        The message's signature  # noqa: E501

        :return: The signature of this VerifyPKCS1.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this VerifyPKCS1.

        The message's signature  # noqa: E501

        :param signature: The signature of this VerifyPKCS1.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and signature is None:  # noqa: E501
            raise ValueError("Invalid value for `signature`, must not be `None`")  # noqa: E501

        self._signature = signature

    @property
    def token(self):
        """Gets the token of this VerifyPKCS1.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this VerifyPKCS1.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this VerifyPKCS1.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this VerifyPKCS1.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this VerifyPKCS1.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this VerifyPKCS1.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this VerifyPKCS1.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this VerifyPKCS1.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def version(self):
        """Gets the version of this VerifyPKCS1.  # noqa: E501

        The version of the key to use for verification  # noqa: E501

        :return: The version of this VerifyPKCS1.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this VerifyPKCS1.

        The version of the key to use for verification  # noqa: E501

        :param version: The version of this VerifyPKCS1.  # noqa: E501
        :type: int
        """

        self._version = version

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
        if not isinstance(other, VerifyPKCS1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VerifyPKCS1):
            return True

        return self.to_dict() != other.to_dict()
