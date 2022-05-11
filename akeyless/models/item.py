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


class Item(object):
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
        'auto_rotate': 'bool',
        'cert_issuer_signer_key_name': 'str',
        'certificate_issue_details': 'CertificateIssueInfo',
        'certificates': 'str',
        'client_permissions': 'list[str]',
        'customer_fragment_id': 'str',
        'deletion_date': 'datetime',
        'display_id': 'str',
        'is_enabled': 'bool',
        'item_accessibility': 'int',
        'item_general_info': 'ItemGeneralInfo',
        'item_id': 'int',
        'item_metadata': 'str',
        'item_name': 'str',
        'item_size': 'int',
        'item_state': 'str',
        'item_sub_type': 'str',
        'item_tags': 'list[str]',
        'item_targets_assoc': 'list[ItemTargetAssociation]',
        'item_type': 'str',
        'item_versions': 'list[ItemVersion]',
        'last_version': 'int',
        'next_rotation_date': 'datetime',
        'protection_key_name': 'str',
        'public_value': 'str',
        'rotation_interval': 'int',
        'target_versions': 'list[TargetItemVersion]',
        'with_customer_fragment': 'bool'
    }

    attribute_map = {
        'auto_rotate': 'auto_rotate',
        'cert_issuer_signer_key_name': 'cert_issuer_signer_key_name',
        'certificate_issue_details': 'certificate_issue_details',
        'certificates': 'certificates',
        'client_permissions': 'client_permissions',
        'customer_fragment_id': 'customer_fragment_id',
        'deletion_date': 'deletion_date',
        'display_id': 'display_id',
        'is_enabled': 'is_enabled',
        'item_accessibility': 'item_accessibility',
        'item_general_info': 'item_general_info',
        'item_id': 'item_id',
        'item_metadata': 'item_metadata',
        'item_name': 'item_name',
        'item_size': 'item_size',
        'item_state': 'item_state',
        'item_sub_type': 'item_sub_type',
        'item_tags': 'item_tags',
        'item_targets_assoc': 'item_targets_assoc',
        'item_type': 'item_type',
        'item_versions': 'item_versions',
        'last_version': 'last_version',
        'next_rotation_date': 'next_rotation_date',
        'protection_key_name': 'protection_key_name',
        'public_value': 'public_value',
        'rotation_interval': 'rotation_interval',
        'target_versions': 'target_versions',
        'with_customer_fragment': 'with_customer_fragment'
    }

    def __init__(self, auto_rotate=None, cert_issuer_signer_key_name=None, certificate_issue_details=None, certificates=None, client_permissions=None, customer_fragment_id=None, deletion_date=None, display_id=None, is_enabled=None, item_accessibility=None, item_general_info=None, item_id=None, item_metadata=None, item_name=None, item_size=None, item_state=None, item_sub_type=None, item_tags=None, item_targets_assoc=None, item_type=None, item_versions=None, last_version=None, next_rotation_date=None, protection_key_name=None, public_value=None, rotation_interval=None, target_versions=None, with_customer_fragment=None, local_vars_configuration=None):  # noqa: E501
        """Item - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._auto_rotate = None
        self._cert_issuer_signer_key_name = None
        self._certificate_issue_details = None
        self._certificates = None
        self._client_permissions = None
        self._customer_fragment_id = None
        self._deletion_date = None
        self._display_id = None
        self._is_enabled = None
        self._item_accessibility = None
        self._item_general_info = None
        self._item_id = None
        self._item_metadata = None
        self._item_name = None
        self._item_size = None
        self._item_state = None
        self._item_sub_type = None
        self._item_tags = None
        self._item_targets_assoc = None
        self._item_type = None
        self._item_versions = None
        self._last_version = None
        self._next_rotation_date = None
        self._protection_key_name = None
        self._public_value = None
        self._rotation_interval = None
        self._target_versions = None
        self._with_customer_fragment = None
        self.discriminator = None

        if auto_rotate is not None:
            self.auto_rotate = auto_rotate
        if cert_issuer_signer_key_name is not None:
            self.cert_issuer_signer_key_name = cert_issuer_signer_key_name
        if certificate_issue_details is not None:
            self.certificate_issue_details = certificate_issue_details
        if certificates is not None:
            self.certificates = certificates
        if client_permissions is not None:
            self.client_permissions = client_permissions
        if customer_fragment_id is not None:
            self.customer_fragment_id = customer_fragment_id
        if deletion_date is not None:
            self.deletion_date = deletion_date
        if display_id is not None:
            self.display_id = display_id
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if item_accessibility is not None:
            self.item_accessibility = item_accessibility
        if item_general_info is not None:
            self.item_general_info = item_general_info
        if item_id is not None:
            self.item_id = item_id
        if item_metadata is not None:
            self.item_metadata = item_metadata
        if item_name is not None:
            self.item_name = item_name
        if item_size is not None:
            self.item_size = item_size
        if item_state is not None:
            self.item_state = item_state
        if item_sub_type is not None:
            self.item_sub_type = item_sub_type
        if item_tags is not None:
            self.item_tags = item_tags
        if item_targets_assoc is not None:
            self.item_targets_assoc = item_targets_assoc
        if item_type is not None:
            self.item_type = item_type
        if item_versions is not None:
            self.item_versions = item_versions
        if last_version is not None:
            self.last_version = last_version
        if next_rotation_date is not None:
            self.next_rotation_date = next_rotation_date
        if protection_key_name is not None:
            self.protection_key_name = protection_key_name
        if public_value is not None:
            self.public_value = public_value
        if rotation_interval is not None:
            self.rotation_interval = rotation_interval
        if target_versions is not None:
            self.target_versions = target_versions
        if with_customer_fragment is not None:
            self.with_customer_fragment = with_customer_fragment

    @property
    def auto_rotate(self):
        """Gets the auto_rotate of this Item.  # noqa: E501


        :return: The auto_rotate of this Item.  # noqa: E501
        :rtype: bool
        """
        return self._auto_rotate

    @auto_rotate.setter
    def auto_rotate(self, auto_rotate):
        """Sets the auto_rotate of this Item.


        :param auto_rotate: The auto_rotate of this Item.  # noqa: E501
        :type: bool
        """

        self._auto_rotate = auto_rotate

    @property
    def cert_issuer_signer_key_name(self):
        """Gets the cert_issuer_signer_key_name of this Item.  # noqa: E501


        :return: The cert_issuer_signer_key_name of this Item.  # noqa: E501
        :rtype: str
        """
        return self._cert_issuer_signer_key_name

    @cert_issuer_signer_key_name.setter
    def cert_issuer_signer_key_name(self, cert_issuer_signer_key_name):
        """Sets the cert_issuer_signer_key_name of this Item.


        :param cert_issuer_signer_key_name: The cert_issuer_signer_key_name of this Item.  # noqa: E501
        :type: str
        """

        self._cert_issuer_signer_key_name = cert_issuer_signer_key_name

    @property
    def certificate_issue_details(self):
        """Gets the certificate_issue_details of this Item.  # noqa: E501


        :return: The certificate_issue_details of this Item.  # noqa: E501
        :rtype: CertificateIssueInfo
        """
        return self._certificate_issue_details

    @certificate_issue_details.setter
    def certificate_issue_details(self, certificate_issue_details):
        """Sets the certificate_issue_details of this Item.


        :param certificate_issue_details: The certificate_issue_details of this Item.  # noqa: E501
        :type: CertificateIssueInfo
        """

        self._certificate_issue_details = certificate_issue_details

    @property
    def certificates(self):
        """Gets the certificates of this Item.  # noqa: E501


        :return: The certificates of this Item.  # noqa: E501
        :rtype: str
        """
        return self._certificates

    @certificates.setter
    def certificates(self, certificates):
        """Sets the certificates of this Item.


        :param certificates: The certificates of this Item.  # noqa: E501
        :type: str
        """

        self._certificates = certificates

    @property
    def client_permissions(self):
        """Gets the client_permissions of this Item.  # noqa: E501


        :return: The client_permissions of this Item.  # noqa: E501
        :rtype: list[str]
        """
        return self._client_permissions

    @client_permissions.setter
    def client_permissions(self, client_permissions):
        """Sets the client_permissions of this Item.


        :param client_permissions: The client_permissions of this Item.  # noqa: E501
        :type: list[str]
        """

        self._client_permissions = client_permissions

    @property
    def customer_fragment_id(self):
        """Gets the customer_fragment_id of this Item.  # noqa: E501


        :return: The customer_fragment_id of this Item.  # noqa: E501
        :rtype: str
        """
        return self._customer_fragment_id

    @customer_fragment_id.setter
    def customer_fragment_id(self, customer_fragment_id):
        """Sets the customer_fragment_id of this Item.


        :param customer_fragment_id: The customer_fragment_id of this Item.  # noqa: E501
        :type: str
        """

        self._customer_fragment_id = customer_fragment_id

    @property
    def deletion_date(self):
        """Gets the deletion_date of this Item.  # noqa: E501


        :return: The deletion_date of this Item.  # noqa: E501
        :rtype: datetime
        """
        return self._deletion_date

    @deletion_date.setter
    def deletion_date(self, deletion_date):
        """Sets the deletion_date of this Item.


        :param deletion_date: The deletion_date of this Item.  # noqa: E501
        :type: datetime
        """

        self._deletion_date = deletion_date

    @property
    def display_id(self):
        """Gets the display_id of this Item.  # noqa: E501


        :return: The display_id of this Item.  # noqa: E501
        :rtype: str
        """
        return self._display_id

    @display_id.setter
    def display_id(self, display_id):
        """Sets the display_id of this Item.


        :param display_id: The display_id of this Item.  # noqa: E501
        :type: str
        """

        self._display_id = display_id

    @property
    def is_enabled(self):
        """Gets the is_enabled of this Item.  # noqa: E501


        :return: The is_enabled of this Item.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this Item.


        :param is_enabled: The is_enabled of this Item.  # noqa: E501
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def item_accessibility(self):
        """Gets the item_accessibility of this Item.  # noqa: E501


        :return: The item_accessibility of this Item.  # noqa: E501
        :rtype: int
        """
        return self._item_accessibility

    @item_accessibility.setter
    def item_accessibility(self, item_accessibility):
        """Sets the item_accessibility of this Item.


        :param item_accessibility: The item_accessibility of this Item.  # noqa: E501
        :type: int
        """

        self._item_accessibility = item_accessibility

    @property
    def item_general_info(self):
        """Gets the item_general_info of this Item.  # noqa: E501


        :return: The item_general_info of this Item.  # noqa: E501
        :rtype: ItemGeneralInfo
        """
        return self._item_general_info

    @item_general_info.setter
    def item_general_info(self, item_general_info):
        """Sets the item_general_info of this Item.


        :param item_general_info: The item_general_info of this Item.  # noqa: E501
        :type: ItemGeneralInfo
        """

        self._item_general_info = item_general_info

    @property
    def item_id(self):
        """Gets the item_id of this Item.  # noqa: E501


        :return: The item_id of this Item.  # noqa: E501
        :rtype: int
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this Item.


        :param item_id: The item_id of this Item.  # noqa: E501
        :type: int
        """

        self._item_id = item_id

    @property
    def item_metadata(self):
        """Gets the item_metadata of this Item.  # noqa: E501


        :return: The item_metadata of this Item.  # noqa: E501
        :rtype: str
        """
        return self._item_metadata

    @item_metadata.setter
    def item_metadata(self, item_metadata):
        """Sets the item_metadata of this Item.


        :param item_metadata: The item_metadata of this Item.  # noqa: E501
        :type: str
        """

        self._item_metadata = item_metadata

    @property
    def item_name(self):
        """Gets the item_name of this Item.  # noqa: E501


        :return: The item_name of this Item.  # noqa: E501
        :rtype: str
        """
        return self._item_name

    @item_name.setter
    def item_name(self, item_name):
        """Sets the item_name of this Item.


        :param item_name: The item_name of this Item.  # noqa: E501
        :type: str
        """

        self._item_name = item_name

    @property
    def item_size(self):
        """Gets the item_size of this Item.  # noqa: E501


        :return: The item_size of this Item.  # noqa: E501
        :rtype: int
        """
        return self._item_size

    @item_size.setter
    def item_size(self, item_size):
        """Sets the item_size of this Item.


        :param item_size: The item_size of this Item.  # noqa: E501
        :type: int
        """

        self._item_size = item_size

    @property
    def item_state(self):
        """Gets the item_state of this Item.  # noqa: E501

        ItemState defines the different states an Item can be in  # noqa: E501

        :return: The item_state of this Item.  # noqa: E501
        :rtype: str
        """
        return self._item_state

    @item_state.setter
    def item_state(self, item_state):
        """Sets the item_state of this Item.

        ItemState defines the different states an Item can be in  # noqa: E501

        :param item_state: The item_state of this Item.  # noqa: E501
        :type: str
        """

        self._item_state = item_state

    @property
    def item_sub_type(self):
        """Gets the item_sub_type of this Item.  # noqa: E501


        :return: The item_sub_type of this Item.  # noqa: E501
        :rtype: str
        """
        return self._item_sub_type

    @item_sub_type.setter
    def item_sub_type(self, item_sub_type):
        """Sets the item_sub_type of this Item.


        :param item_sub_type: The item_sub_type of this Item.  # noqa: E501
        :type: str
        """

        self._item_sub_type = item_sub_type

    @property
    def item_tags(self):
        """Gets the item_tags of this Item.  # noqa: E501


        :return: The item_tags of this Item.  # noqa: E501
        :rtype: list[str]
        """
        return self._item_tags

    @item_tags.setter
    def item_tags(self, item_tags):
        """Sets the item_tags of this Item.


        :param item_tags: The item_tags of this Item.  # noqa: E501
        :type: list[str]
        """

        self._item_tags = item_tags

    @property
    def item_targets_assoc(self):
        """Gets the item_targets_assoc of this Item.  # noqa: E501


        :return: The item_targets_assoc of this Item.  # noqa: E501
        :rtype: list[ItemTargetAssociation]
        """
        return self._item_targets_assoc

    @item_targets_assoc.setter
    def item_targets_assoc(self, item_targets_assoc):
        """Sets the item_targets_assoc of this Item.


        :param item_targets_assoc: The item_targets_assoc of this Item.  # noqa: E501
        :type: list[ItemTargetAssociation]
        """

        self._item_targets_assoc = item_targets_assoc

    @property
    def item_type(self):
        """Gets the item_type of this Item.  # noqa: E501


        :return: The item_type of this Item.  # noqa: E501
        :rtype: str
        """
        return self._item_type

    @item_type.setter
    def item_type(self, item_type):
        """Sets the item_type of this Item.


        :param item_type: The item_type of this Item.  # noqa: E501
        :type: str
        """

        self._item_type = item_type

    @property
    def item_versions(self):
        """Gets the item_versions of this Item.  # noqa: E501


        :return: The item_versions of this Item.  # noqa: E501
        :rtype: list[ItemVersion]
        """
        return self._item_versions

    @item_versions.setter
    def item_versions(self, item_versions):
        """Sets the item_versions of this Item.


        :param item_versions: The item_versions of this Item.  # noqa: E501
        :type: list[ItemVersion]
        """

        self._item_versions = item_versions

    @property
    def last_version(self):
        """Gets the last_version of this Item.  # noqa: E501


        :return: The last_version of this Item.  # noqa: E501
        :rtype: int
        """
        return self._last_version

    @last_version.setter
    def last_version(self, last_version):
        """Sets the last_version of this Item.


        :param last_version: The last_version of this Item.  # noqa: E501
        :type: int
        """

        self._last_version = last_version

    @property
    def next_rotation_date(self):
        """Gets the next_rotation_date of this Item.  # noqa: E501


        :return: The next_rotation_date of this Item.  # noqa: E501
        :rtype: datetime
        """
        return self._next_rotation_date

    @next_rotation_date.setter
    def next_rotation_date(self, next_rotation_date):
        """Sets the next_rotation_date of this Item.


        :param next_rotation_date: The next_rotation_date of this Item.  # noqa: E501
        :type: datetime
        """

        self._next_rotation_date = next_rotation_date

    @property
    def protection_key_name(self):
        """Gets the protection_key_name of this Item.  # noqa: E501


        :return: The protection_key_name of this Item.  # noqa: E501
        :rtype: str
        """
        return self._protection_key_name

    @protection_key_name.setter
    def protection_key_name(self, protection_key_name):
        """Sets the protection_key_name of this Item.


        :param protection_key_name: The protection_key_name of this Item.  # noqa: E501
        :type: str
        """

        self._protection_key_name = protection_key_name

    @property
    def public_value(self):
        """Gets the public_value of this Item.  # noqa: E501


        :return: The public_value of this Item.  # noqa: E501
        :rtype: str
        """
        return self._public_value

    @public_value.setter
    def public_value(self, public_value):
        """Sets the public_value of this Item.


        :param public_value: The public_value of this Item.  # noqa: E501
        :type: str
        """

        self._public_value = public_value

    @property
    def rotation_interval(self):
        """Gets the rotation_interval of this Item.  # noqa: E501


        :return: The rotation_interval of this Item.  # noqa: E501
        :rtype: int
        """
        return self._rotation_interval

    @rotation_interval.setter
    def rotation_interval(self, rotation_interval):
        """Sets the rotation_interval of this Item.


        :param rotation_interval: The rotation_interval of this Item.  # noqa: E501
        :type: int
        """

        self._rotation_interval = rotation_interval

    @property
    def target_versions(self):
        """Gets the target_versions of this Item.  # noqa: E501


        :return: The target_versions of this Item.  # noqa: E501
        :rtype: list[TargetItemVersion]
        """
        return self._target_versions

    @target_versions.setter
    def target_versions(self, target_versions):
        """Sets the target_versions of this Item.


        :param target_versions: The target_versions of this Item.  # noqa: E501
        :type: list[TargetItemVersion]
        """

        self._target_versions = target_versions

    @property
    def with_customer_fragment(self):
        """Gets the with_customer_fragment of this Item.  # noqa: E501


        :return: The with_customer_fragment of this Item.  # noqa: E501
        :rtype: bool
        """
        return self._with_customer_fragment

    @with_customer_fragment.setter
    def with_customer_fragment(self, with_customer_fragment):
        """Sets the with_customer_fragment of this Item.


        :param with_customer_fragment: The with_customer_fragment of this Item.  # noqa: E501
        :type: bool
        """

        self._with_customer_fragment = with_customer_fragment

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
        if not isinstance(other, Item):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Item):
            return True

        return self.to_dict() != other.to_dict()
