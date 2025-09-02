# example to use for loop on string
# write a program to count vowels(a,e,i,o,u) in string
line = input("Enter one line(multiple words)")
#line = the easylearn academy
vowels = 0
for letter in line: #t
    if letter == 'a' or letter == 'e' or letter =='i' or letter == 'o' or letter == 'u':
        vowels=vowels + 1
print(vowels)
