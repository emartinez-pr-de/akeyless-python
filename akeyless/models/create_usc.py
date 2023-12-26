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


class CreateUSC(object):
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
        'azure_kv_name': 'str',
        'delete_protection': 'str',
        'description': 'str',
        'json': 'bool',
        'k8s_namespace': 'str',
        'name': 'str',
        'tags': 'list[str]',
        'target_to_associate': 'str',
        'token': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'azure_kv_name': 'azure-kv-name',
        'delete_protection': 'delete_protection',
        'description': 'description',
        'json': 'json',
        'k8s_namespace': 'k8s-namespace',
        'name': 'name',
        'tags': 'tags',
        'target_to_associate': 'target-to-associate',
        'token': 'token',
        'uid_token': 'uid-token'
    }

    def __init__(self, azure_kv_name=None, delete_protection=None, description=None, json=False, k8s_namespace=None, name=None, tags=None, target_to_associate=None, token=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """CreateUSC - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._azure_kv_name = None
        self._delete_protection = None
        self._description = None
        self._json = None
        self._k8s_namespace = None
        self._name = None
        self._tags = None
        self._target_to_associate = None
        self._token = None
        self._uid_token = None
        self.discriminator = None

        if azure_kv_name is not None:
            self.azure_kv_name = azure_kv_name
        if delete_protection is not None:
            self.delete_protection = delete_protection
        if description is not None:
            self.description = description
        if json is not None:
            self.json = json
        if k8s_namespace is not None:
            self.k8s_namespace = k8s_namespace
        self.name = name
        if tags is not None:
            self.tags = tags
        self.target_to_associate = target_to_associate
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def azure_kv_name(self):
        """Gets the azure_kv_name of this CreateUSC.  # noqa: E501

        Azure Key Vault name (Relevant only for Azure targets)  # noqa: E501

        :return: The azure_kv_name of this CreateUSC.  # noqa: E501
        :rtype: str
        """
        return self._azure_kv_name

    @azure_kv_name.setter
    def azure_kv_name(self, azure_kv_name):
        """Sets the azure_kv_name of this CreateUSC.

        Azure Key Vault name (Relevant only for Azure targets)  # noqa: E501

        :param azure_kv_name: The azure_kv_name of this CreateUSC.  # noqa: E501
        :type: str
        """

        self._azure_kv_name = azure_kv_name

    @property
    def delete_protection(self):
        """Gets the delete_protection of this CreateUSC.  # noqa: E501

        Protection from accidental deletion of this item [true/false]  # noqa: E501

        :return: The delete_protection of this CreateUSC.  # noqa: E501
        :rtype: str
        """
        return self._delete_protection

    @delete_protection.setter
    def delete_protection(self, delete_protection):
        """Sets the delete_protection of this CreateUSC.

        Protection from accidental deletion of this item [true/false]  # noqa: E501

        :param delete_protection: The delete_protection of this CreateUSC.  # noqa: E501
        :type: str
        """

        self._delete_protection = delete_protection

    @property
    def description(self):
        """Gets the description of this CreateUSC.  # noqa: E501

        Description of the Universal Secrets Connector  # noqa: E501

        :return: The description of this CreateUSC.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateUSC.

        Description of the Universal Secrets Connector  # noqa: E501

        :param description: The description of this CreateUSC.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def json(self):
        """Gets the json of this CreateUSC.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this CreateUSC.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this CreateUSC.

        Set output format to JSON  # noqa: E501

        :param json: The json of this CreateUSC.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def k8s_namespace(self):
        """Gets the k8s_namespace of this CreateUSC.  # noqa: E501

        K8s namespace (Relevant to Kubernetes targets)  # noqa: E501

        :return: The k8s_namespace of this CreateUSC.  # noqa: E501
        :rtype: str
        """
        return self._k8s_namespace

    @k8s_namespace.setter
    def k8s_namespace(self, k8s_namespace):
        """Sets the k8s_namespace of this CreateUSC.

        K8s namespace (Relevant to Kubernetes targets)  # noqa: E501

        :param k8s_namespace: The k8s_namespace of this CreateUSC.  # noqa: E501
        :type: str
        """

        self._k8s_namespace = k8s_namespace

    @property
    def name(self):
        """Gets the name of this CreateUSC.  # noqa: E501

        Universal Secrets Connector name  # noqa: E501

        :return: The name of this CreateUSC.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateUSC.

        Universal Secrets Connector name  # noqa: E501

        :param name: The name of this CreateUSC.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def tags(self):
        """Gets the tags of this CreateUSC.  # noqa: E501

        List of the tags attached to this Universal Secrets Connector  # noqa: E501

        :return: The tags of this CreateUSC.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateUSC.

        List of the tags attached to this Universal Secrets Connector  # noqa: E501

        :param tags: The tags of this CreateUSC.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def target_to_associate(self):
        """Gets the target_to_associate of this CreateUSC.  # noqa: E501

        Target Universal Secrets Connector to connect  # noqa: E501

        :return: The target_to_associate of this CreateUSC.  # noqa: E501
        :rtype: str
        """
        return self._target_to_associate

    @target_to_associate.setter
    def target_to_associate(self, target_to_associate):
        """Sets the target_to_associate of this CreateUSC.

        Target Universal Secrets Connector to connect  # noqa: E501

        :param target_to_associate: The target_to_associate of this CreateUSC.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and target_to_associate is None:  # noqa: E501
            raise ValueError("Invalid value for `target_to_associate`, must not be `None`")  # noqa: E501

        self._target_to_associate = target_to_associate

    @property
    def token(self):
        """Gets the token of this CreateUSC.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this CreateUSC.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this CreateUSC.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this CreateUSC.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this CreateUSC.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this CreateUSC.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this CreateUSC.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this CreateUSC.  # noqa: E501
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
        if not isinstance(other, CreateUSC):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateUSC):
            return True

        return self.to_dict() != other.to_dict()
