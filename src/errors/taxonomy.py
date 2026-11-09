"""Unified domain error taxonomy with resolution hints."""
from typing import Optional

class AppError(Exception):
    def __init__(self, message: str, code: str = "ERR_GENERIC", hint: Optional[str] = None):
        super().__init__(message)
        self.message = message
        self.code = code
        self.hint = hint or "Check configuration parameters and telemetry logs."

    def to_dict(self):
        return {"error": self.message, "code": self.code, "hint": self.hint}
