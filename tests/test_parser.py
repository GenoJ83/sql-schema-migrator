from src.parsers.sql_splitter import split_up_down_sql
def test_sql_splitter():
    raw = '-- +migrate Up\nCREATE TABLE users(id INT);\n-- +migrate Down\nDROP TABLE users;'
    up, down = split_up_down_sql(raw)
    assert 'CREATE TABLE users' in up
    assert 'DROP TABLE users' in down
