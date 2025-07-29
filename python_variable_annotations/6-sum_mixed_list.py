#!/usr/bin/env python3
"""
Module: 5-sum_mixed_list

This module contains a function that takes a list of integers and floats,
and returns the sum of all elements as a float.

It uses Python type annotations for clarity and static analysis support.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list of integers and floats, and returns their sum as a float.

    Args:
        mxd_lst (List[Union[int, float]]): A list of numbers (int and/or float)

    Returns:
        float: The sum of the numbers
    """
    return sum(mxd_lst)
