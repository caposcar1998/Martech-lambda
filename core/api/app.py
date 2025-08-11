from decorators.decorators import json_response
from controllers.track import event_track
from controllers.destinations import add_destinations

ROUTES = {
    ("/track", "post"): event_track,
    ("/destinations", "post"): add_destinations,
}


@json_response
def lambda_handler(event, context) -> dict[str, str]:

    path = event.get("path", "")
    method = event.get("httpMethod", "").lower()

    handler = ROUTES.get((path, method))

    body = event.get("body", "{}")
    return handler(body)
