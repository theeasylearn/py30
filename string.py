str='Hello I Am Student'

str1=str.upper()
print(str1)
#o/p:HELLO I AM STUDENT

print(str)
#o/p:Hello I Am Student

print(str.lower())
#o/p:hello i am student

str2='atdjg4756gfjnf'
print(str2.isalnum())
#o/p:True
#in case of space it will return False.

str3="python"
print(str3.isalpha())
#o/p:True
#in case of space it will return False.

print(str3.islower())
#True
#in case of space it will return False.

str4='34567'
print(str4.isnumeric())
#o/p:True

str5='  '
print(str5.isspace())
#o/p:True

print(str.istitle())
#o/p:True

print(str1.isupper())
#o/p:True

print(len(str))
#o/p:18

lit=['mango','orange','banana']
str="-"

print(str.join(lit))
#o/p:mango-orange-banana

line = "India is a country where India’s diversity, India’s culture, India’s history, and India’s unity are celebrated."
print(line.replace('India','Bharat'))
#o/p:Bharat is a country where Bharat’s diversity, Bharat’s culture, Bharat’s history, and Bharat’s unity are celebrated.

print(line.replace('India','Bharat',2))
#o/p:Bharat is a country where Bharat’s diversity, India’s culture, India’s history, and India’s unity are celebrated.

strToSplit="mango,banana,apple,watermelon"

lit3=strToSplit.split()
print(lit3)
#o/p:['mango,banana,apple,watermelon']

lit4=strToSplit.split(',')
print(lit4)
#o/p:['mango', 'banana', 'apple', 'watermelon']

lit5=strToSplit.split(',',2)
print(lit5)
#o/p:['mango', 'banana', 'apple,watermelon']
