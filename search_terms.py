import os
import json

def search_strings_in_files(root_dir, search_strings, file_extensions):
    matching_files = {search_str: [] for search_str in search_strings}

    # Walk through all directories and files in the root directory
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            # Check if the file has one of the specified extensions
            if any(file.endswith(ext) for ext in file_extensions):
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        
                        # Initialize a dictionary for storing matches
                        matches = {search_str: [] for search_str in search_strings}
                        
                        for i, line in enumerate(lines, start=1):
                            for search_str in search_strings:
                                if search_str in line:
                                    matches[search_str].append({
                                        'line_number': i,
                                        'line_content': line.strip()
                                    })
                                    
                        # Add matches to the corresponding search string's list
                        for search_str, occurrences in matches.items():
                            if occurrences:
                                matching_files[search_str].append({
                                    'file_path': file_path,
                                    'matches': occurrences
                                })
                except Exception as e:
                    print(f"Could not read file {file_path} due to {e}")

    return matching_files

def save_results_to_json(matching_files, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for search_str, files in matching_files.items():
        # Sanitize the search string to be a valid filename
        sanitized_search_str = search_str.replace('/', '_').replace('\\', '_')
        output_file = os.path.join(output_dir, f"{sanitized_search_str}.json")
        
        # Write the results to a JSON file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(files, f, indent=4)

# Example usage
root_directory = '/Users/andrew/Documents/projects/solana'
search_strs = ['ed25519-dalek', 'curve25519-dalek', 'bip32', 'secp256k1', 'hmac', 'sha2', 'sha3', 'siphasher', 'blake3', 'FnvHasher', 'tls']  # Specify the search strings
file_types = ['.txt', '.rs', '.toml']  # Specify the file types you want to search in
output_directory = '/Users/andrew/Documents/projects/solana_searcher/json'  # Writable directory for output

matching_files = search_strings_in_files(root_directory, search_strs, file_types)
save_results_to_json(matching_files, output_directory)