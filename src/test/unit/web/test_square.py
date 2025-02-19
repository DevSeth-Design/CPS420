
from main import app  


from fastapi.testclient import TestClient


client = TestClient(app)

test_squares = [
    (8, 15),
    (4.7, 1.1),
    (3, 1.4)
]



def test_get_all_squares():
    response = client.get("/squares/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_and_retrieve_squares():
    for length, width in test_squares:
        response = client.post("/squares/", json={"Length": length, "Width": width})
        assert response.status_code == 200
        
        get_response = client.get(f"/squares/{length}/{width}")
        assert get_response.status_code == 200
        assert get_response.json()["Length"] == length
        assert get_response.json()["Width"] == width

def test_get_one_square():
    response = client.get("/squares/8/15")
    assert response.status_code in [200, 404]  # If found, 200. If not, 404.

def test_area():
    for Length, Width in test_squares:
        response = client.get(f"/squares/{Length}/{Width}/area")
        assert response.status_code == 200
        assert response.json() == Length * Width


def test_circumference():
    for Length, Width in test_squares:
        response = client.get(f"/squares/{Length}/{Width}/circumference")
        assert response.status_code == 200
        assert response.json() == 2 * (Length + Width)
    
