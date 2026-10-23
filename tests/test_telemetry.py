"""Unit tests for telemetry diagnostics."""
from src.telemetry import get_system_telemetry

def test_telemetry_health():
    t = get_system_telemetry()
    assert t["status"] == "healthy"
    assert "pid" in t
    assert "timestamp" in t
