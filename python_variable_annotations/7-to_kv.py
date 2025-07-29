#!/usr/bin/env python3
"""
Module: 7-to_kv

This module defines a function `to_kv` that returns a tuple containing:
a string and the square of a numeric value (int or float), returned as a float.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple where the first element is the input string,
    and the second is the square of the input number as a float.

    Args:
        k (str): A string value (e.g., a key).
        v (Union[int, float]): A numeric value to be squared.

    Returns:
        Tuple[str, float]: A tuple with the string and the square of the
        number.
    """
    return (k, float(v**2))
