#!/usr/bin/env python3
""" Asynchronous generator module """

import asyncio
import random
from typing import AsyncIterator


async def async_generator() -> AsyncIterator[int]:
    """ Asynchronous generator that yields random numbers """
    for _ in range(10):
        await asyncio.sleep(1)
        # Yield a random number between 0 and 10
        yield random.randint(0, 10)
