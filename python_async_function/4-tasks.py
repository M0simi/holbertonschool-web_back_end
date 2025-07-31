#!/usr/bin/env python3
"""Run task_wait_random n times concurrently and return the results"""

import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run task_wait_random n times with the given max_delay.

    Args:
        n (int): Number of tasks to run.
        max_delay (int): Maximum delay for each task.

    Returns:
        List[float]: List of delays in ascending order of completion.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
