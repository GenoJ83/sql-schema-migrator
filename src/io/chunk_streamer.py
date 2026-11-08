"""Streaming chunk reader and writer for high-throughput I/O."""
import io
from typing import Generator

class ChunkStreamer:
    def __init__(self, chunk_size: int = 4096):
        self.chunk_size = chunk_size

    def stream_bytes(self, stream: io.BytesIO) -> Generator[bytes, None, None]:
        while True:
            chunk = stream.read(self.chunk_size)
            if not chunk:
                break
            yield chunk
