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


class EventForwarderUpdateEmail(object):
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
        'auth_methods_event_source_locations': 'list[str]',
        'description': 'str',
        'email_to': 'str',
        'enable': 'str',
        'event_types': 'list[str]',
        'gateways_event_source_locations': 'list[str]',
        'items_event_source_locations': 'list[str]',
        'json': 'bool',
        'keep_prev_version': 'str',
        'key': 'str',
        'name': 'str',
        'new_name': 'str',
        'override_url': 'str',
        'targets_event_source_locations': 'list[str]',
        'token': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'auth_methods_event_source_locations': 'auth-methods-event-source-locations',
        'description': 'description',
        'email_to': 'email-to',
        'enable': 'enable',
        'event_types': 'event-types',
        'gateways_event_source_locations': 'gateways-event-source-locations',
        'items_event_source_locations': 'items-event-source-locations',
        'json': 'json',
        'keep_prev_version': 'keep-prev-version',
        'key': 'key',
        'name': 'name',
        'new_name': 'new-name',
        'override_url': 'override-url',
        'targets_event_source_locations': 'targets-event-source-locations',
        'token': 'token',
        'uid_token': 'uid-token'
    }

    def __init__(self, auth_methods_event_source_locations=None, description=None, email_to=None, enable='true', event_types=None, gateways_event_source_locations=None, items_event_source_locations=None, json=False, keep_prev_version=None, key=None, name=None, new_name=None, override_url=None, targets_event_source_locations=None, token=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """EventForwarderUpdateEmail - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._auth_methods_event_source_locations = None
        self._description = None
        self._email_to = None
        self._enable = None
        self._event_types = None
        self._gateways_event_source_locations = None
        self._items_event_source_locations = None
        self._json = None
        self._keep_prev_version = None
        self._key = None
        self._name = None
        self._new_name = None
        self._override_url = None
        self._targets_event_source_locations = None
        self._token = None
        self._uid_token = None
        self.discriminator = None

        if auth_methods_event_source_locations is not None:
            self.auth_methods_event_source_locations = auth_methods_event_source_locations
        if description is not None:
            self.description = description
        if email_to is not None:
            self.email_to = email_to
        if enable is not None:
            self.enable = enable
        if event_types is not None:
            self.event_types = event_types
        self.gateways_event_source_locations = gateways_event_source_locations
        if items_event_source_locations is not None:
            self.items_event_source_locations = items_event_source_locations
        if json is not None:
            self.json = json
        if keep_prev_version is not None:
            self.keep_prev_version = keep_prev_version
        if key is not None:
            self.key = key
        self.name = name
        if new_name is not None:
            self.new_name = new_name
        if override_url is not None:
            self.override_url = override_url
        if targets_event_source_locations is not None:
            self.targets_event_source_locations = targets_event_source_locations
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def auth_methods_event_source_locations(self):
        """Gets the auth_methods_event_source_locations of this EventForwarderUpdateEmail.  # noqa: E501

        Auth Method Event sources  # noqa: E501

        :return: The auth_methods_event_source_locations of this EventForwarderUpdateEmail.  # noqa: E501
        :rtype: list[str]
        """
        return self._auth_methods_event_source_locations

    @auth_methods_event_source_locations.setter
    def auth_methods_event_source_locations(self, auth_methods_event_source_locations):
        """Sets the auth_methods_event_source_locations of this EventForwarderUpdateEmail.

        Auth Method Event sources  # noqa: E501

        :param auth_methods_event_source_locations: The auth_methods_event_source_locations of this EventForwarderUpdateEmail.  # noqa: E501
        :type: list[str]
        """

        self._auth_methods_event_source_locations = auth_methods_event_source_locations

    @property
    def description(self):
        """Gets the description of this EventForwarderUpdateEmail.  # noqa: E501

        Description of the object  # noqa: E501

        :return: The description of this EventForwarderUpdateEmail.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EventForwarderUpdateEmail.

        Description of the object  # noqa: E501

        :param description: The description of this EventForwarderUpdateEmail.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def email_to(self):
        """Gets the email_to of this EventForwarderUpdateEmail.  # noqa: E501

        A comma seperated list of email addresses to send event to  # noqa: E501

        :return: The email_to of this EventForwarderUpdateEmail.  # noqa: E501
        :rtype: str
        """
        return self._email_to

    @email_to.setter
    def email_to(self, email_to):
        """Sets the email_to of this EventForwarderUpdateEmail.

        A comma seperated list of email addresses to send event to  # noqa: E501

        :param email_to: The email_to of this EventForwarderUpdateEmail.  # noqa: E501
        :type: str
        """

        self._email_to = email_to

    @property
    def enable(self):
        """Gets the enable of this EventForwarderUpdateEmail.  # noqa: E501

        Enable/Disable Event Forwarder [true/false]  # noqa: E501

        :return: The enable of this EventForwarderUpdateEmail.  # noqa: E501
        :rtype: str
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this EventForwarderUpdateEmail.

        Enable/Disable Event Forwarder [true/false]  # noqa: E501

        :param enable: The enable of this EventForwarderUpdateEmail.  # noqa: E501
        :type: str
        """

        self._enable = enable

    @property
    def event_types(self):
        """Gets the event_types of this EventForwarderUpdateEmail.  # noqa: E501

        List of event types to notify about [request-access, certificate-pending-expiration, certificate-expired, certificate-provisioning-success, certificate-provisioning-failure, auth-method-pending-expiration, auth-method-expired, rotated-secret-success, rotated-secret-failure, dynamic-secret-failure, multi-auth-failure, uid-rotation-failure, apply-justification, email-auth-method-approved, usage, rotation-usage, gateway-inactive, static-secret-updated]  # noqa: E501

        :return: The event_types of this EventForwarderUpdateEmail.  # noqa: E501
        :rtype: list[str]
        """
        return self._event_types

    @event_types.setter
    def event_types(self, event_types):
        """Sets the event_types of this EventForwarderUpdateEmail.

        List of event types to notify about [request-access, certificate-pending-expiration, certificate-expired, certificate-provisioning-success, certificate-provisioning-failure, auth-method-pending-expiration, auth-method-expired, rotated-secret-success, rotated-secret-failure, dynamic-secret-failure, multi-auth-failure, uid-rotation-failure, apply-justification, email-auth-method-approved, usage, rotation-usage, gateway-inactive, static-secret-updated]  # noqa: E501

        :param event_types: The event_types of this EventForwarderUpdateEmail.  # noqa: E501
        :type: list[str]
        """

        self._event_types = event_types

    @property
    def gateways_event_source_locations(self):
        """Gets the gateways_event_source_locations of this EventForwarderUpdateEmail.  # noqa: E501

        Event sources  # noqa: E501

        :return: The gateways_event_source_locations of this EventForwarderUpdateEmail.  # noqa: E501
        :rtype: list[str]
        """
        return self._gateways_event_source_locations

    @gateways_event_source_locations.setter
    def gateways_event_source_locations(self, gateways_event_source_locations):
        """Sets the gateways_event_source_locations of this EventForwarderUpdateEmail.

        Event sources  # noqa: E501

        :param gateways_event_source_locations: The gateways_event_source_locations of this EventForwarderUpdateEmail.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and gateways_event_source_locations is None:  # noqa: E501
            raise ValueError("Invalid value for `gateways_event_source_locations`, must not be `None`")  # noqa: E501

        self._gateways_event_source_locations = gateways_event_source_locations

    @property
    def items_event_source_locations(self):
        """Gets the items_event_source_locations of this EventForwarderUpdateEmail.  # noqa: E501

        Items Event sources  # noqa: E501

        :return: The items_event_source_locations of this EventForwarderUpdateEmail.  # noqa: E501
        :rtype: list[str]
        """
        return self._items_event_source_locations

    @items_event_source_locations.setter
    def items_event_source_locations(self, items_event_source_locations):
        """Sets the items_event_source_locations of this EventForwarderUpdateEmail.

        Items Event sources  # noqa: E501

        :param items_event_source_locations: The items_event_source_locations of this EventForwarderUpdateEmail.  # noqa: E501
        :type: list[str]
        """

        self._items_event_source_locations = items_event_source_locations

    @property
    def json(self):
        """Gets the json of this EventForwarderUpdateEmail.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this EventForwarderUpdateEmail.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this EventForwarderUpdateEmail.

        Set output format to JSON  # noqa: E501

        :param json: The json of this EventForwarderUpdateEmail.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def keep_prev_version(self):
        """Gets the keep_prev_version of this EventForwarderUpdateEmail.  # noqa: E501

        Whether to keep previous version [true/false]. If not set, use default according to account settings  # noqa: E501

        :return: The keep_prev_version of this EventForwarderUpdateEmail.  # noqa: E501
        :rtype: str
        """
        return self._keep_prev_version

    @keep_prev_version.setter
    def keep_prev_version(self, keep_prev_version):
        """Sets the keep_prev_version of this EventForwarderUpdateEmail.

        Whether to keep previous version [true/false]. If not set, use default according to account settings  # noqa: E501

        :param keep_prev_version: The keep_prev_version of this EventForwarderUpdateEmail.  # noqa: E501
        :type: str
        """

        self._keep_prev_version = keep_prev_version

    @property
    def key(self):
        """Gets the key of this EventForwarderUpdateEmail.  # noqa: E501

        The name of a key that used to encrypt the EventForwarder secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :return: The key of this EventForwarderUpdateEmail.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this EventForwarderUpdateEmail.

        The name of a key that used to encrypt the EventForwarder secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :param key: The key of this EventForwarderUpdateEmail.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this EventForwarderUpdateEmail.  # noqa: E501

        EventForwarder name  # noqa: E501

        :return: The name of this EventForwarderUpdateEmail.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EventForwarderUpdateEmail.

        EventForwarder name  # noqa: E501

        :param name: The name of this EventForwarderUpdateEmail.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def new_name(self):
        """Gets the new_name of this EventForwarderUpdateEmail.  # noqa: E501

        New EventForwarder name  # noqa: E501

        :return: The new_name of this EventForwarderUpdateEmail.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this EventForwarderUpdateEmail.

        New EventForwarder name  # noqa: E501

        :param new_name: The new_name of this EventForwarderUpdateEmail.  # noqa: E501
        :type: str
        """

        self._new_name = new_name

    @property
    def override_url(self):
        """Gets the override_url of this EventForwarderUpdateEmail.  # noqa: E501

        Override Akeyless default URL with your Gateway url (port 18888)  # noqa: E501

        :return: The override_url of this EventForwarderUpdateEmail.  # noqa: E501
        :rtype: str
        """
        return self._override_url

    @override_url.setter
    def override_url(self, override_url):
        """Sets the override_url of this EventForwarderUpdateEmail.

        Override Akeyless default URL with your Gateway url (port 18888)  # noqa: E501

        :param override_url: The override_url of this EventForwarderUpdateEmail.  # noqa: E501
        :type: str
        """

        self._override_url = override_url

    @property
    def targets_event_source_locations(self):
        """Gets the targets_event_source_locations of this EventForwarderUpdateEmail.  # noqa: E501

        Targets Event sources  # noqa: E501

        :return: The targets_event_source_locations of this EventForwarderUpdateEmail.  # noqa: E501
        :rtype: list[str]
        """
        return self._targets_event_source_locations

    @targets_event_source_locations.setter
    def targets_event_source_locations(self, targets_event_source_locations):
        """Sets the targets_event_source_locations of this EventForwarderUpdateEmail.

        Targets Event sources  # noqa: E501

        :param targets_event_source_locations: The targets_event_source_locations of this EventForwarderUpdateEmail.  # noqa: E501
        :type: list[str]
        """

        self._targets_event_source_locations = targets_event_source_locations

    @property
    def token(self):
        """Gets the token of this EventForwarderUpdateEmail.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this EventForwarderUpdateEmail.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this EventForwarderUpdateEmail.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this EventForwarderUpdateEmail.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this EventForwarderUpdateEmail.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this EventForwarderUpdateEmail.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this EventForwarderUpdateEmail.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this EventForwarderUpdateEmail.  # noqa: E501
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
        if not isinstance(other, EventForwarderUpdateEmail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EventForwarderUpdateEmail):
            return True

        return self.to_dict() != other.to_dict()
