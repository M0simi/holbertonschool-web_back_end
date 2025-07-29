#!/usr/bin/env python3
"""
Module: 5-sum_list

This module defines a function `sum_list` that calculates
the sum of a list of floats.
Type annotations are used to clarify the expected input and output types.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of float numbers.

    Args:
        input_list (List[float]): A list containing float numbers to be summed.

    Returns:
        float: The sum of all the float numbers in the list.

    Example:
        >>> sum_list([1.1, 2.2, 3.3])
        6.6
    """
    return sum(input_list)
