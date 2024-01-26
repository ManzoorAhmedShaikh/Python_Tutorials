#TUPLE Data Structure

"""
Syntax:
tuple = (1,2,3,4)
"""
l = [2,3,4]
t = (2,5,6,5)
print(type(l))
print(type(t))

print(l[2])
print(t[2])

print(t.count(11))
print(t.index(5))

l.append('sd')
l[1] = 'G'
print(l)
t[1] = "G"
print(t)