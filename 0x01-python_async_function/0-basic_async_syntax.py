#!/usr/bin/env python3
""" Module for wait_random async function"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ coroutine that takes in an integer argument """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
