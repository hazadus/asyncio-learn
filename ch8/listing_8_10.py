"""
Приложение для асинхронной задержки
"""
import asyncio
import os
import sys
import tty
from collections import deque

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


async def sleep(delay: int, message_store: MessageStore) -> None:
    await message_store.append(f"Start sleeping for {delay} sec.")
    await asyncio.sleep(delay)
    await message_store.append(f"End sleeping for {delay} sec.")


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

    while True:
        line = await read_line(stdin_reader)
        delay_time = int(line)
        asyncio.create_task((sleep(delay_time, messages)))


asyncio.run(main())
