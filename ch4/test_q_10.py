import asyncio


async def f1():
    while True:
        await asyncio.sleep(1)
    return "f1 done"


async def f2():
    k = 5
    while k:
        await asyncio.sleep(1)
        k -= 1
    return "f2 done"


async def test():
    res = await asyncio.gather(f1(), f2())
    print(res)


# This line was omitted in the test:
asyncio.run(test())
