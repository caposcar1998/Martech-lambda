import requests

def spinPost(url, payload, headers=None, timeout=10):
    try:
        default_headers = {"Content-Type": "application/json"}
        if headers:
            default_headers.update(headers)

        response = requests.post(url, json=payload, headers=default_headers, timeout=timeout)
        response.raise_for_status()

        # Try to parse JSON response
        return response.json()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except ValueError:
        print("Response not JSON.")
    return None


def spinGet(url, params=None, headers=None, timeout=10):
    try:
        default_headers = {"Accept": "application/json"}
        if headers:
            default_headers.update(headers)

        response = requests.get(url, params=params, headers=default_headers, timeout=timeout)
        response.raise_for_status()

        return response.json()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except ValueError:
        print("Response not JSON.")
    return None