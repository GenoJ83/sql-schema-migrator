from src.security.permission_checker import FileSecurityChecker

def test_permission_checker():
    # 0o600 is rw-------
    assert FileSecurityChecker.is_owner_only_permissions(0o600) is True
    assert FileSecurityChecker.evaluate_file_safety(0o600) == "SECURE"

    # 0o644 is rw-r--r--
    assert FileSecurityChecker.is_owner_only_permissions(0o644) is False
    assert FileSecurityChecker.evaluate_file_safety(0o644) == "INSECURE_PERMISSIONS"
