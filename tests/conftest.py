import pytest
import app.tools as tools


@pytest.fixture(autouse=True)
def mock_db(monkeypatch):

    def fake_campaign(client_id: str):
        if client_id == "abc":
            return {
                "client_id": "abc",
                "impressions": 10000,
                "clicks": 850,
                "donations": 120,
                "revenue": 1500.0,
            }
        return None

    def fake_retention(client_id: str):
        return {
            "client_id": client_id,
            "retention_rate": 0.42,
        }

    monkeypatch.setattr(tools, "db_campaign_perf", fake_campaign)
    monkeypatch.setattr(tools, "db_donor_retention", fake_retention)
