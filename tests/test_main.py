from fastapi.testclient import TestClient


from src.main import app

def test_main(client):
    response = client.get("/")
    assert response.status_code == 200
    #assert response.json() == {"message": "Hello World"}


if __name__ == '__main__':
    client = TestClient(app)
    test_main(client)
