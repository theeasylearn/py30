#add all types of exception handling mechnism
import os 
import shutil
file_name = input("Enter file name to copy")
copyfile_name = input("Enter another file name to copy data")
if not os.path.exists(file_name):
    print(f"{file_name} does not exists")
elif os.path.exists(copyfile_name):
    print(f"{copyfile_name} already exists")
else:
    shutil.copyfile(file_name,copyfile_name)
    print("file has been copied successfully")