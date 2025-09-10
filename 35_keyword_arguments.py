# write a program to create function getMerit that has 5 input maths, science, english, gujarati, hindi. this function will display total of all subject, average and return math and science which will decide merit of student as per blow criteria 
#  if total above 180 student can take B Group
#  if total above 160 student can take A Group
#  if total above 140 student can take admission in diploma
#  if total above 120 student can take admission in Bsc
#  if total below 120 student can take admission else
def getMerit(maths,science,english,gujarati,hindi):
    grandTotal = maths + science + english + gujarati + hindi
    average = grandTotal / 5 
    meritTotal = maths + science
    print("All subject total ",grandTotal) 
    print("All subject average ",average) 
    print(f"maths {maths}, science {science}, english {english}, gujarati {gujarati}, hindi {hindi}")
    return meritTotal

# take integer marks with prompt messages
m    = int(input("Enter Maths marks: "))
c  = int(input("Enter Science marks: "))
e  = int(input("Enter English marks: "))
g = int(input("Enter Gujarati marks: "))
h    = int(input("Enter Hindi marks: "))
merit = getMerit(gujarati=g,hindi=h,english=e,maths=m,science=c)
print(merit)



