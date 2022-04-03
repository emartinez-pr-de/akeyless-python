# GatewayUpdateProducerCertificateAutomation

gatewayUpdateProducerCertificateAutomation is a command that updates a Certificate Automation dynamic secret producer to dynamically update certificates generated by Venafi or have Akeyless generated certificates using PKI be monitored by Venafi
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_rotation_interval_days** | **int** | Admin credentials rotation interval (days) | [optional] [default to 0]
**allow_subdomains** | **bool** | Allow subdomains | [optional] 
**allowed_domains** | **list[str]** | Allowed domains | [optional] 
**auto_generated_folder** | **str** | Auto generated folder | [optional] 
**enable_admin_rotation** | **bool** | Automatic admin credentials rotation | [optional] [default to False]
**name** | **str** | Producer name | 
**new_name** | **str** | Producer name | [optional] 
**producer_encryption_key_name** | **str** | Dynamic producer encryption key | [optional] 
**root_first_in_chain** | **bool** | Root first in chain | [optional] 
**sign_using_akeyless_pki** | **bool** | Use Akeyless PKI issuer or Venafi issuer | [optional] 
**signer_key_name** | **str** | Signer key name | [optional] 
**store_private_key** | **bool** | Store private key | [optional] 
**tags** | **list[str]** | List of the tags attached to this secret | [optional] 
**target_name** | **str** | Target name | [optional] 
**token** | **str** | Authentication token (see &#x60;/auth&#x60; and &#x60;/configure&#x60;) | [optional] 
**uid_token** | **str** | The universal identity token, Required only for universal_identity authentication | [optional] 
**user_ttl** | **str** | User TTL in time.Duration format (2160h / 129600m / etc...). When using sign-using-akeyless-pki certificates created will have this validity period, otherwise the user-ttl is taken from the Validity Period field of the Zone&#39;s&#39; Issuing Template. When using cert-manager it is advised to have a TTL of above 60 days (1440h). For more information - https://cert-manager.io/docs/usage/certificate/ | [optional] 
**venafi_api_key** | **str** | Venafi API key | [optional] 
**venafi_baseurl** | **str** | Venafi Baseurl | [optional] 
**venafi_password** | **str** | Venafi Password | [optional] 
**venafi_use_tpp** | **bool** | Venafi using TPP | [optional] 
**venafi_username** | **str** | Venafi Username | [optional] 
**venafi_zone** | **str** | Venafi Zone | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

