#!/usr/bin/python3
"""Module demonstrating multiple inheritance with Fish and Bird classes."""


class Fish:
    """A class representing a fish."""

    def swim(self):
        """Make the fish swim."""
        print("The fish is swimming")

    def habitat(self):
        """Describe the fish's habitat."""
        print("The fish lives in water")


class Bird:
    """A class representing a bird."""

    def fly(self):
        """Make the bird fly."""
        print("The bird is flying")

    def habitat(self):
        """Describe the bird's habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A flying fish class that inherits from Fish and Bird."""

    def fly(self):
        """Make the flying fish soar through the air."""
        print("The flying fish is soaring!")

    def swim(self):
        """Make the flying fish swim in the water."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Describe the flying fish's habitat in both water and sky."""
        print("The flying fish lives both in water and the sky!")
