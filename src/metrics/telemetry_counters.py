"""Prometheus and OpenTelemetry compatible metrics registry."""
import threading
from typing import Dict

class MetricsRegistry:
    def __init__(self):
        self._counters: Dict[str, int] = {}
        self._gauges: Dict[str, float] = {}
        self._lock = threading.Lock()

    def increment_counter(self, name: str, amount: int = 1):
        with self._lock:
            self._counters[name] = self._counters.get(name, 0) + amount

    def set_gauge(self, name: str, value: float):
        with self._lock:
            self._gauges[name] = float(value)

    def snapshot(self) -> Dict[str, Dict]:
        with self._lock:
            return {"counters": self._counters.copy(), "gauges": self._gauges.copy()}
