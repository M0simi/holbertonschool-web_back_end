#!/usr/bin/env python3
"""
Module: 9-element_length

Defines a function that takes an iterable of sequences and returns
a list of tuples with each element and its length.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples with each element and its length.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequence-type elements
                                  (like strings, lists, tuples...).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
                                    the original element and its length.

    Example:
        >>> element_length(["apple", [1, 2], (9, 8)])
        [('apple', 5), ([1, 2], 2), ((9, 8), 2)]
    """
    return [(i, len(i)) for i in lst]
