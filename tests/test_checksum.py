from src.security.checksum import IntegrityVerifier

def test_integrity_verifier():
    sample = b"antigravity-enterprise-payload"
    digest = IntegrityVerifier.compute_sha256(sample)
    assert len(digest) == 64
    assert IntegrityVerifier.verify(sample, digest) is True
    assert IntegrityVerifier.verify(b"corrupted-data", digest) is False
