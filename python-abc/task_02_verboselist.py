#!/usr/bin/python3
"""Module containing a verbose list class."""


class VerboseList(list):
    """A list subclass that prints a message for each modification."""

    def append(self, object):
        """Add an item to the end of the list and print a notification.

        Args:
            object: The item to append to the list.
        """
        print(f"Added [{object}] to the list.")
        return super().append(object)

    def extend(self, iterable):
        """Extend the list with item from an iterable and print a notification.

        Args:
            iterable: An iterable containing items to add to the list.
        """
        items = list(iterable)
        print(f"Extended the list with [{len(items)}] items.")
        return super().extend(items)

    def remove(self, value):
        """Remove the first occurrence of a value and print a notification.

        Args:
            value: The value to remove from the list.
        """
        print(f"Removed [{value}] from the list.")
        return super().remove(value)

    def pop(self, index=-1):
        """Remove and return an item at the given index with a notification.

        Args:
            index: The index of the item to remove (default: -1, last item).

        Returns:
            The removed item.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
