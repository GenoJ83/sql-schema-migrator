import hashlib

class KeyDerivationHelper:
    @staticmethod
    def derive_key(passphrase: str, salt: bytes, iterations: int = 10000, key_length: int = 32) -> bytes:
        return hashlib.pbkdf2_hmac(
            "sha256",
            passphrase.encode("utf-8"),
            salt,
            iterations,
            dklen=key_length
        )
