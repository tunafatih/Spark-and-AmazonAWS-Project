import boto3

s3 = boto3.client('s3', aws_access_key_id = ' ', aws_secret_access_key = ' ')

s3.download_file('fatihtuna-case', 'e-commerce.zip', 'brazilian-ecommerce/e-commerce.zip')
