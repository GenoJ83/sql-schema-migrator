"""Tamper-evident audit trail with SHA-256 hash chains."""
import hashlib
from typing import List, Dict, Any

class AuditChain:
    def __init__(self):
        self.chain: List[Dict[str, Any]] = []
        self._last_hash = "GENESIS_HASH"

    def append_event(self, action: str, details: str) -> str:
        entry = f"{self._last_hash}:{action}:{details}"
        entry_hash = hashlib.sha256(entry.encode()).hexdigest()
        self.chain.append({"action": action, "details": details, "hash": entry_hash, "prev_hash": self._last_hash})
        self._last_hash = entry_hash
        return entry_hash
