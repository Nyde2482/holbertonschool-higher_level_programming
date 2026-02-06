#!/usr/bin/python3
"""Module containing an iterator that counts iterations."""


class CountedIterator:
    """An iterator that keeps track of the number of items iterated over."""

    def __init__(self, iterable):
        """Initialize the CountedIterator with an iterable.

        Args:
            iterable: Any iterable object to iterate over.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return the iterator object itself.

        Returns:
            self: The iterator object.
        """
        return self

    def __next__(self):
        """Return the next item from the iterator and increment the count.

        Returns:
            The next item from the iterable.

        Raises:
            StopIteration: When there are no more items to iterate.
        """
        item = next(self.iterator)
        self.count += 1
        if item > 0:
            return item
        else:
            raise StopIteration

    def get_count(self):
        """Get the number of items that have been iterated over.

        Returns:
            int: The count of items iterated.
        """
        return self.count
