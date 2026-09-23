def filter_pending(available, applied):
    applied_versions = {a.version for a in applied}
    return [m for m in available if m.version not in applied_versions]
