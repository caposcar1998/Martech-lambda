from api.methods import spin_post
from models.models import TrackEventDTO
from utils.parse import safe_json_parse
from typing import Any


def spin_send_communication(
    destination: Any, body: Any, insert_destination: Any
) -> Any:
    destination_url = destination["url"]
    destination_headers = destination.get("headers", None)

    preferd_communication_channel = define_type_communication(body)
    url_communication = destination_url + "/" + preferd_communication_channel

    res = spin_post(url_communication, body, destination_headers)

    if not (200 <= res < 300):
        insert_destination.destinations[destination["destinationName"]] = False
        ## IF FALSE SEND TO A DEAD LETTER QUEUE
    else:
        insert_destination.destinations[destination["destinationName"]] = True
    return res


def define_type_communication(message: TrackEventDTO) -> str:
    messageF = safe_json_parse(message)
    preferred = messageF["metadata"]["preferredChannel"]
    if preferred == "push":
        return "push"
    if preferred == "email":
        return "email"
    if preferred == "sms":
        return "sms"
    return ""
