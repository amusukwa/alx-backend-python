#!/usr/bin/env python3
""" Asynchronous generator module """
import asyncio
import random
from typing import List


async def async_generator():
    """ Asynchronous generator """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def async_comprehension() -> List[float]:
    """ Asynchronous comprehension to collect 10 random numbers """
    random_numbers = [random_number async for random_number in async_generator()]
    return random_numbers
