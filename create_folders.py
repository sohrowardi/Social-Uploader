import os

def create_folders():
    folders = ["facebook", "instagram", "youtube", "tiktok", "reddit", "twitter"]
    
    # Get the current directory
    current_dir = os.getcwd()

    # Create folders if they don't exist
    for folder in folders:
        folder_path = os.path.join(current_dir, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")

if __name__ == "__main__":
    create_folders()
