import stat

class FileSecurityChecker:
    @staticmethod
    def is_owner_only_permissions(mode: int) -> bool:
        # Check that group and others have no read/write/exec permissions
        group_or_other = mode & (stat.S_IRWXG | stat.S_IRWXO)
        return group_or_other == 0

    @staticmethod
    def evaluate_file_safety(file_mode: int) -> str:
        if FileSecurityChecker.is_owner_only_permissions(file_mode):
            return "SECURE"
        return "INSECURE_PERMISSIONS"
