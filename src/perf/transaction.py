def wrap_in_transaction(sql: str) -> str:
    return f'BEGIN;\n{sql}\nCOMMIT;'
