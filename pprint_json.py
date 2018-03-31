import json
import sys


def load_data(path):
    with open(path, "r") as file:
        return json.load(file)


def pretty_print_json(data):
    return json.dumps(data, indent=4, sort_keys=True)


if __name__ == '__main__':
    if ".json" in sys.argv[1]:
        file_path = sys.argv[1]
    else:
        file_path = input("Please, input correct file path: ")
    print(pretty_print_json(load_data(file_path)))
