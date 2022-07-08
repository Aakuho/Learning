# func1()   |
# func2()   |
# func3()   | down

#? func2 is going to run when func1 ends. func3 works the same way, that it starts right after func2 ends
#? This is called synchronous programming

#! Asynchornous programming is not multithreaded
#? Async gives the illusion of multiple functions running at once, in reallity though, it runs another function when the other one is on standby (sleeping etc.)

import asyncio

async def main():
    task = asyncio.create_task(other()) # once i have some extra time, the task 'other' will get executed
    print('a')
    await asyncio.sleep(1) # await keyword is put before a function, it tells us that this is the moment where the function can "waste" time and thus the program can continue in other async functions
    print('b')
    #await task

async def other():
    print('1')
    await asyncio.sleep(2)
    print('2')

#asyncio.run(main())



async def func1():
    task = asyncio.create_task(func2())
    print('a')
    await asyncio.sleep(1)
    print('b')
    returnValue = await task
    print(f'Return value: {returnValue}')


async def func2(): #NOTE: now with return value
    print('1')
    await asyncio.sleep(2)
    print('2')
    return 10

asyncio.run(func1())