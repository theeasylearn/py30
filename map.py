#varName = map(lambda arg:exp, iterator)

#square of each elements in list

lit=[4,5,3,2,6]

res=map(lambda x:x*x,lit)
print(list((res)))

#o/p:[16, 25, 9, 4, 36]

lit=[4,5,3,2,6]
lit1=[1,2,3,4,5]

res1=map(lambda a,b:a+b,lit,lit1)
print(list((res1)))

#o/p:[5, 7, 6, 6, 11]