from unittest.mock import patch, Mock
from api.methods import spin_post, spin_get


@patch("api.methods.requests.post")
def test_spin_post_success(mock_post):
    mock_response = Mock()
    mock_response.json.return_value = {"status": "ok"}
    mock_response.raise_for_status.return_value = None
    mock_post.return_value = mock_response

    result = spin_post("http://example.com/api", {"key": "value"})
    assert result == {"status": "ok"}
    mock_post.assert_called_once()



@patch("api.methods.requests.get")
def test_spin_get_success(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {"status": "ok"}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = spin_get("http://example.com/api", params={"q": "test"})
    assert result == {"status": "ok"}
    mock_get.assert_called_once()
