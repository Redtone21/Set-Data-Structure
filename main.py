# Set items are enclosed in curly brackets 
# Set is unordered
# Set is mutable, can only contain immutable items
# Set elements are unique 
#  Set can contain only immutable items  



'''
Python Set Attritubes
'''

# print(dir(set))

'''
Creating Python Sets
'''

# set = set()
# set = {1,2,3}
# print(set)

'''
Modifying a set in Python
'''

# set_example = {'hello', 'world!'}
# # set_example(0)
# set_example.add('yay')
# set_example.add(('hey'))
# set_example.update([1,2,3])

# print(help(set.add))
# print(help(set.update))
# print(set_example)

'''
Removing elements from a set
'''

#   

# set_example.discard(1)
# set_example.discard(10)
# set_example.remove(1)
# set_example.remove(10)
# set_example.pop()
# set_example.pop(1)

# print(set_example)

# print({'hello', 'world', 'hello', 'hello'})

'''
Set Union Operations
'''

# a = {1,2,3,6,7}
# b = {4,5,6,7,8,9}

# print(a | b)
# print(a.union(b))

'''
Set Intersection Operations
'''

# a = {1,2,3,6,7}
# b = {4,5,6,7,8,9}

# print(a & b)
# print(a.intersection(b))

'''
Set Difference Operations
'''

# a = {1,2,3,4,6,7,9}
# b = {2,5,6,7,8,9}

# print(a - b)
# print(a.difference(b)) 
# print(b - a)
# print(b.difference(a)) 

'''
Set Symmetric Difference
'''

a = {1,2,3,4,6,7,9}
b = {2,5,6,7,8,9}

print(a ^ b)
print(a.symmetric_difference(b))

'''
Set Methods
'''