"""Cryptographically secure nonce and bearer token generators."""
import secrets
import hmac

def generate_secure_token(nbytes: int = 32) -> str:
    return secrets.token_urlsafe(nbytes)

def generate_nonce(length: int = 16) -> str:
    return secrets.token_hex(length)

def constant_time_compare(val1: str, val2: str) -> bool:
    return hmac.compare_digest(val1.encode(), val2.encode())
