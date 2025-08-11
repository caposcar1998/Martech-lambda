import os
from unittest.mock import patch, MagicMock

os.environ["AWS_REGION"] = "us-east-1"
os.environ["QUEUE_URL"] = "https://sqs.us-east-1.amazonaws.com/123456789012/my-queue"

with patch("boto3.client") as mock_boto_client:
    mock_sqs = MagicMock()
    mock_boto_client.return_value = mock_sqs

    from queues.queueSender import spin_send_message_queue


def test_spin_send_message_queue_success():
    # Arrange
    spin_send_message_queue.sqs = mock_sqs  # Optional if spin_send_message_queue uses a module-level sqs variable

    mock_sqs.send_message.return_value = {"MessageId": "abc-123"}

    # Act
    result = spin_send_message_queue("test message")

    # Assert
    assert result == "messageId abc-123"
    mock_sqs.send_message.assert_called_once_with(
        QueueUrl=os.environ["QUEUE_URL"], MessageBody="test message"
    )


def test_spin_send_message_queue_failure():
    mock_sqs.send_message.side_effect = Exception("AWS error")

    result = spin_send_message_queue("test message")

    assert result == "error test message"
    mock_sqs.send_message.assert_called()
