"""Structured JSON log event formatter."""
import json
import time
from typing import Any, Dict

class StructuredJsonFormatter:
    def __init__(self, service_name: str = "app"):
        self.service_name = service_name

    def format_event(self, level: str, message: str, **context: Any) -> str:
        record: Dict[str, Any] = {
            "timestamp": time.time(),
            "service": self.service_name,
            "level": level.upper(),
            "message": message,
            "context": context
        }
        return json.dumps(record)
