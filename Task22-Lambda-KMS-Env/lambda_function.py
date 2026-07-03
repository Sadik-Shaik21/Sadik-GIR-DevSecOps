import json
import os
import boto3

def lambda_handler(event, context):
    secret_name = os.environ["SECRET_NAME"]

    client = boto3.client("secretsmanager")

    response = client.get_secret_value(
        SecretId=secret_name
    )

    secret = json.loads(response["SecretString"])

    api_key = secret["apiKey"]

    masked_key = api_key[:4] + "*" * (len(api_key) - 8) + api_key[-4:]

    print("Secret retrieved successfully")
    print("Masked API Key:", masked_key)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Secret retrieved successfully",
            "maskedKey": masked_key
        })
    }