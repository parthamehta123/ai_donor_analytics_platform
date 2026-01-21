import psycopg
from tenacity import retry, stop_after_attempt, wait_fixed
from app.config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD


def get_connection():
    return psycopg.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        connect_timeout=3,
    )


@retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
def get_campaign_performance(client_id: str):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT impressions, clicks, donations, revenue
                FROM campaign_metrics
                WHERE client_id = %s
            """,
                (client_id,),
            )
            row = cur.fetchone()

    if not row:
        return None

    return {
        "client_id": client_id,
        "impressions": row[0],
        "clicks": row[1],
        "donations": row[2],
        "revenue": float(row[3]),
    }


@retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
def get_donor_retention(client_id: str):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT retention_rate
                FROM donor_retention
                WHERE client_id = %s
            """,
                (client_id,),
            )
            row = cur.fetchone()

    if not row:
        return None

    return {
        "client_id": client_id,
        "retention_rate": float(row[0]),
    }
