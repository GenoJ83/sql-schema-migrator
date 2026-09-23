class SchemaCache:
    _schema = None
    @classmethod
    def get(cls): return cls._schema
    @classmethod
    def set(cls, s): cls._schema = s
