# File Organizer - Certura Internship Task 2
# Author: Muzamal Asghar
# Date: August 14, 2025
# Objective: Organize files by type.
# Usage: Input directory, auto-moves files.
# Details: os for ops, shutil for moves, customizable dict.

import os
import shutil

FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
    'Others': []
}

def create_subfolders(directory):
    """
    Create subfolders if missing.
    """
    for folder in FILE_TYPES.keys():
        os.makedirs(os.path.join(directory, folder), exist_ok=True)

def organize_files(directory):
    """
    Move files by extension.
    """
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            moved = False
            for folder, extensions in FILE_TYPES.items():
                if ext in extensions:
                    shutil.move(file_path, os.path.join(directory, folder, filename))
                    print(f"Moved {filename} to {folder}")
                    moved = True
                    break
            if not moved:
                shutil.move(file_path, os.path.join(directory, 'Others', filename))
                print(f"Moved {filename} to Others")

if __name__ == "__main__":
    print("Welcome to File Organizer! 🗂️")
    while True:
        directory = input("Enter full path to organize: ")
        if os.path.isdir(directory):
            break
        print("Invalid directory.")
    create_subfolders(directory)
    organize_files(directory)
    print("\nFiles organized! 🚀")