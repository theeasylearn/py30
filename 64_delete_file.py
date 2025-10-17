'''
here you have include all types of exception handling mechanism 
like file does not exists 
file is in use by other application
file is directory
'''
import os 
current_file_name = input("Enter existing file name to remove")

os.remove(current_file_name)
print("file has been deleted successfully")

