import copy
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

# Ensure the project root is on the path so src.app can be imported
project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))

from src.app import app, activities  # noqa: E402

original_activities = copy.deepcopy(activities)


def reset_activities() -> None:
    activities.clear()
    activities.update(copy.deepcopy(original_activities))


@pytest.fixture(autouse=True)
def reset_state():
    try:
        yield
    finally:
        reset_activities()


@pytest.fixture
def client():
    return TestClient(app)
