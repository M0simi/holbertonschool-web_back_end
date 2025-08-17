#!/usr/bin/env python3
"""
Module: 2-hypermedia_pagination
This module provides a Server class to paginate a CSV file
and return data with hypermedia-style pagination metadata.
"""

import csv
import math
from typing import List


def index_range(page, page_size):
    """
    Calculate start and end indexes for a given page.

    Args:
        page (int): current page number (1-indexed).
        page_size (int): number of items per page.

    Returns:
        tuple: (start_index, end_index) for slicing.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the server with no dataset loaded."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Load and cache the dataset from the CSV file.

        Returns:
            List[List]: The dataset without the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return one page of the dataset.

        Args:
            page (int): page number (must be > 0).
            page_size (int): number of items per page (must be > 0).

        Returns:
            List[List]: rows for the requested page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Return a dictionary with pagination info and data.

        Args:
            page (int): page number.
            page_size (int): number of items per page.

        Returns:
            dict: contains page_size, page, data, next_page,
                  prev_page, total_pages.
        """
        data = self.get_page(page, page_size)
        dataset_length = len(self.dataset())
        total_pages = math.ceil(dataset_length / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }
