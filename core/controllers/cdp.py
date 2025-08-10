from api.methods import spin_post

def spin_send_communication(destination, body):
    destination_url = destination["url"]
    destination_headers = destination.get("headers", None) 
    spin_post(destination_url, body, destination_headers)