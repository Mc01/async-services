import aiohttp
import asyncio

from config import Config


async def main():
    config = Config()
    for service in config.services:
        async with aiohttp.ClientSession() as session:
            async with session.get(service) as response:
                print(response.status)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
