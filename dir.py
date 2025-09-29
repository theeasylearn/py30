import random
num1=random.randint(1,10)
print(num1)

seq=['r',4,'g',5,'t']
print(random.choice(seq))

random.shuffle(seq)
print(seq)

ret=random.sample(seq, 3)
print(ret)

num=random.uniform(10,99)
print(num)

#randrange(start, stop, step)
num=random.randrange(0,100,5)
print(num)