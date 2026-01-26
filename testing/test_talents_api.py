"""
TDD: Failing test for GET /api/talents returning current_rank.
Run from project root: python -m pytest testing/ -v
Or from backend (so DB is found): pytest ../testing/ -v
"""
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

# allow importing backend.main when run from project root or backend
_backend = Path(__file__).resolve().parent.parent / "backend"
sys.path.insert(0, str(_backend))

from main import app

client = TestClient(app)


def test_get_talents_includes_current_rank_for_each_talent():
    """Each talent in the API response must include current_rank in [0, max_rank]."""
    response = client.get("/api/talents")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict), "response should be a dict keyed by talent id"
    for talent_id, talent in data.items():
        assert "current_rank" in talent, f"talent {talent_id!r} missing 'current_rank'"
        rank = talent["current_rank"]
        max_rank = talent["max_rank"]
        assert isinstance(rank, int), f"talent {talent_id!r} current_rank must be int, got {type(rank)}"
        assert 0 <= rank <= max_rank, f"talent {talent_id!r} current_rank {rank} must be in [0, {max_rank}]"
