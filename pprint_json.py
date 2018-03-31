import json
import sys


def load_data(path):
    with open(path, "r") as file:
        return json.load(file)


def pretty_json(json_loading_data):
    return json.dumps(json_loading_data, ensure_ascii=False, indent=4, sort_keys=True)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("No file or directory")
    else:
        try:
            print(pretty_json(load_data(sys.argv[1])))
        except (IOError, Exception) as e:
            print(e)

