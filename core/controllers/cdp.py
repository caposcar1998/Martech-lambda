import json
from api.methods import spin_post
from models.models import TrackEventDTO

def spin_send_communication(destination, body, insert_destination):
    destination_url = destination["url"]
    destination_headers = destination.get("headers", None) 

    body["communication_channel"] = define_type_communication(body)
    res = spin_post(destination_url, body, destination_headers)

    if res is not 200:
        insert_destination.destinations[destination["destinationName"]] = False
    else:
        insert_destination.destinations[destination["destinationName"]] = True
    return res

def define_type_communication(message: TrackEventDTO) -> str:
    messageF = safe_json_parse(message)
    preferred = messageF["metadata"]["preferredChannel"]
    if preferred is "push":
        return "push"
    if preferred is "email":
        return "email"  
    if preferred is "sms":
        return "sms"    
    return ""  


def safe_json_parse(data):
    # If it's already a dict, return it
    if isinstance(data, dict):
        return data
    
    # If it's bytes, decode it first
    if isinstance(data, (bytes, bytearray)):
        data = data.decode()

    # If it's a string, try parsing it
    if isinstance(data, str):
        try:
            parsed = json.loads(data)
            # If parsed is still a string, try parsing again
            if isinstance(parsed, str):
                parsed = json.loads(parsed)
            return parsed
        except json.JSONDecodeError:
            return None
    
    # Anything else → None
    return None