import os
import json

def process_json_files(input_folder, output_file):
    # List to hold the processed data
    output_data = []
    
    # Loop through each folder (representing a username) in the main directory
    for username_folder in os.listdir(input_folder):
        username_folder_path = os.path.join(input_folder, username_folder)
        
        # Check if it is a directory (username folder)
        if os.path.isdir(username_folder_path):
            print(f"Processing folder: {username_folder_path}")
            
            # Loop through each JSON file in the username folder
            for filename in os.listdir(username_folder_path):
                if filename.endswith('.json'):
                    file_path = os.path.join(username_folder_path, filename)
                    print(f"Processing file: {file_path}")
                    
                    # Read the JSON file
                    try:
                        with open(file_path, 'r') as f:
                            data = json.load(f)
                    except Exception as e:
                        print(f"Error reading {file_path}: {e}")
                        continue
                    
                    # Extract the card names from the "mainboard" section
                    card_names = [item['name'] for item in data.get('mainboard', [])]
                    
                    # Check if the file has valid card names
                    if card_names:
                        # Get the username (folder name)
                        username = username_folder
                        
                        # Create a dictionary for the output
                        file_id = os.path.splitext(filename)[0]  # Use the file name (without extension) as ID
                        output_data.append({
                            "id": file_id,
                            "username": username,
                            "cardNames": card_names
                        })
                    else:
                        print(f"No card names found in {file_path}")
    
    # Check if output_data has been populated
    if output_data:
        # Write the result to the output file
        with open(output_file, 'w') as f:
            json.dump(output_data, f, indent=4)
        print(f"Output written to {output_file}")
    else:
        print("No data to write.")


# Example usage:
input_folder = 'my_data'  # Folder containing the JSON files
output_file = 'output.json'  # Path to the output file
process_json_files(input_folder, output_file)