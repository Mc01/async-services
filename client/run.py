import aiohttp
import asyncio

from aiohttp import InvalidURL, ContentTypeError

from config import Config
from services import Service


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


def validate_status(status: int, service: Service):
    assert status == 200, f"Invalid response of service {service.name}: {status}"


async def main():
    config = Config()
    responses = {}

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
                    validate_status(
                        status=response.status,
                        service=service,
                    )
                    response_json = await response.json()
            except InvalidURL as e:
                raise Exception(dict(
                    endpoint=service.endpoint,
                    url=service.url,
                    error=e,
                ))

            responses[service.name] = service.request_parser.parse_response_data(
                response_data=response_json,
            )

    for service_name, service_response in responses.items():
        for keyword, results in service_response.items():
            print(f'Service {service_name} Keyword {keyword}: {results}')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
