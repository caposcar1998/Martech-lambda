import json
from enum import Enum
from pydantic import BaseModel, ValidationError
from typing import Optional
from database.methods import spin_create


class DestinationType(str, Enum):
    ANALYTICS = "analytics"
    CDP = "CDP"
class DestinationsDTO(BaseModel):
    destinationName: str
    url: str
    type: DestinationType
    headers: Optional[str]
    password: Optional[str]

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