#example of how to read data from text file

filename = "geet.txt"
mode = "r"
#this will open file in read mode 
file = open(filename,mode)
for line in file:
    print(line.strip())
