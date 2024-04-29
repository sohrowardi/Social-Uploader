import os
import json

def load_api_keys():
    try:
        with open('config.json') as f:
            return json.load(f)
    except FileNotFoundError:
        print("config.json file not found.")
        return {}

def upload_content():
    api_keys = load_api_keys()
    folders = ["facebook", "instagram", "youtube", "tiktok", "reddit", "twitter"]
    current_dir = os.getcwd()

    for folder in folders:
        folder_path = os.path.join(current_dir, folder)
        if os.path.exists(folder_path):
            files = os.listdir(folder_path)
            for file in files:
                file_path = os.path.join(folder_path, file)
                api_key = api_keys.get(folder)
                if api_key:
                    print(f"Uploaded {file} to {folder} using API key: {api_key}.")
                else:
                    print(f"No API key found for {folder}. Skipping upload.")
        else:
            print(f"Folder {folder} does not exist. Skipping upload.")

if __name__ == "__main__":
    upload_content()
