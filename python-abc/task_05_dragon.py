#!/usr/bin/python3
"""Module demonstrating mixins with a Dragon class."""


class SwimMixin:
    """A mixin that provides swimming capability."""

    def swim(self):
        """Make the creature swim."""
        print("The creature swims!")


class FlyMixin:
    """A mixin that provides flying capability."""

    def fly(self):
        """Make the creature fly."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon class that inherits from SwimMixin and FlyMixin."""

    def swim(self):
        """Make the dragon swim."""
        print("The creature swims!")

    def fly(self):
        """Make the dragon fly."""
        print("The creature flies!")

    def roar(self):
        """Make the dragon roar."""
        print("The dragon roars!")
