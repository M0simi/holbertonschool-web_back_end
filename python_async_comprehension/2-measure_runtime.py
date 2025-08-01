#!/usr/bin/env python3
"""Measure the runtime of running async_comprehension 4 times in parallel."""

import asyncio
import time
from typing import List

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Measure total time taken to run async_comprehension 4 times in parallel.

    Returns:
        float: total runtime in seconds.
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return end - start
