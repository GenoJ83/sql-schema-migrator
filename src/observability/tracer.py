import time
import uuid
from typing import Dict, Any, Optional

class TraceSpan:
    def __init__(self, name: str, trace_id: str = None, parent_id: str = None):
        self.name = name
        self.trace_id = trace_id or uuid.uuid4().hex
        self.span_id = uuid.uuid4().hex[:16]
        self.parent_id = parent_id
        self.start_time = time.perf_counter()
        self.end_time: Optional[float] = None
        self.duration_ms: float = 0.0
        self.attributes: Dict[str, Any] = {}

    def set_attribute(self, key: str, value: Any) -> None:
        self.attributes[key] = value

    def finish(self) -> float:
        self.end_time = time.perf_counter()
        self.duration_ms = round((self.end_time - self.start_time) * 1000.0, 3)
        return self.duration_ms

    def w3c_traceparent(self) -> str:
        return f"00-{self.trace_id}-{self.span_id}-01"
