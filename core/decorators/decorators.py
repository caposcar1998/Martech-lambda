import json
from functools import wraps


def json_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return {"statusCode": 200, "body": json.dumps(result)}
        except KeyError as e:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": f"Missing key: {str(e)}"}),
            }
        except Exception as e:
            return {"statusCode": 500, "body": json.dumps({"error": str(e)})}

    return wrapper


@json_response
def lambda_handler(event, context):
    # Just return dict or data; decorator wraps it nicely
    return {"message": "Hello world"}
