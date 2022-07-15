import asyncio



async def return_file():
    await asyncio.sleep(4)
    return ("File returned")

async def data_reply():
    await asyncio.sleep(7)
    return {"data": '100'}
    

async def task1():
    print("Waiting for data...")
    x = await data_reply()
    print(x)

async def task2():
    print("Waiting for file...")
    x = await return_file()
    print(x)


async def main():
    x = asyncio.create_task(task1())
    y = asyncio.create_task(task2())

    await y
    await x


asyncio.run(main())