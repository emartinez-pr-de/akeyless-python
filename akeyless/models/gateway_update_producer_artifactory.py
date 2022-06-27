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


class GatewayUpdateProducerArtifactory(object):
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
        'artifactory_admin_name': 'str',
        'artifactory_admin_pwd': 'str',
        'artifactory_token_audience': 'str',
        'artifactory_token_scope': 'str',
        'base_url': 'str',
        'delete_protection': 'str',
        'name': 'str',
        'new_name': 'str',
        'producer_encryption_key_name': 'str',
        'tags': 'list[str]',
        'target_name': 'str',
        'token': 'str',
        'uid_token': 'str',
        'user_ttl': 'str'
    }

    attribute_map = {
        'artifactory_admin_name': 'artifactory-admin-name',
        'artifactory_admin_pwd': 'artifactory-admin-pwd',
        'artifactory_token_audience': 'artifactory-token-audience',
        'artifactory_token_scope': 'artifactory-token-scope',
        'base_url': 'base-url',
        'delete_protection': 'delete_protection',
        'name': 'name',
        'new_name': 'new-name',
        'producer_encryption_key_name': 'producer-encryption-key-name',
        'tags': 'tags',
        'target_name': 'target-name',
        'token': 'token',
        'uid_token': 'uid-token',
        'user_ttl': 'user-ttl'
    }

    def __init__(self, artifactory_admin_name=None, artifactory_admin_pwd=None, artifactory_token_audience=None, artifactory_token_scope=None, base_url=None, delete_protection=None, name=None, new_name=None, producer_encryption_key_name=None, tags=None, target_name=None, token=None, uid_token=None, user_ttl='60m', local_vars_configuration=None):  # noqa: E501
        """GatewayUpdateProducerArtifactory - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._artifactory_admin_name = None
        self._artifactory_admin_pwd = None
        self._artifactory_token_audience = None
        self._artifactory_token_scope = None
        self._base_url = None
        self._delete_protection = None
        self._name = None
        self._new_name = None
        self._producer_encryption_key_name = None
        self._tags = None
        self._target_name = None
        self._token = None
        self._uid_token = None
        self._user_ttl = None
        self.discriminator = None

        if artifactory_admin_name is not None:
            self.artifactory_admin_name = artifactory_admin_name
        if artifactory_admin_pwd is not None:
            self.artifactory_admin_pwd = artifactory_admin_pwd
        self.artifactory_token_audience = artifactory_token_audience
        self.artifactory_token_scope = artifactory_token_scope
        if base_url is not None:
            self.base_url = base_url
        if delete_protection is not None:
            self.delete_protection = delete_protection
        self.name = name
        if new_name is not None:
            self.new_name = new_name
        if producer_encryption_key_name is not None:
            self.producer_encryption_key_name = producer_encryption_key_name
        if tags is not None:
            self.tags = tags
        if target_name is not None:
            self.target_name = target_name
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if user_ttl is not None:
            self.user_ttl = user_ttl

    @property
    def artifactory_admin_name(self):
        """Gets the artifactory_admin_name of this GatewayUpdateProducerArtifactory.  # noqa: E501

        Artifactory Admin Name  # noqa: E501

        :return: The artifactory_admin_name of this GatewayUpdateProducerArtifactory.  # noqa: E501
        :rtype: str
        """
        return self._artifactory_admin_name

    @artifactory_admin_name.setter
    def artifactory_admin_name(self, artifactory_admin_name):
        """Sets the artifactory_admin_name of this GatewayUpdateProducerArtifactory.

        Artifactory Admin Name  # noqa: E501

        :param artifactory_admin_name: The artifactory_admin_name of this GatewayUpdateProducerArtifactory.  # noqa: E501
        :type: str
        """

        self._artifactory_admin_name = artifactory_admin_name

    @property
    def artifactory_admin_pwd(self):
        """Gets the artifactory_admin_pwd of this GatewayUpdateProducerArtifactory.  # noqa: E501

        Artifactory Admin password  # noqa: E501

        :return: The artifactory_admin_pwd of this GatewayUpdateProducerArtifactory.  # noqa: E501
        :rtype: str
        """
        return self._artifactory_admin_pwd

    @artifactory_admin_pwd.setter
    def artifactory_admin_pwd(self, artifactory_admin_pwd):
        """Sets the artifactory_admin_pwd of this GatewayUpdateProducerArtifactory.

        Artifactory Admin password  # noqa: E501

        :param artifactory_admin_pwd: The artifactory_admin_pwd of this GatewayUpdateProducerArtifactory.  # noqa: E501
        :type: str
        """

        self._artifactory_admin_pwd = artifactory_admin_pwd

    @property
    def artifactory_token_audience(self):
        """Gets the artifactory_token_audience of this GatewayUpdateProducerArtifactory.  # noqa: E501

        Token Audience  # noqa: E501

        :return: The artifactory_token_audience of this GatewayUpdateProducerArtifactory.  # noqa: E501
        :rtype: str
        """
        return self._artifactory_token_audience

    @artifactory_token_audience.setter
    def artifactory_token_audience(self, artifactory_token_audience):
        """Sets the artifactory_token_audience of this GatewayUpdateProducerArtifactory.

        Token Audience  # noqa: E501

        :param artifactory_token_audience: The artifactory_token_audience of this GatewayUpdateProducerArtifactory.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and artifactory_token_audience is None:  # noqa: E501
            raise ValueError("Invalid value for `artifactory_token_audience`, must not be `None`")  # noqa: E501

        self._artifactory_token_audience = artifactory_token_audience

    @property
    def artifactory_token_scope(self):
        """Gets the artifactory_token_scope of this GatewayUpdateProducerArtifactory.  # noqa: E501

        Token Scope  # noqa: E501

        :return: The artifactory_token_scope of this GatewayUpdateProducerArtifactory.  # noqa: E501
        :rtype: str
        """
        return self._artifactory_token_scope

    @artifactory_token_scope.setter
    def artifactory_token_scope(self, artifactory_token_scope):
        """Sets the artifactory_token_scope of this GatewayUpdateProducerArtifactory.

        Token Scope  # noqa: E501

        :param artifactory_token_scope: The artifactory_token_scope of this GatewayUpdateProducerArtifactory.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and artifactory_token_scope is None:  # noqa: E501
            raise ValueError("Invalid value for `artifactory_token_scope`, must not be `None`")  # noqa: E501

        self._artifactory_token_scope = artifactory_token_scope

    @property
    def base_url(self):
        """Gets the base_url of this GatewayUpdateProducerArtifactory.  # noqa: E501

        Base URL  # noqa: E501

        :return: The base_url of this GatewayUpdateProducerArtifactory.  # noqa: E501
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """Sets the base_url of this GatewayUpdateProducerArtifactory.

        Base URL  # noqa: E501

        :param base_url: The base_url of this GatewayUpdateProducerArtifactory.  # noqa: E501
        :type: str
        """

        self._base_url = base_url

    @property
    def delete_protection(self):
        """Gets the delete_protection of this GatewayUpdateProducerArtifactory.  # noqa: E501

        Protection from accidental deletion of this item  # noqa: E501

        :return: The delete_protection of this GatewayUpdateProducerArtifactory.  # noqa: E501
        :rtype: str
        """
        return self._delete_protection

    @delete_protection.setter
    def delete_protection(self, delete_protection):
        """Sets the delete_protection of this GatewayUpdateProducerArtifactory.

        Protection from accidental deletion of this item  # noqa: E501

        :param delete_protection: The delete_protection of this GatewayUpdateProducerArtifactory.  # noqa: E501
        :type: str
        """

        self._delete_protection = delete_protection

    @property
    def name(self):
        """Gets the name of this GatewayUpdateProducerArtifactory.  # noqa: E501

        Producer name  # noqa: E501

        :return: The name of this GatewayUpdateProducerArtifactory.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GatewayUpdateProducerArtifactory.

        Producer name  # noqa: E501

        :param name: The name of this GatewayUpdateProducerArtifactory.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def new_name(self):
        """Gets the new_name of this GatewayUpdateProducerArtifactory.  # noqa: E501

        Producer name  # noqa: E501

        :return: The new_name of this GatewayUpdateProducerArtifactory.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this GatewayUpdateProducerArtifactory.

        Producer name  # noqa: E501

        :param new_name: The new_name of this GatewayUpdateProducerArtifactory.  # noqa: E501
        :type: str
        """

        self._new_name = new_name

    @property
    def producer_encryption_key_name(self):
        """Gets the producer_encryption_key_name of this GatewayUpdateProducerArtifactory.  # noqa: E501

        Dynamic producer encryption key  # noqa: E501

        :return: The producer_encryption_key_name of this GatewayUpdateProducerArtifactory.  # noqa: E501
        :rtype: str
        """
        return self._producer_encryption_key_name

    @producer_encryption_key_name.setter
    def producer_encryption_key_name(self, producer_encryption_key_name):
        """Sets the producer_encryption_key_name of this GatewayUpdateProducerArtifactory.

        Dynamic producer encryption key  # noqa: E501

        :param producer_encryption_key_name: The producer_encryption_key_name of this GatewayUpdateProducerArtifactory.  # noqa: E501
        :type: str
        """

        self._producer_encryption_key_name = producer_encryption_key_name

    @property
    def tags(self):
        """Gets the tags of this GatewayUpdateProducerArtifactory.  # noqa: E501

        List of the tags attached to this secret  # noqa: E501

        :return: The tags of this GatewayUpdateProducerArtifactory.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this GatewayUpdateProducerArtifactory.

        List of the tags attached to this secret  # noqa: E501

        :param tags: The tags of this GatewayUpdateProducerArtifactory.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def target_name(self):
        """Gets the target_name of this GatewayUpdateProducerArtifactory.  # noqa: E501

        Target name  # noqa: E501

        :return: The target_name of this GatewayUpdateProducerArtifactory.  # noqa: E501
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """Sets the target_name of this GatewayUpdateProducerArtifactory.

        Target name  # noqa: E501

        :param target_name: The target_name of this GatewayUpdateProducerArtifactory.  # noqa: E501
        :type: str
        """

        self._target_name = target_name

    @property
    def token(self):
        """Gets the token of this GatewayUpdateProducerArtifactory.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GatewayUpdateProducerArtifactory.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GatewayUpdateProducerArtifactory.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GatewayUpdateProducerArtifactory.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this GatewayUpdateProducerArtifactory.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GatewayUpdateProducerArtifactory.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GatewayUpdateProducerArtifactory.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GatewayUpdateProducerArtifactory.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def user_ttl(self):
        """Gets the user_ttl of this GatewayUpdateProducerArtifactory.  # noqa: E501

        User TTL  # noqa: E501

        :return: The user_ttl of this GatewayUpdateProducerArtifactory.  # noqa: E501
        :rtype: str
        """
        return self._user_ttl

    @user_ttl.setter
    def user_ttl(self, user_ttl):
        """Sets the user_ttl of this GatewayUpdateProducerArtifactory.

        User TTL  # noqa: E501

        :param user_ttl: The user_ttl of this GatewayUpdateProducerArtifactory.  # noqa: E501
        :type: str
        """

        self._user_ttl = user_ttl

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
        if not isinstance(other, GatewayUpdateProducerArtifactory):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayUpdateProducerArtifactory):
            return True

        return self.to_dict() != other.to_dict()
