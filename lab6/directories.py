import os

def list_directories(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    return directories

def list_files(path):
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return files

def list_all_contents(path):
    all_contents = os.listdir(path)
    return all_contents

specified_path = input("Enter the path: ")

print("Directories:")
print(list_directories(specified_path))

print("\nFiles:")
print(list_files(specified_path))

print("\nAll Directories and Files:")
print(list_all_contents(specified_path)))

# ex2
import os

def check_access(path):
    access = {
        "Existence": os.path.exists(path),
        "Readability": os.access(path, os.R_OK),
        "Writability": os.access(path, os.W_OK),
        "Executability": os.access(path, os.X_OK)
    }
    return access


specified_path = input("Enter the path: ")

access_info = check_access(specified_path)

print("Access information for path:", specified_path)
for key, value in access_info.items():
    print(f"{key}: {'Yes' if value else 'No'}");


# ex3

import os

def analyze_path(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        return True, filename, directory
    else:
        return False, None, None


specified_path = input("Enter the path: ")

exists, filename, directory = analyze_path(specified_path)

if exists:
    print("Path exists.")
    print("Filename:", filename)
    print("Directory:", directory)
else:
    print("Path does not exist.");


#ex4

def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        print("File not found.")
        return None

file_path = input("Enter the path to the text file: ")

num_lines = count_lines(file_path)

if num_lines is not None:
    print("Number of lines in the file:", num_lines);


#ex5

def write_list_to_file(file_path, data_list):
    try:
        with open(file_path, 'w') as file:
            for item in data_list:
                file.write(str(item) + '\n')
        print("List successfully written to the file.")
    except IOError:
        print("An error occurred while writing to the file.")


file_path = input("Enter the path for the file: ")
data_list = input("Enter the list elements separated by spaces: ").split()

write_list_to_file(file_path, data_list);

# ex6
import string

def generate_files():
    
    file_names = [f"{char}.txt" for char in string.ascii_uppercase]
    
    
    for file_name in file_names:
        with open(file_name, 'w') as file:
            pass
        print(f"Created file: {file_name}")


generate_files()



# ex7

def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                destination.write(source.read())
        print("File contents copied successfully.")
    except FileNotFoundError:
        print("One of the files does not exist.")
    except IOError:
        print("An error occurred while copying the file contents.")


source_file = input("Enter the source file path: ")
destination_file = input("Enter the destination file path: ")

copy_file(source_file, destination_file);


#ex8

import os

def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            try:
                os.remove(file_path)
                print("File deleted successfully.")
            except OSError as e:
                print(f"Error: {e.strerror}")
        else:
            print("No write access to the file.")
    else:
        print("File does not exist.")


specified_path = input("Enter the path of the file to delete: ")

delete_file(specified_path)




