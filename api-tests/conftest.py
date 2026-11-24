import pytest, requests

BASE_URL = "httpS://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")
def api():
    s = requests.Session()
    s.base_url = BASE_URL
    return s