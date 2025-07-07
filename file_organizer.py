import os
import shutil

# Define your source directory (change to your Downloads or Desktop folder if needed)
SOURCE_DIR = os.path.expanduser("~/Downloads")

# Define destination folders for each type
DESTINATIONS = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.pptx', '.xlsx'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Code': ['.py', '.js', '.html', '.css', '.cpp', '.java']
}

def organize_files():
    print(f"📂 Organizing files in: {SOURCE_DIR}")
    
    for filename in os.listdir(SOURCE_DIR):
        file_path = os.path.join(SOURCE_DIR, filename)

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()

            moved = False
            for folder_name, extensions in DESTINATIONS.items():
                if file_ext in extensions:
                    dest_folder = os.path.join(SOURCE_DIR, folder_name)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    print(f"Moved: {filename} → {folder_name}")
                    moved = True
                    break

            if not moved:
                print(f"Skipped (Unknown type): {filename}")

if __name__ == "__main__":
    organize_files()
