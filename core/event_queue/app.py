import json

def lambda_handler(event, context):
    # event['Records'] is a list of messages from SQS
    for record in event['Records']:
        # The message body is a string
        message_body = record['body']

        # You can parse JSON if your messages are JSON encoded
        try:
            data = json.loads(message_body)
        except json.JSONDecodeError:
            data = message_body

        # Now handle your message, e.g. print or process data
        print("Received SQS message:", data)

        # Add your processing logic here

    return {
        'statusCode': 200,
        'body': 'Processed {} messages'.format(len(event['Records']))
    }
