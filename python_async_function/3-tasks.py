#!/usr/bin/env python3
"""Return asyncio.Task for wait_random"""

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task for wait_random with max_delay.

    Args:
        max_delay (int): The maximum delay to wait.

    Returns:
        asyncio.Task: A Task object wrapping wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
