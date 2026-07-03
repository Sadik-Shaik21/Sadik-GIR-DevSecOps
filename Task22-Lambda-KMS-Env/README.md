# Task 22 – Lambda with Environment Variables & KMS

## Objective
Create an AWS Lambda function that securely retrieves a secret stored in AWS Secrets Manager using an environment variable and AWS KMS encryption. The function retrieves the secret at runtime and prints only a masked version of the API key in Amazon CloudWatch Logs.

## AWS Services Used
- AWS Lambda
- AWS Secrets Manager
- AWS Key Management Service (AWS KMS)
- AWS IAM
- Amazon CloudWatch Logs

## Resources Created
- Lambda Function: task22-lambda-kms-env
- KMS Key: task22-kms-key
- Secret: task22-secret
- Environment Variable: SECRET_NAME
- IAM Inline Policy: Task22SecretsPolicy

## Implementation Summary
1. Created a customer-managed KMS key.
2. Stored an API key in AWS Secrets Manager.
3. Created an AWS Lambda function using Python.
4. Configured the `SECRET_NAME` environment variable.
5. Granted the Lambda execution role permission to access Secrets Manager and decrypt the KMS-encrypted secret.
6. Retrieved the secret securely at runtime.
7. Displayed only a masked version of the API key in CloudWatch Logs.
8. Verified successful execution through Lambda Test and CloudWatch Logs.
9. Cleaned up all AWS resources after successful testing.

## Files
- `lambda_function.py` – Python Lambda function
- `README.md` – Project documentation

## Outcome
Task 22 was completed successfully by integrating AWS Lambda, Secrets Manager, AWS KMS, IAM, and CloudWatch Logs to securely retrieve and mask sensitive information using environment variables.