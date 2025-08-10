import requests
from typing import Any


def spin_post(url: str, payload: Any | None, headers=None, timeout=10):
    try:
        default_headers = {"Content-Type": "application/json"}
        if headers:
            default_headers.update(headers)

        response = requests.post(
            url, json=payload, headers=default_headers, timeout=timeout
        )
        return response.status_code
    except requests.RequestException:
        return 500
    except ValueError:
        return 500


def spin_get(url, params=None, headers=None, timeout=10):
    try:
        default_headers = {"Accept": "application/json"}
        if headers:
            default_headers.update(headers)

        response = requests.get(
            url, params=params, headers=default_headers, timeout=timeout
        )
        response.raise_for_status()

        return response.status_code
    except requests.RequestException:
        return 500
    except ValueError:
        return 500
