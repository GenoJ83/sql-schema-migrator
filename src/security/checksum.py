import hashlib

class IntegrityVerifier:
    @staticmethod
    def compute_sha256(data: bytes) -> str:
        return hashlib.sha256(data).hexdigest()

    @staticmethod
    def compute_blake2b(data: bytes) -> str:
        return hashlib.blake2b(data).hexdigest()

    @staticmethod
    def verify(data: bytes, expected_hash: str) -> bool:
        computed = hashlib.sha256(data).hexdigest()
        return computed.lower() == expected_hash.strip().lower()
