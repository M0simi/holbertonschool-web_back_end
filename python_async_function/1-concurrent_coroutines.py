#!/usr/bin/env python3
"""Asynchronous coroutine that runs multiple wait_random coroutines
concurrently"""

import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run wait_random n times concurrently with max_delay as maximum delay.

    Args:
        n (int): The number of times to run wait_random.
        max_delay (int): The maximum possible delay.

    Returns:
        List[float]: A list of all delays in ascending order.
    """
    delays = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
