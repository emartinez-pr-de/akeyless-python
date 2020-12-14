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


class SAMLAccessRules(object):
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
        'bound_attributes': 'list[SAMLAttribute]',
        'idp_metadata_url': 'str',
        'idp_metadata_xml': 'str',
        'unique_identifier': 'str'
    }

    attribute_map = {
        'bound_attributes': 'bound_attributes',
        'idp_metadata_url': 'idp_metadata_url',
        'idp_metadata_xml': 'idp_metadata_xml',
        'unique_identifier': 'unique_identifier'
    }

    def __init__(self, bound_attributes=None, idp_metadata_url=None, idp_metadata_xml=None, unique_identifier=None, local_vars_configuration=None):  # noqa: E501
        """SAMLAccessRules - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bound_attributes = None
        self._idp_metadata_url = None
        self._idp_metadata_xml = None
        self._unique_identifier = None
        self.discriminator = None

        if bound_attributes is not None:
            self.bound_attributes = bound_attributes
        if idp_metadata_url is not None:
            self.idp_metadata_url = idp_metadata_url
        if idp_metadata_xml is not None:
            self.idp_metadata_xml = idp_metadata_xml
        if unique_identifier is not None:
            self.unique_identifier = unique_identifier

    @property
    def bound_attributes(self):
        """Gets the bound_attributes of this SAMLAccessRules.  # noqa: E501

        The attributes that login is restricted to.  # noqa: E501

        :return: The bound_attributes of this SAMLAccessRules.  # noqa: E501
        :rtype: list[SAMLAttribute]
        """
        return self._bound_attributes

    @bound_attributes.setter
    def bound_attributes(self, bound_attributes):
        """Sets the bound_attributes of this SAMLAccessRules.

        The attributes that login is restricted to.  # noqa: E501

        :param bound_attributes: The bound_attributes of this SAMLAccessRules.  # noqa: E501
        :type: list[SAMLAttribute]
        """

        self._bound_attributes = bound_attributes

    @property
    def idp_metadata_url(self):
        """Gets the idp_metadata_url of this SAMLAccessRules.  # noqa: E501

        IDP metadata url  # noqa: E501

        :return: The idp_metadata_url of this SAMLAccessRules.  # noqa: E501
        :rtype: str
        """
        return self._idp_metadata_url

    @idp_metadata_url.setter
    def idp_metadata_url(self, idp_metadata_url):
        """Sets the idp_metadata_url of this SAMLAccessRules.

        IDP metadata url  # noqa: E501

        :param idp_metadata_url: The idp_metadata_url of this SAMLAccessRules.  # noqa: E501
        :type: str
        """

        self._idp_metadata_url = idp_metadata_url

    @property
    def idp_metadata_xml(self):
        """Gets the idp_metadata_xml of this SAMLAccessRules.  # noqa: E501

        IDP metadata XML  # noqa: E501

        :return: The idp_metadata_xml of this SAMLAccessRules.  # noqa: E501
        :rtype: str
        """
        return self._idp_metadata_xml

    @idp_metadata_xml.setter
    def idp_metadata_xml(self, idp_metadata_xml):
        """Sets the idp_metadata_xml of this SAMLAccessRules.

        IDP metadata XML  # noqa: E501

        :param idp_metadata_xml: The idp_metadata_xml of this SAMLAccessRules.  # noqa: E501
        :type: str
        """

        self._idp_metadata_xml = idp_metadata_xml

    @property
    def unique_identifier(self):
        """Gets the unique_identifier of this SAMLAccessRules.  # noqa: E501

        A unique identifier to distinguish different users  # noqa: E501

        :return: The unique_identifier of this SAMLAccessRules.  # noqa: E501
        :rtype: str
        """
        return self._unique_identifier

    @unique_identifier.setter
    def unique_identifier(self, unique_identifier):
        """Sets the unique_identifier of this SAMLAccessRules.

        A unique identifier to distinguish different users  # noqa: E501

        :param unique_identifier: The unique_identifier of this SAMLAccessRules.  # noqa: E501
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
        if not isinstance(other, SAMLAccessRules):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SAMLAccessRules):
            return True

        return self.to_dict() != other.to_dict()
