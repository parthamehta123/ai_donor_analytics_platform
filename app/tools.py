from functools import lru_cache
from app.db.queries import (
    get_campaign_performance as db_campaign_perf,
    get_donor_retention as db_donor_retention,
)
from app.models import CampaignPerformance, DonorRetention, ErrorResponse


@lru_cache(maxsize=128)
def get_campaign_performance(client_id: str):
    result = db_campaign_perf(client_id)

    if result is None:
        return ErrorResponse(client_id=client_id, error="No data found")

    return CampaignPerformance(**result)


def get_donor_retention(client_id: str) -> DonorRetention:
    result = db_donor_retention(client_id)

    if isinstance(result, dict):
        return DonorRetention(**result)

    return DonorRetention(client_id=client_id, retention_rate=0.0)
