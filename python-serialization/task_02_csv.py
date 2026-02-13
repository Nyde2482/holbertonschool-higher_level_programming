#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(filename):
    try:
        with open(filename, "r") as csv_file:
            dict_covert = list(csv.DictReader(csv_file))
        with open("data.json", "w+") as file:
            json.dump(dict_covert, file)
        return True
    except FileNotFoundError:
        return False
