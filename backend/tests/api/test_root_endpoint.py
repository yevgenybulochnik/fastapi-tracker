from fastapi.testclient import TestClient


def test_root_endpoint(client: TestClient):
    res = client.get('/')
    print(res.json())
    assert False
