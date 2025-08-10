from api.methods import spin_post
from models.models import TrackEventDTO

def spin_send_communication(destination, body):
    destination_url = destination["url"]
    destination_headers = destination.get("headers", None) 

    body["communication_channel"] = define_type_communication(body)
    spin_post(destination_url, body, destination_headers)

def define_type_communication(message: TrackEventDTO) -> str:
    if message.metadata.preferredChannel is "push":
        return "push"
    if message.metadata.preferredChannel is "email":
        return "email"  
    if message.metadata.preferredChannel is "sms":
        return "sms"      