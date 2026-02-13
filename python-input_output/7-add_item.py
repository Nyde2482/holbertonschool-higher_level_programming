#!/usr/bin/python3
"""
Script that adds all command line arguments to a Python list,
and saves this list to a JSON file ('add_item.json').
"""
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
args = sys.argv[1:]

try:
    item = load_from_json_file(filename)
except Exception:
    item = []

item.extend(args)
save_to_json_file(item, filename)
