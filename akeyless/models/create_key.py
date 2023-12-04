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


class CreateKey(object):
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
        'certificate_common_name': 'str',
        'certificate_country': 'str',
        'certificate_digest_algo': 'str',
        'certificate_locality': 'str',
        'certificate_organization': 'str',
        'certificate_province': 'str',
        'certificate_ttl': 'int',
        'customer_frg_id': 'str',
        'delete_protection': 'str',
        'description': 'str',
        'generate_self_signed_certificate': 'bool',
        'json': 'bool',
        'metadata': 'str',
        'name': 'str',
        'split_level': 'int',
        'tag': 'list[str]',
        'token': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'alg': 'alg',
        'certificate_common_name': 'certificate-common-name',
        'certificate_country': 'certificate-country',
        'certificate_digest_algo': 'certificate-digest-algo',
        'certificate_locality': 'certificate-locality',
        'certificate_organization': 'certificate-organization',
        'certificate_province': 'certificate-province',
        'certificate_ttl': 'certificate-ttl',
        'customer_frg_id': 'customer-frg-id',
        'delete_protection': 'delete_protection',
        'description': 'description',
        'generate_self_signed_certificate': 'generate-self-signed-certificate',
        'json': 'json',
        'metadata': 'metadata',
        'name': 'name',
        'split_level': 'split-level',
        'tag': 'tag',
        'token': 'token',
        'uid_token': 'uid-token'
    }

    def __init__(self, alg=None, certificate_common_name=None, certificate_country=None, certificate_digest_algo=None, certificate_locality=None, certificate_organization=None, certificate_province=None, certificate_ttl=None, customer_frg_id=None, delete_protection=None, description=None, generate_self_signed_certificate=None, json=False, metadata=None, name=None, split_level=3, tag=None, token=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """CreateKey - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._alg = None
        self._certificate_common_name = None
        self._certificate_country = None
        self._certificate_digest_algo = None
        self._certificate_locality = None
        self._certificate_organization = None
        self._certificate_province = None
        self._certificate_ttl = None
        self._customer_frg_id = None
        self._delete_protection = None
        self._description = None
        self._generate_self_signed_certificate = None
        self._json = None
        self._metadata = None
        self._name = None
        self._split_level = None
        self._tag = None
        self._token = None
        self._uid_token = None
        self.discriminator = None

        self.alg = alg
        if certificate_common_name is not None:
            self.certificate_common_name = certificate_common_name
        if certificate_country is not None:
            self.certificate_country = certificate_country
        if certificate_digest_algo is not None:
            self.certificate_digest_algo = certificate_digest_algo
        if certificate_locality is not None:
            self.certificate_locality = certificate_locality
        if certificate_organization is not None:
            self.certificate_organization = certificate_organization
        if certificate_province is not None:
            self.certificate_province = certificate_province
        if certificate_ttl is not None:
            self.certificate_ttl = certificate_ttl
        if customer_frg_id is not None:
            self.customer_frg_id = customer_frg_id
        if delete_protection is not None:
            self.delete_protection = delete_protection
        if description is not None:
            self.description = description
        if generate_self_signed_certificate is not None:
            self.generate_self_signed_certificate = generate_self_signed_certificate
        if json is not None:
            self.json = json
        if metadata is not None:
            self.metadata = metadata
        self.name = name
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
        """Gets the alg of this CreateKey.  # noqa: E501

        Key type; options: [AES128GCM, AES256GCM, AES128SIV, AES256SIV, AES128CBC, AES256CBC, RSA1024, RSA2048, RSA3072, RSA4096]  # noqa: E501

        :return: The alg of this CreateKey.  # noqa: E501
        :rtype: str
        """
        return self._alg

    @alg.setter
    def alg(self, alg):
        """Sets the alg of this CreateKey.

        Key type; options: [AES128GCM, AES256GCM, AES128SIV, AES256SIV, AES128CBC, AES256CBC, RSA1024, RSA2048, RSA3072, RSA4096]  # noqa: E501

        :param alg: The alg of this CreateKey.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and alg is None:  # noqa: E501
            raise ValueError("Invalid value for `alg`, must not be `None`")  # noqa: E501

        self._alg = alg

    @property
    def certificate_common_name(self):
        """Gets the certificate_common_name of this CreateKey.  # noqa: E501

        Common name for the generated certificate. Relevant only for generate-self-signed-certificate.  # noqa: E501

        :return: The certificate_common_name of this CreateKey.  # noqa: E501
        :rtype: str
        """
        return self._certificate_common_name

    @certificate_common_name.setter
    def certificate_common_name(self, certificate_common_name):
        """Sets the certificate_common_name of this CreateKey.

        Common name for the generated certificate. Relevant only for generate-self-signed-certificate.  # noqa: E501

        :param certificate_common_name: The certificate_common_name of this CreateKey.  # noqa: E501
        :type: str
        """

        self._certificate_common_name = certificate_common_name

    @property
    def certificate_country(self):
        """Gets the certificate_country of this CreateKey.  # noqa: E501

        Country name for the generated certificate. Relevant only for generate-self-signed-certificate.  # noqa: E501

        :return: The certificate_country of this CreateKey.  # noqa: E501
        :rtype: str
        """
        return self._certificate_country

    @certificate_country.setter
    def certificate_country(self, certificate_country):
        """Sets the certificate_country of this CreateKey.

        Country name for the generated certificate. Relevant only for generate-self-signed-certificate.  # noqa: E501

        :param certificate_country: The certificate_country of this CreateKey.  # noqa: E501
        :type: str
        """

        self._certificate_country = certificate_country

    @property
    def certificate_digest_algo(self):
        """Gets the certificate_digest_algo of this CreateKey.  # noqa: E501

        Digest algorithm to be used for the certificate key signing. Currently, we support only \"sha256\" so we hide this option for CLI.  # noqa: E501

        :return: The certificate_digest_algo of this CreateKey.  # noqa: E501
        :rtype: str
        """
        return self._certificate_digest_algo

    @certificate_digest_algo.setter
    def certificate_digest_algo(self, certificate_digest_algo):
        """Sets the certificate_digest_algo of this CreateKey.

        Digest algorithm to be used for the certificate key signing. Currently, we support only \"sha256\" so we hide this option for CLI.  # noqa: E501

        :param certificate_digest_algo: The certificate_digest_algo of this CreateKey.  # noqa: E501
        :type: str
        """

        self._certificate_digest_algo = certificate_digest_algo

    @property
    def certificate_locality(self):
        """Gets the certificate_locality of this CreateKey.  # noqa: E501

        Locality for the generated certificate. Relevant only for generate-self-signed-certificate.  # noqa: E501

        :return: The certificate_locality of this CreateKey.  # noqa: E501
        :rtype: str
        """
        return self._certificate_locality

    @certificate_locality.setter
    def certificate_locality(self, certificate_locality):
        """Sets the certificate_locality of this CreateKey.

        Locality for the generated certificate. Relevant only for generate-self-signed-certificate.  # noqa: E501

        :param certificate_locality: The certificate_locality of this CreateKey.  # noqa: E501
        :type: str
        """

        self._certificate_locality = certificate_locality

    @property
    def certificate_organization(self):
        """Gets the certificate_organization of this CreateKey.  # noqa: E501

        Organization name for the generated certificate. Relevant only for generate-self-signed-certificate.  # noqa: E501

        :return: The certificate_organization of this CreateKey.  # noqa: E501
        :rtype: str
        """
        return self._certificate_organization

    @certificate_organization.setter
    def certificate_organization(self, certificate_organization):
        """Sets the certificate_organization of this CreateKey.

        Organization name for the generated certificate. Relevant only for generate-self-signed-certificate.  # noqa: E501

        :param certificate_organization: The certificate_organization of this CreateKey.  # noqa: E501
        :type: str
        """

        self._certificate_organization = certificate_organization

    @property
    def certificate_province(self):
        """Gets the certificate_province of this CreateKey.  # noqa: E501

        Province name for the generated certificate. Relevant only for generate-self-signed-certificate.  # noqa: E501

        :return: The certificate_province of this CreateKey.  # noqa: E501
        :rtype: str
        """
        return self._certificate_province

    @certificate_province.setter
    def certificate_province(self, certificate_province):
        """Sets the certificate_province of this CreateKey.

        Province name for the generated certificate. Relevant only for generate-self-signed-certificate.  # noqa: E501

        :param certificate_province: The certificate_province of this CreateKey.  # noqa: E501
        :type: str
        """

        self._certificate_province = certificate_province

    @property
    def certificate_ttl(self):
        """Gets the certificate_ttl of this CreateKey.  # noqa: E501

        TTL in days for the generated certificate. Required only for generate-self-signed-certificate.  # noqa: E501

        :return: The certificate_ttl of this CreateKey.  # noqa: E501
        :rtype: int
        """
        return self._certificate_ttl

    @certificate_ttl.setter
    def certificate_ttl(self, certificate_ttl):
        """Sets the certificate_ttl of this CreateKey.

        TTL in days for the generated certificate. Required only for generate-self-signed-certificate.  # noqa: E501

        :param certificate_ttl: The certificate_ttl of this CreateKey.  # noqa: E501
        :type: int
        """

        self._certificate_ttl = certificate_ttl

    @property
    def customer_frg_id(self):
        """Gets the customer_frg_id of this CreateKey.  # noqa: E501

        The customer fragment ID that will be used to create the key (if empty, the key will be created independently of a customer fragment)  # noqa: E501

        :return: The customer_frg_id of this CreateKey.  # noqa: E501
        :rtype: str
        """
        return self._customer_frg_id

    @customer_frg_id.setter
    def customer_frg_id(self, customer_frg_id):
        """Sets the customer_frg_id of this CreateKey.

        The customer fragment ID that will be used to create the key (if empty, the key will be created independently of a customer fragment)  # noqa: E501

        :param customer_frg_id: The customer_frg_id of this CreateKey.  # noqa: E501
        :type: str
        """

        self._customer_frg_id = customer_frg_id

    @property
    def delete_protection(self):
        """Gets the delete_protection of this CreateKey.  # noqa: E501

        Protection from accidental deletion of this item [true/false]  # noqa: E501

        :return: The delete_protection of this CreateKey.  # noqa: E501
        :rtype: str
        """
        return self._delete_protection

    @delete_protection.setter
    def delete_protection(self, delete_protection):
        """Sets the delete_protection of this CreateKey.

        Protection from accidental deletion of this item [true/false]  # noqa: E501

        :param delete_protection: The delete_protection of this CreateKey.  # noqa: E501
        :type: str
        """

        self._delete_protection = delete_protection

    @property
    def description(self):
        """Gets the description of this CreateKey.  # noqa: E501

        Description of the object  # noqa: E501

        :return: The description of this CreateKey.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateKey.

        Description of the object  # noqa: E501

        :param description: The description of this CreateKey.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def generate_self_signed_certificate(self):
        """Gets the generate_self_signed_certificate of this CreateKey.  # noqa: E501

        Whether to generate a self signed certificate with the key. If set, --certificate-ttl must be provided.  # noqa: E501

        :return: The generate_self_signed_certificate of this CreateKey.  # noqa: E501
        :rtype: bool
        """
        return self._generate_self_signed_certificate

    @generate_self_signed_certificate.setter
    def generate_self_signed_certificate(self, generate_self_signed_certificate):
        """Sets the generate_self_signed_certificate of this CreateKey.

        Whether to generate a self signed certificate with the key. If set, --certificate-ttl must be provided.  # noqa: E501

        :param generate_self_signed_certificate: The generate_self_signed_certificate of this CreateKey.  # noqa: E501
        :type: bool
        """

        self._generate_self_signed_certificate = generate_self_signed_certificate

    @property
    def json(self):
        """Gets the json of this CreateKey.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this CreateKey.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this CreateKey.

        Set output format to JSON  # noqa: E501

        :param json: The json of this CreateKey.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def metadata(self):
        """Gets the metadata of this CreateKey.  # noqa: E501

        Deprecated - use description  # noqa: E501

        :return: The metadata of this CreateKey.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CreateKey.

        Deprecated - use description  # noqa: E501

        :param metadata: The metadata of this CreateKey.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this CreateKey.  # noqa: E501

        Key name  # noqa: E501

        :return: The name of this CreateKey.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateKey.

        Key name  # noqa: E501

        :param name: The name of this CreateKey.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def split_level(self):
        """Gets the split_level of this CreateKey.  # noqa: E501

        The number of fragments that the item will be split into (not includes customer fragment)  # noqa: E501

        :return: The split_level of this CreateKey.  # noqa: E501
        :rtype: int
        """
        return self._split_level

    @split_level.setter
    def split_level(self, split_level):
        """Sets the split_level of this CreateKey.

        The number of fragments that the item will be split into (not includes customer fragment)  # noqa: E501

        :param split_level: The split_level of this CreateKey.  # noqa: E501
        :type: int
        """

        self._split_level = split_level

    @property
    def tag(self):
        """Gets the tag of this CreateKey.  # noqa: E501

        List of the tags attached to this key  # noqa: E501

        :return: The tag of this CreateKey.  # noqa: E501
        :rtype: list[str]
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this CreateKey.

        List of the tags attached to this key  # noqa: E501

        :param tag: The tag of this CreateKey.  # noqa: E501
        :type: list[str]
        """

        self._tag = tag

    @property
    def token(self):
        """Gets the token of this CreateKey.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this CreateKey.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this CreateKey.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this CreateKey.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this CreateKey.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this CreateKey.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this CreateKey.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this CreateKey.  # noqa: E501
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
        if not isinstance(other, CreateKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateKey):
            return True

        return self.to_dict() != other.to_dict()
