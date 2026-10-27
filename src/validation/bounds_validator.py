"""Numerical bounds and string length validators."""

def validate_numeric_bounds(value: float, min_val: float, max_val: float) -> bool:
    if not (min_val <= value <= max_val):
        raise ValueError(f"Value {value} out of bounds [{min_val}, {max_val}]")
    return True

def validate_string_length(text: str, min_len: int = 1, max_len: int = 1000) -> bool:
    if not (min_len <= len(text) <= max_len):
        raise ValueError(f"String length {len(text)} out of bounds [{min_len}, {max_len}]")
    return True
