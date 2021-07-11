# akeyless
The purpose of this application is to provide access to Akeyless API.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.0
- Package version: 2.5.2
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [http://akeyless.io](http://akeyless.io)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/akeylesslabs/akeyless-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/akeylesslabs/akeyless-python.git`)

Then import the package:
```python
import akeyless
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import akeyless
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import akeyless
from akeyless.rest import ApiException

# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
        # default: public API Gateway
        host = "https://api.akeyless.io"

        # use port 8081 exposed by the deployment:
        # host = "https://gateway.company.com:8081"

        # use port 8080 exposed by the deployment with /v2 prefix:
        # host = "https://gateway.company.com:8080/v2"
)

with akeyless.ApiClient(configuration) as api_client:
    api = akeyless.V2Api(api_client)

    body = akeyless.Auth(access_id='p-1234567890', access_key='aXQncyBvbmx5IGJhc2U2NC4uLgo=')
    res = api.auth(body)
    token = res.token

    body = akeyless.CreateSecret(name='my-secret', value='some-value', token=token)
    api.create_secret(body)

    body = akeyless.GetSecretValue(names=['my-secret'], token=token)
    res = api.get_secret_value(body)
    print(res['my-secret']) # some-value
```

## Documentation for API Endpoints

All URIs are relative to *https://api.akeyless.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*V2Api* | [**assoc_role_auth_method**](docs/V2Api.md#assoc_role_auth_method) | **POST** /assoc-role-am | 
*V2Api* | [**assoc_target_item**](docs/V2Api.md#assoc_target_item) | **POST** /assoc-target-item | 
*V2Api* | [**auth**](docs/V2Api.md#auth) | **POST** /auth | 
*V2Api* | [**configure**](docs/V2Api.md#configure) | **POST** /configure | 
*V2Api* | [**create_artifactory_target**](docs/V2Api.md#create_artifactory_target) | **POST** /create-artifactory-target | 
*V2Api* | [**create_auth_method**](docs/V2Api.md#create_auth_method) | **POST** /create-auth-method | 
*V2Api* | [**create_auth_method_awsiam**](docs/V2Api.md#create_auth_method_awsiam) | **POST** /create-auth-method-aws-iam | 
*V2Api* | [**create_auth_method_azure_ad**](docs/V2Api.md#create_auth_method_azure_ad) | **POST** /create-auth-method-azure-ad | 
*V2Api* | [**create_auth_method_gcp**](docs/V2Api.md#create_auth_method_gcp) | **POST** /create-auth-method-gcp | 
*V2Api* | [**create_auth_method_huawei**](docs/V2Api.md#create_auth_method_huawei) | **POST** /create-auth-method-huawei | 
*V2Api* | [**create_auth_method_o_auth2**](docs/V2Api.md#create_auth_method_o_auth2) | **POST** /create-auth-method-oauth2 | 
*V2Api* | [**create_auth_method_saml**](docs/V2Api.md#create_auth_method_saml) | **POST** /create-auth-method-saml | 
*V2Api* | [**create_auth_method_universal_identity**](docs/V2Api.md#create_auth_method_universal_identity) | **POST** /create-auth-method-universal-identity | 
*V2Api* | [**create_aws_target**](docs/V2Api.md#create_aws_target) | **POST** /create-aws-target | 
*V2Api* | [**create_azure_target**](docs/V2Api.md#create_azure_target) | **POST** /create-azure-target | 
*V2Api* | [**create_classic_key**](docs/V2Api.md#create_classic_key) | **POST** /create-classic-key | 
*V2Api* | [**create_db_target**](docs/V2Api.md#create_db_target) | **POST** /create-db-target | 
*V2Api* | [**create_dfc_key**](docs/V2Api.md#create_dfc_key) | **POST** /create-dfc-key | 
*V2Api* | [**create_dynamic_secret**](docs/V2Api.md#create_dynamic_secret) | **POST** /create-dynamic-secret | 
*V2Api* | [**create_eks_target**](docs/V2Api.md#create_eks_target) | **POST** /create-eks-target | 
*V2Api* | [**create_gcp_target**](docs/V2Api.md#create_gcp_target) | **POST** /create-gcp-target | 
*V2Api* | [**create_gke_target**](docs/V2Api.md#create_gke_target) | **POST** /create-gke-target | 
*V2Api* | [**create_key**](docs/V2Api.md#create_key) | **POST** /create-key | 
*V2Api* | [**create_native_k8_s_target**](docs/V2Api.md#create_native_k8_s_target) | **POST** /create-k8s-target | 
*V2Api* | [**create_pki_cert_issuer**](docs/V2Api.md#create_pki_cert_issuer) | **POST** /create-pki-cert-issuer | 
*V2Api* | [**create_rabbit_mq_target**](docs/V2Api.md#create_rabbit_mq_target) | **POST** /create-rabbitmq-target | 
*V2Api* | [**create_role**](docs/V2Api.md#create_role) | **POST** /create-role | 
*V2Api* | [**create_rotated_secret**](docs/V2Api.md#create_rotated_secret) | **POST** /create-rotated-secret | 
*V2Api* | [**create_secret**](docs/V2Api.md#create_secret) | **POST** /create-secret | 
*V2Api* | [**create_ssh_cert_issuer**](docs/V2Api.md#create_ssh_cert_issuer) | **POST** /create-ssh-cert-issuer | 
*V2Api* | [**create_ssh_target**](docs/V2Api.md#create_ssh_target) | **POST** /create-ssh-target | 
*V2Api* | [**create_web_target**](docs/V2Api.md#create_web_target) | **POST** /create-web-target | 
*V2Api* | [**decrypt**](docs/V2Api.md#decrypt) | **POST** /decrypt | 
*V2Api* | [**decrypt_pkcs1**](docs/V2Api.md#decrypt_pkcs1) | **POST** /decrypt-pkcs1 | 
*V2Api* | [**decrypt_with_classic_key**](docs/V2Api.md#decrypt_with_classic_key) | **POST** /decrypt-with-classic-key | 
*V2Api* | [**delete_auth_method**](docs/V2Api.md#delete_auth_method) | **POST** /delete-auth-method | 
*V2Api* | [**delete_auth_methods**](docs/V2Api.md#delete_auth_methods) | **POST** /delete-auth-methods | 
*V2Api* | [**delete_item**](docs/V2Api.md#delete_item) | **POST** /delete-item | 
*V2Api* | [**delete_items**](docs/V2Api.md#delete_items) | **POST** /delete-items | 
*V2Api* | [**delete_role**](docs/V2Api.md#delete_role) | **POST** /delete-role | 
*V2Api* | [**delete_role_association**](docs/V2Api.md#delete_role_association) | **POST** /delete-assoc | 
*V2Api* | [**delete_role_rule**](docs/V2Api.md#delete_role_rule) | **POST** /delete-role-rule | 
*V2Api* | [**delete_roles**](docs/V2Api.md#delete_roles) | **POST** /delete-roles | 
*V2Api* | [**delete_target**](docs/V2Api.md#delete_target) | **POST** /delete-target | 
*V2Api* | [**delete_target_association**](docs/V2Api.md#delete_target_association) | **POST** /delete-assoc-target-item | 
*V2Api* | [**delete_targets**](docs/V2Api.md#delete_targets) | **POST** /delete-targets | 
*V2Api* | [**describe_item**](docs/V2Api.md#describe_item) | **POST** /describe-item | 
*V2Api* | [**describe_permissions**](docs/V2Api.md#describe_permissions) | **POST** /describe-permissions | 
*V2Api* | [**encrypt**](docs/V2Api.md#encrypt) | **POST** /encrypt | 
*V2Api* | [**encrypt_pkcs1**](docs/V2Api.md#encrypt_pkcs1) | **POST** /encrypt-pkcs1 | 
*V2Api* | [**encrypt_with_classic_key**](docs/V2Api.md#encrypt_with_classic_key) | **POST** /encrypt-with-classic-key | 
*V2Api* | [**gateway_create_producer_artifactory**](docs/V2Api.md#gateway_create_producer_artifactory) | **POST** /gateway-create-producer-artifactory | 
*V2Api* | [**gateway_create_producer_aws**](docs/V2Api.md#gateway_create_producer_aws) | **POST** /gateway-create-producer-aws | 
*V2Api* | [**gateway_create_producer_azure**](docs/V2Api.md#gateway_create_producer_azure) | **POST** /gateway-create-producer-azure | 
*V2Api* | [**gateway_create_producer_certificate_automation**](docs/V2Api.md#gateway_create_producer_certificate_automation) | **POST** /gateway-create-producer-certificate-automation | 
*V2Api* | [**gateway_create_producer_custom**](docs/V2Api.md#gateway_create_producer_custom) | **POST** /gateway-create-producer-custom | 
*V2Api* | [**gateway_create_producer_eks**](docs/V2Api.md#gateway_create_producer_eks) | **POST** /gateway-create-producer-eks | 
*V2Api* | [**gateway_create_producer_gcp**](docs/V2Api.md#gateway_create_producer_gcp) | **POST** /gateway-create-producer-gcp | 
*V2Api* | [**gateway_create_producer_gke**](docs/V2Api.md#gateway_create_producer_gke) | **POST** /gateway-create-producer-gke | 
*V2Api* | [**gateway_create_producer_mongo**](docs/V2Api.md#gateway_create_producer_mongo) | **POST** /gateway-create-producer-mongo | 
*V2Api* | [**gateway_create_producer_mssql**](docs/V2Api.md#gateway_create_producer_mssql) | **POST** /gateway-create-producer-mssql | 
*V2Api* | [**gateway_create_producer_my_sql**](docs/V2Api.md#gateway_create_producer_my_sql) | **POST** /gateway-create-producer-mysql | 
*V2Api* | [**gateway_create_producer_native_k8_s**](docs/V2Api.md#gateway_create_producer_native_k8_s) | **POST** /gateway-create-producer-k8s-native | 
*V2Api* | [**gateway_create_producer_postgre_sql**](docs/V2Api.md#gateway_create_producer_postgre_sql) | **POST** /gateway-create-producer-postgresql | 
*V2Api* | [**gateway_create_producer_rabbit_mq**](docs/V2Api.md#gateway_create_producer_rabbit_mq) | **POST** /gateway-create-producer-rabbitmq | 
*V2Api* | [**gateway_create_producer_rdp**](docs/V2Api.md#gateway_create_producer_rdp) | **POST** /gateway-create-producer-rdp | 
*V2Api* | [**gateway_create_producer_snowflake**](docs/V2Api.md#gateway_create_producer_snowflake) | **POST** /gateway-create-producer-snowflake | 
*V2Api* | [**gateway_delete_allowed_management_access**](docs/V2Api.md#gateway_delete_allowed_management_access) | **POST** /gateway-delete-allowed-management-access | 
*V2Api* | [**gateway_delete_producer**](docs/V2Api.md#gateway_delete_producer) | **POST** /gateway-delete-producer | 
*V2Api* | [**gateway_get_config**](docs/V2Api.md#gateway_get_config) | **POST** /gateway-get-config | 
*V2Api* | [**gateway_get_producer**](docs/V2Api.md#gateway_get_producer) | **POST** /gateway-get-producer | 
*V2Api* | [**gateway_get_tmp_users**](docs/V2Api.md#gateway_get_tmp_users) | **POST** /gateway-get-producer-tmp-creds | 
*V2Api* | [**gateway_list_allowed_management_access**](docs/V2Api.md#gateway_list_allowed_management_access) | **POST** /gateway-list-allowed-management-access | 
*V2Api* | [**gateway_list_producers**](docs/V2Api.md#gateway_list_producers) | **POST** /gateway-list-producers | 
*V2Api* | [**gateway_revoke_tmp_users**](docs/V2Api.md#gateway_revoke_tmp_users) | **POST** /gateway-revoke-producer-tmp-creds | 
*V2Api* | [**gateway_start_producer**](docs/V2Api.md#gateway_start_producer) | **POST** /gateway-start-producer | 
*V2Api* | [**gateway_stop_producer**](docs/V2Api.md#gateway_stop_producer) | **POST** /gateway-stop-producer | 
*V2Api* | [**gateway_update_tmp_users**](docs/V2Api.md#gateway_update_tmp_users) | **POST** /gateway-update-producer-tmp-creds | 
*V2Api* | [**get_account_logo**](docs/V2Api.md#get_account_logo) | **POST** /get-account-logo | 
*V2Api* | [**get_auth_method**](docs/V2Api.md#get_auth_method) | **POST** /get-auth-method | 
*V2Api* | [**get_dynamic_secret_value**](docs/V2Api.md#get_dynamic_secret_value) | **POST** /get-dynamic-secret-value | 
*V2Api* | [**get_kube_exec_creds**](docs/V2Api.md#get_kube_exec_creds) | **POST** /get-kube-exec-creds | 
*V2Api* | [**get_pki_certificate**](docs/V2Api.md#get_pki_certificate) | **POST** /get-pki-certificate | 
*V2Api* | [**get_role**](docs/V2Api.md#get_role) | **POST** /get-role | 
*V2Api* | [**get_rotated_secret_value**](docs/V2Api.md#get_rotated_secret_value) | **POST** /get-rotated-secret-value | 
*V2Api* | [**get_rsa_public**](docs/V2Api.md#get_rsa_public) | **POST** /get-rsa-public | 
*V2Api* | [**get_secret_value**](docs/V2Api.md#get_secret_value) | **POST** /get-secret-value | 
*V2Api* | [**get_ssh_certificate**](docs/V2Api.md#get_ssh_certificate) | **POST** /get-ssh-certificate | 
*V2Api* | [**get_target**](docs/V2Api.md#get_target) | **POST** /get-target | 
*V2Api* | [**get_target_details**](docs/V2Api.md#get_target_details) | **POST** /get-target-details | 
*V2Api* | [**list_auth_methods**](docs/V2Api.md#list_auth_methods) | **POST** /list-auth-methods | 
*V2Api* | [**list_items**](docs/V2Api.md#list_items) | **POST** /list-items | 
*V2Api* | [**list_roles**](docs/V2Api.md#list_roles) | **POST** /list-roles | 
*V2Api* | [**list_targets**](docs/V2Api.md#list_targets) | **POST** /list-targets | 
*V2Api* | [**move_objects**](docs/V2Api.md#move_objects) | **POST** /move-objects | 
*V2Api* | [**raw_creds**](docs/V2Api.md#raw_creds) | **POST** /raw-creds | 
*V2Api* | [**refresh_key**](docs/V2Api.md#refresh_key) | **POST** /refresh-key | 
*V2Api* | [**reverse_rbac**](docs/V2Api.md#reverse_rbac) | **POST** /reverse-rbac | 
*V2Api* | [**rollback_secret**](docs/V2Api.md#rollback_secret) | **POST** /rollback-secret | 
*V2Api* | [**rotate_key**](docs/V2Api.md#rotate_key) | **POST** /rotate-key | 
*V2Api* | [**set_item_state**](docs/V2Api.md#set_item_state) | **POST** /set-item-state | 
*V2Api* | [**set_role_rule**](docs/V2Api.md#set_role_rule) | **POST** /set-role-rule | 
*V2Api* | [**sign_jwt_with_classic_key**](docs/V2Api.md#sign_jwt_with_classic_key) | **POST** /sign-jwt-with-classic-key | 
*V2Api* | [**sign_pkcs1**](docs/V2Api.md#sign_pkcs1) | **POST** /sign-pkcs1 | 
*V2Api* | [**sign_pki_cert_with_classic_key**](docs/V2Api.md#sign_pki_cert_with_classic_key) | **POST** /sign-pki-cert-with-classic-key | 
*V2Api* | [**static_creds_auth**](docs/V2Api.md#static_creds_auth) | **POST** /static-creds-auth | 
*V2Api* | [**uid_create_child_token**](docs/V2Api.md#uid_create_child_token) | **POST** /uid-create-child-token | 
*V2Api* | [**uid_generate_token**](docs/V2Api.md#uid_generate_token) | **POST** /uid-generate-token | 
*V2Api* | [**uid_list_children**](docs/V2Api.md#uid_list_children) | **POST** /uid-list-children | 
*V2Api* | [**uid_revoke_token**](docs/V2Api.md#uid_revoke_token) | **POST** /uid-revoke-token | 
*V2Api* | [**uid_rotate_token**](docs/V2Api.md#uid_rotate_token) | **POST** /uid-rotate-token | 
*V2Api* | [**update_assoc**](docs/V2Api.md#update_assoc) | **POST** /update-assoc | 
*V2Api* | [**update_aws_target**](docs/V2Api.md#update_aws_target) | **PUT** /update-aws-target | 
*V2Api* | [**update_aws_target_details**](docs/V2Api.md#update_aws_target_details) | **POST** /update-aws-target-details | 
*V2Api* | [**update_azure_target**](docs/V2Api.md#update_azure_target) | **PUT** /update-azure-target | 
*V2Api* | [**update_db_target**](docs/V2Api.md#update_db_target) | **POST** /update-db-target | 
*V2Api* | [**update_db_target_details**](docs/V2Api.md#update_db_target_details) | **POST** /update-db-target-details | 
*V2Api* | [**update_eks_target**](docs/V2Api.md#update_eks_target) | **PUT** /update-eks-target | 
*V2Api* | [**update_gcp_target**](docs/V2Api.md#update_gcp_target) | **PUT** /update-gcp-target | 
*V2Api* | [**update_gke_target**](docs/V2Api.md#update_gke_target) | **PUT** /update-gke-target | 
*V2Api* | [**update_item**](docs/V2Api.md#update_item) | **POST** /update-item | 
*V2Api* | [**update_native_k8_s_target**](docs/V2Api.md#update_native_k8_s_target) | **PUT** /update-k8s-target | 
*V2Api* | [**update_rabbit_mq_target**](docs/V2Api.md#update_rabbit_mq_target) | **PUT** /update-rabbitmq-target | 
*V2Api* | [**update_rabbit_mq_target_details**](docs/V2Api.md#update_rabbit_mq_target_details) | **POST** /update-rabbitmq-target-details | 
*V2Api* | [**update_rdp_target_details**](docs/V2Api.md#update_rdp_target_details) | **POST** /update-rdp-target-details | 
*V2Api* | [**update_role**](docs/V2Api.md#update_role) | **POST** /update-role | 
*V2Api* | [**update_rotated_secret**](docs/V2Api.md#update_rotated_secret) | **POST** /update-rotated-secret | 
*V2Api* | [**update_rotation_settings**](docs/V2Api.md#update_rotation_settings) | **POST** /update-rotation-settingsrotate-key | 
*V2Api* | [**update_secret_val**](docs/V2Api.md#update_secret_val) | **POST** /update-secret-val | 
*V2Api* | [**update_ssh_target**](docs/V2Api.md#update_ssh_target) | **POST** /update-ssh-target | 
*V2Api* | [**update_ssh_target_details**](docs/V2Api.md#update_ssh_target_details) | **POST** /update-ssh-target-details | 
*V2Api* | [**update_target**](docs/V2Api.md#update_target) | **POST** /update-target | 
*V2Api* | [**update_target_details**](docs/V2Api.md#update_target_details) | **POST** /update-target-details | 
*V2Api* | [**update_web_target**](docs/V2Api.md#update_web_target) | **POST** /update-web-target | 
*V2Api* | [**update_web_target_details**](docs/V2Api.md#update_web_target_details) | **POST** /update-web-target-details | 
*V2Api* | [**upload_rsa**](docs/V2Api.md#upload_rsa) | **POST** /upload-rsa | 
*V2Api* | [**verify_jwt_with_classic_key**](docs/V2Api.md#verify_jwt_with_classic_key) | **POST** /verify-jwt-with-classic-key | 
*V2Api* | [**verify_pkcs1**](docs/V2Api.md#verify_pkcs1) | **POST** /verify-pkcs1 | 
*V2Api* | [**verify_pki_cert_with_classic_key**](docs/V2Api.md#verify_pki_cert_with_classic_key) | **POST** /verify-pki-cert-with-classic-key | 


## Documentation For Models

 - [APIKeyAccessRules](docs/APIKeyAccessRules.md)
 - [AWSIAMAccessRules](docs/AWSIAMAccessRules.md)
 - [AWSPayload](docs/AWSPayload.md)
 - [AWSSecretsMigration](docs/AWSSecretsMigration.md)
 - [AdminsConfigPart](docs/AdminsConfigPart.md)
 - [AkeylessGatewayConfig](docs/AkeylessGatewayConfig.md)
 - [AllowedAccess](docs/AllowedAccess.md)
 - [AssocRoleAuthMethod](docs/AssocRoleAuthMethod.md)
 - [AssocTargetItem](docs/AssocTargetItem.md)
 - [Auth](docs/Auth.md)
 - [AuthMethod](docs/AuthMethod.md)
 - [AuthMethodAccessInfo](docs/AuthMethodAccessInfo.md)
 - [AuthMethodRoleAssociation](docs/AuthMethodRoleAssociation.md)
 - [AuthOutput](docs/AuthOutput.md)
 - [AwsS3LogForwardingConfig](docs/AwsS3LogForwardingConfig.md)
 - [AzureADAccessRules](docs/AzureADAccessRules.md)
 - [AzureKeyVaultMigration](docs/AzureKeyVaultMigration.md)
 - [AzureLogAnalyticsForwardingConfig](docs/AzureLogAnalyticsForwardingConfig.md)
 - [AzurePayload](docs/AzurePayload.md)
 - [CFConfigPart](docs/CFConfigPart.md)
 - [CacheConfigPart](docs/CacheConfigPart.md)
 - [CertificateIssueInfo](docs/CertificateIssueInfo.md)
 - [ClassicKeyDetailsInfo](docs/ClassicKeyDetailsInfo.md)
 - [ClassicKeyStatusInfo](docs/ClassicKeyStatusInfo.md)
 - [ClassicKeyTargetInfo](docs/ClassicKeyTargetInfo.md)
 - [ClientData](docs/ClientData.md)
 - [Configure](docs/Configure.md)
 - [ConfigureOutput](docs/ConfigureOutput.md)
 - [CreateAWSTarget](docs/CreateAWSTarget.md)
 - [CreateAWSTargetOutput](docs/CreateAWSTargetOutput.md)
 - [CreateArtifactoryTarget](docs/CreateArtifactoryTarget.md)
 - [CreateArtifactoryTargetOutput](docs/CreateArtifactoryTargetOutput.md)
 - [CreateAuthMethod](docs/CreateAuthMethod.md)
 - [CreateAuthMethodAWSIAM](docs/CreateAuthMethodAWSIAM.md)
 - [CreateAuthMethodAWSIAMOutput](docs/CreateAuthMethodAWSIAMOutput.md)
 - [CreateAuthMethodAzureAD](docs/CreateAuthMethodAzureAD.md)
 - [CreateAuthMethodAzureADOutput](docs/CreateAuthMethodAzureADOutput.md)
 - [CreateAuthMethodGCP](docs/CreateAuthMethodGCP.md)
 - [CreateAuthMethodGCPOutput](docs/CreateAuthMethodGCPOutput.md)
 - [CreateAuthMethodHuawei](docs/CreateAuthMethodHuawei.md)
 - [CreateAuthMethodHuaweiOutput](docs/CreateAuthMethodHuaweiOutput.md)
 - [CreateAuthMethodLDAP](docs/CreateAuthMethodLDAP.md)
 - [CreateAuthMethodLDAPOutput](docs/CreateAuthMethodLDAPOutput.md)
 - [CreateAuthMethodOAuth2](docs/CreateAuthMethodOAuth2.md)
 - [CreateAuthMethodOAuth2Output](docs/CreateAuthMethodOAuth2Output.md)
 - [CreateAuthMethodOutput](docs/CreateAuthMethodOutput.md)
 - [CreateAuthMethodSAML](docs/CreateAuthMethodSAML.md)
 - [CreateAuthMethodSAMLOutput](docs/CreateAuthMethodSAMLOutput.md)
 - [CreateAuthMethodUniversalIdentity](docs/CreateAuthMethodUniversalIdentity.md)
 - [CreateAuthMethodUniversalIdentityOutput](docs/CreateAuthMethodUniversalIdentityOutput.md)
 - [CreateAzureTarget](docs/CreateAzureTarget.md)
 - [CreateAzureTargetOutput](docs/CreateAzureTargetOutput.md)
 - [CreateClassicKey](docs/CreateClassicKey.md)
 - [CreateClassicKeyOutput](docs/CreateClassicKeyOutput.md)
 - [CreateDBTarget](docs/CreateDBTarget.md)
 - [CreateDBTargetOutput](docs/CreateDBTargetOutput.md)
 - [CreateDFCKey](docs/CreateDFCKey.md)
 - [CreateDFCKeyOutput](docs/CreateDFCKeyOutput.md)
 - [CreateDynamicSecret](docs/CreateDynamicSecret.md)
 - [CreateEKSTarget](docs/CreateEKSTarget.md)
 - [CreateEKSTargetOutput](docs/CreateEKSTargetOutput.md)
 - [CreateGKETarget](docs/CreateGKETarget.md)
 - [CreateGKETargetOutput](docs/CreateGKETargetOutput.md)
 - [CreateGcpTarget](docs/CreateGcpTarget.md)
 - [CreateGcpTargetOutput](docs/CreateGcpTargetOutput.md)
 - [CreateKey](docs/CreateKey.md)
 - [CreateKeyOutput](docs/CreateKeyOutput.md)
 - [CreateNativeK8STarget](docs/CreateNativeK8STarget.md)
 - [CreateNativeK8STargetOutput](docs/CreateNativeK8STargetOutput.md)
 - [CreatePKICertIssuer](docs/CreatePKICertIssuer.md)
 - [CreatePKICertIssuerOutput](docs/CreatePKICertIssuerOutput.md)
 - [CreateRabbitMQTarget](docs/CreateRabbitMQTarget.md)
 - [CreateRabbitMQTargetOutput](docs/CreateRabbitMQTargetOutput.md)
 - [CreateRole](docs/CreateRole.md)
 - [CreateRoleAuthMethodAssocOutput](docs/CreateRoleAuthMethodAssocOutput.md)
 - [CreateRotatedSecret](docs/CreateRotatedSecret.md)
 - [CreateRotatedSecretOutput](docs/CreateRotatedSecretOutput.md)
 - [CreateSSHCertIssuer](docs/CreateSSHCertIssuer.md)
 - [CreateSSHCertIssuerOutput](docs/CreateSSHCertIssuerOutput.md)
 - [CreateSSHTarget](docs/CreateSSHTarget.md)
 - [CreateSSHTargetOutput](docs/CreateSSHTargetOutput.md)
 - [CreateSecret](docs/CreateSecret.md)
 - [CreateSecretOutput](docs/CreateSecretOutput.md)
 - [CreateTargetItemAssocOutput](docs/CreateTargetItemAssocOutput.md)
 - [CreateWebTarget](docs/CreateWebTarget.md)
 - [CreateWebTargetOutput](docs/CreateWebTargetOutput.md)
 - [CustomerFragment](docs/CustomerFragment.md)
 - [CustomerFragmentsJson](docs/CustomerFragmentsJson.md)
 - [DSProducerDetails](docs/DSProducerDetails.md)
 - [Decrypt](docs/Decrypt.md)
 - [DecryptFile](docs/DecryptFile.md)
 - [DecryptFileOutput](docs/DecryptFileOutput.md)
 - [DecryptOutput](docs/DecryptOutput.md)
 - [DecryptPKCS1](docs/DecryptPKCS1.md)
 - [DecryptPKCS1Output](docs/DecryptPKCS1Output.md)
 - [DecryptWithClassicKey](docs/DecryptWithClassicKey.md)
 - [DecryptWithClassicKeyOutput](docs/DecryptWithClassicKeyOutput.md)
 - [DefaultConfigPart](docs/DefaultConfigPart.md)
 - [DeleteAuthMethod](docs/DeleteAuthMethod.md)
 - [DeleteAuthMethodOutput](docs/DeleteAuthMethodOutput.md)
 - [DeleteAuthMethods](docs/DeleteAuthMethods.md)
 - [DeleteAuthMethodsOutput](docs/DeleteAuthMethodsOutput.md)
 - [DeleteItem](docs/DeleteItem.md)
 - [DeleteItemOutput](docs/DeleteItemOutput.md)
 - [DeleteItems](docs/DeleteItems.md)
 - [DeleteItemsOutput](docs/DeleteItemsOutput.md)
 - [DeleteRole](docs/DeleteRole.md)
 - [DeleteRoleAssociation](docs/DeleteRoleAssociation.md)
 - [DeleteRoleRule](docs/DeleteRoleRule.md)
 - [DeleteRoleRuleOutput](docs/DeleteRoleRuleOutput.md)
 - [DeleteRoles](docs/DeleteRoles.md)
 - [DeleteTarget](docs/DeleteTarget.md)
 - [DeleteTargetAssociation](docs/DeleteTargetAssociation.md)
 - [DeleteTargets](docs/DeleteTargets.md)
 - [DescribeItem](docs/DescribeItem.md)
 - [DescribePermissions](docs/DescribePermissions.md)
 - [DescribePermissionsOutput](docs/DescribePermissionsOutput.md)
 - [DynamicSecretProducerInfo](docs/DynamicSecretProducerInfo.md)
 - [ElasticsearchLogForwardingConfig](docs/ElasticsearchLogForwardingConfig.md)
 - [EmailPassAccessRules](docs/EmailPassAccessRules.md)
 - [Encrypt](docs/Encrypt.md)
 - [EncryptFile](docs/EncryptFile.md)
 - [EncryptFileOutput](docs/EncryptFileOutput.md)
 - [EncryptOutput](docs/EncryptOutput.md)
 - [EncryptPKCS1](docs/EncryptPKCS1.md)
 - [EncryptPKCS1Output](docs/EncryptPKCS1Output.md)
 - [EncryptWithClassicKey](docs/EncryptWithClassicKey.md)
 - [EncryptWithClassicKeyOutput](docs/EncryptWithClassicKeyOutput.md)
 - [ExternalKMSKeyId](docs/ExternalKMSKeyId.md)
 - [GCPAccessRules](docs/GCPAccessRules.md)
 - [GatewayAddAllowedManagementAccess](docs/GatewayAddAllowedManagementAccess.md)
 - [GatewayCreateProducerArtifactory](docs/GatewayCreateProducerArtifactory.md)
 - [GatewayCreateProducerArtifactoryOutput](docs/GatewayCreateProducerArtifactoryOutput.md)
 - [GatewayCreateProducerAws](docs/GatewayCreateProducerAws.md)
 - [GatewayCreateProducerAwsOutput](docs/GatewayCreateProducerAwsOutput.md)
 - [GatewayCreateProducerAzure](docs/GatewayCreateProducerAzure.md)
 - [GatewayCreateProducerAzureOutput](docs/GatewayCreateProducerAzureOutput.md)
 - [GatewayCreateProducerCertificateAutomation](docs/GatewayCreateProducerCertificateAutomation.md)
 - [GatewayCreateProducerCertificateAutomationOutput](docs/GatewayCreateProducerCertificateAutomationOutput.md)
 - [GatewayCreateProducerChef](docs/GatewayCreateProducerChef.md)
 - [GatewayCreateProducerChefOutput](docs/GatewayCreateProducerChefOutput.md)
 - [GatewayCreateProducerCustom](docs/GatewayCreateProducerCustom.md)
 - [GatewayCreateProducerCustomOutput](docs/GatewayCreateProducerCustomOutput.md)
 - [GatewayCreateProducerEks](docs/GatewayCreateProducerEks.md)
 - [GatewayCreateProducerEksOutput](docs/GatewayCreateProducerEksOutput.md)
 - [GatewayCreateProducerGcp](docs/GatewayCreateProducerGcp.md)
 - [GatewayCreateProducerGcpOutput](docs/GatewayCreateProducerGcpOutput.md)
 - [GatewayCreateProducerGke](docs/GatewayCreateProducerGke.md)
 - [GatewayCreateProducerGkeOutput](docs/GatewayCreateProducerGkeOutput.md)
 - [GatewayCreateProducerMSSQL](docs/GatewayCreateProducerMSSQL.md)
 - [GatewayCreateProducerMSSQLOutput](docs/GatewayCreateProducerMSSQLOutput.md)
 - [GatewayCreateProducerMongo](docs/GatewayCreateProducerMongo.md)
 - [GatewayCreateProducerMongoOutput](docs/GatewayCreateProducerMongoOutput.md)
 - [GatewayCreateProducerMySQL](docs/GatewayCreateProducerMySQL.md)
 - [GatewayCreateProducerMySQLOutput](docs/GatewayCreateProducerMySQLOutput.md)
 - [GatewayCreateProducerNativeK8S](docs/GatewayCreateProducerNativeK8S.md)
 - [GatewayCreateProducerNativeK8SOutput](docs/GatewayCreateProducerNativeK8SOutput.md)
 - [GatewayCreateProducerPostgreSQL](docs/GatewayCreateProducerPostgreSQL.md)
 - [GatewayCreateProducerPostgreSQLOutput](docs/GatewayCreateProducerPostgreSQLOutput.md)
 - [GatewayCreateProducerRabbitMQ](docs/GatewayCreateProducerRabbitMQ.md)
 - [GatewayCreateProducerRabbitMQOutput](docs/GatewayCreateProducerRabbitMQOutput.md)
 - [GatewayCreateProducerRdp](docs/GatewayCreateProducerRdp.md)
 - [GatewayCreateProducerRdpOutput](docs/GatewayCreateProducerRdpOutput.md)
 - [GatewayCreateProducerSnowflake](docs/GatewayCreateProducerSnowflake.md)
 - [GatewayCreateProducerSnowflakeOutput](docs/GatewayCreateProducerSnowflakeOutput.md)
 - [GatewayDeleteAllowedManagementAccess](docs/GatewayDeleteAllowedManagementAccess.md)
 - [GatewayDeleteProducer](docs/GatewayDeleteProducer.md)
 - [GatewayDeleteProducerOutput](docs/GatewayDeleteProducerOutput.md)
 - [GatewayGetConfig](docs/GatewayGetConfig.md)
 - [GatewayGetProducer](docs/GatewayGetProducer.md)
 - [GatewayGetTmpUsers](docs/GatewayGetTmpUsers.md)
 - [GatewayListAllowedManagementAccess](docs/GatewayListAllowedManagementAccess.md)
 - [GatewayListProducers](docs/GatewayListProducers.md)
 - [GatewayRevokeTmpUsers](docs/GatewayRevokeTmpUsers.md)
 - [GatewayStartProducer](docs/GatewayStartProducer.md)
 - [GatewayStartProducerOutput](docs/GatewayStartProducerOutput.md)
 - [GatewayStopProducer](docs/GatewayStopProducer.md)
 - [GatewayStopProducerOutput](docs/GatewayStopProducerOutput.md)
 - [GatewayUpdateItemOutput](docs/GatewayUpdateItemOutput.md)
 - [GatewayUpdateTmpUsers](docs/GatewayUpdateTmpUsers.md)
 - [GenCustomerFragment](docs/GenCustomerFragment.md)
 - [GeneralConfigPart](docs/GeneralConfigPart.md)
 - [GetAuthMethod](docs/GetAuthMethod.md)
 - [GetCloudIdentity](docs/GetCloudIdentity.md)
 - [GetCloudIdentityOutput](docs/GetCloudIdentityOutput.md)
 - [GetDynamicSecretValue](docs/GetDynamicSecretValue.md)
 - [GetKubeExecCreds](docs/GetKubeExecCreds.md)
 - [GetKubeExecCredsOutput](docs/GetKubeExecCredsOutput.md)
 - [GetPKICertificate](docs/GetPKICertificate.md)
 - [GetPKICertificateOutput](docs/GetPKICertificateOutput.md)
 - [GetProducersListReplyObj](docs/GetProducersListReplyObj.md)
 - [GetRSAPublic](docs/GetRSAPublic.md)
 - [GetRSAPublicOutput](docs/GetRSAPublicOutput.md)
 - [GetRole](docs/GetRole.md)
 - [GetRotatedSecretValue](docs/GetRotatedSecretValue.md)
 - [GetSSHCertificate](docs/GetSSHCertificate.md)
 - [GetSSHCertificateOutput](docs/GetSSHCertificateOutput.md)
 - [GetSecretValue](docs/GetSecretValue.md)
 - [GetSubAdminsListReplyObj](docs/GetSubAdminsListReplyObj.md)
 - [GetTarget](docs/GetTarget.md)
 - [GetTargetDetails](docs/GetTargetDetails.md)
 - [GetTargetDetailsOutput](docs/GetTargetDetailsOutput.md)
 - [HashiMigration](docs/HashiMigration.md)
 - [HashiPayload](docs/HashiPayload.md)
 - [HuaweiAccessRules](docs/HuaweiAccessRules.md)
 - [Item](docs/Item.md)
 - [ItemGeneralInfo](docs/ItemGeneralInfo.md)
 - [ItemTargetAssociation](docs/ItemTargetAssociation.md)
 - [ItemVersion](docs/ItemVersion.md)
 - [JSONError](docs/JSONError.md)
 - [K8SMigration](docs/K8SMigration.md)
 - [K8SPayload](docs/K8SPayload.md)
 - [KMIPClient](docs/KMIPClient.md)
 - [KMIPClientsConfigPart](docs/KMIPClientsConfigPart.md)
 - [LDAPAccessRules](docs/LDAPAccessRules.md)
 - [LdapConfigPart](docs/LdapConfigPart.md)
 - [LeadershipConfigPart](docs/LeadershipConfigPart.md)
 - [ListAuthMethods](docs/ListAuthMethods.md)
 - [ListAuthMethodsOutput](docs/ListAuthMethodsOutput.md)
 - [ListItems](docs/ListItems.md)
 - [ListItemsInPathOutput](docs/ListItemsInPathOutput.md)
 - [ListRoles](docs/ListRoles.md)
 - [ListRolesOutput](docs/ListRolesOutput.md)
 - [ListTargets](docs/ListTargets.md)
 - [ListTargetsOutput](docs/ListTargetsOutput.md)
 - [LogForwardingConfigPart](docs/LogForwardingConfigPart.md)
 - [LogstashLogForwardingConfig](docs/LogstashLogForwardingConfig.md)
 - [LogzIoLogForwardingConfig](docs/LogzIoLogForwardingConfig.md)
 - [MigrationGeneral](docs/MigrationGeneral.md)
 - [MigrationsConfigPart](docs/MigrationsConfigPart.md)
 - [MoveObjects](docs/MoveObjects.md)
 - [OAuth2AccessRules](docs/OAuth2AccessRules.md)
 - [OAuth2CustomClaim](docs/OAuth2CustomClaim.md)
 - [PKICertificateIssueDetails](docs/PKICertificateIssueDetails.md)
 - [PathRule](docs/PathRule.md)
 - [Producer](docs/Producer.md)
 - [ProducersConfigPart](docs/ProducersConfigPart.md)
 - [RawCreds](docs/RawCreds.md)
 - [RefreshKey](docs/RefreshKey.md)
 - [RefreshKeyOutput](docs/RefreshKeyOutput.md)
 - [ReverseRBAC](docs/ReverseRBAC.md)
 - [ReverseRBACClient](docs/ReverseRBACClient.md)
 - [ReverseRBACOutput](docs/ReverseRBACOutput.md)
 - [Role](docs/Role.md)
 - [RoleAuthMethodAssociation](docs/RoleAuthMethodAssociation.md)
 - [RollbackSecret](docs/RollbackSecret.md)
 - [RollbackSecretOutput](docs/RollbackSecretOutput.md)
 - [RotateKey](docs/RotateKey.md)
 - [RotateKeyOutput](docs/RotateKeyOutput.md)
 - [RotatedSecretDetailsInfo](docs/RotatedSecretDetailsInfo.md)
 - [Rotator](docs/Rotator.md)
 - [RotatorsConfigPart](docs/RotatorsConfigPart.md)
 - [Rules](docs/Rules.md)
 - [SAMLAccessRules](docs/SAMLAccessRules.md)
 - [SAMLAttribute](docs/SAMLAttribute.md)
 - [SSHCertificateIssueDetails](docs/SSHCertificateIssueDetails.md)
 - [SetItemState](docs/SetItemState.md)
 - [SetRoleRule](docs/SetRoleRule.md)
 - [SignJWTOutput](docs/SignJWTOutput.md)
 - [SignJWTWithClassicKey](docs/SignJWTWithClassicKey.md)
 - [SignPKCS1](docs/SignPKCS1.md)
 - [SignPKCS1Output](docs/SignPKCS1Output.md)
 - [SignPKICertOutput](docs/SignPKICertOutput.md)
 - [SignPKICertWithClassicKey](docs/SignPKICertWithClassicKey.md)
 - [SplunkLogForwardingConfig](docs/SplunkLogForwardingConfig.md)
 - [StaticCredsAuth](docs/StaticCredsAuth.md)
 - [StaticCredsAuthOutput](docs/StaticCredsAuthOutput.md)
 - [SyslogLogForwardingConfig](docs/SyslogLogForwardingConfig.md)
 - [SystemAccessCredentialsReplyObj](docs/SystemAccessCredentialsReplyObj.md)
 - [Target](docs/Target.md)
 - [TargetItemAssociation](docs/TargetItemAssociation.md)
 - [TargetTypeDetailsInput](docs/TargetTypeDetailsInput.md)
 - [TmpUserData](docs/TmpUserData.md)
 - [UIDTokenDetails](docs/UIDTokenDetails.md)
 - [UIdentityConfigPart](docs/UIdentityConfigPart.md)
 - [UidCreateChildToken](docs/UidCreateChildToken.md)
 - [UidCreateChildTokenOutput](docs/UidCreateChildTokenOutput.md)
 - [UidGenerateToken](docs/UidGenerateToken.md)
 - [UidGenerateTokenOutput](docs/UidGenerateTokenOutput.md)
 - [UidListChildren](docs/UidListChildren.md)
 - [UidRevokeToken](docs/UidRevokeToken.md)
 - [UidRotateToken](docs/UidRotateToken.md)
 - [UidRotateTokenOutput](docs/UidRotateTokenOutput.md)
 - [Unconfigure](docs/Unconfigure.md)
 - [UniversalIdentityAccessRules](docs/UniversalIdentityAccessRules.md)
 - [UniversalIdentityDetails](docs/UniversalIdentityDetails.md)
 - [UpdateAWSTarget](docs/UpdateAWSTarget.md)
 - [UpdateAWSTargetDetails](docs/UpdateAWSTargetDetails.md)
 - [UpdateAssoc](docs/UpdateAssoc.md)
 - [UpdateAzureTarget](docs/UpdateAzureTarget.md)
 - [UpdateAzureTargetOutput](docs/UpdateAzureTargetOutput.md)
 - [UpdateDBTarget](docs/UpdateDBTarget.md)
 - [UpdateDBTargetDetails](docs/UpdateDBTargetDetails.md)
 - [UpdateDBTargetOutput](docs/UpdateDBTargetOutput.md)
 - [UpdateEKSTarget](docs/UpdateEKSTarget.md)
 - [UpdateEKSTargetOutput](docs/UpdateEKSTargetOutput.md)
 - [UpdateGKETarget](docs/UpdateGKETarget.md)
 - [UpdateGKETargetOutput](docs/UpdateGKETargetOutput.md)
 - [UpdateGcpTarget](docs/UpdateGcpTarget.md)
 - [UpdateGcpTargetOutput](docs/UpdateGcpTargetOutput.md)
 - [UpdateItem](docs/UpdateItem.md)
 - [UpdateItemOutput](docs/UpdateItemOutput.md)
 - [UpdateNativeK8STarget](docs/UpdateNativeK8STarget.md)
 - [UpdateNativeK8STargetOutput](docs/UpdateNativeK8STargetOutput.md)
 - [UpdateOutput](docs/UpdateOutput.md)
 - [UpdateRDPTargetDetails](docs/UpdateRDPTargetDetails.md)
 - [UpdateRabbitMQTarget](docs/UpdateRabbitMQTarget.md)
 - [UpdateRabbitMQTargetDetails](docs/UpdateRabbitMQTargetDetails.md)
 - [UpdateRabbitMQTargetOutput](docs/UpdateRabbitMQTargetOutput.md)
 - [UpdateRole](docs/UpdateRole.md)
 - [UpdateRoleOutput](docs/UpdateRoleOutput.md)
 - [UpdateRotatedSecret](docs/UpdateRotatedSecret.md)
 - [UpdateRotatedSecretOutput](docs/UpdateRotatedSecretOutput.md)
 - [UpdateRotationSettings](docs/UpdateRotationSettings.md)
 - [UpdateSSHTarget](docs/UpdateSSHTarget.md)
 - [UpdateSSHTargetDetails](docs/UpdateSSHTargetDetails.md)
 - [UpdateSSHTargetOutput](docs/UpdateSSHTargetOutput.md)
 - [UpdateSecretVal](docs/UpdateSecretVal.md)
 - [UpdateSecretValOutput](docs/UpdateSecretValOutput.md)
 - [UpdateTarget](docs/UpdateTarget.md)
 - [UpdateTargetDetailsOutput](docs/UpdateTargetDetailsOutput.md)
 - [UpdateTargetOutput](docs/UpdateTargetOutput.md)
 - [UpdateWebTarget](docs/UpdateWebTarget.md)
 - [UpdateWebTargetDetails](docs/UpdateWebTargetDetails.md)
 - [UpdateWebTargetOutput](docs/UpdateWebTargetOutput.md)
 - [UploadPKCS12](docs/UploadPKCS12.md)
 - [UploadRSA](docs/UploadRSA.md)
 - [VerifyJWTOutput](docs/VerifyJWTOutput.md)
 - [VerifyJWTWithClassicKey](docs/VerifyJWTWithClassicKey.md)
 - [VerifyPKCS1](docs/VerifyPKCS1.md)
 - [VerifyPKICertOutput](docs/VerifyPKICertOutput.md)
 - [VerifyPKICertWithClassicKey](docs/VerifyPKICertWithClassicKey.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author

support@akeyless.io


