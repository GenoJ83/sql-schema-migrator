def execute_migration_plan(plan: list):
    applied = []
    for m in plan:
        applied.append(m.version)
    return applied
