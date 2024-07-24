import os
import json
from pprint import pprint

def get_unique_filepaths(json_folder):
    filepaths = set()

    for filename in os.listdir(json_folder):
        if filename.endswith('.json'):
            filepath = os.path.join(json_folder, filename)
            with open(filepath) as file:
                data = json.load(file)
                for item in data:
                    filepaths.add(item['file_path'])
                    
    

    return filepaths

json_folder = './json'
unique_filepaths = get_unique_filepaths(json_folder)
pprint(unique_filepaths)
unique_filepaths_count = len(unique_filepaths)
print(f"Number of unique filepaths: {unique_filepaths_count}")