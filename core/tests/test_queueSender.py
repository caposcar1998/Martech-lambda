import os
os.environ["QUEUE_URL"] = "https://sqs.us-east-1.amazonaws.com/123456789012/my-queue"

from unittest.mock import patch
from queues.queueSender import spin_send_message_queue


@patch("queues.queueSender.sqs")
def test_spin_send_message_queue_success(mock_sqs):
    mock_sqs.send_message.return_value = {"MessageId": "abc-123"}

    result = spin_send_message_queue("test message")
    assert result == "messageId abc-123"
    mock_sqs.send_message.assert_called_once_with(
        QueueUrl=os.environ["QUEUE_URL"], MessageBody="test message"
    )


@patch("queues.queueSender.sqs")
def test_spin_send_message_queue_failure(mock_sqs):
    mock_sqs.send_message.side_effect = Exception("AWS error")

    result = spin_send_message_queue("test message")
    assert result == "error test message"
    mock_sqs.send_message.assert_called_once()
