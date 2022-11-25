import asyncio
import aiohttp

async def main():
     async with aiohttp.ClientSession() as session:
        async with session.get('http://127.0.0.1:5000/users/list') as resp:
           print(await resp.json())

asyncio.run(main())

