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


class GatewayRevokeTmpUsers(object):
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
        'host': 'str',
        'json': 'bool',
        'name': 'str',
        'revoke_all': 'bool',
        'soft_delete': 'bool',
        'tmp_creds_id': 'str',
        'token': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'host': 'host',
        'json': 'json',
        'name': 'name',
        'revoke_all': 'revoke-all',
        'soft_delete': 'soft-delete',
        'tmp_creds_id': 'tmp-creds-id',
        'token': 'token',
        'uid_token': 'uid-token'
    }

    def __init__(self, host=None, json=None, name=None, revoke_all=None, soft_delete=None, tmp_creds_id='demo_default_tmp_creds_id_for_sdk_bc', token=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """GatewayRevokeTmpUsers - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._host = None
        self._json = None
        self._name = None
        self._revoke_all = None
        self._soft_delete = None
        self._tmp_creds_id = None
        self._token = None
        self._uid_token = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if json is not None:
            self.json = json
        self.name = name
        if revoke_all is not None:
            self.revoke_all = revoke_all
        if soft_delete is not None:
            self.soft_delete = soft_delete
        self.tmp_creds_id = tmp_creds_id
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def host(self):
        """Gets the host of this GatewayRevokeTmpUsers.  # noqa: E501

        Deprecated: has no effect  # noqa: E501

        :return: The host of this GatewayRevokeTmpUsers.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this GatewayRevokeTmpUsers.

        Deprecated: has no effect  # noqa: E501

        :param host: The host of this GatewayRevokeTmpUsers.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def json(self):
        """Gets the json of this GatewayRevokeTmpUsers.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this GatewayRevokeTmpUsers.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this GatewayRevokeTmpUsers.

        Set output format to JSON  # noqa: E501

        :param json: The json of this GatewayRevokeTmpUsers.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def name(self):
        """Gets the name of this GatewayRevokeTmpUsers.  # noqa: E501

        Producer Name  # noqa: E501

        :return: The name of this GatewayRevokeTmpUsers.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GatewayRevokeTmpUsers.

        Producer Name  # noqa: E501

        :param name: The name of this GatewayRevokeTmpUsers.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def revoke_all(self):
        """Gets the revoke_all of this GatewayRevokeTmpUsers.  # noqa: E501

        Revoke All Temp Creds  # noqa: E501

        :return: The revoke_all of this GatewayRevokeTmpUsers.  # noqa: E501
        :rtype: bool
        """
        return self._revoke_all

    @revoke_all.setter
    def revoke_all(self, revoke_all):
        """Sets the revoke_all of this GatewayRevokeTmpUsers.

        Revoke All Temp Creds  # noqa: E501

        :param revoke_all: The revoke_all of this GatewayRevokeTmpUsers.  # noqa: E501
        :type: bool
        """

        self._revoke_all = revoke_all

    @property
    def soft_delete(self):
        """Gets the soft_delete of this GatewayRevokeTmpUsers.  # noqa: E501

        Soft Delete  # noqa: E501

        :return: The soft_delete of this GatewayRevokeTmpUsers.  # noqa: E501
        :rtype: bool
        """
        return self._soft_delete

    @soft_delete.setter
    def soft_delete(self, soft_delete):
        """Sets the soft_delete of this GatewayRevokeTmpUsers.

        Soft Delete  # noqa: E501

        :param soft_delete: The soft_delete of this GatewayRevokeTmpUsers.  # noqa: E501
        :type: bool
        """

        self._soft_delete = soft_delete

    @property
    def tmp_creds_id(self):
        """Gets the tmp_creds_id of this GatewayRevokeTmpUsers.  # noqa: E501

        Tmp Creds ID  # noqa: E501

        :return: The tmp_creds_id of this GatewayRevokeTmpUsers.  # noqa: E501
        :rtype: str
        """
        return self._tmp_creds_id

    @tmp_creds_id.setter
    def tmp_creds_id(self, tmp_creds_id):
        """Sets the tmp_creds_id of this GatewayRevokeTmpUsers.

        Tmp Creds ID  # noqa: E501

        :param tmp_creds_id: The tmp_creds_id of this GatewayRevokeTmpUsers.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and tmp_creds_id is None:  # noqa: E501
            raise ValueError("Invalid value for `tmp_creds_id`, must not be `None`")  # noqa: E501

        self._tmp_creds_id = tmp_creds_id

    @property
    def token(self):
        """Gets the token of this GatewayRevokeTmpUsers.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GatewayRevokeTmpUsers.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GatewayRevokeTmpUsers.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GatewayRevokeTmpUsers.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this GatewayRevokeTmpUsers.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GatewayRevokeTmpUsers.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GatewayRevokeTmpUsers.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GatewayRevokeTmpUsers.  # noqa: E501
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
        if not isinstance(other, GatewayRevokeTmpUsers):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayRevokeTmpUsers):
            return True

        return self.to_dict() != other.to_dict()
