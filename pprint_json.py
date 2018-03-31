import json
import sys


def load_data(path):
    with open(path, "r") as file:
        return json.load(file)


def make_pretty_json(json_content):
    return json.dumps(json_content, ensure_ascii=False, indent=4, sort_keys=True)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        exit("Need input file path as parameter")
    try:
        print(make_pretty_json(load_data(sys.argv[1])))
    except (FileNotFoundError):
        print("File not found")
