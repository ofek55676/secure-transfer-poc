import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import create_app
import os


TEST_ENV_VARS = {
    "AWS_ACCESS_KEY_ID": "access-key",
    "AWS_SECRET_ACCESS_KEY": "secret-key",
    "AWS_REGION": "eu-west-1",
    "DYNAMODB_TABLE_NAME": "test-table",
    "CODE_NAME": "test-code",
    "DOCKERHUB_URL": "https://hub.docker.com/r/ofektest/ofektest",
    "GITHUB_URL": "https://github.com/ofek55676/secure-transfer-poc",
}


@pytest.fixture(scope="module")
def client():
    with patch.dict(os.environ, TEST_ENV_VARS):
        app = create_app()
        with TestClient(app) as client:
            yield client


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200
    json_data = response.json()

    assert json_data.get("status") == "healthy"
    assert json_data.get("container")
    assert json_data.get("project")


def test_secret_endpoint(client):
    with patch("app.services.secret.Secret.retrieve_secret") as mock_get_secret:
        mock_get_secret.return_value = "mocked-secret-value"
        response = client.get("/secret")

        assert response.status_code == 200

        json_data = response.json()
        assert json_data.get("secret_code") == "mocked-secret-value"
