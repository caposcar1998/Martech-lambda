import boto3
from botocore.exceptions import ClientError
from typing import Any

dynamodb = boto3.resource("dynamodb")


def spin_add_item(table_name: str, item: list[dict]) -> str:
    table = dynamodb.Table(table_name)
    try:
        table.put_item(Item=item)
        return "ok"
    except ClientError:
        return "error"


def spin_get_item(table_name: str, key: str) -> Any:
    table = dynamodb.Table(table_name)
    try:
        response = table.get_item(Key=key)
        return response.get("Item")
    except ClientError as e:
        return None


def spin_get_all(table_name: str) -> list[dict]:
    table = dynamodb.Table(table_name)
    try:
        response = table.scan()
        items = response.get("Items", [])

        # Handle pagination if there are more items
        while "LastEvaluatedKey" in response:
            response = table.scan(ExclusiveStartKey=response["LastEvaluatedKey"])
            items.extend(response.get("Items", []))

        return items
    except ClientError as e:
        return None


def spin_create(table_name: str, item: dict[str, Any]) -> str:
    table = dynamodb.Table(table_name)
    try:
        table.put_item(Item=item)
        return "success"
    except Exception as e:
        print("error", e)
        return "error"
