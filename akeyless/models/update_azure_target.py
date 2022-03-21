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


class UpdateAzureTarget(object):
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
        'client_id': 'str',
        'client_secret': 'str',
        'comment': 'str',
        'keep_prev_version': 'str',
        'key': 'str',
        'name': 'str',
        'new_name': 'str',
        'tenant_id': 'str',
        'token': 'str',
        'uid_token': 'str',
        'update_version': 'bool',
        'use_gw_cloud_identity': 'bool'
    }

    attribute_map = {
        'client_id': 'client-id',
        'client_secret': 'client-secret',
        'comment': 'comment',
        'keep_prev_version': 'keep-prev-version',
        'key': 'key',
        'name': 'name',
        'new_name': 'new-name',
        'tenant_id': 'tenant-id',
        'token': 'token',
        'uid_token': 'uid-token',
        'update_version': 'update-version',
        'use_gw_cloud_identity': 'use-gw-cloud-identity'
    }

    def __init__(self, client_id=None, client_secret=None, comment=None, keep_prev_version=None, key=None, name=None, new_name=None, tenant_id=None, token=None, uid_token=None, update_version=None, use_gw_cloud_identity=None, local_vars_configuration=None):  # noqa: E501
        """UpdateAzureTarget - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._client_id = None
        self._client_secret = None
        self._comment = None
        self._keep_prev_version = None
        self._key = None
        self._name = None
        self._new_name = None
        self._tenant_id = None
        self._token = None
        self._uid_token = None
        self._update_version = None
        self._use_gw_cloud_identity = None
        self.discriminator = None

        if client_id is not None:
            self.client_id = client_id
        if client_secret is not None:
            self.client_secret = client_secret
        if comment is not None:
            self.comment = comment
        if keep_prev_version is not None:
            self.keep_prev_version = keep_prev_version
        if key is not None:
            self.key = key
        self.name = name
        if new_name is not None:
            self.new_name = new_name
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if update_version is not None:
            self.update_version = update_version
        if use_gw_cloud_identity is not None:
            self.use_gw_cloud_identity = use_gw_cloud_identity

    @property
    def client_id(self):
        """Gets the client_id of this UpdateAzureTarget.  # noqa: E501


        :return: The client_id of this UpdateAzureTarget.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this UpdateAzureTarget.


        :param client_id: The client_id of this UpdateAzureTarget.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def client_secret(self):
        """Gets the client_secret of this UpdateAzureTarget.  # noqa: E501


        :return: The client_secret of this UpdateAzureTarget.  # noqa: E501
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this UpdateAzureTarget.


        :param client_secret: The client_secret of this UpdateAzureTarget.  # noqa: E501
        :type: str
        """

        self._client_secret = client_secret

    @property
    def comment(self):
        """Gets the comment of this UpdateAzureTarget.  # noqa: E501

        Comment about the target  # noqa: E501

        :return: The comment of this UpdateAzureTarget.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this UpdateAzureTarget.

        Comment about the target  # noqa: E501

        :param comment: The comment of this UpdateAzureTarget.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def keep_prev_version(self):
        """Gets the keep_prev_version of this UpdateAzureTarget.  # noqa: E501


        :return: The keep_prev_version of this UpdateAzureTarget.  # noqa: E501
        :rtype: str
        """
        return self._keep_prev_version

    @keep_prev_version.setter
    def keep_prev_version(self, keep_prev_version):
        """Sets the keep_prev_version of this UpdateAzureTarget.


        :param keep_prev_version: The keep_prev_version of this UpdateAzureTarget.  # noqa: E501
        :type: str
        """

        self._keep_prev_version = keep_prev_version

    @property
    def key(self):
        """Gets the key of this UpdateAzureTarget.  # noqa: E501

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :return: The key of this UpdateAzureTarget.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this UpdateAzureTarget.

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :param key: The key of this UpdateAzureTarget.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this UpdateAzureTarget.  # noqa: E501

        Target name  # noqa: E501

        :return: The name of this UpdateAzureTarget.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateAzureTarget.

        Target name  # noqa: E501

        :param name: The name of this UpdateAzureTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def new_name(self):
        """Gets the new_name of this UpdateAzureTarget.  # noqa: E501

        New target name  # noqa: E501

        :return: The new_name of this UpdateAzureTarget.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this UpdateAzureTarget.

        New target name  # noqa: E501

        :param new_name: The new_name of this UpdateAzureTarget.  # noqa: E501
        :type: str
        """

        self._new_name = new_name

    @property
    def tenant_id(self):
        """Gets the tenant_id of this UpdateAzureTarget.  # noqa: E501


        :return: The tenant_id of this UpdateAzureTarget.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this UpdateAzureTarget.


        :param tenant_id: The tenant_id of this UpdateAzureTarget.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def token(self):
        """Gets the token of this UpdateAzureTarget.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this UpdateAzureTarget.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this UpdateAzureTarget.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this UpdateAzureTarget.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this UpdateAzureTarget.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this UpdateAzureTarget.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this UpdateAzureTarget.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this UpdateAzureTarget.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def update_version(self):
        """Gets the update_version of this UpdateAzureTarget.  # noqa: E501

        Deprecated  # noqa: E501

        :return: The update_version of this UpdateAzureTarget.  # noqa: E501
        :rtype: bool
        """
        return self._update_version

    @update_version.setter
    def update_version(self, update_version):
        """Sets the update_version of this UpdateAzureTarget.

        Deprecated  # noqa: E501

        :param update_version: The update_version of this UpdateAzureTarget.  # noqa: E501
        :type: bool
        """

        self._update_version = update_version

    @property
    def use_gw_cloud_identity(self):
        """Gets the use_gw_cloud_identity of this UpdateAzureTarget.  # noqa: E501


        :return: The use_gw_cloud_identity of this UpdateAzureTarget.  # noqa: E501
        :rtype: bool
        """
        return self._use_gw_cloud_identity

    @use_gw_cloud_identity.setter
    def use_gw_cloud_identity(self, use_gw_cloud_identity):
        """Sets the use_gw_cloud_identity of this UpdateAzureTarget.


        :param use_gw_cloud_identity: The use_gw_cloud_identity of this UpdateAzureTarget.  # noqa: E501
        :type: bool
        """

        self._use_gw_cloud_identity = use_gw_cloud_identity

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
        if not isinstance(other, UpdateAzureTarget):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateAzureTarget):
            return True

        return self.to_dict() != other.to_dict()
