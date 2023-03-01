import json
import pathlib
import os
BASE_DIR = pathlib.Path(__file__).parent.resolve()
FILES_DIR = f"{BASE_DIR}/files"

python_data = {
    "user": {
        "name": " kamil",
        "age": 43,
        "Place": "Ethiopia",
        "gender": "male"
    }
}
# saving Python dictionary object to JSON file
with open(f"{FILES_DIR}/json_data.json", "w") as file_stream:
    json.dump(python_data, file_stream)
    file_stream.write('\n')