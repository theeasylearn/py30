'''
here you have include all types of exception handling mechanism 
like file does not exists 
     new file name already exists
     file is in use by other application
     file is directory
'''
import os 
current_file_name = input("Enter existing file name to rename")
new_file_name = input("Enter new file name to rename")

os.rename(current_file_name,new_file_name)
print("file has been renamed successfully")
