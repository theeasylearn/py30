t1= (132564,16.262,'the','easy',True,"learn",'we','are',123,'learning')
t2 = ('batch','python',30)
print('t1',t1);print('t1',t2)
print("t1[3]",t1[3])
print("t1[start:end:step] t1[2:]",t1[2:])
print('t1[:5]',t1[:5])
print('t1[::3]',t1[::3])
print('t1+t2',t1+t2)
print('t1*4',t1*4)

#count method
print('count',t1.count(132564))

#index
print('index',t1.index(True))




# del t1[3]  # get error because tuple is inmutable
del t1
print(t1)