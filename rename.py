import os
import json
import random
import string

def generate_random_filename(extension):
    random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return f"{random_name}.{extension}"

def rename_icons_and_update_json(json_file_path):
    with open(json_file_path, 'r') as f:
        data = json.load(f)

    icon_directory = './icons/'

    for entry in data:
        if 'image' in entry:
            old_image_path = entry['image']
            old_image_name = os.path.basename(old_image_path)
            
            extension = old_image_name.split('.')[-1]
            
            new_image_name = generate_random_filename(extension)
            
            old_image_full_path = os.path.join(icon_directory, old_image_name)
            new_image_full_path = os.path.join(icon_directory, new_image_name)
            
            if os.path.exists(old_image_full_path):
                os.rename(old_image_full_path, new_image_full_path)
                entry['image'] = f"/icons/{new_image_name}"

    with open(json_file_path, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"Icons renamed and {json_file_path} updated successfully!")

json_files = ['./json/apps.json', './json/games.json']

for json_file in json_files:
    rename_icons_and_update_json(json_file)
