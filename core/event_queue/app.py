import json

from api.methods import spinPost, spinGet
def lambda_handler(event, context):
    # event['Records'] is a list of messages from SQS
    for record in event['Records']:
        # The message body is a string
        message_body = record['body']

        # You can parse JSON if your messages are JSON encoded
        try:
            data = json.loads(message_body)
            spinPost("https://testoscar.free.beeceptor.com", data)
            spinGet("https://testoscar.free.beeceptor.com", data)
        except json.JSONDecodeError:
            data = message_body

    return {
        'statusCode': 200,
        'body': 'Processed {} messages'.format(len(event['Records']))
    }
