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


class UpdateNativeK8STarget(object):
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
        'comment': 'str',
        'json': 'bool',
        'k8s_cluster_ca_cert': 'str',
        'k8s_cluster_endpoint': 'str',
        'k8s_cluster_token': 'str',
        'keep_prev_version': 'str',
        'key': 'str',
        'name': 'str',
        'new_name': 'str',
        'token': 'str',
        'uid_token': 'str',
        'update_version': 'bool'
    }

    attribute_map = {
        'comment': 'comment',
        'json': 'json',
        'k8s_cluster_ca_cert': 'k8s-cluster-ca-cert',
        'k8s_cluster_endpoint': 'k8s-cluster-endpoint',
        'k8s_cluster_token': 'k8s-cluster-token',
        'keep_prev_version': 'keep-prev-version',
        'key': 'key',
        'name': 'name',
        'new_name': 'new-name',
        'token': 'token',
        'uid_token': 'uid-token',
        'update_version': 'update-version'
    }

    def __init__(self, comment=None, json=None, k8s_cluster_ca_cert=None, k8s_cluster_endpoint=None, k8s_cluster_token=None, keep_prev_version=None, key=None, name=None, new_name=None, token=None, uid_token=None, update_version=None, local_vars_configuration=None):  # noqa: E501
        """UpdateNativeK8STarget - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._comment = None
        self._json = None
        self._k8s_cluster_ca_cert = None
        self._k8s_cluster_endpoint = None
        self._k8s_cluster_token = None
        self._keep_prev_version = None
        self._key = None
        self._name = None
        self._new_name = None
        self._token = None
        self._uid_token = None
        self._update_version = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        if json is not None:
            self.json = json
        self.k8s_cluster_ca_cert = k8s_cluster_ca_cert
        self.k8s_cluster_endpoint = k8s_cluster_endpoint
        self.k8s_cluster_token = k8s_cluster_token
        if keep_prev_version is not None:
            self.keep_prev_version = keep_prev_version
        if key is not None:
            self.key = key
        self.name = name
        if new_name is not None:
            self.new_name = new_name
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if update_version is not None:
            self.update_version = update_version

    @property
    def comment(self):
        """Gets the comment of this UpdateNativeK8STarget.  # noqa: E501

        Comment about the target  # noqa: E501

        :return: The comment of this UpdateNativeK8STarget.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this UpdateNativeK8STarget.

        Comment about the target  # noqa: E501

        :param comment: The comment of this UpdateNativeK8STarget.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def json(self):
        """Gets the json of this UpdateNativeK8STarget.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this UpdateNativeK8STarget.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this UpdateNativeK8STarget.

        Set output format to JSON  # noqa: E501

        :param json: The json of this UpdateNativeK8STarget.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def k8s_cluster_ca_cert(self):
        """Gets the k8s_cluster_ca_cert of this UpdateNativeK8STarget.  # noqa: E501

        K8S cluster CA certificate  # noqa: E501

        :return: The k8s_cluster_ca_cert of this UpdateNativeK8STarget.  # noqa: E501
        :rtype: str
        """
        return self._k8s_cluster_ca_cert

    @k8s_cluster_ca_cert.setter
    def k8s_cluster_ca_cert(self, k8s_cluster_ca_cert):
        """Sets the k8s_cluster_ca_cert of this UpdateNativeK8STarget.

        K8S cluster CA certificate  # noqa: E501

        :param k8s_cluster_ca_cert: The k8s_cluster_ca_cert of this UpdateNativeK8STarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and k8s_cluster_ca_cert is None:  # noqa: E501
            raise ValueError("Invalid value for `k8s_cluster_ca_cert`, must not be `None`")  # noqa: E501

        self._k8s_cluster_ca_cert = k8s_cluster_ca_cert

    @property
    def k8s_cluster_endpoint(self):
        """Gets the k8s_cluster_endpoint of this UpdateNativeK8STarget.  # noqa: E501

        K8S cluster URL endpoint  # noqa: E501

        :return: The k8s_cluster_endpoint of this UpdateNativeK8STarget.  # noqa: E501
        :rtype: str
        """
        return self._k8s_cluster_endpoint

    @k8s_cluster_endpoint.setter
    def k8s_cluster_endpoint(self, k8s_cluster_endpoint):
        """Sets the k8s_cluster_endpoint of this UpdateNativeK8STarget.

        K8S cluster URL endpoint  # noqa: E501

        :param k8s_cluster_endpoint: The k8s_cluster_endpoint of this UpdateNativeK8STarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and k8s_cluster_endpoint is None:  # noqa: E501
            raise ValueError("Invalid value for `k8s_cluster_endpoint`, must not be `None`")  # noqa: E501

        self._k8s_cluster_endpoint = k8s_cluster_endpoint

    @property
    def k8s_cluster_token(self):
        """Gets the k8s_cluster_token of this UpdateNativeK8STarget.  # noqa: E501

        K8S cluster Bearer token  # noqa: E501

        :return: The k8s_cluster_token of this UpdateNativeK8STarget.  # noqa: E501
        :rtype: str
        """
        return self._k8s_cluster_token

    @k8s_cluster_token.setter
    def k8s_cluster_token(self, k8s_cluster_token):
        """Sets the k8s_cluster_token of this UpdateNativeK8STarget.

        K8S cluster Bearer token  # noqa: E501

        :param k8s_cluster_token: The k8s_cluster_token of this UpdateNativeK8STarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and k8s_cluster_token is None:  # noqa: E501
            raise ValueError("Invalid value for `k8s_cluster_token`, must not be `None`")  # noqa: E501

        self._k8s_cluster_token = k8s_cluster_token

    @property
    def keep_prev_version(self):
        """Gets the keep_prev_version of this UpdateNativeK8STarget.  # noqa: E501


        :return: The keep_prev_version of this UpdateNativeK8STarget.  # noqa: E501
        :rtype: str
        """
        return self._keep_prev_version

    @keep_prev_version.setter
    def keep_prev_version(self, keep_prev_version):
        """Sets the keep_prev_version of this UpdateNativeK8STarget.


        :param keep_prev_version: The keep_prev_version of this UpdateNativeK8STarget.  # noqa: E501
        :type: str
        """

        self._keep_prev_version = keep_prev_version

    @property
    def key(self):
        """Gets the key of this UpdateNativeK8STarget.  # noqa: E501

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :return: The key of this UpdateNativeK8STarget.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this UpdateNativeK8STarget.

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :param key: The key of this UpdateNativeK8STarget.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this UpdateNativeK8STarget.  # noqa: E501

        Target name  # noqa: E501

        :return: The name of this UpdateNativeK8STarget.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateNativeK8STarget.

        Target name  # noqa: E501

        :param name: The name of this UpdateNativeK8STarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def new_name(self):
        """Gets the new_name of this UpdateNativeK8STarget.  # noqa: E501

        New target name  # noqa: E501

        :return: The new_name of this UpdateNativeK8STarget.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this UpdateNativeK8STarget.

        New target name  # noqa: E501

        :param new_name: The new_name of this UpdateNativeK8STarget.  # noqa: E501
        :type: str
        """

        self._new_name = new_name

    @property
    def token(self):
        """Gets the token of this UpdateNativeK8STarget.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this UpdateNativeK8STarget.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this UpdateNativeK8STarget.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this UpdateNativeK8STarget.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this UpdateNativeK8STarget.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this UpdateNativeK8STarget.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this UpdateNativeK8STarget.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this UpdateNativeK8STarget.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def update_version(self):
        """Gets the update_version of this UpdateNativeK8STarget.  # noqa: E501

        Deprecated  # noqa: E501

        :return: The update_version of this UpdateNativeK8STarget.  # noqa: E501
        :rtype: bool
        """
        return self._update_version

    @update_version.setter
    def update_version(self, update_version):
        """Sets the update_version of this UpdateNativeK8STarget.

        Deprecated  # noqa: E501

        :param update_version: The update_version of this UpdateNativeK8STarget.  # noqa: E501
        :type: bool
        """

        self._update_version = update_version

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
        if not isinstance(other, UpdateNativeK8STarget):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateNativeK8STarget):
            return True

        return self.to_dict() != other.to_dict()
