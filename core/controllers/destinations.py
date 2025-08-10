import json
from database.methods import spin_create


def add_destinations(body: str) -> dict[str, str]:
    res = spin_create("destinations", json.loads(body))
    return {"body": json.dumps({"Destination created status ": res})}