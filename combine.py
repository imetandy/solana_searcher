# importing packages
import pandas as pd
import os
 

# get the list of files in the json folder
json_folder = './json'
json_files = os.listdir(json_folder)

# initialize an empty list to store the dataframes
dfs = []

# iterate over each file in the json folder
for file in json_files:
    # construct the file path
    file_path = os.path.join(json_folder, file)
    
    # read the json file and append the dataframe to the list
    df = pd.read_json(file_path)
    dfs.append(df)

# concatenate all the dataframes in the list
df = pd.concat(dfs)

# view the concatenated dataframe
df.to_csv('data.csv')
