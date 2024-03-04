# coding: utf-8

"""
    Akeyless API

    The purpose of this application is to provide access to Akeyless API.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Contact: support@akeyless.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import akeyless
from akeyless.models.gateway_update_producer_venafi_output import GatewayUpdateProducerVenafiOutput  # noqa: E501
from akeyless.rest import ApiException

class TestGatewayUpdateProducerVenafiOutput(unittest.TestCase):
    """GatewayUpdateProducerVenafiOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GatewayUpdateProducerVenafiOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.gateway_update_producer_venafi_output.GatewayUpdateProducerVenafiOutput()  # noqa: E501
        if include_optional :
            return GatewayUpdateProducerVenafiOutput(
                producer_details = akeyless.models.ds_producer_details.DSProducerDetails(
                    access_token_manager_id = '0', 
                    acl_rules = [
                        '0'
                        ], 
                    active = True, 
                    admin_name = '0', 
                    admin_pwd = '0', 
                    admin_rotation_interval_days = 56, 
                    administrative_port = '0', 
                    artifactory_admin_apikey = '0', 
                    artifactory_admin_username = '0', 
                    artifactory_base_url = '0', 
                    artifactory_token_audience = '0', 
                    artifactory_token_scope = '0', 
                    authorization_port = '0', 
                    aws_access_key_id = '0', 
                    aws_access_mode = '0', 
                    aws_region = '0', 
                    aws_role_arns = '0', 
                    aws_secret_access_key = '0', 
                    aws_session_token = '0', 
                    aws_user_console_access = True, 
                    aws_user_groups = '0', 
                    aws_user_policies = '0', 
                    aws_user_programmatic_access = True, 
                    azure_app_object_id = '0', 
                    azure_client_id = '0', 
                    azure_client_secret = '0', 
                    azure_fixed_user_name_sub_claim_key = '0', 
                    azure_fixed_user_only = True, 
                    azure_resource_group_name = '0', 
                    azure_resource_name = '0', 
                    azure_subscription_id = '0', 
                    azure_tenant_id = '0', 
                    azure_user_groups_obj_id = '0', 
                    azure_user_portal_access = True, 
                    azure_user_programmatic_access = True, 
                    azure_user_roles_template_id = '0', 
                    cassandra_creation_statements = '0', 
                    chef_organizations = '0', 
                    chef_server_access_mode = '0', 
                    chef_server_host_name = '0', 
                    chef_server_key = '0', 
                    chef_server_port = '0', 
                    chef_server_url = '0', 
                    chef_server_username = '0', 
                    chef_skip_ssl = True, 
                    client_authentication_type = '0', 
                    cloud_service_provider = '0', 
                    connection_type = '0', 
                    create_sync_url = '0', 
                    db_client_id = '0', 
                    db_client_secret = '0', 
                    db_host_name = '0', 
                    db_isolation_level = '0', 
                    db_max_idle_conns = '0', 
                    db_max_open_conns = '0', 
                    db_name = '0', 
                    db_port = '0', 
                    db_private_key = '0', 
                    db_private_key_passphrase = '0', 
                    db_pwd = '0', 
                    db_server_certificates = '0', 
                    db_server_name = '0', 
                    db_tenant_id = '0', 
                    db_user_name = '0', 
                    delete_protection = True, 
                    dynamic_secret_id = 56, 
                    dynamic_secret_key = '0', 
                    dynamic_secret_name = '0', 
                    dynamic_secret_type = '0', 
                    eks_access_key_id = '0', 
                    eks_assume_role = '0', 
                    eks_cluster_ca_certificate = '0', 
                    eks_cluster_endpoint = '0', 
                    eks_cluster_name = '0', 
                    eks_region = '0', 
                    eks_secret_access_key = '0', 
                    enable_admin_rotation = True, 
                    enforce_replay_prevention = True, 
                    externally_provided_user = '0', 
                    failure_message = '0', 
                    fixed_user_only = '0', 
                    gcp_key_algo = '0', 
                    gcp_role_bindings = {
                        'key' : [
                            '0'
                            ]
                        }, 
                    gcp_service_account_email = '0', 
                    gcp_service_account_key = '0', 
                    gcp_service_account_key_base64 = '0', 
                    gcp_service_account_key_id = '0', 
                    gcp_service_account_type = '0', 
                    gcp_tmp_service_account_name = '0', 
                    gcp_token_lifetime = '0', 
                    gcp_token_scope = '0', 
                    gcp_token_type = '0', 
                    github_app_id = 56, 
                    github_app_private_key = '0', 
                    github_base_url = '0', 
                    github_installation_id = 56, 
                    github_installation_token_permissions = {
                        'key' : '0'
                        }, 
                    github_installation_token_repositories = [
                        '0'
                        ], 
                    github_installation_token_repositories_ids = [
                        56
                        ], 
                    github_organization_name = '0', 
                    github_repository_path = '0', 
                    gke_cluster_ca_certificate = '0', 
                    gke_cluster_endpoint = '0', 
                    gke_cluster_name = '0', 
                    gke_service_account_key = '0', 
                    gke_service_account_name = '0', 
                    grant_types = [
                        '0'
                        ], 
                    groups = '0', 
                    hanadb_creation_statements = '0', 
                    hanadb_revocation_statements = '0', 
                    host_name = '0', 
                    host_port = '0', 
                    implementation_type = '0', 
                    is_fixed_user = '0', 
                    issuer = '0', 
                    item_targets_assoc = [
                        akeyless.models.item_target_association_includes_details_of_an_association_between_an_item.ItemTargetAssociation includes details of an association between an item(
                            assoc_id = '0', 
                            attributes = {
                                'key' : '0'
                                }, 
                            target_id = 56, 
                            target_name = '0', 
                            target_type = '0', )
                        ], 
                    jwks = '0', 
                    jwks_url = '0', 
                    k8s_allowed_namespaces = '0', 
                    k8s_auth_type = '0', 
                    k8s_bearer_token = '0', 
                    k8s_client_cert_data = '0', 
                    k8s_client_key_data = '0', 
                    k8s_cluster_ca_certificate = '0', 
                    k8s_cluster_endpoint = '0', 
                    k8s_dynamic_mode = True, 
                    k8s_multiple_doc_yaml_temp_definition = [
                        56
                        ], 
                    k8s_namespace = '0', 
                    k8s_role_name = '0', 
                    k8s_role_type = '0', 
                    k8s_service_account = '0', 
                    last_admin_rotation = 56, 
                    ldap_audience = '0', 
                    ldap_bind_dn = '0', 
                    ldap_bind_password = '0', 
                    ldap_certificate = '0', 
                    ldap_group_dn = '0', 
                    ldap_token_expiration = '0', 
                    ldap_url = '0', 
                    ldap_user_attr = '0', 
                    ldap_user_dn = '0', 
                    metadata = '0', 
                    mongodb_atlas_api_private_key = '0', 
                    mongodb_atlas_api_public_key = '0', 
                    mongodb_atlas_project_id = '0', 
                    mongodb_custom_data = '0', 
                    mongodb_db_name = '0', 
                    mongodb_default_auth_db = '0', 
                    mongodb_host_port = '0', 
                    mongodb_is_atlas = True, 
                    mongodb_password = '0', 
                    mongodb_roles = '0', 
                    mongodb_uri_connection = '0', 
                    mongodb_uri_options = '0', 
                    mongodb_username = '0', 
                    mssql_creation_statements = '0', 
                    mssql_revocation_statements = '0', 
                    mysql_creation_statements = '0', 
                    mysql_revocation_statements = '0', 
                    oracle_creation_statements = '0', 
                    oracle_revocation_statements = '0', 
                    password = '0', 
                    password_length = 56, 
                    password_policy = '0', 
                    payload = '0', 
                    ping_url = '0', 
                    postgres_creation_statements = '0', 
                    postgres_revocation_statements = '0', 
                    privileged_user = '0', 
                    rabbitmq_server_password = '0', 
                    rabbitmq_server_uri = '0', 
                    rabbitmq_server_user = '0', 
                    rabbitmq_user_conf_permission = '0', 
                    rabbitmq_user_read_permission = '0', 
                    rabbitmq_user_tags = '0', 
                    rabbitmq_user_vhost = '0', 
                    rabbitmq_user_write_permission = '0', 
                    redirect_uris = [
                        '0'
                        ], 
                    redshift_creation_statements = '0', 
                    restricted_scopes = [
                        '0'
                        ], 
                    revoke_sync_url = '0', 
                    rotate_sync_url = '0', 
                    scopes = [
                        '0'
                        ], 
                    secure_remote_access_details = akeyless.models.secure_remote_access.SecureRemoteAccess(
                        account_id = '0', 
                        allow_port_forwarding = True, 
                        allow_providing_external_username = True, 
                        bastion_api = '0', 
                        bastion_issuer = '0', 
                        bastion_issuer_id = 56, 
                        bastion_ssh = '0', 
                        category = '0', 
                        dashboard_url = '0', 
                        db_name = '0', 
                        domain = '0', 
                        enable = True, 
                        endpoint = '0', 
                        host = [
                            '0'
                            ], 
                        host_provider_type = '0', 
                        is_cli = True, 
                        is_web = True, 
                        isolated = True, 
                        native = True, 
                        rd_gateway_server = '0', 
                        rdp_user = '0', 
                        region = '0', 
                        rotate_after_disconnect = True, 
                        schema = '0', 
                        ssh_password = True, 
                        ssh_private_key = True, 
                        ssh_user = '0', 
                        target_hosts = [
                            akeyless.models.target_name_with_hosts.TargetNameWithHosts(
                                hosts = [
                                    '0'
                                    ], 
                                target_name = '0', )
                            ], 
                        targets = [
                            '0'
                            ], 
                        url = '0', 
                        use_internal_bastion = True, 
                        web_proxy = True, ), 
                    session_extension_warn_interval_min = 56, 
                    sf_account = '0', 
                    sf_user_role = '0', 
                    sf_warehouse_name = '0', 
                    should_stop = '0', 
                    signing_algorithm = '0', 
                    ssl_connection_certificate = '0', 
                    ssl_connection_mode = True, 
                    subject_dn = '0', 
                    tags = [
                        '0'
                        ], 
                    timeout_seconds = 56, 
                    use_gw_cloud_identity = True, 
                    use_gw_service_account = True, 
                    user_name = '0', 
                    user_password = '0', 
                    user_principal_name = '0', 
                    user_ttl = '0', 
                    username_length = 56, 
                    username_policy = '0', 
                    venafi_allow_subdomains = True, 
                    venafi_allowed_domains = [
                        '0'
                        ], 
                    venafi_api_key = '0', 
                    venafi_auto_generated_folder = '0', 
                    venafi_base_url = '0', 
                    venafi_root_first_in_chain = True, 
                    venafi_sign_using_akeyless_pki = True, 
                    venafi_signer_key_name = '0', 
                    venafi_store_private_key = True, 
                    venafi_tpp_access_token = '0', 
                    venafi_tpp_client_id = '0', 
                    venafi_tpp_password = '0', 
                    venafi_tpp_refresh_token = '0', 
                    venafi_tpp_username = '0', 
                    venafi_use_tpp = True, 
                    venafi_zone = '0', 
                    warn_before_user_expiration_min = 56, )
            )
        else :
            return GatewayUpdateProducerVenafiOutput(
        )

    def testGatewayUpdateProducerVenafiOutput(self):
        """Test GatewayUpdateProducerVenafiOutput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
