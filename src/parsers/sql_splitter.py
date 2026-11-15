def split_up_down_sql(sql: str):
    parts = sql.split('-- +migrate Down')
    up = parts[0].replace('-- +migrate Up', '').strip()
    down = parts[1].strip() if len(parts) > 1 else ''
    return up, down
