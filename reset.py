import os
import json

def delete_folders():
    # List of folders to delete
    folders = ["facebook", "instagram", "youtube", "tiktok", "reddit", "twitter"]
    current_dir = os.getcwd()

    for folder in folders:
        folder_path = os.path.join(current_dir, folder)
        if os.path.exists(folder_path):
            try:
                # Remove the folder and its contents recursively
                os.system(f'rmdir /s /q "{folder_path}"')
                print(f"Deleted folder: {folder_path}")
            except OSError as e:
                print(f"Error deleting folder {folder}: {e}")
        else:
            print(f"Folder {folder} does not exist. Skipping deletion.")

def delete_tags_file():
    tags_file = "tags.json"
    if os.path.exists(tags_file):
        try:
            os.remove(tags_file)
            print(f"Deleted {tags_file}")
        except OSError as e:
            print(f"Error deleting {tags_file}: {e}")
    else:
        print(f"{tags_file} does not exist. Skipping deletion.")

if __name__ == "__main__":
    delete_folders()
    delete_tags_file()
    print("Folder reset completed successfully.")
