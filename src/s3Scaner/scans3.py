import json
import boto3
#1.20.32
#https://www.kodyaz.com/aws/s3-buckets-list-using-aws-lambda-function-with-python-code.aspx

s3 = boto3.resource('s3')
client = boto3.client('s3')

def getJpgObjects(bucket):
    """Returns only jpg objects in s3 bucket"""
    myout = []
    for item in bucket.objects.all():
        if item.key.endswith('.jpg'):
            obj = s3.Object(item.bucket_name,item.key)
            myout.append(item)
            print(f"{item.key=}")
            print(f" - {item.bucket_name=}")
            print(f" - {obj.content_type=}")
            print(f" - {obj.content_length=}")
            print(f" - {obj.e_tag=}")
            print(f" - {obj.metadata=}")
            print(f" - {obj.missing_meta=}")
            print(f" - {obj.website_redirect_location=}")
            tagSet = getBucketTags(item.bucket_name,item.key)
            print(f" - {tagSet=}")

            #print(s3.ObjectSummary('foo',item.key))
            #print(s3.Object('foo',item.key).content_type) #returns image/jpeg
    return myout 
def getBucketTags(bucket,key):
    response = client.get_object_tagging(
    Bucket=bucket,
    Key=key)
    #print(f" {key} tag: {response['TagSet']}")
    return response['TagSet']

  
#object_summary = s3.ObjectSummary('bucket_name','key')
    

def lambda_handler(event, context):
    
    response = {}
    
    print(boto3.__version__)
    
    my_bucket = s3.Bucket('foo-c4c')
    jpg_objects = getJpgObjects(my_bucket)
    jpgs_keys = [x.key for x in jpg_objects]
    print(jpgs_keys)
    
    
    response['bucket'] = my_bucket.name
    response['files'] = jpgs_keys
    
    
    
    

    #'body': json.dumps(f'Hello from Lambda!   ')
            
    
    
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
