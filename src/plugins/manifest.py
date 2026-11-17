from typing import Dict, List, Any

class PluginManifest:
    def __init__(self, name: str, version: str, description: str = "", entrypoint: str = "main", dependencies: List[str] = None):
        self.name = name
        self.version = version
        self.description = description
        self.entrypoint = entrypoint
        self.dependencies = dependencies or []

    def validate(self) -> bool:
        if not self.name or not isinstance(self.name, str):
            raise ValueError("Manifest name must be a non-empty string.")
        parts = self.version.split(".")
        if len(parts) != 3 or not all(p.isdigit() for p in parts):
            raise ValueError(f"Manifest version '{self.version}' must adhere to semantic versioning (MAJOR.MINOR.PATCH).")
        return True

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "version": self.version,
            "description": self.description,
            "entrypoint": self.entrypoint,
            "dependencies": self.dependencies
        }
