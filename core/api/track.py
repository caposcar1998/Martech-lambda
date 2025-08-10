import boto3
import os

sqs = boto3.client("sqs")
#QUEUE_URL = os.environ["https://sqs.us-east-1.amazonaws.com/477287708544/events"]

def eventTrack(body):

    print("oscar manda")
    res = sqs.send_message(
        QueueUrl="https://sqs.us-east-1.amazonaws.com/477287708544/events",
        MessageBody=body
    )

    print("hola oscar")
    # Handle tracking event
    return {
        "statusCode": 200,
        "body": f"Tracked: {body}"
    }