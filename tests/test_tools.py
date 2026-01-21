from app.tools import get_campaign_performance, get_donor_retention


def test_campaign_perf():
    res = get_campaign_performance("abc")
    assert res.client_id == "abc"
    assert res.revenue == 1500.0


def test_campaign_invalid_client():
    res = get_campaign_performance("invalid")
    assert hasattr(res, "error")


def test_donor_retention():
    res = get_donor_retention("abc")
    assert res.retention_rate == 0.42
