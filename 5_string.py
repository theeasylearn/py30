s1 = "we are learning python batch code is 30 our fees is 7500.0 course is started True"
s2 = "we are learning python batch code is 30 our fees is 7500."
print("all",s1)
print(len(s1))
print("s1[10]",s1[10])  # r
print("s1[600]",s1[80])
print("s1[0:]",s1[0:]) # s1[start :end:step]
print("s1[0:6]",s1[0:6])
print("s1[::2]",s1[::2])
print("s1[::2]",s1[::3])
print("s1[::2]",s1[5:40:4])
print("s1+s2",(s1+s2))
print("s1*3",s1*3)
s1[0:6] ="i am" # get error because string is immutable
print("s1",s1)