from app.tools import get_campaign_performance, get_donor_retention
import pytest


@pytest.mark.unit
def test_campaign_perf():
    res = get_campaign_performance("abc")
    assert res.client_id == "abc"
    assert res.revenue == 1500.0


@pytest.mark.unit
def test_campaign_invalid_client():
    res = get_campaign_performance("invalid")
    assert hasattr(res, "error")


@pytest.mark.unit
def test_donor_retention():
    res = get_donor_retention("abc")
    assert res.retention_rate == 0.42
