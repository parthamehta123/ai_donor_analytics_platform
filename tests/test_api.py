from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_campaign_performance_authorized():
    res = client.get(
        "/tools/campaign-performance?client_id=abc",
        headers={"x-role": "analyst"},
    )
    assert res.status_code == 200
    assert res.json()["client_id"] == "abc"


def test_campaign_performance_forbidden():
    res = client.get(
        "/tools/campaign-performance?client_id=abc",
        headers={"x-role": "strategist"},
    )
    assert res.status_code == 403


def test_donor_retention_authorized():
    res = client.get(
        "/tools/donor-retention?client_id=abc",
        headers={"x-role": "strategist"},
    )
    assert res.status_code == 200
    assert res.json()["retention_rate"] == 0.42
