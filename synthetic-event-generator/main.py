import os
import boto3
import time
import random

sqs = boto3.client('sqs')

# Fetch SQS queue URL from environment variable
queue_url = os.getenv('SQS_QUEUE_URL')

if queue_url is None:
    print('The environment variable SQS_QUEUE_URL is not set.')
    exit(1)

while True:
    # Generate a random sentiment score between -1.0 (negative) and 1.0 (positive)
    sentiment_score = random.uniform(-1.0, 1.0)

    # Send the sentiment score to SQS
    sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=str(sentiment_score),
    )

    # Wait for a bit before sending the next message
    time.sleep(0.1)