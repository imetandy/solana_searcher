import os
import json
from pprint import pprint

def get_unique_filepaths(json_folder):
    filepaths = set()

    for filename in os.listdir(json_folder):
        # check if the file is a json file
        if filename.endswith('.json'):
            filepath = os.path.join(json_folder, filename)
            # open the json file
            with open(filepath) as file:
                data = json.load(file)
                # iterate over the items in the json file
                for item in data:
                    filepaths.add(item['file_path'])
                    
    return filepaths

json_folder = './json'
# print the filepaths
unique_filepaths = get_unique_filepaths(json_folder)
pprint(unique_filepaths)
#print number of unique filepaths
unique_filepaths_count = len(unique_filepaths)
print(f"Number of unique filepaths: {unique_filepaths_count}")