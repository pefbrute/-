#!/usr/bin/env python3
import os
import sys
import re
import shutil

def get_highest_number(path):
    max_number = 0
    for folder in os.listdir(path):
        if os.path.isdir(os.path.join(path, folder)):
            match = re.match(r'^(\d+). ', folder)
            if match:
                max_number = max(max_number, int(match.group(1)))
    return max_number

def rename_folder(selected_folder, new_number):
    parent_dir = os.path.dirname(selected_folder)
    folder_name = os.path.basename(selected_folder)
    new_folder_name = f"{new_number}. {folder_name}"
    new_folder_path = os.path.join(parent_dir, new_folder_name)
    os.rename(selected_folder, new_folder_path)
    return new_folder_path

def move_folder(source_folder, destination_folder):
    shutil.move(source_folder, destination_folder)

if __name__ == "__main__":
    base_path = "/home/pefbrute/Pictures/Картинки на Продажу/Редбабл, ТиПаблик (Копирайт, Мемы и ИИ Арт)"
    selected_folder = sys.argv[1]  # The folder selected in Nautilus

    highest_number = get_highest_number(base_path)
    new_folder_path = rename_folder(selected_folder, highest_number + 1)
    move_folder(new_folder_path, base_path)
