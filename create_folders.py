import os

def create_folders():
    folders = ["facebook", "instagram", "youtube", "tiktok", "reddit", "twitter"]
    current_dir = os.getcwd()

    for folder in folders:
        folder_path = os.path.join(current_dir, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created folder: {folder_path}")

if __name__ == "__main__":
    create_folders()
