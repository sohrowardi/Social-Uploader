import os
import json
import requests  # Import requests library for API key validation

def load_api_keys():
    try:
        with open('config.json') as f:
            return json.load(f)
    except FileNotFoundError:
        print("config.json file not found.")
        return {}

def load_tags():
    try:
        with open('tags.json') as f:
            return json.load(f)
    except FileNotFoundError:
        print("tags.json file not found.")
        return {}

def get_title_from_filename(filename):
    # Extract the title from the filename (remove the extension)
    return os.path.splitext(filename)[0]

def validate_api_key(api_key):
    # Example: Validate the API key by making a test request
    # Replace this with your actual API validation logic
    try:
        response = requests.get("https://api.example.com/validate", headers={"Authorization": api_key})
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error validating API key: {e}")
        return False

def upload_content():
    api_keys = load_api_keys()
    tags = load_tags()
    folders = ["facebook", "instagram", "youtube", "tiktok", "reddit", "twitter"]
    current_dir = os.getcwd()

    for folder in folders:
        folder_path = os.path.join(current_dir, folder)
        if os.path.exists(folder_path):
            files = os.listdir(folder_path)
            if files:
                for file in files:
                    file_path = os.path.join(folder_path, file)
                    api_key = api_keys.get(folder)
                    if api_key:
                        # Validate the API key
                        if validate_api_key(api_key):
                            # Get the title from the filename
                            title = get_title_from_filename(file)
                            # Get tags for the file
                            file_tags = tags.get(folder, {}).get(file, [])
                            print(f"Uploading {file} to {folder} with title: {title}, tags: {file_tags} using API key: {api_key}...")
                            # Simulate upload (replace with actual upload logic)
                            upload_successful = True  # Replace with your upload logic
                            if upload_successful:
                                print(f"Successfully uploaded {file} to {folder}.")
                            else:
                                print(f"Failed to upload {file} to {folder}.")
                                retry = input("Do you want to retry uploading this file? (yes/no): ")
                                if retry.lower() == "yes":
                                    # Retry upload logic here
                                    print(f"Retrying upload for {file}...")
                                else:
                                    print(f"Skipping upload for {file}.")
                        else:
                            print(f"Invalid API key for {folder}. Skipping upload.")
                    else:
                        print(f"No API key found for {folder}. Skipping upload.")
            else:
                print(f"No files found in {folder}. Skipping upload.")
        else:
            print(f"Folder {folder} does not exist. Skipping upload.")

if __name__ == "__main__":
    upload_content()
    input("Press Enter to exit...")  # Add this line to wait for user input