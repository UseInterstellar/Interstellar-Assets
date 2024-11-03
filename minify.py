import json
import os

def minimize_json(json_file_path):
    with open(json_file_path, 'r') as f:
        data = json.load(f)

    minimized_file_name = os.path.splitext(json_file_path)[0] + '.min.json'

    with open(minimized_file_name, 'w') as f:
        json.dump(data, f, separators=(',', ':'), ensure_ascii=False)

    print(f"Minimized {json_file_path} to {minimized_file_name} successfully!")

json_files = ['./json/apps.json', './json/games.json']

for json_file in json_files:
    minimize_json(json_file)
