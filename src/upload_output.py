import boto3

s3 = boto3.client('s3', aws_access_key_id = 'AKIAR6FH7HG7PJFCEFJV', aws_secret_access_key = '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')
s3.upload_file('sellers/sellers.csv', 'fatihtuna-case', 'sellers/sellers.csv')