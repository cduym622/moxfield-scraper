import os

def count_files_in_subfolders(folder_path):
    # Dictionary to store subfolder names and their respective file counts
    folder_file_count = {}
    total_file_count = 0  # Initialize a counter for the total number of files

    # Loop through each subfolder in the provided folder
    for subfolder in os.listdir(folder_path):
        subfolder_path = os.path.join(folder_path, subfolder)

        # Check if it is a folder
        if os.path.isdir(subfolder_path):
            # Count the number of files in the subfolder
            file_count = sum([1 for f in os.listdir(subfolder_path) if os.path.isfile(os.path.join(subfolder_path, f))])
            folder_file_count[subfolder] = file_count
            total_file_count += file_count  # Add to total count

    # Print the total number of files first
    print(f"Total number of files across all subfolders: {total_file_count}")

    # Sort the subfolders by file count in ascending order
    sorted_folders = sorted(folder_file_count.items(), key=lambda x: x[1])

    # Print the folder name and file count
    for folder, count in sorted_folders:
        print(f"Folder: {folder}, Number of files: {count}")

# Replace 'your_folder_path' with the path to your folder
folder_path = "my_data"
count_files_in_subfolders(folder_path)