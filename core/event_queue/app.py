import json

from api.methods import spin_post
from database.methods import spin_add_item, spin_get_all


def lambda_handler(event, context):
    # event['Records'] is a list of messages from SQS
    for record in event["Records"]:
        # The message body is a string
        message_body = record["body"]
        message_id = record["messageId"]

        # You can parse JSON if your messages are JSON encoded
        try:
            destinations = spin_get_all("destinations")
            data = json.loads(message_body)
            for destination in destinations:
                res = spin_post(destination["url"], data)
                item = {
                    "responseId": message_id,
                    "responseCode": 200,
                    "responseBody": res,
                }
        except Exception as e:
            item = {"responseId": message_id, "responseCode": 500, "responseBody": e}
        spin_add_item("responses", item)
    return {
        "statusCode": 200,
        "body": "Processed {} messages".format(len(event["Records"])),
    }
