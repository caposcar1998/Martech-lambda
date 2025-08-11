from typing import Any
import json


def safe_json_parse(data: Any) -> Any:
    if isinstance(data, dict):
        return data

    if isinstance(data, (bytes, bytearray)):
        data = data.decode()

    if isinstance(data, str):
        try:
            parsed = json.loads(data)
            if isinstance(parsed, str):
                parsed = json.loads(parsed)
            return parsed
        except json.JSONDecodeError:
            return None

    return None
