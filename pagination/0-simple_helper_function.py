#!/usr/bin/env python3

"""
Module: 0-simple_helper_function
This module provides a simple helper function for pagination.
"""


def index_range(page, page_size):
    """
    Calculate the start and end indexes for a given pagination setup.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing two integers:
            - start_index (int): The starting index of the items for the page.
            - end_index (int): The ending index (exclusive) of the items
            for the page.

    Example:
        >>> index_range(1, 7)
        (0, 7)
        >>> index_range(3, 15)
        (30, 45)
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
