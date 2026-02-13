#!/usr/bin/python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    tree = ET.ElementTree(root)

    for key, value in dictionary.items():

        child = ET.SubElement(root, key)
        child.text = str(value)
    tree.write(filename)


def deserialize_from_xml(filename):
    my_dict = {}
    tree = ET.parse(filename)
    root = tree.getroot()
    for child in root:
        my_dict[child.tag] = child.text
    return my_dict


def main():
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)


if __name__ == "__main__":
    main()
