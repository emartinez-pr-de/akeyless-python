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


class GatewayCreateProducerAws(object):
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
        'access_mode': 'str',
        'admin_rotation_interval_days': 'int',
        'aws_access_key_id': 'str',
        'aws_access_secret_key': 'str',
        'aws_role_arns': 'str',
        'aws_user_console_access': 'bool',
        'aws_user_groups': 'str',
        'aws_user_policies': 'str',
        'aws_user_programmatic_access': 'bool',
        'delete_protection': 'str',
        'enable_admin_rotation': 'bool',
        'json': 'bool',
        'name': 'str',
        'producer_encryption_key_name': 'str',
        'region': 'str',
        'secure_access_aws_account_id': 'str',
        'secure_access_aws_native_cli': 'bool',
        'secure_access_bastion_issuer': 'str',
        'secure_access_enable': 'str',
        'secure_access_web': 'bool',
        'secure_access_web_browsing': 'bool',
        'secure_access_web_proxy': 'bool',
        'tags': 'list[str]',
        'target_name': 'str',
        'token': 'str',
        'uid_token': 'str',
        'user_ttl': 'str'
    }

    attribute_map = {
        'access_mode': 'access-mode',
        'admin_rotation_interval_days': 'admin-rotation-interval-days',
        'aws_access_key_id': 'aws-access-key-id',
        'aws_access_secret_key': 'aws-access-secret-key',
        'aws_role_arns': 'aws-role-arns',
        'aws_user_console_access': 'aws-user-console-access',
        'aws_user_groups': 'aws-user-groups',
        'aws_user_policies': 'aws-user-policies',
        'aws_user_programmatic_access': 'aws-user-programmatic-access',
        'delete_protection': 'delete_protection',
        'enable_admin_rotation': 'enable-admin-rotation',
        'json': 'json',
        'name': 'name',
        'producer_encryption_key_name': 'producer-encryption-key-name',
        'region': 'region',
        'secure_access_aws_account_id': 'secure-access-aws-account-id',
        'secure_access_aws_native_cli': 'secure-access-aws-native-cli',
        'secure_access_bastion_issuer': 'secure-access-bastion-issuer',
        'secure_access_enable': 'secure-access-enable',
        'secure_access_web': 'secure-access-web',
        'secure_access_web_browsing': 'secure-access-web-browsing',
        'secure_access_web_proxy': 'secure-access-web-proxy',
        'tags': 'tags',
        'target_name': 'target-name',
        'token': 'token',
        'uid_token': 'uid-token',
        'user_ttl': 'user-ttl'
    }

    def __init__(self, access_mode=None, admin_rotation_interval_days=0, aws_access_key_id=None, aws_access_secret_key=None, aws_role_arns=None, aws_user_console_access=False, aws_user_groups=None, aws_user_policies=None, aws_user_programmatic_access=True, delete_protection=None, enable_admin_rotation=False, json=False, name=None, producer_encryption_key_name=None, region='us-east-2', secure_access_aws_account_id=None, secure_access_aws_native_cli=None, secure_access_bastion_issuer=None, secure_access_enable=None, secure_access_web=True, secure_access_web_browsing=False, secure_access_web_proxy=False, tags=None, target_name=None, token=None, uid_token=None, user_ttl='60m', local_vars_configuration=None):  # noqa: E501
        """GatewayCreateProducerAws - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_mode = None
        self._admin_rotation_interval_days = None
        self._aws_access_key_id = None
        self._aws_access_secret_key = None
        self._aws_role_arns = None
        self._aws_user_console_access = None
        self._aws_user_groups = None
        self._aws_user_policies = None
        self._aws_user_programmatic_access = None
        self._delete_protection = None
        self._enable_admin_rotation = None
        self._json = None
        self._name = None
        self._producer_encryption_key_name = None
        self._region = None
        self._secure_access_aws_account_id = None
        self._secure_access_aws_native_cli = None
        self._secure_access_bastion_issuer = None
        self._secure_access_enable = None
        self._secure_access_web = None
        self._secure_access_web_browsing = None
        self._secure_access_web_proxy = None
        self._tags = None
        self._target_name = None
        self._token = None
        self._uid_token = None
        self._user_ttl = None
        self.discriminator = None

        if access_mode is not None:
            self.access_mode = access_mode
        if admin_rotation_interval_days is not None:
            self.admin_rotation_interval_days = admin_rotation_interval_days
        if aws_access_key_id is not None:
            self.aws_access_key_id = aws_access_key_id
        if aws_access_secret_key is not None:
            self.aws_access_secret_key = aws_access_secret_key
        if aws_role_arns is not None:
            self.aws_role_arns = aws_role_arns
        if aws_user_console_access is not None:
            self.aws_user_console_access = aws_user_console_access
        if aws_user_groups is not None:
            self.aws_user_groups = aws_user_groups
        if aws_user_policies is not None:
            self.aws_user_policies = aws_user_policies
        if aws_user_programmatic_access is not None:
            self.aws_user_programmatic_access = aws_user_programmatic_access
        if delete_protection is not None:
            self.delete_protection = delete_protection
        if enable_admin_rotation is not None:
            self.enable_admin_rotation = enable_admin_rotation
        if json is not None:
            self.json = json
        self.name = name
        if producer_encryption_key_name is not None:
            self.producer_encryption_key_name = producer_encryption_key_name
        if region is not None:
            self.region = region
        if secure_access_aws_account_id is not None:
            self.secure_access_aws_account_id = secure_access_aws_account_id
        if secure_access_aws_native_cli is not None:
            self.secure_access_aws_native_cli = secure_access_aws_native_cli
        if secure_access_bastion_issuer is not None:
            self.secure_access_bastion_issuer = secure_access_bastion_issuer
        if secure_access_enable is not None:
            self.secure_access_enable = secure_access_enable
        if secure_access_web is not None:
            self.secure_access_web = secure_access_web
        if secure_access_web_browsing is not None:
            self.secure_access_web_browsing = secure_access_web_browsing
        if secure_access_web_proxy is not None:
            self.secure_access_web_proxy = secure_access_web_proxy
        if tags is not None:
            self.tags = tags
        if target_name is not None:
            self.target_name = target_name
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if user_ttl is not None:
            self.user_ttl = user_ttl

    @property
    def access_mode(self):
        """Gets the access_mode of this GatewayCreateProducerAws.  # noqa: E501


        :return: The access_mode of this GatewayCreateProducerAws.  # noqa: E501
        :rtype: str
        """
        return self._access_mode

    @access_mode.setter
    def access_mode(self, access_mode):
        """Sets the access_mode of this GatewayCreateProducerAws.


        :param access_mode: The access_mode of this GatewayCreateProducerAws.  # noqa: E501
        :type: str
        """

        self._access_mode = access_mode

    @property
    def admin_rotation_interval_days(self):
        """Gets the admin_rotation_interval_days of this GatewayCreateProducerAws.  # noqa: E501

        Admin credentials rotation interval (days)  # noqa: E501

        :return: The admin_rotation_interval_days of this GatewayCreateProducerAws.  # noqa: E501
        :rtype: int
        """
        return self._admin_rotation_interval_days

    @admin_rotation_interval_days.setter
    def admin_rotation_interval_days(self, admin_rotation_interval_days):
        """Sets the admin_rotation_interval_days of this GatewayCreateProducerAws.

        Admin credentials rotation interval (days)  # noqa: E501

        :param admin_rotation_interval_days: The admin_rotation_interval_days of this GatewayCreateProducerAws.  # noqa: E501
        :type: int
        """

        self._admin_rotation_interval_days = admin_rotation_interval_days

    @property
    def aws_access_key_id(self):
        """Gets the aws_access_key_id of this GatewayCreateProducerAws.  # noqa: E501

        Access Key ID  # noqa: E501

        :return: The aws_access_key_id of this GatewayCreateProducerAws.  # noqa: E501
        :rtype: str
        """
        return self._aws_access_key_id

    @aws_access_key_id.setter
    def aws_access_key_id(self, aws_access_key_id):
        """Sets the aws_access_key_id of this GatewayCreateProducerAws.

        Access Key ID  # noqa: E501

        :param aws_access_key_id: The aws_access_key_id of this GatewayCreateProducerAws.  # noqa: E501
        :type: str
        """

        self._aws_access_key_id = aws_access_key_id

    @property
    def aws_access_secret_key(self):
        """Gets the aws_access_secret_key of this GatewayCreateProducerAws.  # noqa: E501

        Secret Access Key  # noqa: E501

        :return: The aws_access_secret_key of this GatewayCreateProducerAws.  # noqa: E501
        :rtype: str
        """
        return self._aws_access_secret_key

    @aws_access_secret_key.setter
    def aws_access_secret_key(self, aws_access_secret_key):
        """Sets the aws_access_secret_key of this GatewayCreateProducerAws.

        Secret Access Key  # noqa: E501

        :param aws_access_secret_key: The aws_access_secret_key of this GatewayCreateProducerAws.  # noqa: E501
        :type: str
        """

        self._aws_access_secret_key = aws_access_secret_key

    @property
    def aws_role_arns(self):
        """Gets the aws_role_arns of this GatewayCreateProducerAws.  # noqa: E501

        AWS Role ARNs to be used in the Assume Role operation (relevant only for assume_role mode)  # noqa: E501

        :return: The aws_role_arns of this GatewayCreateProducerAws.  # noqa: E501
        :rtype: str
        """
        return self._aws_role_arns

    @aws_role_arns.setter
    def aws_role_arns(self, aws_role_arns):
        """Sets the aws_role_arns of this GatewayCreateProducerAws.

        AWS Role ARNs to be used in the Assume Role operation (relevant only for assume_role mode)  # noqa: E501

        :param aws_role_arns: The aws_role_arns of this GatewayCreateProducerAws.  # noqa: E501
        :type: str
        """

        self._aws_role_arns = aws_role_arns

    @property
    def aws_user_console_access(self):
        """Gets the aws_user_console_access of this GatewayCreateProducerAws.  # noqa: E501

        AWS User console access  # noqa: E501

        :return: The aws_user_console_access of this GatewayCreateProducerAws.  # noqa: E501
        :rtype: bool
        """
        return self._aws_user_console_access

    @aws_user_console_access.setter
    def aws_user_console_access(self, aws_user_console_access):
        """Sets the aws_user_console_access of this GatewayCreateProducerAws.

        AWS User console access  # noqa: E501

        :param aws_user_console_access: The aws_user_console_access of this GatewayCreateProducerAws.  # noqa: E501
        :type: bool
        """

        self._aws_user_console_access = aws_user_console_access

    @property
    def aws_user_groups(self):
        """Gets the aws_user_groups of this GatewayCreateProducerAws.  # noqa: E501

        AWS User groups  # noqa: E501

        :return: The aws_user_groups of this GatewayCreateProducerAws.  # noqa: E501
        :rtype: str
        """
        return self._aws_user_groups

    @aws_user_groups.setter
    def aws_user_groups(self, aws_user_groups):
        """Sets the aws_user_groups of this GatewayCreateProducerAws.

        AWS User groups  # noqa: E501

        :param aws_user_groups: The aws_user_groups of this GatewayCreateProducerAws.  # noqa: E501
        :type: str
        """

        self._aws_user_groups = aws_user_groups

    @property
    def aws_user_policies(self):
        """Gets the aws_user_policies of this GatewayCreateProducerAws.  # noqa: E501

        AWS User policies  # noqa: E501

        :return: The aws_user_policies of this GatewayCreateProducerAws.  # noqa: E501
        :rtype: str
        """
        return self._aws_user_policies

    @aws_user_policies.setter
    def aws_user_policies(self, aws_user_policies):
        """Sets the aws_user_policies of this GatewayCreateProducerAws.

        AWS User policies  # noqa: E501

        :param aws_user_policies: The aws_user_policies of this GatewayCreateProducerAws.  # noqa: E501
        :type: str
        """

        self._aws_user_policies = aws_user_policies

    @property
    def aws_user_programmatic_access(self):
        """Gets the aws_user_programmatic_access of this GatewayCreateProducerAws.  # noqa: E501

        Enable AWS User programmatic access  # noqa: E501

        :return: The aws_user_programmatic_access of this GatewayCreateProducerAws.  # noqa: E501
        :rtype: bool
        """
        return self._aws_user_programmatic_access

    @aws_user_programmatic_access.setter
    def aws_user_programmatic_access(self, aws_user_programmatic_access):
        """Sets the aws_user_programmatic_access of this GatewayCreateProducerAws.

        Enable AWS User programmatic access  # noqa: E501

        :param aws_user_programmatic_access: The aws_user_programmatic_access of this GatewayCreateProducerAws.  # noqa: E501
        :type: bool
        """

        self._aws_user_programmatic_access = aws_user_programmatic_access

    @property
    def delete_protection(self):
        """Gets the delete_protection of this GatewayCreateProducerAws.  # noqa: E501

        Protection from accidental deletion of this item [true/false]  # noqa: E501

        :return: The delete_protection of this GatewayCreateProducerAws.  # noqa: E501
        :rtype: str
        """
        return self._delete_protection

    @delete_protection.setter
    def delete_protection(self, delete_protection):
        """Sets the delete_protection of this GatewayCreateProducerAws.

        Protection from accidental deletion of this item [true/false]  # noqa: E501

        :param delete_protection: The delete_protection of this GatewayCreateProducerAws.  # noqa: E501
        :type: str
        """

        self._delete_protection = delete_protection

    @property
    def enable_admin_rotation(self):
        """Gets the enable_admin_rotation of this GatewayCreateProducerAws.  # noqa: E501

        Automatic admin credentials rotation  # noqa: E501

        :return: The enable_admin_rotation of this GatewayCreateProducerAws.  # noqa: E501
        :rtype: bool
        """
        return self._enable_admin_rotation

    @enable_admin_rotation.setter
    def enable_admin_rotation(self, enable_admin_rotation):
        """Sets the enable_admin_rotation of this GatewayCreateProducerAws.

        Automatic admin credentials rotation  # noqa: E501

        :param enable_admin_rotation: The enable_admin_rotation of this GatewayCreateProducerAws.  # noqa: E501
        :type: bool
        """

        self._enable_admin_rotation = enable_admin_rotation

    @property
    def json(self):
        """Gets the json of this GatewayCreateProducerAws.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this GatewayCreateProducerAws.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this GatewayCreateProducerAws.

        Set output format to JSON  # noqa: E501

        :param json: The json of this GatewayCreateProducerAws.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def name(self):
        """Gets the name of this GatewayCreateProducerAws.  # noqa: E501

        Producer name  # noqa: E501

        :return: The name of this GatewayCreateProducerAws.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GatewayCreateProducerAws.

        Producer name  # noqa: E501

        :param name: The name of this GatewayCreateProducerAws.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def producer_encryption_key_name(self):
        """Gets the producer_encryption_key_name of this GatewayCreateProducerAws.  # noqa: E501

        Dynamic producer encryption key  # noqa: E501

        :return: The producer_encryption_key_name of this GatewayCreateProducerAws.  # noqa: E501
        :rtype: str
        """
        return self._producer_encryption_key_name

    @producer_encryption_key_name.setter
    def producer_encryption_key_name(self, producer_encryption_key_name):
        """Sets the producer_encryption_key_name of this GatewayCreateProducerAws.

        Dynamic producer encryption key  # noqa: E501

        :param producer_encryption_key_name: The producer_encryption_key_name of this GatewayCreateProducerAws.  # noqa: E501
        :type: str
        """

        self._producer_encryption_key_name = producer_encryption_key_name

    @property
    def region(self):
        """Gets the region of this GatewayCreateProducerAws.  # noqa: E501

        Region  # noqa: E501

        :return: The region of this GatewayCreateProducerAws.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this GatewayCreateProducerAws.

        Region  # noqa: E501

        :param region: The region of this GatewayCreateProducerAws.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def secure_access_aws_account_id(self):
        """Gets the secure_access_aws_account_id of this GatewayCreateProducerAws.  # noqa: E501

        The AWS account id  # noqa: E501

        :return: The secure_access_aws_account_id of this GatewayCreateProducerAws.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_aws_account_id

    @secure_access_aws_account_id.setter
    def secure_access_aws_account_id(self, secure_access_aws_account_id):
        """Sets the secure_access_aws_account_id of this GatewayCreateProducerAws.

        The AWS account id  # noqa: E501

        :param secure_access_aws_account_id: The secure_access_aws_account_id of this GatewayCreateProducerAws.  # noqa: E501
        :type: str
        """

        self._secure_access_aws_account_id = secure_access_aws_account_id

    @property
    def secure_access_aws_native_cli(self):
        """Gets the secure_access_aws_native_cli of this GatewayCreateProducerAws.  # noqa: E501

        The AWS native cli  # noqa: E501

        :return: The secure_access_aws_native_cli of this GatewayCreateProducerAws.  # noqa: E501
        :rtype: bool
        """
        return self._secure_access_aws_native_cli

    @secure_access_aws_native_cli.setter
    def secure_access_aws_native_cli(self, secure_access_aws_native_cli):
        """Sets the secure_access_aws_native_cli of this GatewayCreateProducerAws.

        The AWS native cli  # noqa: E501

        :param secure_access_aws_native_cli: The secure_access_aws_native_cli of this GatewayCreateProducerAws.  # noqa: E501
        :type: bool
        """

        self._secure_access_aws_native_cli = secure_access_aws_native_cli

    @property
    def secure_access_bastion_issuer(self):
        """Gets the secure_access_bastion_issuer of this GatewayCreateProducerAws.  # noqa: E501

        Path to the SSH Certificate Issuer for your Akeyless Bastion  # noqa: E501

        :return: The secure_access_bastion_issuer of this GatewayCreateProducerAws.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_bastion_issuer

    @secure_access_bastion_issuer.setter
    def secure_access_bastion_issuer(self, secure_access_bastion_issuer):
        """Sets the secure_access_bastion_issuer of this GatewayCreateProducerAws.

        Path to the SSH Certificate Issuer for your Akeyless Bastion  # noqa: E501

        :param secure_access_bastion_issuer: The secure_access_bastion_issuer of this GatewayCreateProducerAws.  # noqa: E501
        :type: str
        """

        self._secure_access_bastion_issuer = secure_access_bastion_issuer

    @property
    def secure_access_enable(self):
        """Gets the secure_access_enable of this GatewayCreateProducerAws.  # noqa: E501

        Enable/Disable secure remote access [true/false]  # noqa: E501

        :return: The secure_access_enable of this GatewayCreateProducerAws.  # noqa: E501
        :rtype: str
        """
        return self._secure_access_enable

    @secure_access_enable.setter
    def secure_access_enable(self, secure_access_enable):
        """Sets the secure_access_enable of this GatewayCreateProducerAws.

        Enable/Disable secure remote access [true/false]  # noqa: E501

        :param secure_access_enable: The secure_access_enable of this GatewayCreateProducerAws.  # noqa: E501
        :type: str
        """

        self._secure_access_enable = secure_access_enable

    @property
    def secure_access_web(self):
        """Gets the secure_access_web of this GatewayCreateProducerAws.  # noqa: E501

        Enable Web Secure Remote Access  # noqa: E501

        :return: The secure_access_web of this GatewayCreateProducerAws.  # noqa: E501
        :rtype: bool
        """
        return self._secure_access_web

    @secure_access_web.setter
    def secure_access_web(self, secure_access_web):
        """Sets the secure_access_web of this GatewayCreateProducerAws.

        Enable Web Secure Remote Access  # noqa: E501

        :param secure_access_web: The secure_access_web of this GatewayCreateProducerAws.  # noqa: E501
        :type: bool
        """

        self._secure_access_web = secure_access_web

    @property
    def secure_access_web_browsing(self):
        """Gets the secure_access_web_browsing of this GatewayCreateProducerAws.  # noqa: E501

        Secure browser via Akeyless Web Access Bastion  # noqa: E501

        :return: The secure_access_web_browsing of this GatewayCreateProducerAws.  # noqa: E501
        :rtype: bool
        """
        return self._secure_access_web_browsing

    @secure_access_web_browsing.setter
    def secure_access_web_browsing(self, secure_access_web_browsing):
        """Sets the secure_access_web_browsing of this GatewayCreateProducerAws.

        Secure browser via Akeyless Web Access Bastion  # noqa: E501

        :param secure_access_web_browsing: The secure_access_web_browsing of this GatewayCreateProducerAws.  # noqa: E501
        :type: bool
        """

        self._secure_access_web_browsing = secure_access_web_browsing

    @property
    def secure_access_web_proxy(self):
        """Gets the secure_access_web_proxy of this GatewayCreateProducerAws.  # noqa: E501

        Web-Proxy via Akeyless Web Access Bastion  # noqa: E501

        :return: The secure_access_web_proxy of this GatewayCreateProducerAws.  # noqa: E501
        :rtype: bool
        """
        return self._secure_access_web_proxy

    @secure_access_web_proxy.setter
    def secure_access_web_proxy(self, secure_access_web_proxy):
        """Sets the secure_access_web_proxy of this GatewayCreateProducerAws.

        Web-Proxy via Akeyless Web Access Bastion  # noqa: E501

        :param secure_access_web_proxy: The secure_access_web_proxy of this GatewayCreateProducerAws.  # noqa: E501
        :type: bool
        """

        self._secure_access_web_proxy = secure_access_web_proxy

    @property
    def tags(self):
        """Gets the tags of this GatewayCreateProducerAws.  # noqa: E501

        List of the tags attached to this secret  # noqa: E501

        :return: The tags of this GatewayCreateProducerAws.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this GatewayCreateProducerAws.

        List of the tags attached to this secret  # noqa: E501

        :param tags: The tags of this GatewayCreateProducerAws.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def target_name(self):
        """Gets the target_name of this GatewayCreateProducerAws.  # noqa: E501

        Target name  # noqa: E501

        :return: The target_name of this GatewayCreateProducerAws.  # noqa: E501
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """Sets the target_name of this GatewayCreateProducerAws.

        Target name  # noqa: E501

        :param target_name: The target_name of this GatewayCreateProducerAws.  # noqa: E501
        :type: str
        """

        self._target_name = target_name

    @property
    def token(self):
        """Gets the token of this GatewayCreateProducerAws.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GatewayCreateProducerAws.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GatewayCreateProducerAws.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GatewayCreateProducerAws.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this GatewayCreateProducerAws.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GatewayCreateProducerAws.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GatewayCreateProducerAws.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GatewayCreateProducerAws.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def user_ttl(self):
        """Gets the user_ttl of this GatewayCreateProducerAws.  # noqa: E501

        User TTL  # noqa: E501

        :return: The user_ttl of this GatewayCreateProducerAws.  # noqa: E501
        :rtype: str
        """
        return self._user_ttl

    @user_ttl.setter
    def user_ttl(self, user_ttl):
        """Sets the user_ttl of this GatewayCreateProducerAws.

        User TTL  # noqa: E501

        :param user_ttl: The user_ttl of this GatewayCreateProducerAws.  # noqa: E501
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
        if not isinstance(other, GatewayCreateProducerAws):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayCreateProducerAws):
            return True

        return self.to_dict() != other.to_dict()
