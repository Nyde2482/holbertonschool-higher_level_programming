#!/usr/bin/python3
"""Module that defines a Student class."""


class Student:
    """Represent a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list): List of attribute names to retrieve (optional).

        Returns:
            dict: Dictionary containing requested or all attributes.
        """
        if attrs is None:
            return self.__dict__
        if isinstance(attrs, list) and \
                all(isinstance(element, str) for element in attrs):
            result = {
                key: value for key, value in self.__dict__.items()
                if key in attrs
            }
            return result
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance.

        Args:
            json (dict): Dictionary of attributes to update.

        Returns:
            None
        """
        self.__dict__.update(json)
