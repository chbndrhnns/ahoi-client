# MonthlySummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Internal ID of this monthlySummary (generated value) | 
**month** | **str** | The month to which this entry belongs (year-month in ISO-8601: \&quot;yyyy-MM\&quot;) | 
**account_id** | **int** | ID of account to which this entry belongs | 
**income** | [**Amount**](Amount.md) | Sum of all incoming transactions for this month | 
**outgoings** | [**Amount**](Amount.md) | Sum of all outgoing transactions for this month | 
**balance** | [**Amount**](Amount.md) | Balance at end of month | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


