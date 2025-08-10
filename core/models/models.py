from typing import Optional
from pydantic import BaseModel
from enum import Enum

class MetadataDTO(BaseModel):
    promoId: str
    device: str
    preferredChannel: Optional[str] = None

class TrackEventDTO(BaseModel):
    userId: str
    event: str
    timestamp: str
    metadata: MetadataDTO

class DestinationType(str, Enum):
    ANALYTICS = "analytics"
    CDP = "CDP"

class DestinationsDTO(BaseModel):
    destinationName: str
    url: str
    type: DestinationType
    headers: Optional[str]
    password: Optional[str]

class SQSRecordDTO(BaseModel):
    messageId: str
    receiptHandle: str
    body: str
    attributes: Optional[Dict[str, str]]
    messageAttributes: Optional[Dict[str, Dict[str, str]]]
    md5OfBody: str
    eventSource: str
    eventSourceARN: str
    awsRegion: str