import json
from queues.queueSender import send_message_queue

def eventTrack(body):
        messageId = send_message_queue(body)
        return { "body": json.dumps({"messageId": messageId})}