def format_migration_plan(pending: list) -> str:
    return '\n'.join(f'-> Pending: {m.version}_{m.name}' for m in pending)
