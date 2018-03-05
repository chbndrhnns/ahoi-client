# InputFieldDescription

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Internal ID for this field description | 
**label** | **str** | Label for this field description (e.g., &#39;PIN&#39;, &#39;Login name&#39;, &#39;Customer No.&#39;) | 
**masked** | **bool** | Flag that indicates whether the given field value must be masked when entered on client side or encrypted when persisted  on the server side | 
**format** | **str** | Format of field value  Can be &#x60;DEFINITELYNUMERIC&#x60; (format is definitely numeric), &#x60;DEFINITELYALPHANUMERIC&#x60; (format is definitely alphanumeric),  &#x60;PROBABLYALPHANUMERIC&#x60; (format is probably alphanumeric; numeric is unlikely but possible), &#x60;PROBABLYNUMERIC&#x60; (format is probably  numeric; alphanumeric is unlikely but possible) or &#x60;UNSPECIFIED&#x60; (default, no hint available) | 
**length_min** | **int** | Minimum length of field value (0 &#x3D; no limit) | [optional] 
**length_max** | **int** | Maximum length of field value (0 &#x3D; no limit) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


