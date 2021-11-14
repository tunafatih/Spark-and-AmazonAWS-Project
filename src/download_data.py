import boto3

client = boto3.client('s3', aws_access_key_id = 'AKIAR6FH7HG7PJFCEFJV', aws_secret_access_key = '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')

client.download_file('fatihtuna-case', 'e-commerce.zip', 'data/e-commerce.zip')