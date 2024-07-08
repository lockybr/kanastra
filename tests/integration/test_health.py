def test_health_should_return_200(client):
  response = client.get("/health")
  assert response.status_code == 200
  assert response.json() == {
    "status": "OK"
  }
