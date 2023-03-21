import os
import shutil
# Get the path of the current working directory (where python is operating)
print(os.getcwd())
# Get the path of the current file
print(os.path.realpath(__file__))
print(os.listdir())

# Create a file and move it in the current script directory
with open('./my_text_file.txt', 'w+') as my_file:
    my_file.write('This is a test text')
    shutil.move(f'{os.getcwd()}/my_text_file.txt', os.path.dirname(os.path.realpath(__file__)))


# Get a list of folders, sub folders and files within a path
for folder, sub_folders, file in os.walk(f'{os.getcwd()}/python-course/modules'):
    print(f'Current folder: {folder}') 
    for sub_folder in sub_folders:
        print(f'\tCurrent sub folder: {sub_folder}')
    print(f'\tCurrent files: {file}')