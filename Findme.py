import os
import sys
import random
import shutil

root_directory = os.path.expanduser("~")

def make_file():
    if len(sys.argv) > 1:
        second_command = sys.argv[1]
    else:
        print("Second command is not given, so a default file will be created")
        second_command = "default.txt"
    
    with open(second_command, "w") as f:
        f.write("This file is created with the name provided or a default name.")
    
    return second_command

def move_file(second_command, destination_directory):
    if second_command:
        shutil.move("./" + second_command, os.path.join(destination_directory, second_command))
    else:
        print("Second command is not given")

def take_random_directory(filtered_directory):
    random_directory = random.choice(filtered_directory)
    print("Stored at:" + random_directory)
    return random_directory

def list_directories(root_dir):
    directories = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # This line below I needed some help from chatgpt because I couldn't find it online, probably because I am blind 
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        for dirname in dirnames:
            directories.append(os.path.join(dirpath, dirname))
    return directories

if __name__ == "__main__":
    all_directories = list_directories(root_directory)
    filtered_directories = []
    for directory in all_directories:
        directory_name = os.path.basename(directory)
        if "node_modules" not in directory:
            filtered_directories.append(directory)
    
    random_directory = take_random_directory(filtered_directories)
    file_made = make_file()
    if file_made:
        move_file(file_made, random_directory)
    else:
        print("No valid file to move.")