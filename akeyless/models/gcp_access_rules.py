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


class GCPAccessRules(object):
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
        'audience': 'str',
        'bound_labels': 'dict(str, str)',
        'bound_projects': 'list[str]',
        'bound_regions': 'list[str]',
        'bound_service_accounts': 'list[str]',
        'bound_zones': 'list[str]',
        'service_account': 'str',
        'type': 'str'
    }

    attribute_map = {
        'audience': 'audience',
        'bound_labels': 'bound_labels',
        'bound_projects': 'bound_projects',
        'bound_regions': 'bound_regions',
        'bound_service_accounts': 'bound_service_accounts',
        'bound_zones': 'bound_zones',
        'service_account': 'service_account',
        'type': 'type'
    }

    def __init__(self, audience='akeyless.io', bound_labels=None, bound_projects=None, bound_regions=None, bound_service_accounts=None, bound_zones=None, service_account=None, type=None, local_vars_configuration=None):  # noqa: E501
        """GCPAccessRules - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._audience = None
        self._bound_labels = None
        self._bound_projects = None
        self._bound_regions = None
        self._bound_service_accounts = None
        self._bound_zones = None
        self._service_account = None
        self._type = None
        self.discriminator = None

        if audience is not None:
            self.audience = audience
        if bound_labels is not None:
            self.bound_labels = bound_labels
        if bound_projects is not None:
            self.bound_projects = bound_projects
        if bound_regions is not None:
            self.bound_regions = bound_regions
        if bound_service_accounts is not None:
            self.bound_service_accounts = bound_service_accounts
        if bound_zones is not None:
            self.bound_zones = bound_zones
        if service_account is not None:
            self.service_account = service_account
        if type is not None:
            self.type = type

    @property
    def audience(self):
        """Gets the audience of this GCPAccessRules.  # noqa: E501

        The audience in the JWT  # noqa: E501

        :return: The audience of this GCPAccessRules.  # noqa: E501
        :rtype: str
        """
        return self._audience

    @audience.setter
    def audience(self, audience):
        """Sets the audience of this GCPAccessRules.

        The audience in the JWT  # noqa: E501

        :param audience: The audience of this GCPAccessRules.  # noqa: E501
        :type: str
        """

        self._audience = audience

    @property
    def bound_labels(self):
        """Gets the bound_labels of this GCPAccessRules.  # noqa: E501

        A map of GCP labels formatted as \"key:value\" strings that must be set on authorized GCE instances. TODO: Because GCP labels are not currently ACL'd ....  # noqa: E501

        :return: The bound_labels of this GCPAccessRules.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._bound_labels

    @bound_labels.setter
    def bound_labels(self, bound_labels):
        """Sets the bound_labels of this GCPAccessRules.

        A map of GCP labels formatted as \"key:value\" strings that must be set on authorized GCE instances. TODO: Because GCP labels are not currently ACL'd ....  # noqa: E501

        :param bound_labels: The bound_labels of this GCPAccessRules.  # noqa: E501
        :type: dict(str, str)
        """

        self._bound_labels = bound_labels

    @property
    def bound_projects(self):
        """Gets the bound_projects of this GCPAccessRules.  # noqa: E501

        Human and Machine authentication section Array of GCP project IDs. Only entities belonging to any of the provided projects can authenticate.  # noqa: E501

        :return: The bound_projects of this GCPAccessRules.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_projects

    @bound_projects.setter
    def bound_projects(self, bound_projects):
        """Sets the bound_projects of this GCPAccessRules.

        Human and Machine authentication section Array of GCP project IDs. Only entities belonging to any of the provided projects can authenticate.  # noqa: E501

        :param bound_projects: The bound_projects of this GCPAccessRules.  # noqa: E501
        :type: list[str]
        """

        self._bound_projects = bound_projects

    @property
    def bound_regions(self):
        """Gets the bound_regions of this GCPAccessRules.  # noqa: E501

        List of regions that a GCE instance must belong to in order to be authenticated. TODO: If bound_instance_groups is provided, it is assumed to be a regional group and the group must belong to this region. If bound_zones are provided, this attribute is ignored.  # noqa: E501

        :return: The bound_regions of this GCPAccessRules.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_regions

    @bound_regions.setter
    def bound_regions(self, bound_regions):
        """Sets the bound_regions of this GCPAccessRules.

        List of regions that a GCE instance must belong to in order to be authenticated. TODO: If bound_instance_groups is provided, it is assumed to be a regional group and the group must belong to this region. If bound_zones are provided, this attribute is ignored.  # noqa: E501

        :param bound_regions: The bound_regions of this GCPAccessRules.  # noqa: E501
        :type: list[str]
        """

        self._bound_regions = bound_regions

    @property
    def bound_service_accounts(self):
        """Gets the bound_service_accounts of this GCPAccessRules.  # noqa: E501

        === Human authentication section === List of service accounts the service account must be part of in order to be authenticated  # noqa: E501

        :return: The bound_service_accounts of this GCPAccessRules.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_service_accounts

    @bound_service_accounts.setter
    def bound_service_accounts(self, bound_service_accounts):
        """Sets the bound_service_accounts of this GCPAccessRules.

        === Human authentication section === List of service accounts the service account must be part of in order to be authenticated  # noqa: E501

        :param bound_service_accounts: The bound_service_accounts of this GCPAccessRules.  # noqa: E501
        :type: list[str]
        """

        self._bound_service_accounts = bound_service_accounts

    @property
    def bound_zones(self):
        """Gets the bound_zones of this GCPAccessRules.  # noqa: E501

        === Machine authentication section === List of zones that a GCE instance must belong to in order to be authenticated. TODO: If bound_instance_groups is provided, it is assumed to be a zonal group and the group must belong to this zone.  # noqa: E501

        :return: The bound_zones of this GCPAccessRules.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_zones

    @bound_zones.setter
    def bound_zones(self, bound_zones):
        """Sets the bound_zones of this GCPAccessRules.

        === Machine authentication section === List of zones that a GCE instance must belong to in order to be authenticated. TODO: If bound_instance_groups is provided, it is assumed to be a zonal group and the group must belong to this zone.  # noqa: E501

        :param bound_zones: The bound_zones of this GCPAccessRules.  # noqa: E501
        :type: list[str]
        """

        self._bound_zones = bound_zones

    @property
    def service_account(self):
        """Gets the service_account of this GCPAccessRules.  # noqa: E501

        ServiceAccount holds the credentials file contents to be used by Akeyless to validate IAM (Human) and GCE (Machine) logins against GCP base64 encoded string  # noqa: E501

        :return: The service_account of this GCPAccessRules.  # noqa: E501
        :rtype: str
        """
        return self._service_account

    @service_account.setter
    def service_account(self, service_account):
        """Sets the service_account of this GCPAccessRules.

        ServiceAccount holds the credentials file contents to be used by Akeyless to validate IAM (Human) and GCE (Machine) logins against GCP base64 encoded string  # noqa: E501

        :param service_account: The service_account of this GCPAccessRules.  # noqa: E501
        :type: str
        """

        self._service_account = service_account

    @property
    def type(self):
        """Gets the type of this GCPAccessRules.  # noqa: E501


        :return: The type of this GCPAccessRules.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GCPAccessRules.


        :param type: The type of this GCPAccessRules.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, GCPAccessRules):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GCPAccessRules):
            return True

        return self.to_dict() != other.to_dict()
