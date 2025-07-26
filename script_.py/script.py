import os
import shutil

# Define source and destination folders
source_folder = 'source_folder'
destination_folder = 'destination_folder'
# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Loop through all files in source
for filename in os.listdir(source_folder):
    if filename.lower().endswith('.jpg'):
        # Full path of source and destination
        src_path = os.path.join(source_folder, filename)
        dst_path = os.path.join(destination_folder, filename)

        # Move the file
        shutil.move(src_path, dst_path)
        print(f"Moved: {filename} - script.py:20")
