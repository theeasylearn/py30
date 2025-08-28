#concept of is and not is 
box1 = 10
box2 = 50
box3 = 10

result = box1 is box2
print("result of is =",result,id(box1),id(box2),id(box3))

result = box1 is not box2
print("result of is not =",result,id(box1),id(box2),id(box3))