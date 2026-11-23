import os
from src.security.config_hierarchy import CascadingConfig

def test_cascading_config_precedence():
    cfg = CascadingConfig(defaults={"port": 8080, "host": "127.0.0.1", "debug": False})
    cfg.file_config = {"host": "0.0.0.0", "debug": True}
    cfg.cli_overrides = {"port": 9000}

    resolved = cfg.resolve()
    assert resolved["port"] == 9000       # CLI overrides all
    assert resolved["host"] == "0.0.0.0"  # File overrides default
    assert resolved["debug"] is True
