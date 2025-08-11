from api.methods import spin_post
from typing import Any


def send_analytics(destination: Any, body: Any, insert_destination: Any) -> Any:
    destination_url = destination["url"]
    destination_headers = destination.get("headers", None)
    res = spin_post(destination_url, body, destination_headers)
    if not (200 <= res < 300):
        insert_destination.destinations[destination["destinationName"]] = False
        ## IF FALSE SEND TO A DEAD LETTER QUEUE
    else:
        insert_destination.destinations[destination["destinationName"]] = True
    return res
