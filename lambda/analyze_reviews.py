import boto3
import time
import uuid

# Clients
s3 = boto3.client('s3')
comprehend = boto3.client('comprehend')

# Replace with your actual values
S3_BUCKET_NAME = "stacy-comprehend-demo"
COMPREHEND_ROLE_ARN = " "

def lambda_handler(event, context):
    print("=== EVENT RECEIVED ===")
    print(event)
    
    # Extract file info from the S3 trigger event
    record = event['Records'][0]
    s3_key = record['s3']['object']['key']
    input_s3_uri = f"s3://{S3_BUCKET_NAME}/{s3_key}"

    # Generate unique job names using timestamp
    timestamp = str(int(time.time()))
    uuid_suffix = str(uuid.uuid4())
    
    sentiment_job_name = f"sentiment-{timestamp}-{uuid_suffix}"
    pii_job_name = f"pii-{timestamp}-{uuid_suffix}"
    entity_job_name = f"entity-{timestamp}-{uuid_suffix}"

    # Output locations
    output_sentiment_uri = f"s3://{S3_BUCKET_NAME}/output/sentiment/{sentiment_job_name}/"
    output_pii_uri = f"s3://{S3_BUCKET_NAME}/output/pii/{pii_job_name}/"
    output_entity_uri = f"s3://{S3_BUCKET_NAME}/output/entity/{entity_job_name}/"

    # Start Sentiment Detection Job
    sentiment_response = comprehend.start_sentiment_detection_job(
        InputDataConfig={
            'S3Uri': input_s3_uri,
            'InputFormat': 'ONE_DOC_PER_LINE'
        },
        OutputDataConfig={
            'S3Uri': output_sentiment_uri
        },
        DataAccessRoleArn=COMPREHEND_ROLE_ARN,
        JobName=sentiment_job_name,
        LanguageCode='en'
    )
    print("Sentiment job started:", sentiment_response['JobId'])

    # Start PII Redaction Job
    pii_response = comprehend.start_pii_entities_detection_job(
        InputDataConfig={
            'S3Uri': input_s3_uri,
            'InputFormat': 'ONE_DOC_PER_LINE'
        },
        OutputDataConfig={
            'S3Uri': output_pii_uri
        },
        Mode='ONLY_REDACTION',
        RedactionConfig={
            'PiiEntityTypes': ['ALL'],
            'MaskMode': 'REPLACE_WITH_PII_ENTITY_TYPE'
        },
        DataAccessRoleArn=COMPREHEND_ROLE_ARN,
        JobName=pii_job_name,
        LanguageCode='en'
    )
    print("PII detection job started:", pii_response['JobId'])

    # Start Entity Detection Job
    entity_response = comprehend.start_entities_detection_job(
        InputDataConfig={
            'S3Uri': input_s3_uri,
            'InputFormat': 'ONE_DOC_PER_LINE'
        },
        OutputDataConfig={
            'S3Uri': output_entity_uri
        },
        DataAccessRoleArn=COMPREHEND_ROLE_ARN,
        JobName=entity_job_name,
        LanguageCode='en'
    )
    print("Entity detection job started:", entity_response['JobId'])

    return {
        'statusCode': 200,
        'body': 'All Comprehend jobs triggered successfully.'
    }
