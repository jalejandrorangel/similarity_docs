import boto3

s3 = boto3.resource('s3')
bucket = s3.create_bucket(
    ACL='public-read-write',
    Bucket='bucket-chido',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-1'   },
)

for i in s3.bucket.all():
    print(i.name)
