from src.organizer import organize_files
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <folder_path>")
        exit()

    folder = sys.argv[1]
    print(organize_files(folder))
