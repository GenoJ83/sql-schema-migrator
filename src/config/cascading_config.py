"""Cascading configuration manager supporting environment overrides."""
import os
from typing import Any, Dict

class CascadingConfig:
    def __init__(self, defaults: Dict[str, Any] = None):
        self._config = defaults.copy() if defaults else {}

    def get(self, key: str, default: Any = None) -> Any:
        env_val = os.getenv(key.upper())
        if env_val is not None:
            return env_val
        return self._config.get(key, default)

    def set(self, key: str, value: Any):
        self._config[key] = value

    def to_dict(self) -> Dict[str, Any]:
        return self._config.copy()
