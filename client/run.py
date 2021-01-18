import aiohttp
import asyncio

from aiohttp import InvalidURL

from config import Config


keywords = [
    "bangkok",
    "miami vice",
    "mobbed by raccoons",
    "light it up",
    "rewind",
    "dumb ways to die",
    "Winnie the Pooh",
    "You talk the talk do you walk the walk",
    "banana split",
    "pseudopseudohypoparathyroidism",
    "how to make sushi",
    "come clean",
    "what does idk mean",
    "is this the reebok or the nike",
    "limitless",
    "it works on my machine",
    "beyond imagination",
    "tea time",
]


async def main():
    config = Config()
    for service in config.services:
        async with aiohttp.ClientSession() as session:
            request_data = service.request_parser.prepare_request_data(
                keywords=keywords,
            )
            try:
                async with session.post(
                    url=service.url,
                    json=request_data,
                ) as response:
                    print(response.status)
            except InvalidURL as e:
                print(dict(
                    endpoint=service.endpoint,
                    url=service.url,
                    error=e,
                ))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
