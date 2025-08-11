import json
from controllers.analytics import send_analytics
from controllers.cdp import spin_send_communication
from database.methods import spin_add_item, spin_get_all
from models.models import SQSRecordDTO, InsertDestinationDTO

def lambda_handler(event, context) -> dict[str, str]:
    for record_dict in event["Records"]:
        record = SQSRecordDTO(**record_dict)
        
        try:
            parsed_body = json.loads(record.body)
        except json.JSONDecodeError as e:
            raise Exception({
                "responseId": record.messageId,
                "responseCode": 400,
                "responseBody": f"Invalid JSON in SQS body: {e}"
            })
        
        insert_destination = InsertDestinationDTO(
            responseId=record.messageId,
            responseBody=parsed_body,
            destinations={}
        )

        destinations = spin_get_all("destinations")

        try:
            for destination in destinations:
                if destination["type"] == "CDP":
                    spin_send_communication(destination, parsed_body, insert_destination)
                else:
                    send_analytics(destination, parsed_body, insert_destination)
                

        except Exception as e:
            pass

        spin_add_item("responses", insert_destination.model_dump())

    return {
        "statusCode": 200,
        "body": f"Processed {len(event['Records'])} messages",
    }

