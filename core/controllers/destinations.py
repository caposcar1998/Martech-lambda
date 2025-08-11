import json
from pydantic import ValidationError
from database.methods import spin_create
from models.models import DestinationsDTO


def add_destinations(body: str) -> dict[str, str]:
    try:
        body_dict = json.loads(body)
    except json.JSONDecodeError as e:
        raise Exception(f"Invalid JSON input: {str(e)}")

    try:
        DestinationsDTO(**body_dict)
    except ValidationError as e:
        raise Exception(f"Validation error: {e.json()}")

    res = spin_create("destinations", json.loads(body))

    return {"body": json.dumps({"Destination created status": res})}
