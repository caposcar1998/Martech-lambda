import json

from api.methods import spinPost, spinGet
from database.methods import spin_add_item
def lambda_handler(event, context):
    # event['Records'] is a list of messages from SQS
    for record in event['Records']:
        # The message body is a string
        message_body = record['body']

        # You can parse JSON if your messages are JSON encoded
        try:
            data = json.loads(message_body)
            res = spinPost("https://testoscar.free.beeceptor.com", data)
            item = {
                "responseId": "1",
                "responseCode": 200,
                "responseBody": res
            }
            spin_add_item("responses",item)
        except json.JSONDecodeError:
            data = message_body

    return {
        'statusCode': 200,
        'body': 'Processed {} messages'.format(len(event['Records']))
    }
