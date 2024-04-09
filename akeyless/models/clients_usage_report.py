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


class ClientsUsageReport(object):
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
        'account_id': 'str',
        'clients': 'list[ClientUsageInfo]',
        'product': 'str',
        'time': 'datetime',
        'total_clients': 'int'
    }

    attribute_map = {
        'account_id': 'account_id',
        'clients': 'clients',
        'product': 'product',
        'time': 'time',
        'total_clients': 'total_clients'
    }

    def __init__(self, account_id=None, clients=None, product=None, time=None, total_clients=None, local_vars_configuration=None):  # noqa: E501
        """ClientsUsageReport - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._clients = None
        self._product = None
        self._time = None
        self._total_clients = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if clients is not None:
            self.clients = clients
        if product is not None:
            self.product = product
        if time is not None:
            self.time = time
        if total_clients is not None:
            self.total_clients = total_clients

    @property
    def account_id(self):
        """Gets the account_id of this ClientsUsageReport.  # noqa: E501


        :return: The account_id of this ClientsUsageReport.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ClientsUsageReport.


        :param account_id: The account_id of this ClientsUsageReport.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def clients(self):
        """Gets the clients of this ClientsUsageReport.  # noqa: E501


        :return: The clients of this ClientsUsageReport.  # noqa: E501
        :rtype: list[ClientUsageInfo]
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """Sets the clients of this ClientsUsageReport.


        :param clients: The clients of this ClientsUsageReport.  # noqa: E501
        :type: list[ClientUsageInfo]
        """

        self._clients = clients

    @property
    def product(self):
        """Gets the product of this ClientsUsageReport.  # noqa: E501


        :return: The product of this ClientsUsageReport.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this ClientsUsageReport.


        :param product: The product of this ClientsUsageReport.  # noqa: E501
        :type: str
        """

        self._product = product

    @property
    def time(self):
        """Gets the time of this ClientsUsageReport.  # noqa: E501


        :return: The time of this ClientsUsageReport.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ClientsUsageReport.


        :param time: The time of this ClientsUsageReport.  # noqa: E501
        :type: datetime
        """

        self._time = time

    @property
    def total_clients(self):
        """Gets the total_clients of this ClientsUsageReport.  # noqa: E501


        :return: The total_clients of this ClientsUsageReport.  # noqa: E501
        :rtype: int
        """
        return self._total_clients

    @total_clients.setter
    def total_clients(self, total_clients):
        """Sets the total_clients of this ClientsUsageReport.


        :param total_clients: The total_clients of this ClientsUsageReport.  # noqa: E501
        :type: int
        """

        self._total_clients = total_clients

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
        if not isinstance(other, ClientsUsageReport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClientsUsageReport):
            return True

        return self.to_dict() != other.to_dict()
