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


class AuthMethodAccessInfo(object):
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
        'access_expires': 'int',
        'access_id_alias': 'str',
        'api_key_access_rules': 'APIKeyAccessRules',
        'aws_iam_access_rules': 'AWSIAMAccessRules',
        'azure_ad_access_rules': 'AzureADAccessRules',
        'cert_access_rules': 'CertAccessRules',
        'cidr_whitelist': 'str',
        'email_pass_access_rules': 'EmailPassAccessRules',
        'force_sub_claims': 'bool',
        'gcp_access_rules': 'GCPAccessRules',
        'gw_cidr_whitelist': 'str',
        'huawei_access_rules': 'HuaweiAccessRules',
        'jwt_ttl': 'int',
        'k8s_access_rules': 'KubernetesAccessRules',
        'ldap_access_rules': 'LDAPAccessRules',
        'oauth2_access_rules': 'OAuth2AccessRules',
        'oci_access_rules': 'OCIAccessRules',
        'oidc_access_rules': 'OIDCAccessRules',
        'rules_type': 'str',
        'saml_access_rules': 'SAMLAccessRules',
        'sub_claims_delimiters': 'list[str]',
        'universal_identity_access_rules': 'UniversalIdentityAccessRules'
    }

    attribute_map = {
        'access_expires': 'access_expires',
        'access_id_alias': 'access_id_alias',
        'api_key_access_rules': 'api_key_access_rules',
        'aws_iam_access_rules': 'aws_iam_access_rules',
        'azure_ad_access_rules': 'azure_ad_access_rules',
        'cert_access_rules': 'cert_access_rules',
        'cidr_whitelist': 'cidr_whitelist',
        'email_pass_access_rules': 'email_pass_access_rules',
        'force_sub_claims': 'force_sub_claims',
        'gcp_access_rules': 'gcp_access_rules',
        'gw_cidr_whitelist': 'gw_cidr_whitelist',
        'huawei_access_rules': 'huawei_access_rules',
        'jwt_ttl': 'jwt_ttl',
        'k8s_access_rules': 'k8s_access_rules',
        'ldap_access_rules': 'ldap_access_rules',
        'oauth2_access_rules': 'oauth2_access_rules',
        'oci_access_rules': 'oci_access_rules',
        'oidc_access_rules': 'oidc_access_rules',
        'rules_type': 'rules_type',
        'saml_access_rules': 'saml_access_rules',
        'sub_claims_delimiters': 'sub_claims_delimiters',
        'universal_identity_access_rules': 'universal_identity_access_rules'
    }

    def __init__(self, access_expires=None, access_id_alias=None, api_key_access_rules=None, aws_iam_access_rules=None, azure_ad_access_rules=None, cert_access_rules=None, cidr_whitelist=None, email_pass_access_rules=None, force_sub_claims=None, gcp_access_rules=None, gw_cidr_whitelist=None, huawei_access_rules=None, jwt_ttl=None, k8s_access_rules=None, ldap_access_rules=None, oauth2_access_rules=None, oci_access_rules=None, oidc_access_rules=None, rules_type=None, saml_access_rules=None, sub_claims_delimiters=None, universal_identity_access_rules=None, local_vars_configuration=None):  # noqa: E501
        """AuthMethodAccessInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_expires = None
        self._access_id_alias = None
        self._api_key_access_rules = None
        self._aws_iam_access_rules = None
        self._azure_ad_access_rules = None
        self._cert_access_rules = None
        self._cidr_whitelist = None
        self._email_pass_access_rules = None
        self._force_sub_claims = None
        self._gcp_access_rules = None
        self._gw_cidr_whitelist = None
        self._huawei_access_rules = None
        self._jwt_ttl = None
        self._k8s_access_rules = None
        self._ldap_access_rules = None
        self._oauth2_access_rules = None
        self._oci_access_rules = None
        self._oidc_access_rules = None
        self._rules_type = None
        self._saml_access_rules = None
        self._sub_claims_delimiters = None
        self._universal_identity_access_rules = None
        self.discriminator = None

        if access_expires is not None:
            self.access_expires = access_expires
        if access_id_alias is not None:
            self.access_id_alias = access_id_alias
        if api_key_access_rules is not None:
            self.api_key_access_rules = api_key_access_rules
        if aws_iam_access_rules is not None:
            self.aws_iam_access_rules = aws_iam_access_rules
        if azure_ad_access_rules is not None:
            self.azure_ad_access_rules = azure_ad_access_rules
        if cert_access_rules is not None:
            self.cert_access_rules = cert_access_rules
        if cidr_whitelist is not None:
            self.cidr_whitelist = cidr_whitelist
        if email_pass_access_rules is not None:
            self.email_pass_access_rules = email_pass_access_rules
        if force_sub_claims is not None:
            self.force_sub_claims = force_sub_claims
        if gcp_access_rules is not None:
            self.gcp_access_rules = gcp_access_rules
        if gw_cidr_whitelist is not None:
            self.gw_cidr_whitelist = gw_cidr_whitelist
        if huawei_access_rules is not None:
            self.huawei_access_rules = huawei_access_rules
        if jwt_ttl is not None:
            self.jwt_ttl = jwt_ttl
        if k8s_access_rules is not None:
            self.k8s_access_rules = k8s_access_rules
        if ldap_access_rules is not None:
            self.ldap_access_rules = ldap_access_rules
        if oauth2_access_rules is not None:
            self.oauth2_access_rules = oauth2_access_rules
        if oci_access_rules is not None:
            self.oci_access_rules = oci_access_rules
        if oidc_access_rules is not None:
            self.oidc_access_rules = oidc_access_rules
        if rules_type is not None:
            self.rules_type = rules_type
        if saml_access_rules is not None:
            self.saml_access_rules = saml_access_rules
        if sub_claims_delimiters is not None:
            self.sub_claims_delimiters = sub_claims_delimiters
        if universal_identity_access_rules is not None:
            self.universal_identity_access_rules = universal_identity_access_rules

    @property
    def access_expires(self):
        """Gets the access_expires of this AuthMethodAccessInfo.  # noqa: E501


        :return: The access_expires of this AuthMethodAccessInfo.  # noqa: E501
        :rtype: int
        """
        return self._access_expires

    @access_expires.setter
    def access_expires(self, access_expires):
        """Sets the access_expires of this AuthMethodAccessInfo.


        :param access_expires: The access_expires of this AuthMethodAccessInfo.  # noqa: E501
        :type: int
        """

        self._access_expires = access_expires

    @property
    def access_id_alias(self):
        """Gets the access_id_alias of this AuthMethodAccessInfo.  # noqa: E501

        for accounts where AccessId holds encrypted email this field will hold generated AccessId, for accounts based on regular AccessId it will be equal to accessId itself  # noqa: E501

        :return: The access_id_alias of this AuthMethodAccessInfo.  # noqa: E501
        :rtype: str
        """
        return self._access_id_alias

    @access_id_alias.setter
    def access_id_alias(self, access_id_alias):
        """Sets the access_id_alias of this AuthMethodAccessInfo.

        for accounts where AccessId holds encrypted email this field will hold generated AccessId, for accounts based on regular AccessId it will be equal to accessId itself  # noqa: E501

        :param access_id_alias: The access_id_alias of this AuthMethodAccessInfo.  # noqa: E501
        :type: str
        """

        self._access_id_alias = access_id_alias

    @property
    def api_key_access_rules(self):
        """Gets the api_key_access_rules of this AuthMethodAccessInfo.  # noqa: E501


        :return: The api_key_access_rules of this AuthMethodAccessInfo.  # noqa: E501
        :rtype: APIKeyAccessRules
        """
        return self._api_key_access_rules

    @api_key_access_rules.setter
    def api_key_access_rules(self, api_key_access_rules):
        """Sets the api_key_access_rules of this AuthMethodAccessInfo.


        :param api_key_access_rules: The api_key_access_rules of this AuthMethodAccessInfo.  # noqa: E501
        :type: APIKeyAccessRules
        """

        self._api_key_access_rules = api_key_access_rules

    @property
    def aws_iam_access_rules(self):
        """Gets the aws_iam_access_rules of this AuthMethodAccessInfo.  # noqa: E501


        :return: The aws_iam_access_rules of this AuthMethodAccessInfo.  # noqa: E501
        :rtype: AWSIAMAccessRules
        """
        return self._aws_iam_access_rules

    @aws_iam_access_rules.setter
    def aws_iam_access_rules(self, aws_iam_access_rules):
        """Sets the aws_iam_access_rules of this AuthMethodAccessInfo.


        :param aws_iam_access_rules: The aws_iam_access_rules of this AuthMethodAccessInfo.  # noqa: E501
        :type: AWSIAMAccessRules
        """

        self._aws_iam_access_rules = aws_iam_access_rules

    @property
    def azure_ad_access_rules(self):
        """Gets the azure_ad_access_rules of this AuthMethodAccessInfo.  # noqa: E501


        :return: The azure_ad_access_rules of this AuthMethodAccessInfo.  # noqa: E501
        :rtype: AzureADAccessRules
        """
        return self._azure_ad_access_rules

    @azure_ad_access_rules.setter
    def azure_ad_access_rules(self, azure_ad_access_rules):
        """Sets the azure_ad_access_rules of this AuthMethodAccessInfo.


        :param azure_ad_access_rules: The azure_ad_access_rules of this AuthMethodAccessInfo.  # noqa: E501
        :type: AzureADAccessRules
        """

        self._azure_ad_access_rules = azure_ad_access_rules

    @property
    def cert_access_rules(self):
        """Gets the cert_access_rules of this AuthMethodAccessInfo.  # noqa: E501


        :return: The cert_access_rules of this AuthMethodAccessInfo.  # noqa: E501
        :rtype: CertAccessRules
        """
        return self._cert_access_rules

    @cert_access_rules.setter
    def cert_access_rules(self, cert_access_rules):
        """Sets the cert_access_rules of this AuthMethodAccessInfo.


        :param cert_access_rules: The cert_access_rules of this AuthMethodAccessInfo.  # noqa: E501
        :type: CertAccessRules
        """

        self._cert_access_rules = cert_access_rules

    @property
    def cidr_whitelist(self):
        """Gets the cidr_whitelist of this AuthMethodAccessInfo.  # noqa: E501


        :return: The cidr_whitelist of this AuthMethodAccessInfo.  # noqa: E501
        :rtype: str
        """
        return self._cidr_whitelist

    @cidr_whitelist.setter
    def cidr_whitelist(self, cidr_whitelist):
        """Sets the cidr_whitelist of this AuthMethodAccessInfo.


        :param cidr_whitelist: The cidr_whitelist of this AuthMethodAccessInfo.  # noqa: E501
        :type: str
        """

        self._cidr_whitelist = cidr_whitelist

    @property
    def email_pass_access_rules(self):
        """Gets the email_pass_access_rules of this AuthMethodAccessInfo.  # noqa: E501


        :return: The email_pass_access_rules of this AuthMethodAccessInfo.  # noqa: E501
        :rtype: EmailPassAccessRules
        """
        return self._email_pass_access_rules

    @email_pass_access_rules.setter
    def email_pass_access_rules(self, email_pass_access_rules):
        """Sets the email_pass_access_rules of this AuthMethodAccessInfo.


        :param email_pass_access_rules: The email_pass_access_rules of this AuthMethodAccessInfo.  # noqa: E501
        :type: EmailPassAccessRules
        """

        self._email_pass_access_rules = email_pass_access_rules

    @property
    def force_sub_claims(self):
        """Gets the force_sub_claims of this AuthMethodAccessInfo.  # noqa: E501

        if true the role associated with this auth method must include sub claims  # noqa: E501

        :return: The force_sub_claims of this AuthMethodAccessInfo.  # noqa: E501
        :rtype: bool
        """
        return self._force_sub_claims

    @force_sub_claims.setter
    def force_sub_claims(self, force_sub_claims):
        """Sets the force_sub_claims of this AuthMethodAccessInfo.

        if true the role associated with this auth method must include sub claims  # noqa: E501

        :param force_sub_claims: The force_sub_claims of this AuthMethodAccessInfo.  # noqa: E501
        :type: bool
        """

        self._force_sub_claims = force_sub_claims

    @property
    def gcp_access_rules(self):
        """Gets the gcp_access_rules of this AuthMethodAccessInfo.  # noqa: E501


        :return: The gcp_access_rules of this AuthMethodAccessInfo.  # noqa: E501
        :rtype: GCPAccessRules
        """
        return self._gcp_access_rules

    @gcp_access_rules.setter
    def gcp_access_rules(self, gcp_access_rules):
        """Sets the gcp_access_rules of this AuthMethodAccessInfo.


        :param gcp_access_rules: The gcp_access_rules of this AuthMethodAccessInfo.  # noqa: E501
        :type: GCPAccessRules
        """

        self._gcp_access_rules = gcp_access_rules

    @property
    def gw_cidr_whitelist(self):
        """Gets the gw_cidr_whitelist of this AuthMethodAccessInfo.  # noqa: E501


        :return: The gw_cidr_whitelist of this AuthMethodAccessInfo.  # noqa: E501
        :rtype: str
        """
        return self._gw_cidr_whitelist

    @gw_cidr_whitelist.setter
    def gw_cidr_whitelist(self, gw_cidr_whitelist):
        """Sets the gw_cidr_whitelist of this AuthMethodAccessInfo.


        :param gw_cidr_whitelist: The gw_cidr_whitelist of this AuthMethodAccessInfo.  # noqa: E501
        :type: str
        """

        self._gw_cidr_whitelist = gw_cidr_whitelist

    @property
    def huawei_access_rules(self):
        """Gets the huawei_access_rules of this AuthMethodAccessInfo.  # noqa: E501


        :return: The huawei_access_rules of this AuthMethodAccessInfo.  # noqa: E501
        :rtype: HuaweiAccessRules
        """
        return self._huawei_access_rules

    @huawei_access_rules.setter
    def huawei_access_rules(self, huawei_access_rules):
        """Sets the huawei_access_rules of this AuthMethodAccessInfo.


        :param huawei_access_rules: The huawei_access_rules of this AuthMethodAccessInfo.  # noqa: E501
        :type: HuaweiAccessRules
        """

        self._huawei_access_rules = huawei_access_rules

    @property
    def jwt_ttl(self):
        """Gets the jwt_ttl of this AuthMethodAccessInfo.  # noqa: E501


        :return: The jwt_ttl of this AuthMethodAccessInfo.  # noqa: E501
        :rtype: int
        """
        return self._jwt_ttl

    @jwt_ttl.setter
    def jwt_ttl(self, jwt_ttl):
        """Sets the jwt_ttl of this AuthMethodAccessInfo.


        :param jwt_ttl: The jwt_ttl of this AuthMethodAccessInfo.  # noqa: E501
        :type: int
        """

        self._jwt_ttl = jwt_ttl

    @property
    def k8s_access_rules(self):
        """Gets the k8s_access_rules of this AuthMethodAccessInfo.  # noqa: E501


        :return: The k8s_access_rules of this AuthMethodAccessInfo.  # noqa: E501
        :rtype: KubernetesAccessRules
        """
        return self._k8s_access_rules

    @k8s_access_rules.setter
    def k8s_access_rules(self, k8s_access_rules):
        """Sets the k8s_access_rules of this AuthMethodAccessInfo.


        :param k8s_access_rules: The k8s_access_rules of this AuthMethodAccessInfo.  # noqa: E501
        :type: KubernetesAccessRules
        """

        self._k8s_access_rules = k8s_access_rules

    @property
    def ldap_access_rules(self):
        """Gets the ldap_access_rules of this AuthMethodAccessInfo.  # noqa: E501


        :return: The ldap_access_rules of this AuthMethodAccessInfo.  # noqa: E501
        :rtype: LDAPAccessRules
        """
        return self._ldap_access_rules

    @ldap_access_rules.setter
    def ldap_access_rules(self, ldap_access_rules):
        """Sets the ldap_access_rules of this AuthMethodAccessInfo.


        :param ldap_access_rules: The ldap_access_rules of this AuthMethodAccessInfo.  # noqa: E501
        :type: LDAPAccessRules
        """

        self._ldap_access_rules = ldap_access_rules

    @property
    def oauth2_access_rules(self):
        """Gets the oauth2_access_rules of this AuthMethodAccessInfo.  # noqa: E501


        :return: The oauth2_access_rules of this AuthMethodAccessInfo.  # noqa: E501
        :rtype: OAuth2AccessRules
        """
        return self._oauth2_access_rules

    @oauth2_access_rules.setter
    def oauth2_access_rules(self, oauth2_access_rules):
        """Sets the oauth2_access_rules of this AuthMethodAccessInfo.


        :param oauth2_access_rules: The oauth2_access_rules of this AuthMethodAccessInfo.  # noqa: E501
        :type: OAuth2AccessRules
        """

        self._oauth2_access_rules = oauth2_access_rules

    @property
    def oci_access_rules(self):
        """Gets the oci_access_rules of this AuthMethodAccessInfo.  # noqa: E501


        :return: The oci_access_rules of this AuthMethodAccessInfo.  # noqa: E501
        :rtype: OCIAccessRules
        """
        return self._oci_access_rules

    @oci_access_rules.setter
    def oci_access_rules(self, oci_access_rules):
        """Sets the oci_access_rules of this AuthMethodAccessInfo.


        :param oci_access_rules: The oci_access_rules of this AuthMethodAccessInfo.  # noqa: E501
        :type: OCIAccessRules
        """

        self._oci_access_rules = oci_access_rules

    @property
    def oidc_access_rules(self):
        """Gets the oidc_access_rules of this AuthMethodAccessInfo.  # noqa: E501


        :return: The oidc_access_rules of this AuthMethodAccessInfo.  # noqa: E501
        :rtype: OIDCAccessRules
        """
        return self._oidc_access_rules

    @oidc_access_rules.setter
    def oidc_access_rules(self, oidc_access_rules):
        """Sets the oidc_access_rules of this AuthMethodAccessInfo.


        :param oidc_access_rules: The oidc_access_rules of this AuthMethodAccessInfo.  # noqa: E501
        :type: OIDCAccessRules
        """

        self._oidc_access_rules = oidc_access_rules

    @property
    def rules_type(self):
        """Gets the rules_type of this AuthMethodAccessInfo.  # noqa: E501


        :return: The rules_type of this AuthMethodAccessInfo.  # noqa: E501
        :rtype: str
        """
        return self._rules_type

    @rules_type.setter
    def rules_type(self, rules_type):
        """Sets the rules_type of this AuthMethodAccessInfo.


        :param rules_type: The rules_type of this AuthMethodAccessInfo.  # noqa: E501
        :type: str
        """

        self._rules_type = rules_type

    @property
    def saml_access_rules(self):
        """Gets the saml_access_rules of this AuthMethodAccessInfo.  # noqa: E501


        :return: The saml_access_rules of this AuthMethodAccessInfo.  # noqa: E501
        :rtype: SAMLAccessRules
        """
        return self._saml_access_rules

    @saml_access_rules.setter
    def saml_access_rules(self, saml_access_rules):
        """Sets the saml_access_rules of this AuthMethodAccessInfo.


        :param saml_access_rules: The saml_access_rules of this AuthMethodAccessInfo.  # noqa: E501
        :type: SAMLAccessRules
        """

        self._saml_access_rules = saml_access_rules

    @property
    def sub_claims_delimiters(self):
        """Gets the sub_claims_delimiters of this AuthMethodAccessInfo.  # noqa: E501


        :return: The sub_claims_delimiters of this AuthMethodAccessInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._sub_claims_delimiters

    @sub_claims_delimiters.setter
    def sub_claims_delimiters(self, sub_claims_delimiters):
        """Sets the sub_claims_delimiters of this AuthMethodAccessInfo.


        :param sub_claims_delimiters: The sub_claims_delimiters of this AuthMethodAccessInfo.  # noqa: E501
        :type: list[str]
        """

        self._sub_claims_delimiters = sub_claims_delimiters

    @property
    def universal_identity_access_rules(self):
        """Gets the universal_identity_access_rules of this AuthMethodAccessInfo.  # noqa: E501


        :return: The universal_identity_access_rules of this AuthMethodAccessInfo.  # noqa: E501
        :rtype: UniversalIdentityAccessRules
        """
        return self._universal_identity_access_rules

    @universal_identity_access_rules.setter
    def universal_identity_access_rules(self, universal_identity_access_rules):
        """Sets the universal_identity_access_rules of this AuthMethodAccessInfo.


        :param universal_identity_access_rules: The universal_identity_access_rules of this AuthMethodAccessInfo.  # noqa: E501
        :type: UniversalIdentityAccessRules
        """

        self._universal_identity_access_rules = universal_identity_access_rules

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
        if not isinstance(other, AuthMethodAccessInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuthMethodAccessInfo):
            return True

        return self.to_dict() != other.to_dict()
