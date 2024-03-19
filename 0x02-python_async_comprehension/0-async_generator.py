#!/usr/bin/env python3
""" Asynchronous generator module """

import asyncio
import random

async def async_generator():
    """ Asynchronous generator """
    for _ in range(10):
        await asyncio.sleep(1)
        # Yield a random number between 0 and 10
        yield random.randint(0, 10)
