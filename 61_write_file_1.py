#example of how to write data into file
import errno
try:
    filename = input("Enter file name to write data")
    mode = "w"
    #if file does not exist, new file will be created, else existing data will be deleted and new data will be stored
    file = open(filename,mode)
    while True:
        friend = input("Enter your friend name (type exit to stop)")
        if friend == 'exit':
            break  #loop stop 
        else:
            #write friend name into file 
            file.write(friend + "\n")

    file.close()
    print("file has been saved...")
except PermissionError as e:
    print(f"PermissionError: Access denied to '{filename}'. It may be locked by another program or you lack permissions. or it is directory")