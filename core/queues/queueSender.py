import boto3
import os

sqs = boto3.client("sqs")
QUEUE_URL = os.environ["QUEUE_URL"]


def spin_send_message_queue(message: str):
    try:
        response = sqs.send_message(QueueUrl=QUEUE_URL, MessageBody=message)
        return f"messageId {response['MessageId']}"
    except:
        return f"error {message}"
