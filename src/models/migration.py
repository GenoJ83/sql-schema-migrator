from pydantic import BaseModel
class MigrationFile(BaseModel):
    version: str
    name: str
    checksum: str
    applied_at: str = None
