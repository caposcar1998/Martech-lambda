from decorators.decorators import json_response
from api.track import eventTrack

ROUTES = {
    ("/track", "post"): eventTrack,
}

@json_response
def lambda_handler(event, context):

    path = event.get("path", "")
    method = event.get("httpMethod", "").lower()

    handler = ROUTES.get((path, method))

    body = event.get("body", "{}")
    return handler(body) 
