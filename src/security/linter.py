DANGEROUS = ['DROP TABLE', 'TRUNCATE', 'ALTER TABLE DROP COLUMN']
def lint_sql_safety(sql: str):
    warnings = [w for w in DANGEROUS if w in sql.upper()]
    return warnings
