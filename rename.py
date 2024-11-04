import os
import json
import random
import string

def generate_random_filename(extension, length=10):
    length = max(10, min(length, 40))
    random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return f"{random_name}.{extension}"

def preload_name_map(json_files, name_map):
    for json_file in json_files:
        with open(json_file, 'r') as f:
            data = json.load(f)
            for entry in data:
                if 'image' in entry:
                    old_image_name = os.path.basename(entry['image'])
                    if old_image_name not in name_map:
                        name_map[old_image_name] = None  

def rename_icons_and_update_json(json_file_path, name_map, icon_directory):
    with open(json_file_path, 'r') as f:
        data = json.load(f)

    for entry in data:
        if 'image' in entry:
            old_image_path = entry['image']
            old_image_name = os.path.basename(old_image_path)

            if name_map[old_image_name] is None:
                extension = old_image_name.split('.')[-1]
                new_image_name = generate_random_filename(extension, random.randint(10, 40))
                old_image_full_path = os.path.join(icon_directory, old_image_name)
                new_image_full_path = os.path.join(icon_directory, new_image_name)

                if os.path.exists(old_image_full_path):
                    os.rename(old_image_full_path, new_image_full_path)
                    name_map[old_image_name] = new_image_name  

            entry['image'] = f"/icons/{name_map[old_image_name]}"

    with open(json_file_path, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"Icons renamed and {json_file_path} updated successfully!")

name_map = {}
icon_directory = './icons/'

json_files = ['./json/apps.json', './json/games.json']

preload_name_map(json_files, name_map)

for json_file in json_files:
    rename_icons_and_update_json(json_file, name_map, icon_directory)
