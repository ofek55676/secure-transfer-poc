### DynamoDB Key Schema Mismatch
`ValidationException from GetItem: key element doesn’t match schema.`

The request used code_name instead of the correct camelCase key codeName, causing the error (confirmed with Eliran).

### Travis CI
This is my first time using Travis CI, and I’m still learning. I encountered an error: `Owner ofek55676 is not on a new pricing`, because Travis has no free plan.