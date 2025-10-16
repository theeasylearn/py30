#example of how to read data from text file

filename = input("Enter file name to read(display)")
mode = "r"
try:
    #this will open file in read mode 
    file = open(filename,mode)
    for line in file:
        print(line.strip())
    file.close()
except FileNotFoundError:
    print(filename , "does not exists")
except PermissionError:
    print(filename, "is not file, it is folder")
else:
    print("file has been read successfully")