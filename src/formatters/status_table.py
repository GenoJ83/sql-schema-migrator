def format_status_table(migrations: list) -> str:
    return '\n'.join(f'{m.version} | {m.name} | {m.applied_at or "PENDING"}' for m in migrations)
