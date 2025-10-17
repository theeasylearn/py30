# handle all exception using exceptional handling mechnism 
import os 
# delete for each and every directory in list 
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'papaya', 'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'watermelon']

#change current working directory
os.chdir('fruits')
print(os.getcwd())
for item in fruits:
    os.rmdir(item)
    print(f"{item} folder deleted...")

print('thank you')
