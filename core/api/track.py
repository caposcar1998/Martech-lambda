import boto3
import os

sqs = boto3.client("sqs")
QUEUE_URL = os.environ["QUEUE_URL"]

def eventTrack(body):
    print("oscar manda")
    res = sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=body
    )
    print("hola oscar")
    return {
        "statusCode": 200,
        "body": f"Tracked: {body}"
    }