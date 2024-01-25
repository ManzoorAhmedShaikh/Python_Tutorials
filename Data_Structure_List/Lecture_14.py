#LIST Data Structure

"""
List
Tuple
Set
Dictionary
"""

# a = 's'
# b = 2
#
# c = [2,'s',False,2,True]

l = [1,2,3,4]
print(l)
print(type(l))

'''
1)  insert()
2)  append()
'''
l.append(22)
print(l)
l.insert(0,11)
print(l)

print(l[1])

'''
3)  remove()
4)  pop()
'''
print(l)
l.remove(4)
print(l)
l.pop()
print(l)

'''
5)  clear()
6)  count()
7)  index()
'''
l.append(2)
print(l)
print(l.count(55))
print(l.index(11))
del l[0]
print(l)
l.clear()
print(l)

