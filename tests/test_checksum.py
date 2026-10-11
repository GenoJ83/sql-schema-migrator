from src.engine.checksum import compute_checksum
def test_checksum():
    c1 = compute_checksum('CREATE TABLE t();')
    c2 = compute_checksum('CREATE TABLE t();')
    assert c1 == c2
