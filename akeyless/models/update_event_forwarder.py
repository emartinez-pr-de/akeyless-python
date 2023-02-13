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


class UpdateEventForwarder(object):
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
        'admin_name': 'str',
        'description': 'str',
        'email_to': 'str',
        'enable': 'str',
        'event_source_locations': 'list[str]',
        'event_types': 'list[str]',
        'host': 'str',
        'json': 'bool',
        'name': 'str',
        'new_comment': 'str',
        'new_name': 'str',
        'token': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'admin_name': 'admin-name',
        'description': 'description',
        'email_to': 'email-to',
        'enable': 'enable',
        'event_source_locations': 'event-source-locations',
        'event_types': 'event-types',
        'host': 'host',
        'json': 'json',
        'name': 'name',
        'new_comment': 'new-comment',
        'new_name': 'new-name',
        'token': 'token',
        'uid_token': 'uid-token'
    }

    def __init__(self, admin_name=None, description='default_comment', email_to=None, enable='true', event_source_locations=None, event_types=None, host=None, json=False, name=None, new_comment='default_comment', new_name=None, token=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """UpdateEventForwarder - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._admin_name = None
        self._description = None
        self._email_to = None
        self._enable = None
        self._event_source_locations = None
        self._event_types = None
        self._host = None
        self._json = None
        self._name = None
        self._new_comment = None
        self._new_name = None
        self._token = None
        self._uid_token = None
        self.discriminator = None

        if admin_name is not None:
            self.admin_name = admin_name
        if description is not None:
            self.description = description
        if email_to is not None:
            self.email_to = email_to
        if enable is not None:
            self.enable = enable
        if event_source_locations is not None:
            self.event_source_locations = event_source_locations
        if event_types is not None:
            self.event_types = event_types
        if host is not None:
            self.host = host
        if json is not None:
            self.json = json
        self.name = name
        if new_comment is not None:
            self.new_comment = new_comment
        if new_name is not None:
            self.new_name = new_name
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def admin_name(self):
        """Gets the admin_name of this UpdateEventForwarder.  # noqa: E501

        Workstation Admin Name  # noqa: E501

        :return: The admin_name of this UpdateEventForwarder.  # noqa: E501
        :rtype: str
        """
        return self._admin_name

    @admin_name.setter
    def admin_name(self, admin_name):
        """Sets the admin_name of this UpdateEventForwarder.

        Workstation Admin Name  # noqa: E501

        :param admin_name: The admin_name of this UpdateEventForwarder.  # noqa: E501
        :type: str
        """

        self._admin_name = admin_name

    @property
    def description(self):
        """Gets the description of this UpdateEventForwarder.  # noqa: E501

        Description of the object  # noqa: E501

        :return: The description of this UpdateEventForwarder.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateEventForwarder.

        Description of the object  # noqa: E501

        :param description: The description of this UpdateEventForwarder.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def email_to(self):
        """Gets the email_to of this UpdateEventForwarder.  # noqa: E501

        A comma seperated list of email addresses to send event to (relevant only for \\\"email\\\" Event Forwarder)  # noqa: E501

        :return: The email_to of this UpdateEventForwarder.  # noqa: E501
        :rtype: str
        """
        return self._email_to

    @email_to.setter
    def email_to(self, email_to):
        """Sets the email_to of this UpdateEventForwarder.

        A comma seperated list of email addresses to send event to (relevant only for \\\"email\\\" Event Forwarder)  # noqa: E501

        :param email_to: The email_to of this UpdateEventForwarder.  # noqa: E501
        :type: str
        """

        self._email_to = email_to

    @property
    def enable(self):
        """Gets the enable of this UpdateEventForwarder.  # noqa: E501

        Enable/Disable Event Forwarder [true/false]  # noqa: E501

        :return: The enable of this UpdateEventForwarder.  # noqa: E501
        :rtype: str
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this UpdateEventForwarder.

        Enable/Disable Event Forwarder [true/false]  # noqa: E501

        :param enable: The enable of this UpdateEventForwarder.  # noqa: E501
        :type: str
        """

        self._enable = enable

    @property
    def event_source_locations(self):
        """Gets the event_source_locations of this UpdateEventForwarder.  # noqa: E501

        Event sources  # noqa: E501

        :return: The event_source_locations of this UpdateEventForwarder.  # noqa: E501
        :rtype: list[str]
        """
        return self._event_source_locations

    @event_source_locations.setter
    def event_source_locations(self, event_source_locations):
        """Sets the event_source_locations of this UpdateEventForwarder.

        Event sources  # noqa: E501

        :param event_source_locations: The event_source_locations of this UpdateEventForwarder.  # noqa: E501
        :type: list[str]
        """

        self._event_source_locations = event_source_locations

    @property
    def event_types(self):
        """Gets the event_types of this UpdateEventForwarder.  # noqa: E501

        Event types  # noqa: E501

        :return: The event_types of this UpdateEventForwarder.  # noqa: E501
        :rtype: list[str]
        """
        return self._event_types

    @event_types.setter
    def event_types(self, event_types):
        """Sets the event_types of this UpdateEventForwarder.

        Event types  # noqa: E501

        :param event_types: The event_types of this UpdateEventForwarder.  # noqa: E501
        :type: list[str]
        """

        self._event_types = event_types

    @property
    def host(self):
        """Gets the host of this UpdateEventForwarder.  # noqa: E501

        Workstation Host  # noqa: E501

        :return: The host of this UpdateEventForwarder.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this UpdateEventForwarder.

        Workstation Host  # noqa: E501

        :param host: The host of this UpdateEventForwarder.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def json(self):
        """Gets the json of this UpdateEventForwarder.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this UpdateEventForwarder.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this UpdateEventForwarder.

        Set output format to JSON  # noqa: E501

        :param json: The json of this UpdateEventForwarder.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def name(self):
        """Gets the name of this UpdateEventForwarder.  # noqa: E501

        EventForwarder name  # noqa: E501

        :return: The name of this UpdateEventForwarder.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateEventForwarder.

        EventForwarder name  # noqa: E501

        :param name: The name of this UpdateEventForwarder.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def new_comment(self):
        """Gets the new_comment of this UpdateEventForwarder.  # noqa: E501

        Deprecated - use description  # noqa: E501

        :return: The new_comment of this UpdateEventForwarder.  # noqa: E501
        :rtype: str
        """
        return self._new_comment

    @new_comment.setter
    def new_comment(self, new_comment):
        """Sets the new_comment of this UpdateEventForwarder.

        Deprecated - use description  # noqa: E501

        :param new_comment: The new_comment of this UpdateEventForwarder.  # noqa: E501
        :type: str
        """

        self._new_comment = new_comment

    @property
    def new_name(self):
        """Gets the new_name of this UpdateEventForwarder.  # noqa: E501

        New EventForwarder name  # noqa: E501

        :return: The new_name of this UpdateEventForwarder.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this UpdateEventForwarder.

        New EventForwarder name  # noqa: E501

        :param new_name: The new_name of this UpdateEventForwarder.  # noqa: E501
        :type: str
        """

        self._new_name = new_name

    @property
    def token(self):
        """Gets the token of this UpdateEventForwarder.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this UpdateEventForwarder.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this UpdateEventForwarder.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this UpdateEventForwarder.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this UpdateEventForwarder.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this UpdateEventForwarder.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this UpdateEventForwarder.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this UpdateEventForwarder.  # noqa: E501
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
        if not isinstance(other, UpdateEventForwarder):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateEventForwarder):
            return True

        return self.to_dict() != other.to_dict()
