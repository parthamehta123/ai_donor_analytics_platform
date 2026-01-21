from app.rag.generator import answer


def test_rag_basic():
    resp = answer("What is donor retention?")
    assert isinstance(resp, str)
    assert len(resp) > 5
