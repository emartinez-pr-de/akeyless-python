# coding: utf-8

# flake8: noqa

"""
    Akeyless API

    The purpose of this application is to provide access to Akeyless API.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Contact: support@akeyless.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "2.16.2"

# import apis into sdk package
from akeyless.api.v2_api import V2Api

# import ApiClient
from akeyless.api_client import ApiClient
from akeyless.configuration import Configuration
from akeyless.exceptions import OpenApiException
from akeyless.exceptions import ApiTypeError
from akeyless.exceptions import ApiValueError
from akeyless.exceptions import ApiKeyError
from akeyless.exceptions import ApiException
# import models into sdk package
from akeyless.models.api_key_access_rules import APIKeyAccessRules
from akeyless.models.awsiam_access_rules import AWSIAMAccessRules
from akeyless.models.aws_payload import AWSPayload
from akeyless.models.aws_secrets_migration import AWSSecretsMigration
from akeyless.models.account_object_version_settings_output import AccountObjectVersionSettingsOutput
from akeyless.models.admins_config_part import AdminsConfigPart
from akeyless.models.akeyless_gateway_config import AkeylessGatewayConfig
from akeyless.models.allowed_access import AllowedAccess
from akeyless.models.assoc_role_auth_method import AssocRoleAuthMethod
from akeyless.models.assoc_target_item import AssocTargetItem
from akeyless.models.auth import Auth
from akeyless.models.auth_method import AuthMethod
from akeyless.models.auth_method_access_info import AuthMethodAccessInfo
from akeyless.models.auth_method_role_association import AuthMethodRoleAssociation
from akeyless.models.auth_output import AuthOutput
from akeyless.models.aws_s3_log_forwarding_config import AwsS3LogForwardingConfig
from akeyless.models.azure_ad_access_rules import AzureADAccessRules
from akeyless.models.azure_key_vault_migration import AzureKeyVaultMigration
from akeyless.models.azure_log_analytics_forwarding_config import AzureLogAnalyticsForwardingConfig
from akeyless.models.azure_payload import AzurePayload
from akeyless.models.cf_config_part import CFConfigPart
from akeyless.models.cache_config_part import CacheConfigPart
from akeyless.models.cert_access_rules import CertAccessRules
from akeyless.models.certificate_issue_info import CertificateIssueInfo
from akeyless.models.classic_key_details_info import ClassicKeyDetailsInfo
from akeyless.models.classic_key_status_info import ClassicKeyStatusInfo
from akeyless.models.classic_key_target_info import ClassicKeyTargetInfo
from akeyless.models.client_data import ClientData
from akeyless.models.config_change import ConfigChange
from akeyless.models.config_hash import ConfigHash
from akeyless.models.configure import Configure
from akeyless.models.configure_output import ConfigureOutput
from akeyless.models.connect import Connect
from akeyless.models.create_aws_target import CreateAWSTarget
from akeyless.models.create_aws_target_output import CreateAWSTargetOutput
from akeyless.models.create_artifactory_target import CreateArtifactoryTarget
from akeyless.models.create_artifactory_target_output import CreateArtifactoryTargetOutput
from akeyless.models.create_auth_method import CreateAuthMethod
from akeyless.models.create_auth_method_awsiam import CreateAuthMethodAWSIAM
from akeyless.models.create_auth_method_awsiam_output import CreateAuthMethodAWSIAMOutput
from akeyless.models.create_auth_method_azure_ad import CreateAuthMethodAzureAD
from akeyless.models.create_auth_method_azure_ad_output import CreateAuthMethodAzureADOutput
from akeyless.models.create_auth_method_cert import CreateAuthMethodCert
from akeyless.models.create_auth_method_cert_output import CreateAuthMethodCertOutput
from akeyless.models.create_auth_method_gcp import CreateAuthMethodGCP
from akeyless.models.create_auth_method_gcp_output import CreateAuthMethodGCPOutput
from akeyless.models.create_auth_method_huawei import CreateAuthMethodHuawei
from akeyless.models.create_auth_method_huawei_output import CreateAuthMethodHuaweiOutput
from akeyless.models.create_auth_method_k8_s import CreateAuthMethodK8S
from akeyless.models.create_auth_method_k8_s_output import CreateAuthMethodK8SOutput
from akeyless.models.create_auth_method_ldap import CreateAuthMethodLDAP
from akeyless.models.create_auth_method_ldap_output import CreateAuthMethodLDAPOutput
from akeyless.models.create_auth_method_o_auth2 import CreateAuthMethodOAuth2
from akeyless.models.create_auth_method_o_auth2_output import CreateAuthMethodOAuth2Output
from akeyless.models.create_auth_method_oidc import CreateAuthMethodOIDC
from akeyless.models.create_auth_method_oidc_output import CreateAuthMethodOIDCOutput
from akeyless.models.create_auth_method_output import CreateAuthMethodOutput
from akeyless.models.create_auth_method_saml import CreateAuthMethodSAML
from akeyless.models.create_auth_method_saml_output import CreateAuthMethodSAMLOutput
from akeyless.models.create_auth_method_universal_identity import CreateAuthMethodUniversalIdentity
from akeyless.models.create_auth_method_universal_identity_output import CreateAuthMethodUniversalIdentityOutput
from akeyless.models.create_azure_target import CreateAzureTarget
from akeyless.models.create_azure_target_output import CreateAzureTargetOutput
from akeyless.models.create_classic_key import CreateClassicKey
from akeyless.models.create_classic_key_output import CreateClassicKeyOutput
from akeyless.models.create_db_target import CreateDBTarget
from akeyless.models.create_db_target_output import CreateDBTargetOutput
from akeyless.models.create_dfc_key import CreateDFCKey
from akeyless.models.create_dfc_key_output import CreateDFCKeyOutput
from akeyless.models.create_dockerhub_target import CreateDockerhubTarget
from akeyless.models.create_dockerhub_target_output import CreateDockerhubTargetOutput
from akeyless.models.create_dynamic_secret import CreateDynamicSecret
from akeyless.models.create_eks_target import CreateEKSTarget
from akeyless.models.create_eks_target_output import CreateEKSTargetOutput
from akeyless.models.create_gke_target import CreateGKETarget
from akeyless.models.create_gke_target_output import CreateGKETargetOutput
from akeyless.models.create_gcp_target import CreateGcpTarget
from akeyless.models.create_gcp_target_output import CreateGcpTargetOutput
from akeyless.models.create_github_target import CreateGithubTarget
from akeyless.models.create_github_target_output import CreateGithubTargetOutput
from akeyless.models.create_key import CreateKey
from akeyless.models.create_key_output import CreateKeyOutput
from akeyless.models.create_ldap_target import CreateLdapTarget
from akeyless.models.create_ldap_target_output import CreateLdapTargetOutput
from akeyless.models.create_native_k8_s_target import CreateNativeK8STarget
from akeyless.models.create_native_k8_s_target_output import CreateNativeK8STargetOutput
from akeyless.models.create_pki_cert_issuer import CreatePKICertIssuer
from akeyless.models.create_pki_cert_issuer_output import CreatePKICertIssuerOutput
from akeyless.models.create_rabbit_mq_target import CreateRabbitMQTarget
from akeyless.models.create_rabbit_mq_target_output import CreateRabbitMQTargetOutput
from akeyless.models.create_role import CreateRole
from akeyless.models.create_role_auth_method_assoc_output import CreateRoleAuthMethodAssocOutput
from akeyless.models.create_rotated_secret import CreateRotatedSecret
from akeyless.models.create_rotated_secret_output import CreateRotatedSecretOutput
from akeyless.models.create_ssh_cert_issuer import CreateSSHCertIssuer
from akeyless.models.create_ssh_cert_issuer_output import CreateSSHCertIssuerOutput
from akeyless.models.create_ssh_target import CreateSSHTarget
from akeyless.models.create_ssh_target_output import CreateSSHTargetOutput
from akeyless.models.create_secret import CreateSecret
from akeyless.models.create_secret_output import CreateSecretOutput
from akeyless.models.create_target_item_assoc_output import CreateTargetItemAssocOutput
from akeyless.models.create_web_target import CreateWebTarget
from akeyless.models.create_web_target_output import CreateWebTargetOutput
from akeyless.models.customer_fragment import CustomerFragment
from akeyless.models.customer_fragments_json import CustomerFragmentsJson
from akeyless.models.customer_full_address import CustomerFullAddress
from akeyless.models.ds_producer_details import DSProducerDetails
from akeyless.models.datadog_forwarding_config import DatadogForwardingConfig
from akeyless.models.decrypt import Decrypt
from akeyless.models.decrypt_file import DecryptFile
from akeyless.models.decrypt_file_output import DecryptFileOutput
from akeyless.models.decrypt_output import DecryptOutput
from akeyless.models.decrypt_pkcs1 import DecryptPKCS1
from akeyless.models.decrypt_pkcs1_output import DecryptPKCS1Output
from akeyless.models.decrypt_with_classic_key import DecryptWithClassicKey
from akeyless.models.decrypt_with_classic_key_output import DecryptWithClassicKeyOutput
from akeyless.models.default_config_part import DefaultConfigPart
from akeyless.models.delete_auth_method import DeleteAuthMethod
from akeyless.models.delete_auth_method_output import DeleteAuthMethodOutput
from akeyless.models.delete_auth_methods import DeleteAuthMethods
from akeyless.models.delete_auth_methods_output import DeleteAuthMethodsOutput
from akeyless.models.delete_item import DeleteItem
from akeyless.models.delete_item_output import DeleteItemOutput
from akeyless.models.delete_items import DeleteItems
from akeyless.models.delete_items_output import DeleteItemsOutput
from akeyless.models.delete_role import DeleteRole
from akeyless.models.delete_role_association import DeleteRoleAssociation
from akeyless.models.delete_role_rule import DeleteRoleRule
from akeyless.models.delete_role_rule_output import DeleteRoleRuleOutput
from akeyless.models.delete_roles import DeleteRoles
from akeyless.models.delete_target import DeleteTarget
from akeyless.models.delete_target_association import DeleteTargetAssociation
from akeyless.models.delete_targets import DeleteTargets
from akeyless.models.describe_item import DescribeItem
from akeyless.models.describe_permissions import DescribePermissions
from akeyless.models.describe_permissions_output import DescribePermissionsOutput
from akeyless.models.dynamic_secret_producer_info import DynamicSecretProducerInfo
from akeyless.models.elasticsearch_log_forwarding_config import ElasticsearchLogForwardingConfig
from akeyless.models.email_pass_access_rules import EmailPassAccessRules
from akeyless.models.encrypt import Encrypt
from akeyless.models.encrypt_file import EncryptFile
from akeyless.models.encrypt_file_output import EncryptFileOutput
from akeyless.models.encrypt_output import EncryptOutput
from akeyless.models.encrypt_pkcs1 import EncryptPKCS1
from akeyless.models.encrypt_pkcs1_output import EncryptPKCS1Output
from akeyless.models.encrypt_with_classic_key import EncryptWithClassicKey
from akeyless.models.encrypt_with_classic_key_output import EncryptWithClassicKeyOutput
from akeyless.models.external_kms_key_id import ExternalKMSKeyId
from akeyless.models.gcp_access_rules import GCPAccessRules
from akeyless.models.gateway_add_allowed_management_access import GatewayAddAllowedManagementAccess
from akeyless.models.gateway_create_k8_s_auth_config import GatewayCreateK8SAuthConfig
from akeyless.models.gateway_create_k8_s_auth_config_output import GatewayCreateK8SAuthConfigOutput
from akeyless.models.gateway_create_producer_artifactory import GatewayCreateProducerArtifactory
from akeyless.models.gateway_create_producer_artifactory_output import GatewayCreateProducerArtifactoryOutput
from akeyless.models.gateway_create_producer_aws import GatewayCreateProducerAws
from akeyless.models.gateway_create_producer_aws_output import GatewayCreateProducerAwsOutput
from akeyless.models.gateway_create_producer_azure import GatewayCreateProducerAzure
from akeyless.models.gateway_create_producer_azure_output import GatewayCreateProducerAzureOutput
from akeyless.models.gateway_create_producer_cassandra import GatewayCreateProducerCassandra
from akeyless.models.gateway_create_producer_cassandra_output import GatewayCreateProducerCassandraOutput
from akeyless.models.gateway_create_producer_certificate_automation import GatewayCreateProducerCertificateAutomation
from akeyless.models.gateway_create_producer_certificate_automation_output import GatewayCreateProducerCertificateAutomationOutput
from akeyless.models.gateway_create_producer_chef import GatewayCreateProducerChef
from akeyless.models.gateway_create_producer_chef_output import GatewayCreateProducerChefOutput
from akeyless.models.gateway_create_producer_custom import GatewayCreateProducerCustom
from akeyless.models.gateway_create_producer_custom_output import GatewayCreateProducerCustomOutput
from akeyless.models.gateway_create_producer_dockerhub import GatewayCreateProducerDockerhub
from akeyless.models.gateway_create_producer_dockerhub_output import GatewayCreateProducerDockerhubOutput
from akeyless.models.gateway_create_producer_eks import GatewayCreateProducerEks
from akeyless.models.gateway_create_producer_eks_output import GatewayCreateProducerEksOutput
from akeyless.models.gateway_create_producer_gcp import GatewayCreateProducerGcp
from akeyless.models.gateway_create_producer_gcp_output import GatewayCreateProducerGcpOutput
from akeyless.models.gateway_create_producer_github import GatewayCreateProducerGithub
from akeyless.models.gateway_create_producer_github_output import GatewayCreateProducerGithubOutput
from akeyless.models.gateway_create_producer_gke import GatewayCreateProducerGke
from akeyless.models.gateway_create_producer_gke_output import GatewayCreateProducerGkeOutput
from akeyless.models.gateway_create_producer_hana_db import GatewayCreateProducerHanaDb
from akeyless.models.gateway_create_producer_hana_db_output import GatewayCreateProducerHanaDbOutput
from akeyless.models.gateway_create_producer_ldap import GatewayCreateProducerLdap
from akeyless.models.gateway_create_producer_ldap_output import GatewayCreateProducerLdapOutput
from akeyless.models.gateway_create_producer_mssql import GatewayCreateProducerMSSQL
from akeyless.models.gateway_create_producer_mssql_output import GatewayCreateProducerMSSQLOutput
from akeyless.models.gateway_create_producer_mongo import GatewayCreateProducerMongo
from akeyless.models.gateway_create_producer_mongo_output import GatewayCreateProducerMongoOutput
from akeyless.models.gateway_create_producer_my_sql import GatewayCreateProducerMySQL
from akeyless.models.gateway_create_producer_my_sql_output import GatewayCreateProducerMySQLOutput
from akeyless.models.gateway_create_producer_native_k8_s import GatewayCreateProducerNativeK8S
from akeyless.models.gateway_create_producer_native_k8_s_output import GatewayCreateProducerNativeK8SOutput
from akeyless.models.gateway_create_producer_oracle_db import GatewayCreateProducerOracleDb
from akeyless.models.gateway_create_producer_oracle_db_output import GatewayCreateProducerOracleDbOutput
from akeyless.models.gateway_create_producer_postgre_sql import GatewayCreateProducerPostgreSQL
from akeyless.models.gateway_create_producer_postgre_sql_output import GatewayCreateProducerPostgreSQLOutput
from akeyless.models.gateway_create_producer_rabbit_mq import GatewayCreateProducerRabbitMQ
from akeyless.models.gateway_create_producer_rabbit_mq_output import GatewayCreateProducerRabbitMQOutput
from akeyless.models.gateway_create_producer_rdp import GatewayCreateProducerRdp
from akeyless.models.gateway_create_producer_rdp_output import GatewayCreateProducerRdpOutput
from akeyless.models.gateway_create_producer_redshift import GatewayCreateProducerRedshift
from akeyless.models.gateway_create_producer_redshift_output import GatewayCreateProducerRedshiftOutput
from akeyless.models.gateway_create_producer_snowflake import GatewayCreateProducerSnowflake
from akeyless.models.gateway_create_producer_snowflake_output import GatewayCreateProducerSnowflakeOutput
from akeyless.models.gateway_delete_allowed_management_access import GatewayDeleteAllowedManagementAccess
from akeyless.models.gateway_delete_k8_s_auth_config import GatewayDeleteK8SAuthConfig
from akeyless.models.gateway_delete_k8_s_auth_config_output import GatewayDeleteK8SAuthConfigOutput
from akeyless.models.gateway_delete_producer import GatewayDeleteProducer
from akeyless.models.gateway_delete_producer_output import GatewayDeleteProducerOutput
from akeyless.models.gateway_get_config import GatewayGetConfig
from akeyless.models.gateway_get_k8_s_auth_config import GatewayGetK8SAuthConfig
from akeyless.models.gateway_get_k8_s_auth_config_output import GatewayGetK8SAuthConfigOutput
from akeyless.models.gateway_get_producer import GatewayGetProducer
from akeyless.models.gateway_get_tmp_users import GatewayGetTmpUsers
from akeyless.models.gateway_list_allowed_management_access import GatewayListAllowedManagementAccess
from akeyless.models.gateway_list_migration import GatewayListMigration
from akeyless.models.gateway_list_producers import GatewayListProducers
from akeyless.models.gateway_message_queue_info import GatewayMessageQueueInfo
from akeyless.models.gateway_migration_list_output import GatewayMigrationListOutput
from akeyless.models.gateway_migration_sync_output import GatewayMigrationSyncOutput
from akeyless.models.gateway_revoke_tmp_users import GatewayRevokeTmpUsers
from akeyless.models.gateway_start_producer import GatewayStartProducer
from akeyless.models.gateway_start_producer_output import GatewayStartProducerOutput
from akeyless.models.gateway_stop_producer import GatewayStopProducer
from akeyless.models.gateway_stop_producer_output import GatewayStopProducerOutput
from akeyless.models.gateway_sync_migration import GatewaySyncMigration
from akeyless.models.gateway_update_item import GatewayUpdateItem
from akeyless.models.gateway_update_item_output import GatewayUpdateItemOutput
from akeyless.models.gateway_update_k8_s_auth_config import GatewayUpdateK8SAuthConfig
from akeyless.models.gateway_update_k8_s_auth_config_output import GatewayUpdateK8SAuthConfigOutput
from akeyless.models.gateway_update_producer_artifactory import GatewayUpdateProducerArtifactory
from akeyless.models.gateway_update_producer_artifactory_output import GatewayUpdateProducerArtifactoryOutput
from akeyless.models.gateway_update_producer_aws import GatewayUpdateProducerAws
from akeyless.models.gateway_update_producer_aws_output import GatewayUpdateProducerAwsOutput
from akeyless.models.gateway_update_producer_azure import GatewayUpdateProducerAzure
from akeyless.models.gateway_update_producer_azure_output import GatewayUpdateProducerAzureOutput
from akeyless.models.gateway_update_producer_cassandra import GatewayUpdateProducerCassandra
from akeyless.models.gateway_update_producer_cassandra_output import GatewayUpdateProducerCassandraOutput
from akeyless.models.gateway_update_producer_certificate_automation import GatewayUpdateProducerCertificateAutomation
from akeyless.models.gateway_update_producer_certificate_automation_output import GatewayUpdateProducerCertificateAutomationOutput
from akeyless.models.gateway_update_producer_chef import GatewayUpdateProducerChef
from akeyless.models.gateway_update_producer_chef_output import GatewayUpdateProducerChefOutput
from akeyless.models.gateway_update_producer_custom import GatewayUpdateProducerCustom
from akeyless.models.gateway_update_producer_custom_output import GatewayUpdateProducerCustomOutput
from akeyless.models.gateway_update_producer_dockerhub import GatewayUpdateProducerDockerhub
from akeyless.models.gateway_update_producer_dockerhub_output import GatewayUpdateProducerDockerhubOutput
from akeyless.models.gateway_update_producer_eks import GatewayUpdateProducerEks
from akeyless.models.gateway_update_producer_eks_output import GatewayUpdateProducerEksOutput
from akeyless.models.gateway_update_producer_gcp import GatewayUpdateProducerGcp
from akeyless.models.gateway_update_producer_gcp_output import GatewayUpdateProducerGcpOutput
from akeyless.models.gateway_update_producer_github import GatewayUpdateProducerGithub
from akeyless.models.gateway_update_producer_github_output import GatewayUpdateProducerGithubOutput
from akeyless.models.gateway_update_producer_gke import GatewayUpdateProducerGke
from akeyless.models.gateway_update_producer_gke_output import GatewayUpdateProducerGkeOutput
from akeyless.models.gateway_update_producer_hana_db import GatewayUpdateProducerHanaDb
from akeyless.models.gateway_update_producer_hana_db_output import GatewayUpdateProducerHanaDbOutput
from akeyless.models.gateway_update_producer_ldap import GatewayUpdateProducerLdap
from akeyless.models.gateway_update_producer_ldap_output import GatewayUpdateProducerLdapOutput
from akeyless.models.gateway_update_producer_mssql import GatewayUpdateProducerMSSQL
from akeyless.models.gateway_update_producer_mssql_output import GatewayUpdateProducerMSSQLOutput
from akeyless.models.gateway_update_producer_mongo import GatewayUpdateProducerMongo
from akeyless.models.gateway_update_producer_mongo_output import GatewayUpdateProducerMongoOutput
from akeyless.models.gateway_update_producer_my_sql import GatewayUpdateProducerMySQL
from akeyless.models.gateway_update_producer_my_sql_output import GatewayUpdateProducerMySQLOutput
from akeyless.models.gateway_update_producer_native_k8_s import GatewayUpdateProducerNativeK8S
from akeyless.models.gateway_update_producer_native_k8_s_output import GatewayUpdateProducerNativeK8SOutput
from akeyless.models.gateway_update_producer_oracle_db import GatewayUpdateProducerOracleDb
from akeyless.models.gateway_update_producer_oracle_db_output import GatewayUpdateProducerOracleDbOutput
from akeyless.models.gateway_update_producer_postgre_sql import GatewayUpdateProducerPostgreSQL
from akeyless.models.gateway_update_producer_postgre_sql_output import GatewayUpdateProducerPostgreSQLOutput
from akeyless.models.gateway_update_producer_rabbit_mq import GatewayUpdateProducerRabbitMQ
from akeyless.models.gateway_update_producer_rabbit_mq_output import GatewayUpdateProducerRabbitMQOutput
from akeyless.models.gateway_update_producer_rdp import GatewayUpdateProducerRdp
from akeyless.models.gateway_update_producer_rdp_output import GatewayUpdateProducerRdpOutput
from akeyless.models.gateway_update_producer_redshift import GatewayUpdateProducerRedshift
from akeyless.models.gateway_update_producer_redshift_output import GatewayUpdateProducerRedshiftOutput
from akeyless.models.gateway_update_producer_snowflake import GatewayUpdateProducerSnowflake
from akeyless.models.gateway_update_producer_snowflake_output import GatewayUpdateProducerSnowflakeOutput
from akeyless.models.gateway_update_tmp_users import GatewayUpdateTmpUsers
from akeyless.models.gen_customer_fragment import GenCustomerFragment
from akeyless.models.general_config_part import GeneralConfigPart
from akeyless.models.get_account_settings import GetAccountSettings
from akeyless.models.get_account_settings_command_output import GetAccountSettingsCommandOutput
from akeyless.models.get_auth_method import GetAuthMethod
from akeyless.models.get_cloud_identity import GetCloudIdentity
from akeyless.models.get_cloud_identity_output import GetCloudIdentityOutput
from akeyless.models.get_dynamic_secret_value import GetDynamicSecretValue
from akeyless.models.get_kube_exec_creds import GetKubeExecCreds
from akeyless.models.get_kube_exec_creds_output import GetKubeExecCredsOutput
from akeyless.models.get_pki_certificate import GetPKICertificate
from akeyless.models.get_pki_certificate_output import GetPKICertificateOutput
from akeyless.models.get_producers_list_reply_obj import GetProducersListReplyObj
from akeyless.models.get_rsa_public import GetRSAPublic
from akeyless.models.get_rsa_public_output import GetRSAPublicOutput
from akeyless.models.get_role import GetRole
from akeyless.models.get_rotated_secret_value import GetRotatedSecretValue
from akeyless.models.get_ssh_certificate import GetSSHCertificate
from akeyless.models.get_ssh_certificate_output import GetSSHCertificateOutput
from akeyless.models.get_secret_value import GetSecretValue
from akeyless.models.get_sub_admins_list_reply_obj import GetSubAdminsListReplyObj
from akeyless.models.get_tags import GetTags
from akeyless.models.get_target import GetTarget
from akeyless.models.get_target_details import GetTargetDetails
from akeyless.models.get_target_details_output import GetTargetDetailsOutput
from akeyless.models.hashi_migration import HashiMigration
from akeyless.models.hashi_payload import HashiPayload
from akeyless.models.huawei_access_rules import HuaweiAccessRules
from akeyless.models.item import Item
from akeyless.models.item_general_info import ItemGeneralInfo
from akeyless.models.item_target_association import ItemTargetAssociation
from akeyless.models.item_version import ItemVersion
from akeyless.models.json_error import JSONError
from akeyless.models.k8_s_auth import K8SAuth
from akeyless.models.k8_s_auths_config_last_change import K8SAuthsConfigLastChange
from akeyless.models.k8_s_auths_config_part import K8SAuthsConfigPart
from akeyless.models.k8_s_migration import K8SMigration
from akeyless.models.k8_s_payload import K8SPayload
from akeyless.models.kmip_client import KMIPClient
from akeyless.models.kmip_client_get_response import KMIPClientGetResponse
from akeyless.models.kmip_client_list_response import KMIPClientListResponse
from akeyless.models.kmip_client_update_response import KMIPClientUpdateResponse
from akeyless.models.kmip_config_part import KMIPConfigPart
from akeyless.models.kmip_environment_create_response import KMIPEnvironmentCreateResponse
from akeyless.models.kmip_server import KMIPServer
from akeyless.models.kmip_client_delete_rule import KmipClientDeleteRule
from akeyless.models.kmip_client_set_rule import KmipClientSetRule
from akeyless.models.kmip_create_client import KmipCreateClient
from akeyless.models.kmip_create_client_output import KmipCreateClientOutput
from akeyless.models.kmip_delete_client import KmipDeleteClient
from akeyless.models.kmip_delete_server import KmipDeleteServer
from akeyless.models.kmip_describe_client import KmipDescribeClient
from akeyless.models.kmip_describe_server import KmipDescribeServer
from akeyless.models.kmip_describe_server_output import KmipDescribeServerOutput
from akeyless.models.kmip_list_clients import KmipListClients
from akeyless.models.kmip_move_server import KmipMoveServer
from akeyless.models.kmip_move_server_output import KmipMoveServerOutput
from akeyless.models.kmip_renew_client_certificate import KmipRenewClientCertificate
from akeyless.models.kmip_renew_client_certificate_output import KmipRenewClientCertificateOutput
from akeyless.models.kmip_renew_server_certificate import KmipRenewServerCertificate
from akeyless.models.kmip_renew_server_certificate_output import KmipRenewServerCertificateOutput
from akeyless.models.kmip_server_setup import KmipServerSetup
from akeyless.models.kmip_set_server_state import KmipSetServerState
from akeyless.models.kmip_set_server_state_output import KmipSetServerStateOutput
from akeyless.models.kubernetes_access_rules import KubernetesAccessRules
from akeyless.models.ldap_access_rules import LDAPAccessRules
from akeyless.models.last_config_change import LastConfigChange
from akeyless.models.last_status_info import LastStatusInfo
from akeyless.models.ldap_config_part import LdapConfigPart
from akeyless.models.leadership_config_part import LeadershipConfigPart
from akeyless.models.list_auth_methods import ListAuthMethods
from akeyless.models.list_auth_methods_output import ListAuthMethodsOutput
from akeyless.models.list_items import ListItems
from akeyless.models.list_items_in_path_output import ListItemsInPathOutput
from akeyless.models.list_roles import ListRoles
from akeyless.models.list_roles_output import ListRolesOutput
from akeyless.models.list_targets import ListTargets
from akeyless.models.list_targets_output import ListTargetsOutput
from akeyless.models.log_forwarding_config_part import LogForwardingConfigPart
from akeyless.models.logstash_log_forwarding_config import LogstashLogForwardingConfig
from akeyless.models.logz_io_log_forwarding_config import LogzIoLogForwardingConfig
from akeyless.models.migration_general import MigrationGeneral
from akeyless.models.migration_status import MigrationStatus
from akeyless.models.migrations_config_last_change import MigrationsConfigLastChange
from akeyless.models.migrations_config_part import MigrationsConfigPart
from akeyless.models.move_objects import MoveObjects
from akeyless.models.o_auth2_access_rules import OAuth2AccessRules
from akeyless.models.o_auth2_custom_claim import OAuth2CustomClaim
from akeyless.models.oidc_access_rules import OIDCAccessRules
from akeyless.models.oidc_custom_claim import OIDCCustomClaim
from akeyless.models.object_version_settings_output import ObjectVersionSettingsOutput
from akeyless.models.pki_certificate_issue_details import PKICertificateIssueDetails
from akeyless.models.password_policy_info import PasswordPolicyInfo
from akeyless.models.path_rule import PathRule
from akeyless.models.producer import Producer
from akeyless.models.producers_config_part import ProducersConfigPart
from akeyless.models.raw_creds import RawCreds
from akeyless.models.refresh_key import RefreshKey
from akeyless.models.refresh_key_output import RefreshKeyOutput
from akeyless.models.required_activity import RequiredActivity
from akeyless.models.reverse_rbac import ReverseRBAC
from akeyless.models.reverse_rbac_client import ReverseRBACClient
from akeyless.models.reverse_rbac_output import ReverseRBACOutput
from akeyless.models.revoke_creds import RevokeCreds
from akeyless.models.role import Role
from akeyless.models.role_auth_method_association import RoleAuthMethodAssociation
from akeyless.models.rollback_secret import RollbackSecret
from akeyless.models.rollback_secret_output import RollbackSecretOutput
from akeyless.models.rotate_key import RotateKey
from akeyless.models.rotate_key_output import RotateKeyOutput
from akeyless.models.rotated_secret_details_info import RotatedSecretDetailsInfo
from akeyless.models.rotator import Rotator
from akeyless.models.rotators_config_part import RotatorsConfigPart
from akeyless.models.rules import Rules
from akeyless.models.saml_access_rules import SAMLAccessRules
from akeyless.models.saml_attribute import SAMLAttribute
from akeyless.models.ssh_certificate_issue_details import SSHCertificateIssueDetails
from akeyless.models.secure_remote_access import SecureRemoteAccess
from akeyless.models.set_item_state import SetItemState
from akeyless.models.set_role_rule import SetRoleRule
from akeyless.models.sign_jwt_output import SignJWTOutput
from akeyless.models.sign_jwt_with_classic_key import SignJWTWithClassicKey
from akeyless.models.sign_pkcs1 import SignPKCS1
from akeyless.models.sign_pkcs1_output import SignPKCS1Output
from akeyless.models.sign_pki_cert_output import SignPKICertOutput
from akeyless.models.sign_pki_cert_with_classic_key import SignPKICertWithClassicKey
from akeyless.models.sm_info import SmInfo
from akeyless.models.splunk_log_forwarding_config import SplunkLogForwardingConfig
from akeyless.models.sra_info import SraInfo
from akeyless.models.static_creds_auth import StaticCredsAuth
from akeyless.models.static_creds_auth_output import StaticCredsAuthOutput
from akeyless.models.static_secret_details_info import StaticSecretDetailsInfo
from akeyless.models.syslog_log_forwarding_config import SyslogLogForwardingConfig
from akeyless.models.system_access_credentials_reply_obj import SystemAccessCredentialsReplyObj
from akeyless.models.system_access_creds_settings import SystemAccessCredsSettings
from akeyless.models.target import Target
from akeyless.models.target_item_association import TargetItemAssociation
from akeyless.models.target_item_version import TargetItemVersion
from akeyless.models.target_type_details_input import TargetTypeDetailsInput
from akeyless.models.tmp_user_data import TmpUserData
from akeyless.models.uid_token_details import UIDTokenDetails
from akeyless.models.uid_create_child_token import UidCreateChildToken
from akeyless.models.uid_create_child_token_output import UidCreateChildTokenOutput
from akeyless.models.uid_generate_token import UidGenerateToken
from akeyless.models.uid_generate_token_output import UidGenerateTokenOutput
from akeyless.models.uid_list_children import UidListChildren
from akeyless.models.uid_revoke_token import UidRevokeToken
from akeyless.models.uid_rotate_token import UidRotateToken
from akeyless.models.uid_rotate_token_output import UidRotateTokenOutput
from akeyless.models.unconfigure import Unconfigure
from akeyless.models.universal_identity_access_rules import UniversalIdentityAccessRules
from akeyless.models.universal_identity_details import UniversalIdentityDetails
from akeyless.models.update import Update
from akeyless.models.update_aws_target import UpdateAWSTarget
from akeyless.models.update_aws_target_details import UpdateAWSTargetDetails
from akeyless.models.update_account_settings import UpdateAccountSettings
from akeyless.models.update_account_settings_output import UpdateAccountSettingsOutput
from akeyless.models.update_artifactory_target import UpdateArtifactoryTarget
from akeyless.models.update_artifactory_target_output import UpdateArtifactoryTargetOutput
from akeyless.models.update_assoc import UpdateAssoc
from akeyless.models.update_auth_method import UpdateAuthMethod
from akeyless.models.update_auth_method_awsiam import UpdateAuthMethodAWSIAM
from akeyless.models.update_auth_method_azure_ad import UpdateAuthMethodAzureAD
from akeyless.models.update_auth_method_cert import UpdateAuthMethodCert
from akeyless.models.update_auth_method_cert_output import UpdateAuthMethodCertOutput
from akeyless.models.update_auth_method_gcp import UpdateAuthMethodGCP
from akeyless.models.update_auth_method_k8_s import UpdateAuthMethodK8S
from akeyless.models.update_auth_method_k8_s_output import UpdateAuthMethodK8SOutput
from akeyless.models.update_auth_method_ldap import UpdateAuthMethodLDAP
from akeyless.models.update_auth_method_o_auth2 import UpdateAuthMethodOAuth2
from akeyless.models.update_auth_method_oidc import UpdateAuthMethodOIDC
from akeyless.models.update_auth_method_output import UpdateAuthMethodOutput
from akeyless.models.update_auth_method_saml import UpdateAuthMethodSAML
from akeyless.models.update_auth_method_universal_identity import UpdateAuthMethodUniversalIdentity
from akeyless.models.update_azure_target import UpdateAzureTarget
from akeyless.models.update_azure_target_output import UpdateAzureTargetOutput
from akeyless.models.update_db_target import UpdateDBTarget
from akeyless.models.update_db_target_details import UpdateDBTargetDetails
from akeyless.models.update_db_target_output import UpdateDBTargetOutput
from akeyless.models.update_dockerhub_target import UpdateDockerhubTarget
from akeyless.models.update_dockerhub_target_output import UpdateDockerhubTargetOutput
from akeyless.models.update_eks_target import UpdateEKSTarget
from akeyless.models.update_eks_target_output import UpdateEKSTargetOutput
from akeyless.models.update_gke_target import UpdateGKETarget
from akeyless.models.update_gke_target_output import UpdateGKETargetOutput
from akeyless.models.update_gcp_target import UpdateGcpTarget
from akeyless.models.update_gcp_target_output import UpdateGcpTargetOutput
from akeyless.models.update_github_target import UpdateGithubTarget
from akeyless.models.update_github_target_output import UpdateGithubTargetOutput
from akeyless.models.update_item import UpdateItem
from akeyless.models.update_item_output import UpdateItemOutput
from akeyless.models.update_native_k8_s_target import UpdateNativeK8STarget
from akeyless.models.update_native_k8_s_target_output import UpdateNativeK8STargetOutput
from akeyless.models.update_output import UpdateOutput
from akeyless.models.update_pki_cert_issuer import UpdatePKICertIssuer
from akeyless.models.update_pki_cert_issuer_output import UpdatePKICertIssuerOutput
from akeyless.models.update_rdp_target_details import UpdateRDPTargetDetails
from akeyless.models.update_rabbit_mq_target import UpdateRabbitMQTarget
from akeyless.models.update_rabbit_mq_target_details import UpdateRabbitMQTargetDetails
from akeyless.models.update_rabbit_mq_target_output import UpdateRabbitMQTargetOutput
from akeyless.models.update_role import UpdateRole
from akeyless.models.update_role_output import UpdateRoleOutput
from akeyless.models.update_rotated_secret import UpdateRotatedSecret
from akeyless.models.update_rotated_secret_output import UpdateRotatedSecretOutput
from akeyless.models.update_rotation_settings import UpdateRotationSettings
from akeyless.models.update_ssh_cert_issuer import UpdateSSHCertIssuer
from akeyless.models.update_ssh_cert_issuer_output import UpdateSSHCertIssuerOutput
from akeyless.models.update_ssh_target import UpdateSSHTarget
from akeyless.models.update_ssh_target_details import UpdateSSHTargetDetails
from akeyless.models.update_ssh_target_output import UpdateSSHTargetOutput
from akeyless.models.update_secret_val import UpdateSecretVal
from akeyless.models.update_secret_val_output import UpdateSecretValOutput
from akeyless.models.update_target import UpdateTarget
from akeyless.models.update_target_details_output import UpdateTargetDetailsOutput
from akeyless.models.update_target_output import UpdateTargetOutput
from akeyless.models.update_web_target import UpdateWebTarget
from akeyless.models.update_web_target_details import UpdateWebTargetDetails
from akeyless.models.update_web_target_output import UpdateWebTargetOutput
from akeyless.models.upload_pkcs12 import UploadPKCS12
from akeyless.models.upload_rsa import UploadRSA
from akeyless.models.validate_token import ValidateToken
from akeyless.models.validate_token_output import ValidateTokenOutput
from akeyless.models.verify_jwt_output import VerifyJWTOutput
from akeyless.models.verify_jwt_with_classic_key import VerifyJWTWithClassicKey
from akeyless.models.verify_pkcs1 import VerifyPKCS1
from akeyless.models.verify_pki_cert_output import VerifyPKICertOutput
from akeyless.models.verify_pki_cert_with_classic_key import VerifyPKICertWithClassicKey

