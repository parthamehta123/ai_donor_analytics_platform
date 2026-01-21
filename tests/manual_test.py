from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

print(
    client.get(
        "/tools/campaign-performance?client_id=abc",
        headers={"x-role": "analyst"},
    ).json()
)

print(
    client.get(
        "/tools/donor-retention?client_id=abc",
        headers={"x-role": "strategist"},
    ).json()
)

print(client.get("/rag/ask?q=What is donor retention?").json())
