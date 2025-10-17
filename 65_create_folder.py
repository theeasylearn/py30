import os 
# create for each and every item in list 
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'papaya', 'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'watermelon']

#change current working directory
os.chdir('fruits')
print(os.getcwd())
for item in fruits:
    os.mkdir(item)
    print(f"{item} folder created...")

print('thank you')
