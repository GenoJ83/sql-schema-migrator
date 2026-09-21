def parse_migration_filename(filename: str):
    parts = filename.replace('.sql', '').split('_', 1)
    return parts[0], parts[1] if len(parts) > 1 else 'migration'
