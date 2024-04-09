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


class CreateArtifactoryTarget(object):
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
        'base_url': 'str',
        'comment': 'str',
        'description': 'str',
        'json': 'bool',
        'key': 'str',
        'max_versions': 'str',
        'name': 'str',
        'token': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'artifactory_admin_name': 'artifactory-admin-name',
        'artifactory_admin_pwd': 'artifactory-admin-pwd',
        'base_url': 'base-url',
        'comment': 'comment',
        'description': 'description',
        'json': 'json',
        'key': 'key',
        'max_versions': 'max-versions',
        'name': 'name',
        'token': 'token',
        'uid_token': 'uid-token'
    }

    def __init__(self, artifactory_admin_name=None, artifactory_admin_pwd=None, base_url=None, comment=None, description=None, json=False, key=None, max_versions=None, name=None, token=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """CreateArtifactoryTarget - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._artifactory_admin_name = None
        self._artifactory_admin_pwd = None
        self._base_url = None
        self._comment = None
        self._description = None
        self._json = None
        self._key = None
        self._max_versions = None
        self._name = None
        self._token = None
        self._uid_token = None
        self.discriminator = None

        self.artifactory_admin_name = artifactory_admin_name
        self.artifactory_admin_pwd = artifactory_admin_pwd
        self.base_url = base_url
        if comment is not None:
            self.comment = comment
        if description is not None:
            self.description = description
        if json is not None:
            self.json = json
        if key is not None:
            self.key = key
        if max_versions is not None:
            self.max_versions = max_versions
        self.name = name
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def artifactory_admin_name(self):
        """Gets the artifactory_admin_name of this CreateArtifactoryTarget.  # noqa: E501

        Artifactory Admin Name  # noqa: E501

        :return: The artifactory_admin_name of this CreateArtifactoryTarget.  # noqa: E501
        :rtype: str
        """
        return self._artifactory_admin_name

    @artifactory_admin_name.setter
    def artifactory_admin_name(self, artifactory_admin_name):
        """Sets the artifactory_admin_name of this CreateArtifactoryTarget.

        Artifactory Admin Name  # noqa: E501

        :param artifactory_admin_name: The artifactory_admin_name of this CreateArtifactoryTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and artifactory_admin_name is None:  # noqa: E501
            raise ValueError("Invalid value for `artifactory_admin_name`, must not be `None`")  # noqa: E501

        self._artifactory_admin_name = artifactory_admin_name

    @property
    def artifactory_admin_pwd(self):
        """Gets the artifactory_admin_pwd of this CreateArtifactoryTarget.  # noqa: E501

        Artifactory Admin password  # noqa: E501

        :return: The artifactory_admin_pwd of this CreateArtifactoryTarget.  # noqa: E501
        :rtype: str
        """
        return self._artifactory_admin_pwd

    @artifactory_admin_pwd.setter
    def artifactory_admin_pwd(self, artifactory_admin_pwd):
        """Sets the artifactory_admin_pwd of this CreateArtifactoryTarget.

        Artifactory Admin password  # noqa: E501

        :param artifactory_admin_pwd: The artifactory_admin_pwd of this CreateArtifactoryTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and artifactory_admin_pwd is None:  # noqa: E501
            raise ValueError("Invalid value for `artifactory_admin_pwd`, must not be `None`")  # noqa: E501

        self._artifactory_admin_pwd = artifactory_admin_pwd

    @property
    def base_url(self):
        """Gets the base_url of this CreateArtifactoryTarget.  # noqa: E501

        Base URL  # noqa: E501

        :return: The base_url of this CreateArtifactoryTarget.  # noqa: E501
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """Sets the base_url of this CreateArtifactoryTarget.

        Base URL  # noqa: E501

        :param base_url: The base_url of this CreateArtifactoryTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and base_url is None:  # noqa: E501
            raise ValueError("Invalid value for `base_url`, must not be `None`")  # noqa: E501

        self._base_url = base_url

    @property
    def comment(self):
        """Gets the comment of this CreateArtifactoryTarget.  # noqa: E501

        Deprecated - use description  # noqa: E501

        :return: The comment of this CreateArtifactoryTarget.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this CreateArtifactoryTarget.

        Deprecated - use description  # noqa: E501

        :param comment: The comment of this CreateArtifactoryTarget.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def description(self):
        """Gets the description of this CreateArtifactoryTarget.  # noqa: E501

        Description of the object  # noqa: E501

        :return: The description of this CreateArtifactoryTarget.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateArtifactoryTarget.

        Description of the object  # noqa: E501

        :param description: The description of this CreateArtifactoryTarget.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def json(self):
        """Gets the json of this CreateArtifactoryTarget.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this CreateArtifactoryTarget.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this CreateArtifactoryTarget.

        Set output format to JSON  # noqa: E501

        :param json: The json of this CreateArtifactoryTarget.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def key(self):
        """Gets the key of this CreateArtifactoryTarget.  # noqa: E501

        The name of a key used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :return: The key of this CreateArtifactoryTarget.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CreateArtifactoryTarget.

        The name of a key used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :param key: The key of this CreateArtifactoryTarget.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def max_versions(self):
        """Gets the max_versions of this CreateArtifactoryTarget.  # noqa: E501

        Set the maximum number of versions, limited by the account settings defaults.  # noqa: E501

        :return: The max_versions of this CreateArtifactoryTarget.  # noqa: E501
        :rtype: str
        """
        return self._max_versions

    @max_versions.setter
    def max_versions(self, max_versions):
        """Sets the max_versions of this CreateArtifactoryTarget.

        Set the maximum number of versions, limited by the account settings defaults.  # noqa: E501

        :param max_versions: The max_versions of this CreateArtifactoryTarget.  # noqa: E501
        :type: str
        """

        self._max_versions = max_versions

    @property
    def name(self):
        """Gets the name of this CreateArtifactoryTarget.  # noqa: E501

        Target name  # noqa: E501

        :return: The name of this CreateArtifactoryTarget.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateArtifactoryTarget.

        Target name  # noqa: E501

        :param name: The name of this CreateArtifactoryTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def token(self):
        """Gets the token of this CreateArtifactoryTarget.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this CreateArtifactoryTarget.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this CreateArtifactoryTarget.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this CreateArtifactoryTarget.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this CreateArtifactoryTarget.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this CreateArtifactoryTarget.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this CreateArtifactoryTarget.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this CreateArtifactoryTarget.  # noqa: E501
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
        if not isinstance(other, CreateArtifactoryTarget):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateArtifactoryTarget):
            return True

        return self.to_dict() != other.to_dict()
