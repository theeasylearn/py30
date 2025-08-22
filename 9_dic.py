d1 = {
    'name':'D patel',
    'age':26,
    'subject':'python'
}
print(d1)
d1['add']='python'
print(d1)
d1['add']='py'  #modify/update value for key add
d1['ch'] =(1,2,3)
d1['ch_name']=['intro','loop','function']
print("d1",d1)
d2 = {}
d2['name'] = 'abc'
d2['age'] = 22
d2['subject'] = 'django'
print("d2",d2)

del d1['add']  # add delete with value
print("d1",d1)

del d2  # delete dic
print(d2)  # get error of name error because d2 is deleted