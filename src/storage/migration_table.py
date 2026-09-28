def get_migration_table_ddl(table_name='schema_migrations'):
    return f'CREATE TABLE IF NOT EXISTS {table_name} (version VARCHAR(64) PRIMARY KEY, applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, checksum VARCHAR(32));'
