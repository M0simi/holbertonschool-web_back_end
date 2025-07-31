#!/usr/bin/env python3
"""Measure the runtime of wait_n"""

import time
import asyncio
from typing import Callable

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time for wait_n.

    Args:
        n (int): Number of tasks to run.
        max_delay (int): Maximum delay for each task.

    Returns:
        float: The average time per task (total_time / n)
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n
