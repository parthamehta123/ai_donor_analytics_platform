import requests

BASE_URL = "http://localhost:8000"


def check(endpoint, headers=None):
    try:
        r = requests.get(f"{BASE_URL}{endpoint}", headers=headers, timeout=3)
        r.raise_for_status()
        print(f"✅ {endpoint} ->", r.json())
    except requests.exceptions.ConnectionError:
        print("❌ API not reachable. Did you run `make up`?")
        exit(1)
    except Exception as e:
        print(f"❌ {endpoint} failed:", e)
        exit(1)


if __name__ == "__main__":
    print("\nRunning API smoke tests...\n")

    check(
        "/tools/campaign-performance?client_id=abc",
        headers={"x-role": "analyst"},
    )

    check(
        "/tools/donor-retention?client_id=abc",
        headers={"x-role": "strategist"},
    )

    check("/rag/ask?q=What is donor retention?")

    print("\n🎉 All smoke checks passed\n")
