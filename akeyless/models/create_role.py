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


class CreateRole(object):
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
        'analytics_access': 'str',
        'audit_access': 'str',
        'comment': 'str',
        'description': 'str',
        'gw_analytics_access': 'str',
        'json': 'bool',
        'name': 'str',
        'sra_reports_access': 'str',
        'token': 'str',
        'uid_token': 'str',
        'usage_reports_access': 'str'
    }

    attribute_map = {
        'analytics_access': 'analytics-access',
        'audit_access': 'audit-access',
        'comment': 'comment',
        'description': 'description',
        'gw_analytics_access': 'gw-analytics-access',
        'json': 'json',
        'name': 'name',
        'sra_reports_access': 'sra-reports-access',
        'token': 'token',
        'uid_token': 'uid-token',
        'usage_reports_access': 'usage-reports-access'
    }

    def __init__(self, analytics_access=None, audit_access=None, comment=None, description=None, gw_analytics_access=None, json=False, name=None, sra_reports_access=None, token=None, uid_token=None, usage_reports_access=None, local_vars_configuration=None):  # noqa: E501
        """CreateRole - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._analytics_access = None
        self._audit_access = None
        self._comment = None
        self._description = None
        self._gw_analytics_access = None
        self._json = None
        self._name = None
        self._sra_reports_access = None
        self._token = None
        self._uid_token = None
        self._usage_reports_access = None
        self.discriminator = None

        if analytics_access is not None:
            self.analytics_access = analytics_access
        if audit_access is not None:
            self.audit_access = audit_access
        if comment is not None:
            self.comment = comment
        if description is not None:
            self.description = description
        if gw_analytics_access is not None:
            self.gw_analytics_access = gw_analytics_access
        if json is not None:
            self.json = json
        self.name = name
        if sra_reports_access is not None:
            self.sra_reports_access = sra_reports_access
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if usage_reports_access is not None:
            self.usage_reports_access = usage_reports_access

    @property
    def analytics_access(self):
        """Gets the analytics_access of this CreateRole.  # noqa: E501

        Allow this role to view analytics. Currently only 'none', 'own', 'all' values are supported, allowing associated auth methods to view reports produced by the same auth methods.  # noqa: E501

        :return: The analytics_access of this CreateRole.  # noqa: E501
        :rtype: str
        """
        return self._analytics_access

    @analytics_access.setter
    def analytics_access(self, analytics_access):
        """Sets the analytics_access of this CreateRole.

        Allow this role to view analytics. Currently only 'none', 'own', 'all' values are supported, allowing associated auth methods to view reports produced by the same auth methods.  # noqa: E501

        :param analytics_access: The analytics_access of this CreateRole.  # noqa: E501
        :type: str
        """

        self._analytics_access = analytics_access

    @property
    def audit_access(self):
        """Gets the audit_access of this CreateRole.  # noqa: E501

        Allow this role to view audit logs. Currently only 'none', 'own' and 'all' values are supported, allowing associated auth methods to view audit logs produced by the same auth methods.  # noqa: E501

        :return: The audit_access of this CreateRole.  # noqa: E501
        :rtype: str
        """
        return self._audit_access

    @audit_access.setter
    def audit_access(self, audit_access):
        """Sets the audit_access of this CreateRole.

        Allow this role to view audit logs. Currently only 'none', 'own' and 'all' values are supported, allowing associated auth methods to view audit logs produced by the same auth methods.  # noqa: E501

        :param audit_access: The audit_access of this CreateRole.  # noqa: E501
        :type: str
        """

        self._audit_access = audit_access

    @property
    def comment(self):
        """Gets the comment of this CreateRole.  # noqa: E501

        Deprecated - use description  # noqa: E501

        :return: The comment of this CreateRole.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this CreateRole.

        Deprecated - use description  # noqa: E501

        :param comment: The comment of this CreateRole.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def description(self):
        """Gets the description of this CreateRole.  # noqa: E501

        Description of the object  # noqa: E501

        :return: The description of this CreateRole.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateRole.

        Description of the object  # noqa: E501

        :param description: The description of this CreateRole.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def gw_analytics_access(self):
        """Gets the gw_analytics_access of this CreateRole.  # noqa: E501

        Allow this role to view gw analytics. Currently only 'none', 'own', 'all' values are supported, allowing associated auth methods to view reports produced by the same auth methods.  # noqa: E501

        :return: The gw_analytics_access of this CreateRole.  # noqa: E501
        :rtype: str
        """
        return self._gw_analytics_access

    @gw_analytics_access.setter
    def gw_analytics_access(self, gw_analytics_access):
        """Sets the gw_analytics_access of this CreateRole.

        Allow this role to view gw analytics. Currently only 'none', 'own', 'all' values are supported, allowing associated auth methods to view reports produced by the same auth methods.  # noqa: E501

        :param gw_analytics_access: The gw_analytics_access of this CreateRole.  # noqa: E501
        :type: str
        """

        self._gw_analytics_access = gw_analytics_access

    @property
    def json(self):
        """Gets the json of this CreateRole.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this CreateRole.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this CreateRole.

        Set output format to JSON  # noqa: E501

        :param json: The json of this CreateRole.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def name(self):
        """Gets the name of this CreateRole.  # noqa: E501

        Role name  # noqa: E501

        :return: The name of this CreateRole.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateRole.

        Role name  # noqa: E501

        :param name: The name of this CreateRole.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def sra_reports_access(self):
        """Gets the sra_reports_access of this CreateRole.  # noqa: E501

        Allow this role to view SRA Clusters. Currently only 'none', 'own', 'all' values are supported.  # noqa: E501

        :return: The sra_reports_access of this CreateRole.  # noqa: E501
        :rtype: str
        """
        return self._sra_reports_access

    @sra_reports_access.setter
    def sra_reports_access(self, sra_reports_access):
        """Sets the sra_reports_access of this CreateRole.

        Allow this role to view SRA Clusters. Currently only 'none', 'own', 'all' values are supported.  # noqa: E501

        :param sra_reports_access: The sra_reports_access of this CreateRole.  # noqa: E501
        :type: str
        """

        self._sra_reports_access = sra_reports_access

    @property
    def token(self):
        """Gets the token of this CreateRole.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this CreateRole.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this CreateRole.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this CreateRole.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this CreateRole.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this CreateRole.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this CreateRole.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this CreateRole.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def usage_reports_access(self):
        """Gets the usage_reports_access of this CreateRole.  # noqa: E501

        Allow this role to view Usage Report. Currently only 'none' and 'all' values are supported.  # noqa: E501

        :return: The usage_reports_access of this CreateRole.  # noqa: E501
        :rtype: str
        """
        return self._usage_reports_access

    @usage_reports_access.setter
    def usage_reports_access(self, usage_reports_access):
        """Sets the usage_reports_access of this CreateRole.

        Allow this role to view Usage Report. Currently only 'none' and 'all' values are supported.  # noqa: E501

        :param usage_reports_access: The usage_reports_access of this CreateRole.  # noqa: E501
        :type: str
        """

        self._usage_reports_access = usage_reports_access

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
        if not isinstance(other, CreateRole):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateRole):
            return True

        return self.to_dict() != other.to_dict()
