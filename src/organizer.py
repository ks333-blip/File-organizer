import os
import shutil

# map file extensions to folder names
FILE_TYPES = {
    "images": [".png", ".jpg", ".jpeg", ".gif"],
    "documents": [".pdf", ".docx", ".txt", ".csv"],
    "videos": [".mp4", ".mov", ".avi"],
    "audio": [".mp3", ".wav"],
    "code": [".py", ".js", ".html", ".css"],
}

def organize_files(folder_path):

    # get list of all files in the folder
    for filename in os.listdir(folder_path):
        src_path = os.path.join(folder_path, filename)

        # skip folders
        if os.path.isdir(src_path):
            continue

        # get file extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        # find matching category
        target_folder = None
        for category, extensions in FILE_TYPES.items():
            if ext in extensions:
                target_folder = category
                break

        # if unknown file type → put in "others"
        if target_folder is None:
            target_folder = "others"

        # create folder if missing
        dest_folder = os.path.join(folder_path, target_folder)
        os.makedirs(dest_folder, exist_ok=True)

        # move file
        shutil.move(src_path, os.path.join(dest_folder, filename))

    return "Files organized successfully!"
