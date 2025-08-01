#!/usr/bin/env python3
"""This module defines an asynchronous coroutine that collects 10 random
numbers using an async comprehension."""


from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers from async_generator.

    Returns:
        List[float]: A list containing 10 random float numbers.
    """
    return [num async for num in async_generator()]
