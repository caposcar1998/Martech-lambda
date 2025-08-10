import json
from api.track import eventTrack
# import requests

ROUTES = {
    ("/track", "post"): eventTrack,
}

def lambda_handler(event, context):

    path = event.get("path", "")
    method = event.get("httpMethod", "").lower()

    handler = ROUTES.get((path, method))

    if handler:
        body = event.get("body", "{}")
        return handler(body) 

    return {
        "statusCode": 404,
        "body": "Endpoint not found"
    }
