from src.security.linter import lint_sql_safety
def test_linter():
    w = lint_sql_safety('DROP TABLE users;')
    assert len(w) > 0
