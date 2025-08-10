import json
from functools import wraps


def json_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return {"statusCode": 200, "body": json.dumps(result)}
        except Exception as e:
            return {"statusCode": 500, "body": json.dumps({"error": str(e)})}

    return wrapper

