from pydantic import BaseModel
class MigratorConfig(BaseModel):
    migrations_dir: str = 'migrations'
    table_name: str = 'schema_migrations'
    dialect: str = 'postgresql'
