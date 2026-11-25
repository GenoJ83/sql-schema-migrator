from typing import Dict, Any, List
from src.plugins.manifest import PluginManifest
from src.plugins.registry import HookRegistry

class PluginLoader:
    def __init__(self, registry: HookRegistry):
        self.registry = registry
        self.loaded_plugins: Dict[str, PluginManifest] = {}

    def load_plugin(self, manifest_data: Dict[str, Any], hook_setup_fn) -> bool:
        manifest = PluginManifest(**manifest_data)
        manifest.validate()
        hook_setup_fn(self.registry)
        self.loaded_plugins[manifest.name] = manifest
        return True

    def get_loaded_names(self) -> List[str]:
        return list(self.loaded_plugins.keys())
