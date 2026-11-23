from src.security.redactor import SecretRedactor

def test_secret_redactor():
    raw = "Connecting with token: secret-token-xyz and api_key=123456"
    redacted = SecretRedactor.redact(raw)
    assert "secret-token-xyz" not in redacted
    assert "123456" not in redacted
    assert "[REDACTED]" in redacted

    cert = "-----BEGIN RSA PRIVATE KEY-----"
    assert SecretRedactor.redact(cert) == "[REDACTED]"
