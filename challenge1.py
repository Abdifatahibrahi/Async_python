import asyncio

async def t1():
    await t2()
    print('task 1')


async def t2():
    print('task 2')

async def t3():
    await t1()
    print('task 3')


async def main():
    task1 = asyncio.create_task(t3())
    

    await task1
    

asyncio.run(main())