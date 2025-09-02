# example to use for loop on string
# write a program to count words in string
line = input("Enter one line(multiple words)")
#line = the easylearn academy
word = 1
for letter in line: #t
    if letter == " ":
        word=word+1

print(word)
