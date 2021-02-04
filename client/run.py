import random
import time
from collections import defaultdict
from decimal import Decimal

import aiohttp
import asyncio

from aiohttp import InvalidURL

from config import Config
from config.keywords import keywords
from integrations import Service


def validate_status(status: int, service: Service):
    assert status == 200, f"Invalid response of service {service.name}: {status}"


async def main():
    config = Config()
    sampled_keywords = random.sample(keywords, config.sample_size)

    times = defaultdict(lambda: defaultdict(dict))
    responses = defaultdict(dict)

    print('***  Config  ***\n')
    print(f'  Services: {config.run_services}')
    print(f'  Async mode in services: {config.async_services}')
    print(f'  Keywords sample: {config.sample_size}')
    print(f'  Attempts: {config.attempts}')
    print('---  ---  ---\n')

    for service in config.active_services:
        for attempt in range(config.attempts):
            async with aiohttp.ClientSession() as session:
                request_data = service.request_parser.prepare_request_data(
                    keywords=sampled_keywords,
                )

                times[service.name][attempt]['request_time'] = Decimal(str(time.time()))

                try:
                    async with session.post(
                        url=service.url,
                        json=request_data,
                    ) as response:
                        times[service.name][attempt]['response_time'] = Decimal(str(time.time()))
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

                responses[service.name][attempt] = service.request_parser.parse_response_data(
                    response_data=response_json,
                )

    print('***  Results  ***\n')

    for service_name, attempted_responses in responses.items():
        print(f'>>>  Service {service_name} <<<')
        for attempt, response in attempted_responses.items():
            for keyword, results in response.items():
                print(f'  Attempt {attempt} - Keyword {keyword}: {results}')

        print('---  ---  ---\n')

    print('***  Times  ***\n')

    for service_name, attempted_times in times.items():
        print(f'>>>  Service {service_name} <<<')
        running_times = []

        for attempt, times in attempted_times.items():
            running_time = times["response_time"] - times["request_time"]
            running_times.append(running_time)
            print(f'  Attempt {attempt} - Time {running_time}')

        min_val = min(running_times)
        avg_val = round(sum(running_times) / len(running_times), 7)
        max_val = max(running_times)

        print(f'  :::  Min {min_val} Avg {avg_val} Max {max_val}')
        print('---  ---  ---\n')

    print('***  ***  ***')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
