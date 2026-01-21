from app.rag.generator import answer
import pytest

pytestmark = pytest.mark.unit


def test_rag_basic():
    resp = answer("What is donor retention?")
    assert isinstance(resp, str)
    assert len(resp) > 5
