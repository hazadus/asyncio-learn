import asyncio


async def delay(delay_seconds: int) -> int:
    print(f"Starting sleep for {delay_seconds} sec...")
    await asyncio.sleep(delay_seconds)
    print(f"End sleeping for {delay_seconds} sec.")
    return delay_seconds
