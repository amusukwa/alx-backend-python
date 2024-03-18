#!/usr/bin/env python3
""" Module for meausure_time async function"""
import time
from typing import List
from asyncio import run


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measure the average execution time of wait_n """

    start_time = time.time()
    run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
