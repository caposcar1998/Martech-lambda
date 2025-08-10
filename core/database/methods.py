import boto3
from botocore.exceptions import ClientError
from typing import Any

dynamodb = boto3.resource('dynamodb')

def spin_add_item(table_name, item):
    table = dynamodb.Table(table_name)
    try:
        response = table.put_item(Item=item)
        return response
    except ClientError as e:
        print(f"Error adding item: {e.response['Error']['Message']}")
        return None

def spin_get_item(table_name, key):
    table = dynamodb.Table(table_name)
    try:
        response = table.get_item(Key=key)
        return response.get('Item')
    except ClientError as e:
        print(f"Error getting item: {e.response['Error']['Message']}")
        return None
    
def spin_get_all(table_name) -> list[dict]:
    table = dynamodb.Table(table_name)
    try:
        response = table.scan()
        items = response.get('Items', [])
        
        # Handle pagination if there are more items
        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            items.extend(response.get('Items', []))
            
        return items
    except ClientError as e:
        print(f"Error scanning table: {e.response['Error']['Message']}")
        return None
    
def spin_create(table_name, item: dict[str, Any]):
    table = dynamodb.Table(table_name)
    try:
        table.put_item(Item=item)
        return "success"
    except Exception as e:
        print("error", e)
        return "error"