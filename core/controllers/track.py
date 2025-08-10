import json
from queues.queueSender import spin_send_message_queue


def event_track(body: str) -> dict[str, str]:
    messageId = spin_send_message_queue(body)
    return {"body": json.dumps({"messageId": messageId})}