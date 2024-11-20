import os
import shutil

# Define the source folder name
source_folder_name = "Manzanasf"

# Define the new folder name
new_folder_name = "Manzanasf_renamed"

# Get the current directory (where the script is located)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the paths for the source and destination folders
source_folder_path = os.path.join(current_dir, source_folder_name)
new_folder_path = os.path.join(current_dir, new_folder_name)

# Check if the source folder exists
if not os.path.exists(source_folder_path):
    print(f"The folder '{source_folder_name}' does not exist in the current directory.")
    exit()

# Create the new folder if it doesn't exist
os.makedirs(new_folder_path, exist_ok=True)

# Iterate over each file in the source folder
for filename in os.listdir(source_folder_path):
    # Get the full path of the source file
    source_file_path = os.path.join(source_folder_path, filename)

    # Ensure it's a file (not a folder)
    if os.path.isfile(source_file_path):
        # Split the filename and extension
        name, ext = os.path.splitext(filename)

        # Create the new filename
        new_name = f"{name}_{ext}"

        # Define the path for the new file in the destination folder
        new_file_path = os.path.join(new_folder_path, new_name)

        # Copy the file to the new folder with the new name
        shutil.copy2(source_file_path, new_file_path)
        print(f"Copied and renamed: {filename} -> {new_name}")

print(f"All files have been renamed and saved in the '{new_folder_name}' folder.")
