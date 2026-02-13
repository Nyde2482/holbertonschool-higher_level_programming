#!/usr/bin/python3
import pickle


class CustomObject:
    """A custom object class that can be serialized and deserialized using pickle."""

    def __init__(self, name="", age=0, is_student=False):
        """Initialize a CustomObject instance.

        Args:
            name (str): The name of the person. Defaults to "".
            age (int): The age of the person. Defaults to 0.
            is_student (bool): Whether the person is a student. Defaults to False.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes in a formatted way."""
        print("Name: {}\nAge: {}\nIs Student: {}".format(
            self.name, self.age, self.is_student))

    def serialize(self, filename):
        """Serialize the object and save it to a file.

        Args:
            filename (str): The name of the file to save the serialized object to.
        """

        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file.

        Args:
            filename (str): The name of the file to load the serialized object from.

        Returns:
            CustomObject: The deserialized object instance.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
