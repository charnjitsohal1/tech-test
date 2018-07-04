import os
import boto3
from botocore.exceptions import ClientError
import requests

api_url = "https://api.stores.sainsburys.co.uk/v1/stores/all/"
bucket = os.environ['S3_BUCKET']
s3 = boto3.resource('s3')


def lambda_handler(event, context):
    try:
        response = requests.get(api_url)
        if response.status_code != 200:
            print('Status:', response.status_code, 'Problem with the request. Exiting.')
            exit(2)
        data = response.json()
        list_of_codes = []
        for result in data['results']:
            list_of_codes.append(result['district_code'])
        try:
            formatted_string = '\n'.join(list_of_codes)
            s3.Bucket(bucket).put_object(Key='district_codes.txt', Body=formatted_string.encode())
        except ClientError as e:
            print("Unexpected error: {}".format(e))
    except Exception as e:
        raise Exception("Unexpected error: {}".format(e))
