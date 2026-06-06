import pytest
from src.routing.modality_router import ModalityRouter

def test_router_initialization():
    router = ModalityRouter()
    assert router is not None
