#!/usr/bin/env python3
""" Module for meausure_time async function"""
import asyncio
from asyncio.tasks import Task
from asyncio import run


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """ Function returns task"""
    coroutine = wait_random(max_delay)
    task = asyncio.create_task(coroutine)
    return task
