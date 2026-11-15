class MigrationError(Exception): pass
class ChecksumMismatchError(MigrationError): pass
class RollbackFailedError(MigrationError): pass
