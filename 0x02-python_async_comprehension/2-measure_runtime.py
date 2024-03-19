#!/usr/bin/env python3
""" Measure total runtime of executing async_comprehension module"""
import asyncio
from typing import List
from time import perf_counter


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measure the total runtime of executing async_comprehension  """
    start_time = perf_counter()

    # Execute async_comprehension four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    total_time = perf_counter() - start_time
    return total_time
