#example of how to write data into file
import errno
try:
    filename = input("Enter file name to write data")
    mode = "a" #append mode (write new data at the end of file) 
    #if file does not exist, new file will be created, otherwise existing data will be kept and new data will be stored at the end of file
    file = open(filename,mode)
    while True:
        friend = input("Enter your friend name (type exit to stop)")
        if friend == 'exit':
            break  #loop stop 
        else:
            #write friend name into file 
            file.write("\n" + friend)

    file.close()
    print("file has been saved...")
except PermissionError as e:
    print(f"PermissionError: Access denied to '{filename}'. It may be locked by another program or you lack permissions. or it is directory")