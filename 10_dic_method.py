d1= {'name': 'D patel', 'age': 26, 'subject': 'python', 'ch': (1, 2, 3), 'ch_name': ['intro', 'loop', 'function']}
d2= {'name': 'abc', 'age': 22, 'subject': 'django'}

d2.clear() # clear() Removes all items from the dictionary.
print(d2)
d2=d1.copy() # copy() Returns a shallow copy of the dictionary.
print("d2 copy of d1",d2)
print("d1.get('ch')",d1.get('ch',0)) # get(key[,d]) Returns the value of the key. If the key does not exist, returns d (defaults to None).
print('d1.get("add")',d1.get('add','did not exist'))

print(d1.items()) # items() Return a new object of the dictionary's items in (key, value) format.
print(d1.keys()) # keys() Returns a new object of the dictionary's keys.
print(d1.values()) # Values() The values() method returns a view object that displays a list of all the values in the dictionary.
print(d1.fromkeys('subject',[230063,'gvh'])) # fromkeys(seq[, v]) Returns a new dictionary with keys from seq and value equal to v (defaults to None).
print(d2.pop('subject')) # pop(key[,d]) Removes the item with the key and returns its value or d if key is not found. If d is not provided and the key is not found, it raises KeyError.
print('d2',d2)
print(d2.popitem()) # popitem() Removes and returns last item (key, value). Raises KeyError if the dictionary is empty.
print(d2)
d2.update({'subject':'python'}) # update([other]) update() method adds element(s) to the dictionary from dictionary passed as argument if the key is not in the dictionary then key value will be added . If the key is in the dictionary, it updates the key with the new value.
print(d2)

