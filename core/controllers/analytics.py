from api.methods import spin_post

def send_analytics(destination, body, insert_destination):
    destination_url = destination["url"]
    destination_headers = destination.get("headers", None) 
    res = spin_post(destination_url, body, destination_headers)
    if res is not 200:
        insert_destination.destinations[destination["destinationName"]] = False
    else:
        insert_destination.destinations[destination["destinationName"]] = True
    return res
