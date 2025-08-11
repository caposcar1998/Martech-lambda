import json
from pydantic import ValidationError
from queues.queueSender import spin_send_message_queue
from models.models import TrackEventDTO


def event_track(body: str) -> dict[str, str]:
    try:
        body_dict = json.loads(body)
    except json.JSONDecodeError as e:
        raise Exception(f"Invalid JSON input: {str(e)}")

    try:
        dto = TrackEventDTO(**body_dict)
    except ValidationError as e:
        raise Exception(f"Validation error: {e.json()}")

    body_json = dto.model_dump_json()
    messageId = spin_send_message_queue(body_json)
    return {"body": json.dumps({"messageId": messageId})}
