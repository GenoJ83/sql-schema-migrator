import os
from typing import Dict, Any

class CascadingConfig:
    def __init__(self, defaults: Dict[str, Any] = None):
        self.defaults = defaults or {}
        self.file_config: Dict[str, Any] = {}
        self.env_overrides: Dict[str, Any] = {}
        self.cli_overrides: Dict[str, Any] = {}

    def resolve(self) -> Dict[str, Any]:
        merged = dict(self.defaults)
        merged.update(self.file_config)
        merged.update(self.env_overrides)
        merged.update(self.cli_overrides)
        return merged

    def load_env_prefix(self, prefix: str = "APP_") -> None:
        for k, v in os.environ.items():
            if k.startswith(prefix):
                key_name = k[len(prefix):].lower()
                self.env_overrides[key_name] = v
