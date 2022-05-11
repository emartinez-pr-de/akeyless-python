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


class UpdateAuthMethodAWSIAM(object):
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
        'bound_arn': 'list[str]',
        'bound_aws_account_id': 'list[str]',
        'bound_ips': 'list[str]',
        'bound_resource_id': 'list[str]',
        'bound_role_id': 'list[str]',
        'bound_role_name': 'list[str]',
        'bound_user_id': 'list[str]',
        'bound_user_name': 'list[str]',
        'force_sub_claims': 'bool',
        'jwt_ttl': 'int',
        'name': 'str',
        'new_name': 'str',
        'sts_url': 'str',
        'token': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'access_expires': 'access-expires',
        'bound_arn': 'bound-arn',
        'bound_aws_account_id': 'bound-aws-account-id',
        'bound_ips': 'bound-ips',
        'bound_resource_id': 'bound-resource-id',
        'bound_role_id': 'bound-role-id',
        'bound_role_name': 'bound-role-name',
        'bound_user_id': 'bound-user-id',
        'bound_user_name': 'bound-user-name',
        'force_sub_claims': 'force-sub-claims',
        'jwt_ttl': 'jwt-ttl',
        'name': 'name',
        'new_name': 'new-name',
        'sts_url': 'sts-url',
        'token': 'token',
        'uid_token': 'uid-token'
    }

    def __init__(self, access_expires=0, bound_arn=None, bound_aws_account_id=None, bound_ips=None, bound_resource_id=None, bound_role_id=None, bound_role_name=None, bound_user_id=None, bound_user_name=None, force_sub_claims=None, jwt_ttl=None, name=None, new_name=None, sts_url='https://sts.amazonaws.com', token=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """UpdateAuthMethodAWSIAM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_expires = None
        self._bound_arn = None
        self._bound_aws_account_id = None
        self._bound_ips = None
        self._bound_resource_id = None
        self._bound_role_id = None
        self._bound_role_name = None
        self._bound_user_id = None
        self._bound_user_name = None
        self._force_sub_claims = None
        self._jwt_ttl = None
        self._name = None
        self._new_name = None
        self._sts_url = None
        self._token = None
        self._uid_token = None
        self.discriminator = None

        if access_expires is not None:
            self.access_expires = access_expires
        if bound_arn is not None:
            self.bound_arn = bound_arn
        self.bound_aws_account_id = bound_aws_account_id
        if bound_ips is not None:
            self.bound_ips = bound_ips
        if bound_resource_id is not None:
            self.bound_resource_id = bound_resource_id
        if bound_role_id is not None:
            self.bound_role_id = bound_role_id
        if bound_role_name is not None:
            self.bound_role_name = bound_role_name
        if bound_user_id is not None:
            self.bound_user_id = bound_user_id
        if bound_user_name is not None:
            self.bound_user_name = bound_user_name
        if force_sub_claims is not None:
            self.force_sub_claims = force_sub_claims
        if jwt_ttl is not None:
            self.jwt_ttl = jwt_ttl
        self.name = name
        if new_name is not None:
            self.new_name = new_name
        if sts_url is not None:
            self.sts_url = sts_url
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def access_expires(self):
        """Gets the access_expires of this UpdateAuthMethodAWSIAM.  # noqa: E501

        Access expiration date in Unix timestamp (select 0 for access without expiry date)  # noqa: E501

        :return: The access_expires of this UpdateAuthMethodAWSIAM.  # noqa: E501
        :rtype: int
        """
        return self._access_expires

    @access_expires.setter
    def access_expires(self, access_expires):
        """Sets the access_expires of this UpdateAuthMethodAWSIAM.

        Access expiration date in Unix timestamp (select 0 for access without expiry date)  # noqa: E501

        :param access_expires: The access_expires of this UpdateAuthMethodAWSIAM.  # noqa: E501
        :type: int
        """

        self._access_expires = access_expires

    @property
    def bound_arn(self):
        """Gets the bound_arn of this UpdateAuthMethodAWSIAM.  # noqa: E501

        A list of full arns that the access is restricted to  # noqa: E501

        :return: The bound_arn of this UpdateAuthMethodAWSIAM.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_arn

    @bound_arn.setter
    def bound_arn(self, bound_arn):
        """Sets the bound_arn of this UpdateAuthMethodAWSIAM.

        A list of full arns that the access is restricted to  # noqa: E501

        :param bound_arn: The bound_arn of this UpdateAuthMethodAWSIAM.  # noqa: E501
        :type: list[str]
        """

        self._bound_arn = bound_arn

    @property
    def bound_aws_account_id(self):
        """Gets the bound_aws_account_id of this UpdateAuthMethodAWSIAM.  # noqa: E501

        A list of AWS account-IDs that the access is restricted to  # noqa: E501

        :return: The bound_aws_account_id of this UpdateAuthMethodAWSIAM.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_aws_account_id

    @bound_aws_account_id.setter
    def bound_aws_account_id(self, bound_aws_account_id):
        """Sets the bound_aws_account_id of this UpdateAuthMethodAWSIAM.

        A list of AWS account-IDs that the access is restricted to  # noqa: E501

        :param bound_aws_account_id: The bound_aws_account_id of this UpdateAuthMethodAWSIAM.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and bound_aws_account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `bound_aws_account_id`, must not be `None`")  # noqa: E501

        self._bound_aws_account_id = bound_aws_account_id

    @property
    def bound_ips(self):
        """Gets the bound_ips of this UpdateAuthMethodAWSIAM.  # noqa: E501

        A CIDR whitelist with the IPs that the access is restricted to  # noqa: E501

        :return: The bound_ips of this UpdateAuthMethodAWSIAM.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_ips

    @bound_ips.setter
    def bound_ips(self, bound_ips):
        """Sets the bound_ips of this UpdateAuthMethodAWSIAM.

        A CIDR whitelist with the IPs that the access is restricted to  # noqa: E501

        :param bound_ips: The bound_ips of this UpdateAuthMethodAWSIAM.  # noqa: E501
        :type: list[str]
        """

        self._bound_ips = bound_ips

    @property
    def bound_resource_id(self):
        """Gets the bound_resource_id of this UpdateAuthMethodAWSIAM.  # noqa: E501

        A list of full resource ids that the access is restricted to  # noqa: E501

        :return: The bound_resource_id of this UpdateAuthMethodAWSIAM.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_resource_id

    @bound_resource_id.setter
    def bound_resource_id(self, bound_resource_id):
        """Sets the bound_resource_id of this UpdateAuthMethodAWSIAM.

        A list of full resource ids that the access is restricted to  # noqa: E501

        :param bound_resource_id: The bound_resource_id of this UpdateAuthMethodAWSIAM.  # noqa: E501
        :type: list[str]
        """

        self._bound_resource_id = bound_resource_id

    @property
    def bound_role_id(self):
        """Gets the bound_role_id of this UpdateAuthMethodAWSIAM.  # noqa: E501

        A list of full role ids that the access is restricted to  # noqa: E501

        :return: The bound_role_id of this UpdateAuthMethodAWSIAM.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_role_id

    @bound_role_id.setter
    def bound_role_id(self, bound_role_id):
        """Sets the bound_role_id of this UpdateAuthMethodAWSIAM.

        A list of full role ids that the access is restricted to  # noqa: E501

        :param bound_role_id: The bound_role_id of this UpdateAuthMethodAWSIAM.  # noqa: E501
        :type: list[str]
        """

        self._bound_role_id = bound_role_id

    @property
    def bound_role_name(self):
        """Gets the bound_role_name of this UpdateAuthMethodAWSIAM.  # noqa: E501

        A list of full role-name that the access is restricted to  # noqa: E501

        :return: The bound_role_name of this UpdateAuthMethodAWSIAM.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_role_name

    @bound_role_name.setter
    def bound_role_name(self, bound_role_name):
        """Sets the bound_role_name of this UpdateAuthMethodAWSIAM.

        A list of full role-name that the access is restricted to  # noqa: E501

        :param bound_role_name: The bound_role_name of this UpdateAuthMethodAWSIAM.  # noqa: E501
        :type: list[str]
        """

        self._bound_role_name = bound_role_name

    @property
    def bound_user_id(self):
        """Gets the bound_user_id of this UpdateAuthMethodAWSIAM.  # noqa: E501

        A list of full user ids that the access is restricted to  # noqa: E501

        :return: The bound_user_id of this UpdateAuthMethodAWSIAM.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_user_id

    @bound_user_id.setter
    def bound_user_id(self, bound_user_id):
        """Sets the bound_user_id of this UpdateAuthMethodAWSIAM.

        A list of full user ids that the access is restricted to  # noqa: E501

        :param bound_user_id: The bound_user_id of this UpdateAuthMethodAWSIAM.  # noqa: E501
        :type: list[str]
        """

        self._bound_user_id = bound_user_id

    @property
    def bound_user_name(self):
        """Gets the bound_user_name of this UpdateAuthMethodAWSIAM.  # noqa: E501

        A list of full user-name that the access is restricted to  # noqa: E501

        :return: The bound_user_name of this UpdateAuthMethodAWSIAM.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_user_name

    @bound_user_name.setter
    def bound_user_name(self, bound_user_name):
        """Sets the bound_user_name of this UpdateAuthMethodAWSIAM.

        A list of full user-name that the access is restricted to  # noqa: E501

        :param bound_user_name: The bound_user_name of this UpdateAuthMethodAWSIAM.  # noqa: E501
        :type: list[str]
        """

        self._bound_user_name = bound_user_name

    @property
    def force_sub_claims(self):
        """Gets the force_sub_claims of this UpdateAuthMethodAWSIAM.  # noqa: E501

        if true: enforce role-association must include sub claims  # noqa: E501

        :return: The force_sub_claims of this UpdateAuthMethodAWSIAM.  # noqa: E501
        :rtype: bool
        """
        return self._force_sub_claims

    @force_sub_claims.setter
    def force_sub_claims(self, force_sub_claims):
        """Sets the force_sub_claims of this UpdateAuthMethodAWSIAM.

        if true: enforce role-association must include sub claims  # noqa: E501

        :param force_sub_claims: The force_sub_claims of this UpdateAuthMethodAWSIAM.  # noqa: E501
        :type: bool
        """

        self._force_sub_claims = force_sub_claims

    @property
    def jwt_ttl(self):
        """Gets the jwt_ttl of this UpdateAuthMethodAWSIAM.  # noqa: E501

        Jwt TTL  # noqa: E501

        :return: The jwt_ttl of this UpdateAuthMethodAWSIAM.  # noqa: E501
        :rtype: int
        """
        return self._jwt_ttl

    @jwt_ttl.setter
    def jwt_ttl(self, jwt_ttl):
        """Sets the jwt_ttl of this UpdateAuthMethodAWSIAM.

        Jwt TTL  # noqa: E501

        :param jwt_ttl: The jwt_ttl of this UpdateAuthMethodAWSIAM.  # noqa: E501
        :type: int
        """

        self._jwt_ttl = jwt_ttl

    @property
    def name(self):
        """Gets the name of this UpdateAuthMethodAWSIAM.  # noqa: E501

        Auth Method name  # noqa: E501

        :return: The name of this UpdateAuthMethodAWSIAM.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateAuthMethodAWSIAM.

        Auth Method name  # noqa: E501

        :param name: The name of this UpdateAuthMethodAWSIAM.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def new_name(self):
        """Gets the new_name of this UpdateAuthMethodAWSIAM.  # noqa: E501

        Auth Method new name  # noqa: E501

        :return: The new_name of this UpdateAuthMethodAWSIAM.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this UpdateAuthMethodAWSIAM.

        Auth Method new name  # noqa: E501

        :param new_name: The new_name of this UpdateAuthMethodAWSIAM.  # noqa: E501
        :type: str
        """

        self._new_name = new_name

    @property
    def sts_url(self):
        """Gets the sts_url of this UpdateAuthMethodAWSIAM.  # noqa: E501

        sts URL  # noqa: E501

        :return: The sts_url of this UpdateAuthMethodAWSIAM.  # noqa: E501
        :rtype: str
        """
        return self._sts_url

    @sts_url.setter
    def sts_url(self, sts_url):
        """Sets the sts_url of this UpdateAuthMethodAWSIAM.

        sts URL  # noqa: E501

        :param sts_url: The sts_url of this UpdateAuthMethodAWSIAM.  # noqa: E501
        :type: str
        """

        self._sts_url = sts_url

    @property
    def token(self):
        """Gets the token of this UpdateAuthMethodAWSIAM.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this UpdateAuthMethodAWSIAM.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this UpdateAuthMethodAWSIAM.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this UpdateAuthMethodAWSIAM.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this UpdateAuthMethodAWSIAM.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this UpdateAuthMethodAWSIAM.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this UpdateAuthMethodAWSIAM.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this UpdateAuthMethodAWSIAM.  # noqa: E501
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
        if not isinstance(other, UpdateAuthMethodAWSIAM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateAuthMethodAWSIAM):
            return True

        return self.to_dict() != other.to_dict()
