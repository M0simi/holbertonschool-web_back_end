#!/usr/bin/env python3
"""
Module: 0-basic_async_syntax
This module contains a single coroutine called `wait_random`.
It demonstrates the basics of asynchronous programming in Python
by using async/await along with a random delay.
"""


import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
     """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int, optional): The maximum number of seconds to wait. Default is 10.

    Returns:
        float: The actual delay time (in seconds) that was waited before returning.
    """
    delay = random.uniform(0, max_delay) # chose random number between 0 and max_delay
    await asyncio.sleep(delay)  # waiting random time
    return delay
