import json
import time
from typing import Dict, Any

class SecurityAuditLogger:
    @staticmethod
    def format_event(action: str, user: str, status: str, details: Dict[str, Any] = None) -> str:
        record = {
            "event": "SECURITY_AUDIT",
            "action": action,
            "user": user,
            "status": status,
            "timestamp": time.time(),
            "details": details or {}
        }
        return json.dumps(record, sort_keys=True)
