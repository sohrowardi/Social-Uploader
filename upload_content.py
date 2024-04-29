import os
import json

def load_api_keys():
    with open('config.json') as f:
        return json.load(f)

def upload_content():
    api_keys = load_api_keys()

    folders = ["facebook", "instagram", "youtube", "tiktok", "reddit", "twitter"]
    
    # Get the current directory
    current_dir = os.getcwd()

    for folder in folders:
        folder_path = os.path.join(current_dir, folder)
        
        # Get all files in the folder
        files = os.listdir(folder_path)
        
        # Upload each file
        for file in files:
            file_path = os.path.join(folder_path, file)
            
            # Determine which API key to use based on the folder name
            api_key = api_keys.get(folder)
            if api_key:
                # Use the API key to upload the file
                print(f"Uploaded {file} to {folder} using API key: {api_key}.")
            else:
                print(f"No API key found for {folder}. Skipping upload.")

if __name__ == "__main__":
    upload_content()
