import asyncio


async def fetch_data():
    print("Fetching data")
    await asyncio.sleep(5)
    print("Data returned...")
    return {'data': 100}

async def countDown(n):
    while n > 0:
        print(n)
        n -= 1
        await asyncio.sleep(2)

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(countDown(10))

    data = await task1
    print(data)
    await task2

asyncio.run(main())