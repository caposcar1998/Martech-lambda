import json
from pydantic import BaseModel
from typing import Optional,Dict
from controllers.analytics import send_analytics
from controllers.cdp import spin_send_communication
from database.methods import spin_add_item, spin_get_all

class SQSRecordDTO(BaseModel):
    messageId: str
    receiptHandle: str
    body: str
    attributes: Optional[Dict[str, str]]
    messageAttributes: Optional[Dict[str, Dict[str, str]]]
    md5OfBody: str
    eventSource: str
    eventSourceARN: str
    awsRegion: str

def lambda_handler(event, context):
    for record_dict in event["Records"]:
        record = SQSRecordDTO(**record_dict)
        body_queue = json.loads(record.body)
        destinations = spin_get_all("destinations")
        try:
            destinations = spin_get_all("destinations")
            for destination in destinations:
                if destination["type"] == "analytics":
                    send_analytics(destination, body_queue)
                else:
                    spin_send_communication(destination, body_queue)
        except Exception as e:
            raise Exception ({"responseId": record.messageId, "responseCode": 500, "responseBody": e})
        spin_add_item("responses", body_queue)
    return {
        "statusCode": 200,
        "body": "Processed {} messages".format(len(event["Records"])),
    }
