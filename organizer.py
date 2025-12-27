import os
import shutil

# 1. Define the folder you want to organize (e.g., your Downloads)
# TIP: For testing, create a folder named 'TestFolder' so you don't mess up real files!
TARGET_DIR = "./TestFolder" 

# 2. Define categories and their extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".7z"]
}

def organize_files():
    if not os.path.exists(TARGET_DIR):
        print(f"Directory {TARGET_DIR} not found.")
        return

    for filename in os.listdir(TARGET_DIR):
        filepath = os.path.join(TARGET_DIR, filename)

        # Skip if it's a folder, we only want files
        if os.path.isdir(filepath):
            continue

        # Get the file extension
        _, extension = os.path.splitext(filename)
        
        moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if extension.lower() in extensions:
                category_path = os.path.join(TARGET_DIR, category)
                
                # Create category folder if it doesn't exist
                os.makedirs(category_path, exist_ok=True)
                
                # Move the file
                shutil.move(filepath, os.path.join(category_path, filename))
                print(f"Moved: {filename} -> {category}")
                moved = True
                break
        
        if not moved:
            print(f"Skipped (No category): {filename}")

if __name__ == "__main__":
    organize_files()