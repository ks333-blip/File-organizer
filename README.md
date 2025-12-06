# 📁 File Organizer (Python Automation Project)

A simple and powerful Python automation tool that automatically organizes files in a folder based on their file types.  
Perfect for beginners learning Python, file handling, and automation logic.

This tool sorts files into categories like **Images, Documents, Videos, Audio, Code, Others**, and makes your messy folders clean and structured.

---

## 🌟 Features

✔ Automatically detects file types  
✔ Moves files into categorized folders  
✔ Creates missing folders automatically  
✔ Supports Images, Documents, Videos, Audio, Code files  
✔ Handles unknown file types using "others" folder  
✔ Works on Windows, Mac, and Linux  
✔ Beginner-friendly Python code (no external libraries)

---

## 📂 Project Structure

file-organizer/
│── main.py
│── src/
│ └── organizer.py
│── data/
│ └── messy_folder/
│── README.md
│── .gitignore


---

---

## 🛠️ How It Works

1. You pass a folder path to the script.
2. The script scans all files in that folder.
3. Based on file extensions, it moves them into:
   - `images/`
   - `documents/`
   - `videos/`
   - `audio/`
   - `code/`
   - `others/`
4. It creates missing folders automatically.

---

## ▶️ Usage

### Step 1 — Put your messy files in:

### Step 2 — Run the script:
```bash
python main.py data/messy_folder
 
 output  Files organized successfully!

data/messy_folder/
    images/
    documents/
    videos/
    audio/
    code/
    others/
  🧠 Technologies Used

Python 3

os module

shutil module

🎯 Why This Project is Important

This is one of the best beginner projects for:

Learning file automation

Building a Data Engineering mindset

Practicing loops, conditions, and file paths

Creating real tools for your portfolio

Showing your ability to automate workflows

Great addition for GitHub and resumes.

📝 Example Extensions
| Category  | Extensions              |
| --------- | ----------------------- |
| Images    | .png, .jpg, .jpeg, .gif |
| Documents | .pdf, .docx, .txt, .csv |
| Code      | .py, .js, .html, .css   |
| Videos    | .mp4, .mov, .avi        |
| Audio     | .mp3, .wav              |
| Others    | Anything not listed     |

Future Improvements

You can upgrade this project later by adding:

Logging system

GUI version

Config file for custom rules

Duplicate file detector

File preview

Sorting by file size or date

📜 License

This project is open-source and available under the MIT License.