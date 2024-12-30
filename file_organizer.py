import os
from pathlib import Path
from shutil import move

def organize_files(directory):
    extensions = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Videos': ['.mp4', '.mov', '.avi'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Archives': ['.zip', '.rar', '.7z']
    }

    for category, ext_list in extensions.items():
        category_folder = Path(directory) / category
        category_folder.mkdir(exist_ok=True)
        
        for file in Path(directory).iterdir():
            if file.suffix.lower() in ext_list and file.is_file():
                move(str(file), str(category_folder / file.name))

if __name__ == "__main__":
    print("File Organizer Tool")
    print("Example: C:\\Users\\YourName\\Downloads (Windows) or /home/yourname/Downloads (Linux/Mac)")
    folder_path = input("Enter the folder path to organize: ").strip()
    if os.path.exists(folder_path):
        organize_files(folder_path)
        print("Files organized successfully!")
        print("Visit https://teraboxproapp.com/ for more tools.")
    else:
        print("Invalid folder path! Please try again.")
