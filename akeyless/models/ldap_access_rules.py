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


class LDAPAccessRules(object):
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
        'gen_key_pair': 'str',
        'key': 'str',
        'unique_identifier': 'str'
    }

    attribute_map = {
        'alg': 'alg',
        'gen_key_pair': 'gen_key_pair',
        'key': 'key',
        'unique_identifier': 'unique_identifier'
    }

    def __init__(self, alg=None, gen_key_pair=None, key=None, unique_identifier=None, local_vars_configuration=None):  # noqa: E501
        """LDAPAccessRules - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._alg = None
        self._gen_key_pair = None
        self._key = None
        self._unique_identifier = None
        self.discriminator = None

        if alg is not None:
            self.alg = alg
        if gen_key_pair is not None:
            self.gen_key_pair = gen_key_pair
        if key is not None:
            self.key = key
        if unique_identifier is not None:
            self.unique_identifier = unique_identifier

    @property
    def alg(self):
        """Gets the alg of this LDAPAccessRules.  # noqa: E501


        :return: The alg of this LDAPAccessRules.  # noqa: E501
        :rtype: str
        """
        return self._alg

    @alg.setter
    def alg(self, alg):
        """Sets the alg of this LDAPAccessRules.


        :param alg: The alg of this LDAPAccessRules.  # noqa: E501
        :type: str
        """

        self._alg = alg

    @property
    def gen_key_pair(self):
        """Gets the gen_key_pair of this LDAPAccessRules.  # noqa: E501

        Generate public/private key (the private key is required for the LDAP Auth Config in the Akeyless Gateway)  # noqa: E501

        :return: The gen_key_pair of this LDAPAccessRules.  # noqa: E501
        :rtype: str
        """
        return self._gen_key_pair

    @gen_key_pair.setter
    def gen_key_pair(self, gen_key_pair):
        """Sets the gen_key_pair of this LDAPAccessRules.

        Generate public/private key (the private key is required for the LDAP Auth Config in the Akeyless Gateway)  # noqa: E501

        :param gen_key_pair: The gen_key_pair of this LDAPAccessRules.  # noqa: E501
        :type: str
        """

        self._gen_key_pair = gen_key_pair

    @property
    def key(self):
        """Gets the key of this LDAPAccessRules.  # noqa: E501

        The public key value of LDAP.  # noqa: E501

        :return: The key of this LDAPAccessRules.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this LDAPAccessRules.

        The public key value of LDAP.  # noqa: E501

        :param key: The key of this LDAPAccessRules.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def unique_identifier(self):
        """Gets the unique_identifier of this LDAPAccessRules.  # noqa: E501

        A unique identifier to distinguish different users  # noqa: E501

        :return: The unique_identifier of this LDAPAccessRules.  # noqa: E501
        :rtype: str
        """
        return self._unique_identifier

    @unique_identifier.setter
    def unique_identifier(self, unique_identifier):
        """Sets the unique_identifier of this LDAPAccessRules.

        A unique identifier to distinguish different users  # noqa: E501

        :param unique_identifier: The unique_identifier of this LDAPAccessRules.  # noqa: E501
        :type: str
        """

        self._unique_identifier = unique_identifier

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
        if not isinstance(other, LDAPAccessRules):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LDAPAccessRules):
            return True

        return self.to_dict() != other.to_dict()
