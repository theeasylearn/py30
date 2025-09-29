import random

print(random.random())
#o/p:0.572966537309202

print(random.uniform(10,90))
#o/p:25.075367496335666

print(random.randint(10,90))
#o/p:48

print(random.randrange(10,90,10))
#o/p:70

lit=[10,20,30,40,50,60]

print(random.choice(lit))
#o/p:60

print(random.choices(lit,k=3))
#o/p:[40, 10, 60]

print(random.shuffle(lit))
print(lit)
#o/p:None
#[30, 60, 40, 50, 20, 10]

print(random.sample(lit,2))
#o/p:[30, 60]