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


class CertificateChainInfo(object):
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
        'certificate_chain': 'list[CertificateInfo]',
        'certificate_format': 'str',
        'certificate_issuer_name': 'str',
        'certificate_pem': 'str',
        'certificate_status': 'str',
        'expiration_events': 'list[CertificateExpirationEvent]'
    }

    attribute_map = {
        'certificate_chain': 'certificate_chain',
        'certificate_format': 'certificate_format',
        'certificate_issuer_name': 'certificate_issuer_name',
        'certificate_pem': 'certificate_pem',
        'certificate_status': 'certificate_status',
        'expiration_events': 'expiration_events'
    }

    def __init__(self, certificate_chain=None, certificate_format=None, certificate_issuer_name=None, certificate_pem=None, certificate_status=None, expiration_events=None, local_vars_configuration=None):  # noqa: E501
        """CertificateChainInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._certificate_chain = None
        self._certificate_format = None
        self._certificate_issuer_name = None
        self._certificate_pem = None
        self._certificate_status = None
        self._expiration_events = None
        self.discriminator = None

        if certificate_chain is not None:
            self.certificate_chain = certificate_chain
        if certificate_format is not None:
            self.certificate_format = certificate_format
        if certificate_issuer_name is not None:
            self.certificate_issuer_name = certificate_issuer_name
        if certificate_pem is not None:
            self.certificate_pem = certificate_pem
        if certificate_status is not None:
            self.certificate_status = certificate_status
        if expiration_events is not None:
            self.expiration_events = expiration_events

    @property
    def certificate_chain(self):
        """Gets the certificate_chain of this CertificateChainInfo.  # noqa: E501


        :return: The certificate_chain of this CertificateChainInfo.  # noqa: E501
        :rtype: list[CertificateInfo]
        """
        return self._certificate_chain

    @certificate_chain.setter
    def certificate_chain(self, certificate_chain):
        """Sets the certificate_chain of this CertificateChainInfo.


        :param certificate_chain: The certificate_chain of this CertificateChainInfo.  # noqa: E501
        :type: list[CertificateInfo]
        """

        self._certificate_chain = certificate_chain

    @property
    def certificate_format(self):
        """Gets the certificate_format of this CertificateChainInfo.  # noqa: E501


        :return: The certificate_format of this CertificateChainInfo.  # noqa: E501
        :rtype: str
        """
        return self._certificate_format

    @certificate_format.setter
    def certificate_format(self, certificate_format):
        """Sets the certificate_format of this CertificateChainInfo.


        :param certificate_format: The certificate_format of this CertificateChainInfo.  # noqa: E501
        :type: str
        """

        self._certificate_format = certificate_format

    @property
    def certificate_issuer_name(self):
        """Gets the certificate_issuer_name of this CertificateChainInfo.  # noqa: E501


        :return: The certificate_issuer_name of this CertificateChainInfo.  # noqa: E501
        :rtype: str
        """
        return self._certificate_issuer_name

    @certificate_issuer_name.setter
    def certificate_issuer_name(self, certificate_issuer_name):
        """Sets the certificate_issuer_name of this CertificateChainInfo.


        :param certificate_issuer_name: The certificate_issuer_name of this CertificateChainInfo.  # noqa: E501
        :type: str
        """

        self._certificate_issuer_name = certificate_issuer_name

    @property
    def certificate_pem(self):
        """Gets the certificate_pem of this CertificateChainInfo.  # noqa: E501


        :return: The certificate_pem of this CertificateChainInfo.  # noqa: E501
        :rtype: str
        """
        return self._certificate_pem

    @certificate_pem.setter
    def certificate_pem(self, certificate_pem):
        """Sets the certificate_pem of this CertificateChainInfo.


        :param certificate_pem: The certificate_pem of this CertificateChainInfo.  # noqa: E501
        :type: str
        """

        self._certificate_pem = certificate_pem

    @property
    def certificate_status(self):
        """Gets the certificate_status of this CertificateChainInfo.  # noqa: E501


        :return: The certificate_status of this CertificateChainInfo.  # noqa: E501
        :rtype: str
        """
        return self._certificate_status

    @certificate_status.setter
    def certificate_status(self, certificate_status):
        """Sets the certificate_status of this CertificateChainInfo.


        :param certificate_status: The certificate_status of this CertificateChainInfo.  # noqa: E501
        :type: str
        """

        self._certificate_status = certificate_status

    @property
    def expiration_events(self):
        """Gets the expiration_events of this CertificateChainInfo.  # noqa: E501


        :return: The expiration_events of this CertificateChainInfo.  # noqa: E501
        :rtype: list[CertificateExpirationEvent]
        """
        return self._expiration_events

    @expiration_events.setter
    def expiration_events(self, expiration_events):
        """Sets the expiration_events of this CertificateChainInfo.


        :param expiration_events: The expiration_events of this CertificateChainInfo.  # noqa: E501
        :type: list[CertificateExpirationEvent]
        """

        self._expiration_events = expiration_events

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
        if not isinstance(other, CertificateChainInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CertificateChainInfo):
            return True

        return self.to_dict() != other.to_dict()
