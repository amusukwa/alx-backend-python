#!/usr/bin/env python3
import asyncio
from typing import List
from random import uniform

async def wait_random(max_delay: int = 10) -> float:
    """ Coroutine that waits for a random delay """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Coroutine that spawns wait_random n times with max_delay """
    # Create a list to store the results
    results = []
    for _ in range(n):
        result = await wait_random(max_delay)
        results.append(result)
    return sorted(results)

