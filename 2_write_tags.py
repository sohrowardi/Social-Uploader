import os
import json
import subprocess

def write_tags():
    folders = ["facebook", "instagram", "youtube", "tiktok", "reddit", "twitter"]
    current_dir = os.getcwd()
    tags = {}

    # Iterate through each folder
    for folder in folders:
        folder_path = os.path.join(current_dir, folder)
        
        # Check if the folder exists
        if os.path.exists(folder_path):
            files = os.listdir(folder_path)
            
            # Iterate through each file in the folder
            for file in files:
                file_path = os.path.join(folder_path, file)
                
                # Extract the filename (without extension) as the default title
                title = os.path.splitext(file)[0]
                
                # If the folder is not already in the tags dictionary, add it
                if folder not in tags:
                    tags[folder] = {}
                
                # Add the file to the tags dictionary for the corresponding folder
                tags[folder][file] = {"title": title, "tags": []}

    # Write the tags dictionary to a JSON file
    with open('tags.json', 'w') as json_file:
        json.dump(tags, json_file, indent=4)

    # Open the tags.json file
    try:
        if os.name == 'nt':  # Check if the OS is Windows
            os.startfile('tags.json')
        else:
            subprocess.run(['xdg-open', 'tags.json'])  # Open the file with the default application on Linux
    except Exception as e:
        print(f"Error opening file: {e}")

if __name__ == "__main__":
    write_tags()
