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


class GatewayUpdateK8SAuthConfigOutput(object):
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
        'cluster_id': 'str',
        'parts_change': 'ConfigChange',
        'total_hash': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'parts_change': 'parts_change',
        'total_hash': 'total_hash'
    }

    def __init__(self, cluster_id=None, parts_change=None, total_hash=None, local_vars_configuration=None):  # noqa: E501
        """GatewayUpdateK8SAuthConfigOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cluster_id = None
        self._parts_change = None
        self._total_hash = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if parts_change is not None:
            self.parts_change = parts_change
        if total_hash is not None:
            self.total_hash = total_hash

    @property
    def cluster_id(self):
        """Gets the cluster_id of this GatewayUpdateK8SAuthConfigOutput.  # noqa: E501


        :return: The cluster_id of this GatewayUpdateK8SAuthConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this GatewayUpdateK8SAuthConfigOutput.


        :param cluster_id: The cluster_id of this GatewayUpdateK8SAuthConfigOutput.  # noqa: E501
        :type: str
        """

        self._cluster_id = cluster_id

    @property
    def parts_change(self):
        """Gets the parts_change of this GatewayUpdateK8SAuthConfigOutput.  # noqa: E501


        :return: The parts_change of this GatewayUpdateK8SAuthConfigOutput.  # noqa: E501
        :rtype: ConfigChange
        """
        return self._parts_change

    @parts_change.setter
    def parts_change(self, parts_change):
        """Sets the parts_change of this GatewayUpdateK8SAuthConfigOutput.


        :param parts_change: The parts_change of this GatewayUpdateK8SAuthConfigOutput.  # noqa: E501
        :type: ConfigChange
        """

        self._parts_change = parts_change

    @property
    def total_hash(self):
        """Gets the total_hash of this GatewayUpdateK8SAuthConfigOutput.  # noqa: E501


        :return: The total_hash of this GatewayUpdateK8SAuthConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._total_hash

    @total_hash.setter
    def total_hash(self, total_hash):
        """Sets the total_hash of this GatewayUpdateK8SAuthConfigOutput.


        :param total_hash: The total_hash of this GatewayUpdateK8SAuthConfigOutput.  # noqa: E501
        :type: str
        """

        self._total_hash = total_hash

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
        if not isinstance(other, GatewayUpdateK8SAuthConfigOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayUpdateK8SAuthConfigOutput):
            return True

        return self.to_dict() != other.to_dict()
