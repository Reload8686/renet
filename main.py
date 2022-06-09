import asyncio

async def main():
    print('Hi Aloha')
    await asyncio.sleep(1)
    print('Aloha World!')

asyncio.run(main())
