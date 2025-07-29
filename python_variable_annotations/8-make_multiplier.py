#!/usr/bin/env python3
"""
Module: 8-make_multiplier

Defines a function that returns a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The number to multiply by.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the result of multiplying it by `multiplier`.

    Example:
        >>> doubler = make_multiplier(2.0)
        >>> doubler(5.0)
        10.0
    """
    return lambda x: x * multiplier
