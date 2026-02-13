#!/usr/bin/python3
import json

def serialize_and_save_to_file(data, filename):
    """Serialize data to JSON and save it to a file.

    Args:
        data: The data to serialize (must be JSON serializable).
        filename (str): The name of the file to save the serialized data to.
    """
    with open(filename, "w") as file:
        serialize_data = json.dumps(data)
        file.write(serialize_data)


def load_and_deserialize(filename):
    """Load and deserialize data from a JSON file.

    Args:
        filename (str): The name of the file to load the data from.

    Returns:
        The deserialized data.
    """
    with open(filename, "r") as file:
        data = file.read()
        return json.loads(data)
