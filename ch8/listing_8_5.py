"""
Асинхронный читатель стандартного ввода
"""
import asyncio
import sys
from asyncio import StreamReader, StreamReaderProtocol


async def create_stdin_reader() -> StreamReader:
    stream_reader = StreamReader()
    protocol = StreamReaderProtocol(stream_reader)
    loop = asyncio.get_running_loop()
    await loop.connect_read_pipe(lambda: protocol, sys.stdin)
    return stream_reader
