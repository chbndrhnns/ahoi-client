# Provider

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Internal ID of this provider. A constant to identify provider even when,  for examplr, their bank code changes (provided type is BankProvider) | 
**name** | **str** | Name of this provider (e.g., \&quot;Hamburger Bank\&quot;) | 
**location** | **str** | Location of this provider (e.g., \&quot;Hamburg\&quot;) | 
**access_description** | [**AccessDescription**](AccessDescription.md) | Description of the access for the account setup (e.g., UI input fields) | [optional] 
**supported** | **bool** | Whether this bank is supported by the AHOI API (i.e., whether you can establish a connection to this provider). | 
**type** | **str** | Discriminator for subtypes. At the moment only &#x60;BankProvider&#x60; is supported. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


