#example of how to read data from text file

filename = input("Enter file name to read(display)")
mode = "r"
try:
    #this will open file in read mode 
    file = open(filename,mode)
    content = file.read() #read whole file and store it's data into content variable
    print(content)
    file.close()
except FileNotFoundError:
    print(filename , "does not exists")
except PermissionError:
    print(filename, "is not file, it is folder")
else:
    print("file has been read successfully")