l1 =[132564,16.262,'the','easy',True,"learn",'we','are',123,'learning']
l2 =['batch','python',30]
print('l1',l1)
l1.append('python') # append()  Add an element to the end of the list    
print('l1.append',l1)
l1.extend(l2) # extend(list)  Add  set of values(list) at the end of list. 
print('l1.extend',l1)
l1.insert(5, 'academy') # insert(position,item)  Insert an item at the defined position   
print('l1.insert',l1) 
l1.remove(True) # remove(item)  Removes given item from the list  
print('l1.remove',l1)  
l1.pop(8) # pop(position)  Removes and returns an element at the given position 
print('l1.pop',l1)
l2.clear() # clear()  Removes all items from the list    
print(l2)
print(l1)
print(l1.index('python')) # index()  Returns the index of the first matched item   print(l1) 
print(l1.count('learn'))# count(item)  Returns the count of the number of items passed as an argument  print(l1)  
l2=[123,456,789,963,12,56,852,741,41.2,85.6] # sort()  Sort items in a list in ascending order if all items are of same type   
l2.sort()
print("l2.sort()",l2) 
l2.reverse() # reverse()  Reverse the order of items in the list    
print(l2)
l1.reverse()
print(l1)
l3 = l2.copy()
# copy()  Returns a shallow copy of the list 
print(l3)
l4 =[]
l4.extend(['batch','python',30])
print(l4)
del l3[3]
print(l3)
del l3
# print(l3)

