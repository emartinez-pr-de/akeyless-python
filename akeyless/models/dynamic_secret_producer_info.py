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


class DynamicSecretProducerInfo(object):
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
        'failure_message': 'str',
        'gw_cluster_id': 'int',
        'k8s_allowed_namespaces': 'str',
        'k8s_dynamic_mode': 'bool',
        'producer_last_keep_alive': 'str',
        'producer_metadata': 'str',
        'producer_status': 'str',
        'producer_type': 'str',
        'user_ttl': 'str'
    }

    attribute_map = {
        'failure_message': 'failure_message',
        'gw_cluster_id': 'gw_cluster_id',
        'k8s_allowed_namespaces': 'k8s_allowed_namespaces',
        'k8s_dynamic_mode': 'k8s_dynamic_mode',
        'producer_last_keep_alive': 'producer_last_keep_alive',
        'producer_metadata': 'producer_metadata',
        'producer_status': 'producer_status',
        'producer_type': 'producer_type',
        'user_ttl': 'user_ttl'
    }

    def __init__(self, failure_message=None, gw_cluster_id=None, k8s_allowed_namespaces=None, k8s_dynamic_mode=None, producer_last_keep_alive=None, producer_metadata=None, producer_status=None, producer_type=None, user_ttl=None, local_vars_configuration=None):  # noqa: E501
        """DynamicSecretProducerInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._failure_message = None
        self._gw_cluster_id = None
        self._k8s_allowed_namespaces = None
        self._k8s_dynamic_mode = None
        self._producer_last_keep_alive = None
        self._producer_metadata = None
        self._producer_status = None
        self._producer_type = None
        self._user_ttl = None
        self.discriminator = None

        if failure_message is not None:
            self.failure_message = failure_message
        if gw_cluster_id is not None:
            self.gw_cluster_id = gw_cluster_id
        if k8s_allowed_namespaces is not None:
            self.k8s_allowed_namespaces = k8s_allowed_namespaces
        if k8s_dynamic_mode is not None:
            self.k8s_dynamic_mode = k8s_dynamic_mode
        if producer_last_keep_alive is not None:
            self.producer_last_keep_alive = producer_last_keep_alive
        if producer_metadata is not None:
            self.producer_metadata = producer_metadata
        if producer_status is not None:
            self.producer_status = producer_status
        if producer_type is not None:
            self.producer_type = producer_type
        if user_ttl is not None:
            self.user_ttl = user_ttl

    @property
    def failure_message(self):
        """Gets the failure_message of this DynamicSecretProducerInfo.  # noqa: E501


        :return: The failure_message of this DynamicSecretProducerInfo.  # noqa: E501
        :rtype: str
        """
        return self._failure_message

    @failure_message.setter
    def failure_message(self, failure_message):
        """Sets the failure_message of this DynamicSecretProducerInfo.


        :param failure_message: The failure_message of this DynamicSecretProducerInfo.  # noqa: E501
        :type: str
        """

        self._failure_message = failure_message

    @property
    def gw_cluster_id(self):
        """Gets the gw_cluster_id of this DynamicSecretProducerInfo.  # noqa: E501


        :return: The gw_cluster_id of this DynamicSecretProducerInfo.  # noqa: E501
        :rtype: int
        """
        return self._gw_cluster_id

    @gw_cluster_id.setter
    def gw_cluster_id(self, gw_cluster_id):
        """Sets the gw_cluster_id of this DynamicSecretProducerInfo.


        :param gw_cluster_id: The gw_cluster_id of this DynamicSecretProducerInfo.  # noqa: E501
        :type: int
        """

        self._gw_cluster_id = gw_cluster_id

    @property
    def k8s_allowed_namespaces(self):
        """Gets the k8s_allowed_namespaces of this DynamicSecretProducerInfo.  # noqa: E501

        Relevant only for generic k8s producer  # noqa: E501

        :return: The k8s_allowed_namespaces of this DynamicSecretProducerInfo.  # noqa: E501
        :rtype: str
        """
        return self._k8s_allowed_namespaces

    @k8s_allowed_namespaces.setter
    def k8s_allowed_namespaces(self, k8s_allowed_namespaces):
        """Sets the k8s_allowed_namespaces of this DynamicSecretProducerInfo.

        Relevant only for generic k8s producer  # noqa: E501

        :param k8s_allowed_namespaces: The k8s_allowed_namespaces of this DynamicSecretProducerInfo.  # noqa: E501
        :type: str
        """

        self._k8s_allowed_namespaces = k8s_allowed_namespaces

    @property
    def k8s_dynamic_mode(self):
        """Gets the k8s_dynamic_mode of this DynamicSecretProducerInfo.  # noqa: E501

        Relevant only for generic k8s producer  # noqa: E501

        :return: The k8s_dynamic_mode of this DynamicSecretProducerInfo.  # noqa: E501
        :rtype: bool
        """
        return self._k8s_dynamic_mode

    @k8s_dynamic_mode.setter
    def k8s_dynamic_mode(self, k8s_dynamic_mode):
        """Sets the k8s_dynamic_mode of this DynamicSecretProducerInfo.

        Relevant only for generic k8s producer  # noqa: E501

        :param k8s_dynamic_mode: The k8s_dynamic_mode of this DynamicSecretProducerInfo.  # noqa: E501
        :type: bool
        """

        self._k8s_dynamic_mode = k8s_dynamic_mode

    @property
    def producer_last_keep_alive(self):
        """Gets the producer_last_keep_alive of this DynamicSecretProducerInfo.  # noqa: E501


        :return: The producer_last_keep_alive of this DynamicSecretProducerInfo.  # noqa: E501
        :rtype: str
        """
        return self._producer_last_keep_alive

    @producer_last_keep_alive.setter
    def producer_last_keep_alive(self, producer_last_keep_alive):
        """Sets the producer_last_keep_alive of this DynamicSecretProducerInfo.


        :param producer_last_keep_alive: The producer_last_keep_alive of this DynamicSecretProducerInfo.  # noqa: E501
        :type: str
        """

        self._producer_last_keep_alive = producer_last_keep_alive

    @property
    def producer_metadata(self):
        """Gets the producer_metadata of this DynamicSecretProducerInfo.  # noqa: E501


        :return: The producer_metadata of this DynamicSecretProducerInfo.  # noqa: E501
        :rtype: str
        """
        return self._producer_metadata

    @producer_metadata.setter
    def producer_metadata(self, producer_metadata):
        """Sets the producer_metadata of this DynamicSecretProducerInfo.


        :param producer_metadata: The producer_metadata of this DynamicSecretProducerInfo.  # noqa: E501
        :type: str
        """

        self._producer_metadata = producer_metadata

    @property
    def producer_status(self):
        """Gets the producer_status of this DynamicSecretProducerInfo.  # noqa: E501

        RotationStatus defines types of rotation Status  # noqa: E501

        :return: The producer_status of this DynamicSecretProducerInfo.  # noqa: E501
        :rtype: str
        """
        return self._producer_status

    @producer_status.setter
    def producer_status(self, producer_status):
        """Sets the producer_status of this DynamicSecretProducerInfo.

        RotationStatus defines types of rotation Status  # noqa: E501

        :param producer_status: The producer_status of this DynamicSecretProducerInfo.  # noqa: E501
        :type: str
        """

        self._producer_status = producer_status

    @property
    def producer_type(self):
        """Gets the producer_type of this DynamicSecretProducerInfo.  # noqa: E501


        :return: The producer_type of this DynamicSecretProducerInfo.  # noqa: E501
        :rtype: str
        """
        return self._producer_type

    @producer_type.setter
    def producer_type(self, producer_type):
        """Sets the producer_type of this DynamicSecretProducerInfo.


        :param producer_type: The producer_type of this DynamicSecretProducerInfo.  # noqa: E501
        :type: str
        """

        self._producer_type = producer_type

    @property
    def user_ttl(self):
        """Gets the user_ttl of this DynamicSecretProducerInfo.  # noqa: E501


        :return: The user_ttl of this DynamicSecretProducerInfo.  # noqa: E501
        :rtype: str
        """
        return self._user_ttl

    @user_ttl.setter
    def user_ttl(self, user_ttl):
        """Sets the user_ttl of this DynamicSecretProducerInfo.


        :param user_ttl: The user_ttl of this DynamicSecretProducerInfo.  # noqa: E501
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
        if not isinstance(other, DynamicSecretProducerInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DynamicSecretProducerInfo):
            return True

        return self.to_dict() != other.to_dict()
