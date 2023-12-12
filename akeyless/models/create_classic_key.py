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


class CreateClassicKey(object):
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
        'cert_file_data': 'str',
        'certificate_common_name': 'str',
        'certificate_country': 'str',
        'certificate_digest_algo': 'str',
        'certificate_locality': 'str',
        'certificate_organization': 'str',
        'certificate_province': 'str',
        'certificate_ttl': 'int',
        'conf_file_data': 'str',
        'delete_protection': 'str',
        'description': 'str',
        'generate_self_signed_certificate': 'bool',
        'gpg_alg': 'str',
        'json': 'bool',
        'key_data': 'str',
        'metadata': 'str',
        'name': 'str',
        'protection_key_name': 'str',
        'tags': 'list[str]',
        'token': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'alg': 'alg',
        'cert_file_data': 'cert-file-data',
        'certificate_common_name': 'certificate-common-name',
        'certificate_country': 'certificate-country',
        'certificate_digest_algo': 'certificate-digest-algo',
        'certificate_locality': 'certificate-locality',
        'certificate_organization': 'certificate-organization',
        'certificate_province': 'certificate-province',
        'certificate_ttl': 'certificate-ttl',
        'conf_file_data': 'conf-file-data',
        'delete_protection': 'delete_protection',
        'description': 'description',
        'generate_self_signed_certificate': 'generate-self-signed-certificate',
        'gpg_alg': 'gpg-alg',
        'json': 'json',
        'key_data': 'key-data',
        'metadata': 'metadata',
        'name': 'name',
        'protection_key_name': 'protection-key-name',
        'tags': 'tags',
        'token': 'token',
        'uid_token': 'uid-token'
    }

    def __init__(self, alg=None, cert_file_data=None, certificate_common_name=None, certificate_country=None, certificate_digest_algo=None, certificate_locality=None, certificate_organization=None, certificate_province=None, certificate_ttl=None, conf_file_data=None, delete_protection=None, description=None, generate_self_signed_certificate=None, gpg_alg=None, json=False, key_data=None, metadata=None, name=None, protection_key_name=None, tags=None, token=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """CreateClassicKey - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._alg = None
        self._cert_file_data = None
        self._certificate_common_name = None
        self._certificate_country = None
        self._certificate_digest_algo = None
        self._certificate_locality = None
        self._certificate_organization = None
        self._certificate_province = None
        self._certificate_ttl = None
        self._conf_file_data = None
        self._delete_protection = None
        self._description = None
        self._generate_self_signed_certificate = None
        self._gpg_alg = None
        self._json = None
        self._key_data = None
        self._metadata = None
        self._name = None
        self._protection_key_name = None
        self._tags = None
        self._token = None
        self._uid_token = None
        self.discriminator = None

        self.alg = alg
        if cert_file_data is not None:
            self.cert_file_data = cert_file_data
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
        if conf_file_data is not None:
            self.conf_file_data = conf_file_data
        if delete_protection is not None:
            self.delete_protection = delete_protection
        if description is not None:
            self.description = description
        if generate_self_signed_certificate is not None:
            self.generate_self_signed_certificate = generate_self_signed_certificate
        if gpg_alg is not None:
            self.gpg_alg = gpg_alg
        if json is not None:
            self.json = json
        if key_data is not None:
            self.key_data = key_data
        if metadata is not None:
            self.metadata = metadata
        self.name = name
        if protection_key_name is not None:
            self.protection_key_name = protection_key_name
        if tags is not None:
            self.tags = tags
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def alg(self):
        """Gets the alg of this CreateClassicKey.  # noqa: E501

        Classic Key type; options: [AES128GCM, AES256GCM, AES128SIV, AES256SIV, RSA1024, RSA2048, RSA3072, RSA4096, EC256, EC384, GPG]  # noqa: E501

        :return: The alg of this CreateClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._alg

    @alg.setter
    def alg(self, alg):
        """Sets the alg of this CreateClassicKey.

        Classic Key type; options: [AES128GCM, AES256GCM, AES128SIV, AES256SIV, RSA1024, RSA2048, RSA3072, RSA4096, EC256, EC384, GPG]  # noqa: E501

        :param alg: The alg of this CreateClassicKey.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and alg is None:  # noqa: E501
            raise ValueError("Invalid value for `alg`, must not be `None`")  # noqa: E501

        self._alg = alg

    @property
    def cert_file_data(self):
        """Gets the cert_file_data of this CreateClassicKey.  # noqa: E501

        Certificate in a PEM format.  # noqa: E501

        :return: The cert_file_data of this CreateClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._cert_file_data

    @cert_file_data.setter
    def cert_file_data(self, cert_file_data):
        """Sets the cert_file_data of this CreateClassicKey.

        Certificate in a PEM format.  # noqa: E501

        :param cert_file_data: The cert_file_data of this CreateClassicKey.  # noqa: E501
        :type: str
        """

        self._cert_file_data = cert_file_data

    @property
    def certificate_common_name(self):
        """Gets the certificate_common_name of this CreateClassicKey.  # noqa: E501

        Common name for the generated certificate. Relevant only for generate-self-signed-certificate.  # noqa: E501

        :return: The certificate_common_name of this CreateClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._certificate_common_name

    @certificate_common_name.setter
    def certificate_common_name(self, certificate_common_name):
        """Sets the certificate_common_name of this CreateClassicKey.

        Common name for the generated certificate. Relevant only for generate-self-signed-certificate.  # noqa: E501

        :param certificate_common_name: The certificate_common_name of this CreateClassicKey.  # noqa: E501
        :type: str
        """

        self._certificate_common_name = certificate_common_name

    @property
    def certificate_country(self):
        """Gets the certificate_country of this CreateClassicKey.  # noqa: E501

        Country name for the generated certificate. Relevant only for generate-self-signed-certificate.  # noqa: E501

        :return: The certificate_country of this CreateClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._certificate_country

    @certificate_country.setter
    def certificate_country(self, certificate_country):
        """Sets the certificate_country of this CreateClassicKey.

        Country name for the generated certificate. Relevant only for generate-self-signed-certificate.  # noqa: E501

        :param certificate_country: The certificate_country of this CreateClassicKey.  # noqa: E501
        :type: str
        """

        self._certificate_country = certificate_country

    @property
    def certificate_digest_algo(self):
        """Gets the certificate_digest_algo of this CreateClassicKey.  # noqa: E501

        Digest algorithm to be used for the certificate key signing. Currently, we support only \"sha256\" so we hide this option for CLI.  # noqa: E501

        :return: The certificate_digest_algo of this CreateClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._certificate_digest_algo

    @certificate_digest_algo.setter
    def certificate_digest_algo(self, certificate_digest_algo):
        """Sets the certificate_digest_algo of this CreateClassicKey.

        Digest algorithm to be used for the certificate key signing. Currently, we support only \"sha256\" so we hide this option for CLI.  # noqa: E501

        :param certificate_digest_algo: The certificate_digest_algo of this CreateClassicKey.  # noqa: E501
        :type: str
        """

        self._certificate_digest_algo = certificate_digest_algo

    @property
    def certificate_locality(self):
        """Gets the certificate_locality of this CreateClassicKey.  # noqa: E501

        Locality for the generated certificate. Relevant only for generate-self-signed-certificate.  # noqa: E501

        :return: The certificate_locality of this CreateClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._certificate_locality

    @certificate_locality.setter
    def certificate_locality(self, certificate_locality):
        """Sets the certificate_locality of this CreateClassicKey.

        Locality for the generated certificate. Relevant only for generate-self-signed-certificate.  # noqa: E501

        :param certificate_locality: The certificate_locality of this CreateClassicKey.  # noqa: E501
        :type: str
        """

        self._certificate_locality = certificate_locality

    @property
    def certificate_organization(self):
        """Gets the certificate_organization of this CreateClassicKey.  # noqa: E501

        Organization name for the generated certificate. Relevant only for generate-self-signed-certificate.  # noqa: E501

        :return: The certificate_organization of this CreateClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._certificate_organization

    @certificate_organization.setter
    def certificate_organization(self, certificate_organization):
        """Sets the certificate_organization of this CreateClassicKey.

        Organization name for the generated certificate. Relevant only for generate-self-signed-certificate.  # noqa: E501

        :param certificate_organization: The certificate_organization of this CreateClassicKey.  # noqa: E501
        :type: str
        """

        self._certificate_organization = certificate_organization

    @property
    def certificate_province(self):
        """Gets the certificate_province of this CreateClassicKey.  # noqa: E501

        Province name for the generated certificate. Relevant only for generate-self-signed-certificate.  # noqa: E501

        :return: The certificate_province of this CreateClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._certificate_province

    @certificate_province.setter
    def certificate_province(self, certificate_province):
        """Sets the certificate_province of this CreateClassicKey.

        Province name for the generated certificate. Relevant only for generate-self-signed-certificate.  # noqa: E501

        :param certificate_province: The certificate_province of this CreateClassicKey.  # noqa: E501
        :type: str
        """

        self._certificate_province = certificate_province

    @property
    def certificate_ttl(self):
        """Gets the certificate_ttl of this CreateClassicKey.  # noqa: E501

        TTL in days for the generated certificate. Required only for generate-self-signed-certificate.  # noqa: E501

        :return: The certificate_ttl of this CreateClassicKey.  # noqa: E501
        :rtype: int
        """
        return self._certificate_ttl

    @certificate_ttl.setter
    def certificate_ttl(self, certificate_ttl):
        """Sets the certificate_ttl of this CreateClassicKey.

        TTL in days for the generated certificate. Required only for generate-self-signed-certificate.  # noqa: E501

        :param certificate_ttl: The certificate_ttl of this CreateClassicKey.  # noqa: E501
        :type: int
        """

        self._certificate_ttl = certificate_ttl

    @property
    def conf_file_data(self):
        """Gets the conf_file_data of this CreateClassicKey.  # noqa: E501

        The csr config data in base64 encoding  # noqa: E501

        :return: The conf_file_data of this CreateClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._conf_file_data

    @conf_file_data.setter
    def conf_file_data(self, conf_file_data):
        """Sets the conf_file_data of this CreateClassicKey.

        The csr config data in base64 encoding  # noqa: E501

        :param conf_file_data: The conf_file_data of this CreateClassicKey.  # noqa: E501
        :type: str
        """

        self._conf_file_data = conf_file_data

    @property
    def delete_protection(self):
        """Gets the delete_protection of this CreateClassicKey.  # noqa: E501

        Protection from accidental deletion of this item [true/false]  # noqa: E501

        :return: The delete_protection of this CreateClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._delete_protection

    @delete_protection.setter
    def delete_protection(self, delete_protection):
        """Sets the delete_protection of this CreateClassicKey.

        Protection from accidental deletion of this item [true/false]  # noqa: E501

        :param delete_protection: The delete_protection of this CreateClassicKey.  # noqa: E501
        :type: str
        """

        self._delete_protection = delete_protection

    @property
    def description(self):
        """Gets the description of this CreateClassicKey.  # noqa: E501

        Description of the object  # noqa: E501

        :return: The description of this CreateClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateClassicKey.

        Description of the object  # noqa: E501

        :param description: The description of this CreateClassicKey.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def generate_self_signed_certificate(self):
        """Gets the generate_self_signed_certificate of this CreateClassicKey.  # noqa: E501

        Whether to generate a self signed certificate with the key. If set, --certificate-ttl must be provided.  # noqa: E501

        :return: The generate_self_signed_certificate of this CreateClassicKey.  # noqa: E501
        :rtype: bool
        """
        return self._generate_self_signed_certificate

    @generate_self_signed_certificate.setter
    def generate_self_signed_certificate(self, generate_self_signed_certificate):
        """Sets the generate_self_signed_certificate of this CreateClassicKey.

        Whether to generate a self signed certificate with the key. If set, --certificate-ttl must be provided.  # noqa: E501

        :param generate_self_signed_certificate: The generate_self_signed_certificate of this CreateClassicKey.  # noqa: E501
        :type: bool
        """

        self._generate_self_signed_certificate = generate_self_signed_certificate

    @property
    def gpg_alg(self):
        """Gets the gpg_alg of this CreateClassicKey.  # noqa: E501

        gpg alg: Relevant only if GPG key type selected; options: [RSA1024, RSA2048, RSA3072, RSA4096, Ed25519]  # noqa: E501

        :return: The gpg_alg of this CreateClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._gpg_alg

    @gpg_alg.setter
    def gpg_alg(self, gpg_alg):
        """Sets the gpg_alg of this CreateClassicKey.

        gpg alg: Relevant only if GPG key type selected; options: [RSA1024, RSA2048, RSA3072, RSA4096, Ed25519]  # noqa: E501

        :param gpg_alg: The gpg_alg of this CreateClassicKey.  # noqa: E501
        :type: str
        """

        self._gpg_alg = gpg_alg

    @property
    def json(self):
        """Gets the json of this CreateClassicKey.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this CreateClassicKey.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this CreateClassicKey.

        Set output format to JSON  # noqa: E501

        :param json: The json of this CreateClassicKey.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def key_data(self):
        """Gets the key_data of this CreateClassicKey.  # noqa: E501

        Base64-encoded classic key value  # noqa: E501

        :return: The key_data of this CreateClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._key_data

    @key_data.setter
    def key_data(self, key_data):
        """Sets the key_data of this CreateClassicKey.

        Base64-encoded classic key value  # noqa: E501

        :param key_data: The key_data of this CreateClassicKey.  # noqa: E501
        :type: str
        """

        self._key_data = key_data

    @property
    def metadata(self):
        """Gets the metadata of this CreateClassicKey.  # noqa: E501

        Deprecated - use description  # noqa: E501

        :return: The metadata of this CreateClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CreateClassicKey.

        Deprecated - use description  # noqa: E501

        :param metadata: The metadata of this CreateClassicKey.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this CreateClassicKey.  # noqa: E501

        ClassicKey name  # noqa: E501

        :return: The name of this CreateClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateClassicKey.

        ClassicKey name  # noqa: E501

        :param name: The name of this CreateClassicKey.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def protection_key_name(self):
        """Gets the protection_key_name of this CreateClassicKey.  # noqa: E501

        The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :return: The protection_key_name of this CreateClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._protection_key_name

    @protection_key_name.setter
    def protection_key_name(self, protection_key_name):
        """Sets the protection_key_name of this CreateClassicKey.

        The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :param protection_key_name: The protection_key_name of this CreateClassicKey.  # noqa: E501
        :type: str
        """

        self._protection_key_name = protection_key_name

    @property
    def tags(self):
        """Gets the tags of this CreateClassicKey.  # noqa: E501

        Add tags attached to this object  # noqa: E501

        :return: The tags of this CreateClassicKey.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateClassicKey.

        Add tags attached to this object  # noqa: E501

        :param tags: The tags of this CreateClassicKey.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def token(self):
        """Gets the token of this CreateClassicKey.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this CreateClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this CreateClassicKey.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this CreateClassicKey.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this CreateClassicKey.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this CreateClassicKey.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this CreateClassicKey.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this CreateClassicKey.  # noqa: E501
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
        if not isinstance(other, CreateClassicKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateClassicKey):
            return True

        return self.to_dict() != other.to_dict()
