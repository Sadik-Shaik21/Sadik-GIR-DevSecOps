import json

def lambda_handler(event, context):

    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        size = record['s3']['object']['size']

        print("New file uploaded!")
        print(f"Bucket Name : {bucket}")
        print(f"Object Name : {key}")
        print(f"File Size   : {size} bytes")

    return {
        'statusCode': 200,
        'body': json.dumps('Task 21 executed successfully')
    }
