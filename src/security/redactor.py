import re

class SecretRedactor:
    PATTERNS = [
        re.compile(r"(?i)(api[_-]?key|password|secret|token|bearer)\s*[:=]\s*['\"][^'\"]+['\"]"),
        re.compile(r"(?i)(api[_-]?key|password|secret|token|bearer)\s*[:=]\s*[^\s,]+"),
        re.compile(r"ghp_[A-Za-z0-9_]{36}"),
        re.compile(r"-----BEGIN [A-Z ]+ PRIVATE KEY-----")
    ]

    @classmethod
    def redact(cls, text: str, placeholder: str = "[REDACTED]") -> str:
        res = text
        for pat in cls.PATTERNS:
            res = pat.sub(lambda m: m.group(0).split(":")[0].split("=")[0] + f": {placeholder}" if (":" in m.group(0) or "=" in m.group(0)) else placeholder, res)
        return res
