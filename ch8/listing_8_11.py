"""
Асинхронный командный SQL-клиент
"""
import asyncio
import os
import sys
import tty
from collections import deque

import asyncpg
from asyncpg.pool import Pool
from listing_8_5 import create_stdin_reader
from listing_8_7 import (
    delete_line,
    move_to_bottom_of_screen,
    move_to_top_of_screen,
    restore_cursor_position,
    save_cursor_position,
)
from listing_8_8 import read_line
from listing_8_9 import MessageStore


async def run_query(query: str, pool: Pool, message_store: MessageStore) -> None:
    async with pool.acquire() as connection:
        try:
            result = await connection.fetchrow(query)
            await message_store.append(f"Fetched {len(result)} rows by query: {query}")
        except Exception as ex:
            await message_store.append(f"Query '{query}' resulted in exception: {ex}")


async def main() -> None:
    async def redraw_output(items: deque) -> None:
        save_cursor_position()
        move_to_top_of_screen()
        for item in items:
            delete_line()
            print(item)
        restore_cursor_position()

    tty.setcbreak(sys.stdin)
    os.system("clear")
    rows = move_to_bottom_of_screen()
    messages = MessageStore(redraw_output, rows - 1)
    stdin_reader = await create_stdin_reader()

    async with asyncpg.create_pool(
        host="127.0.0.1",
        port=5432,
        user="postgres",
        password="postgres",
        database="products",
        min_size=6,
        max_size=6,
    ) as pool:
        while True:
            query = await read_line(stdin_reader)
            asyncio.create_task(run_query(query, pool, messages))


asyncio.run(main())
