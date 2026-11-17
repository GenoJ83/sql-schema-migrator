import pytest
from src.plugins.manifest import PluginManifest

def test_manifest_validation():
    manifest = PluginManifest("audit-hook", "1.2.0", description="Security audit hook")
    assert manifest.validate() is True
    data = manifest.to_dict()
    assert data["name"] == "audit-hook"
    assert data["version"] == "1.2.0"

    invalid = PluginManifest("broken", "1.0")
    with pytest.raises(ValueError):
        invalid.validate()
