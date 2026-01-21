from app.tools import get_campaign_performance


def test_db_contract_schema():
    res = get_campaign_performance("abc")

    assert hasattr(res, "client_id")
    assert hasattr(res, "impressions")
    assert hasattr(res, "clicks")
    assert hasattr(res, "donations")
    assert hasattr(res, "revenue")
