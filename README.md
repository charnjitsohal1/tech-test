**Sainsbury's Tech Test**

Lambda function that does a GET request to an API endpoint and parses the 'district_code'. Before storing the codes in an S3 bucket for consumption at a later stage.

Requires the Serverless framework to be installed for testing/deployment to AWS. https://serverless.com/framework/docs/getting-started/

Also requires a S3 bucket to be created where the list of District Codes will be stored. This is set as an Environment variable in the serverless.yml file.

To test locally run the command below:
`serverless invoke local --function DistrictCode`

To deploy lambda function run the following command:
`serverless deploy --stage dev`