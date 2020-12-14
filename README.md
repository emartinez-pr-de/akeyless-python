# akeyless
The purpose of this application is to provide access to Akeyless API.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.0
- Package version: 2.0.5
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
        host = "https://api.akeyless.io"
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
*V2Api* | [**create_auth_method**](docs/V2Api.md#create_auth_method) | **POST** /create-auth-method | 
*V2Api* | [**create_auth_method_awsiam**](docs/V2Api.md#create_auth_method_awsiam) | **POST** /create-auth-method-aws-iam | 
*V2Api* | [**create_auth_method_azure_ad**](docs/V2Api.md#create_auth_method_azure_ad) | **POST** /create-auth-method-azure-ad | 
*V2Api* | [**create_auth_method_huawei**](docs/V2Api.md#create_auth_method_huawei) | **POST** /create-auth-method-huawei | 
*V2Api* | [**create_auth_method_o_auth2**](docs/V2Api.md#create_auth_method_o_auth2) | **POST** /create-auth-method-oauth2 | 
*V2Api* | [**create_auth_method_saml**](docs/V2Api.md#create_auth_method_saml) | **POST** /create-auth-method-saml | 
*V2Api* | [**create_auth_method_universal_identity**](docs/V2Api.md#create_auth_method_universal_identity) | **POST** /create-auth-method-universal-identity | 
*V2Api* | [**create_aws_target**](docs/V2Api.md#create_aws_target) | **POST** /create-aws-target | 
*V2Api* | [**create_db_target**](docs/V2Api.md#create_db_target) | **POST** /create-db-target | 
*V2Api* | [**create_dynamic_secret**](docs/V2Api.md#create_dynamic_secret) | **POST** /create-dynamic-secret | 
*V2Api* | [**create_key**](docs/V2Api.md#create_key) | **POST** /create-key | 
*V2Api* | [**create_pki_cert_issuer**](docs/V2Api.md#create_pki_cert_issuer) | **POST** /create-pki-cert-issuer | 
*V2Api* | [**create_rabbit_mq_target**](docs/V2Api.md#create_rabbit_mq_target) | **POST** /create-rabbitMQ-target | 
*V2Api* | [**create_rdp_target**](docs/V2Api.md#create_rdp_target) | **POST** /create-rdp-target | 
*V2Api* | [**create_role**](docs/V2Api.md#create_role) | **POST** /create-role | 
*V2Api* | [**create_secret**](docs/V2Api.md#create_secret) | **POST** /create-secret | 
*V2Api* | [**create_ssh_cert_issuer**](docs/V2Api.md#create_ssh_cert_issuer) | **POST** /create-ssh-cert-issuer | 
*V2Api* | [**create_ssh_target**](docs/V2Api.md#create_ssh_target) | **POST** /create-ssh-target | 
*V2Api* | [**create_target**](docs/V2Api.md#create_target) | **POST** /create-target | 
*V2Api* | [**create_web_target**](docs/V2Api.md#create_web_target) | **POST** /create-web-target | 
*V2Api* | [**decrypt**](docs/V2Api.md#decrypt) | **POST** /decrypt | 
*V2Api* | [**decrypt_pkcs1**](docs/V2Api.md#decrypt_pkcs1) | **POST** /decrypt-pkcs1 | 
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
*V2Api* | [**encrypt**](docs/V2Api.md#encrypt) | **POST** /encrypt | 
*V2Api* | [**encrypt_pkcs1**](docs/V2Api.md#encrypt_pkcs1) | **POST** /encrypt-pkcs1 | 
*V2Api* | [**get_auth_method**](docs/V2Api.md#get_auth_method) | **POST** /get-auth-method | 
*V2Api* | [**get_dynamic_secret_value**](docs/V2Api.md#get_dynamic_secret_value) | **POST** /get-dynamic-secret-value | 
*V2Api* | [**get_role**](docs/V2Api.md#get_role) | **POST** /get-role | 
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
*V2Api* | [**sign_pkcs1**](docs/V2Api.md#sign_pkcs1) | **POST** /sign-pkcs1 | 
*V2Api* | [**static_creds_auth**](docs/V2Api.md#static_creds_auth) | **POST** /static-creds-auth | 
*V2Api* | [**uid_create_child_token**](docs/V2Api.md#uid_create_child_token) | **POST** /uid-create-child-token | 
*V2Api* | [**uid_generate_token**](docs/V2Api.md#uid_generate_token) | **POST** /uid-generate-token | 
*V2Api* | [**uid_list_children**](docs/V2Api.md#uid_list_children) | **POST** /uid-list-children | 
*V2Api* | [**uid_revoke_token**](docs/V2Api.md#uid_revoke_token) | **POST** /uid-revoke-token | 
*V2Api* | [**uid_rotate_token**](docs/V2Api.md#uid_rotate_token) | **POST** /uid-rotate-token | 
*V2Api* | [**update_aws_target_details**](docs/V2Api.md#update_aws_target_details) | **POST** /update-aws-target-details | 
*V2Api* | [**update_db_target_details**](docs/V2Api.md#update_db_target_details) | **POST** /update-db-target-details | 
*V2Api* | [**update_item**](docs/V2Api.md#update_item) | **POST** /update-item | 
*V2Api* | [**update_rabbit_mq_target_details**](docs/V2Api.md#update_rabbit_mq_target_details) | **POST** /update-rabbitmq-target-details | 
*V2Api* | [**update_rdp_target_details**](docs/V2Api.md#update_rdp_target_details) | **POST** /update-rdp-target-details | 
*V2Api* | [**update_role**](docs/V2Api.md#update_role) | **POST** /update-role | 
*V2Api* | [**update_secret_val**](docs/V2Api.md#update_secret_val) | **POST** /update-secret-val | 
*V2Api* | [**update_ssh_target_details**](docs/V2Api.md#update_ssh_target_details) | **POST** /update-ssh-target-details | 
*V2Api* | [**update_target**](docs/V2Api.md#update_target) | **POST** /update-target | 
*V2Api* | [**update_target_details**](docs/V2Api.md#update_target_details) | **POST** /update-target-details | 
*V2Api* | [**update_web_target_details**](docs/V2Api.md#update_web_target_details) | **POST** /update-web-target-details | 
*V2Api* | [**upload_rsa**](docs/V2Api.md#upload_rsa) | **POST** /upload-rsa | 
*V2Api* | [**verify_pkcs1**](docs/V2Api.md#verify_pkcs1) | **POST** /verify-pkcs1 | 


## Documentation For Models

 - [APIKeyAccessRules](docs/APIKeyAccessRules.md)
 - [AWSIAMAccessRules](docs/AWSIAMAccessRules.md)
 - [AssocRoleAuthMethod](docs/AssocRoleAuthMethod.md)
 - [AssocTargetItem](docs/AssocTargetItem.md)
 - [Auth](docs/Auth.md)
 - [AuthMethod](docs/AuthMethod.md)
 - [AuthMethodAccessInfo](docs/AuthMethodAccessInfo.md)
 - [AuthMethodRoleAssociation](docs/AuthMethodRoleAssociation.md)
 - [AuthOutput](docs/AuthOutput.md)
 - [AzureADAccessRules](docs/AzureADAccessRules.md)
 - [CertificateIssueInfo](docs/CertificateIssueInfo.md)
 - [ClientData](docs/ClientData.md)
 - [Configure](docs/Configure.md)
 - [ConfigureOutput](docs/ConfigureOutput.md)
 - [CreateAuthMethod](docs/CreateAuthMethod.md)
 - [CreateAuthMethodAWSIAM](docs/CreateAuthMethodAWSIAM.md)
 - [CreateAuthMethodAWSIAMOutput](docs/CreateAuthMethodAWSIAMOutput.md)
 - [CreateAuthMethodAzureAD](docs/CreateAuthMethodAzureAD.md)
 - [CreateAuthMethodAzureADOutput](docs/CreateAuthMethodAzureADOutput.md)
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
 - [CreateAwsTarget](docs/CreateAwsTarget.md)
 - [CreateDBTarget](docs/CreateDBTarget.md)
 - [CreateDynamicSecret](docs/CreateDynamicSecret.md)
 - [CreateKey](docs/CreateKey.md)
 - [CreateKeyOutput](docs/CreateKeyOutput.md)
 - [CreatePKICertIssuer](docs/CreatePKICertIssuer.md)
 - [CreatePKICertIssuerOutput](docs/CreatePKICertIssuerOutput.md)
 - [CreateRabbitMQTarget](docs/CreateRabbitMQTarget.md)
 - [CreateRdpTarget](docs/CreateRdpTarget.md)
 - [CreateRole](docs/CreateRole.md)
 - [CreateRoleAuthMethodAssocOutput](docs/CreateRoleAuthMethodAssocOutput.md)
 - [CreateSSHCertIssuer](docs/CreateSSHCertIssuer.md)
 - [CreateSSHCertIssuerOutput](docs/CreateSSHCertIssuerOutput.md)
 - [CreateSSHTarget](docs/CreateSSHTarget.md)
 - [CreateSecret](docs/CreateSecret.md)
 - [CreateSecretOutput](docs/CreateSecretOutput.md)
 - [CreateTargetItemAssocOutput](docs/CreateTargetItemAssocOutput.md)
 - [CreateWebTarget](docs/CreateWebTarget.md)
 - [CustomerFragment](docs/CustomerFragment.md)
 - [CustomerFragmentsJson](docs/CustomerFragmentsJson.md)
 - [Decrypt](docs/Decrypt.md)
 - [DecryptFile](docs/DecryptFile.md)
 - [DecryptFileOutput](docs/DecryptFileOutput.md)
 - [DecryptOutput](docs/DecryptOutput.md)
 - [DecryptPKCS1](docs/DecryptPKCS1.md)
 - [DecryptPKCS1Output](docs/DecryptPKCS1Output.md)
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
 - [DynamicSecretProducerInfo](docs/DynamicSecretProducerInfo.md)
 - [EmailPassAccessRules](docs/EmailPassAccessRules.md)
 - [Encrypt](docs/Encrypt.md)
 - [EncryptFile](docs/EncryptFile.md)
 - [EncryptFileOutput](docs/EncryptFileOutput.md)
 - [EncryptOutput](docs/EncryptOutput.md)
 - [EncryptPKCS1](docs/EncryptPKCS1.md)
 - [EncryptPKCS1Output](docs/EncryptPKCS1Output.md)
 - [GenCustomerFragment](docs/GenCustomerFragment.md)
 - [GetAuthMethod](docs/GetAuthMethod.md)
 - [GetCloudIdentity](docs/GetCloudIdentity.md)
 - [GetCloudIdentityOutput](docs/GetCloudIdentityOutput.md)
 - [GetDynamicSecretValue](docs/GetDynamicSecretValue.md)
 - [GetKubeExecCreds](docs/GetKubeExecCreds.md)
 - [GetKubeExecCredsOutput](docs/GetKubeExecCredsOutput.md)
 - [GetPKICertificate](docs/GetPKICertificate.md)
 - [GetPKICertificateOutput](docs/GetPKICertificateOutput.md)
 - [GetRSAPublic](docs/GetRSAPublic.md)
 - [GetRSAPublicOutput](docs/GetRSAPublicOutput.md)
 - [GetRole](docs/GetRole.md)
 - [GetSSHCertificate](docs/GetSSHCertificate.md)
 - [GetSSHCertificateOutput](docs/GetSSHCertificateOutput.md)
 - [GetSecretValue](docs/GetSecretValue.md)
 - [GetTarget](docs/GetTarget.md)
 - [GetTargetDetails](docs/GetTargetDetails.md)
 - [GetTargetDetailsOutput](docs/GetTargetDetailsOutput.md)
 - [HuaweiAccessRules](docs/HuaweiAccessRules.md)
 - [Item](docs/Item.md)
 - [ItemGeneralInfo](docs/ItemGeneralInfo.md)
 - [ItemTargetAssociation](docs/ItemTargetAssociation.md)
 - [ItemVersion](docs/ItemVersion.md)
 - [JSONError](docs/JSONError.md)
 - [LDAPAccessRules](docs/LDAPAccessRules.md)
 - [ListAuthMethods](docs/ListAuthMethods.md)
 - [ListAuthMethodsOutput](docs/ListAuthMethodsOutput.md)
 - [ListItems](docs/ListItems.md)
 - [ListItemsInPathOutput](docs/ListItemsInPathOutput.md)
 - [ListRoles](docs/ListRoles.md)
 - [ListRolesOutput](docs/ListRolesOutput.md)
 - [ListTargets](docs/ListTargets.md)
 - [ListTargetsOutput](docs/ListTargetsOutput.md)
 - [MoveObjects](docs/MoveObjects.md)
 - [OAuth2AccessRules](docs/OAuth2AccessRules.md)
 - [OAuth2CustomClaim](docs/OAuth2CustomClaim.md)
 - [PKICertificateIssueDetails](docs/PKICertificateIssueDetails.md)
 - [PathRule](docs/PathRule.md)
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
 - [Rules](docs/Rules.md)
 - [SAMLAccessRules](docs/SAMLAccessRules.md)
 - [SAMLAttribute](docs/SAMLAttribute.md)
 - [SSHCertificateIssueDetails](docs/SSHCertificateIssueDetails.md)
 - [SetItemState](docs/SetItemState.md)
 - [SetRoleRule](docs/SetRoleRule.md)
 - [SignPKCS1](docs/SignPKCS1.md)
 - [SignPKCS1Output](docs/SignPKCS1Output.md)
 - [StaticCredsAuth](docs/StaticCredsAuth.md)
 - [StaticCredsAuthOutput](docs/StaticCredsAuthOutput.md)
 - [SystemAccessCredentialsReplyObj](docs/SystemAccessCredentialsReplyObj.md)
 - [Target](docs/Target.md)
 - [TargetItemAssociation](docs/TargetItemAssociation.md)
 - [UIDTokenDetails](docs/UIDTokenDetails.md)
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
 - [Update](docs/Update.md)
 - [UpdateAWSTargetDetails](docs/UpdateAWSTargetDetails.md)
 - [UpdateDBTargetDetails](docs/UpdateDBTargetDetails.md)
 - [UpdateItem](docs/UpdateItem.md)
 - [UpdateItemOutput](docs/UpdateItemOutput.md)
 - [UpdateOutput](docs/UpdateOutput.md)
 - [UpdateRDPTargetDetails](docs/UpdateRDPTargetDetails.md)
 - [UpdateRabbitMQTargetDetails](docs/UpdateRabbitMQTargetDetails.md)
 - [UpdateRole](docs/UpdateRole.md)
 - [UpdateRoleOutput](docs/UpdateRoleOutput.md)
 - [UpdateSSHTargetDetails](docs/UpdateSSHTargetDetails.md)
 - [UpdateSecretVal](docs/UpdateSecretVal.md)
 - [UpdateSecretValOutput](docs/UpdateSecretValOutput.md)
 - [UpdateTarget](docs/UpdateTarget.md)
 - [UpdateTargetDetailsOutput](docs/UpdateTargetDetailsOutput.md)
 - [UpdateTargetOutput](docs/UpdateTargetOutput.md)
 - [UpdateWebTargetDetails](docs/UpdateWebTargetDetails.md)
 - [UploadPKCS12](docs/UploadPKCS12.md)
 - [UploadRSA](docs/UploadRSA.md)
 - [VerifyPKCS1](docs/VerifyPKCS1.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author

support@akeyless.io


