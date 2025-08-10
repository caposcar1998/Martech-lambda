import json
from queues.queueSender import send_message_queue
from database.methods import spin_create

def eventTrack(body):
        messageId = send_message_queue(body)
        return { "body": json.dumps({"messageId": messageId})}

def add_destinations(body):
        res = spin_create("destinations", body)
        return { "body": json.dumps({"Destination created status ": res})}