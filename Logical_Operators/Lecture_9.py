#Logical Operators

#Operators
"""
and
or
not
"""

#Syntax
"""
and     |       (Boolean Expression1) and (Boolean Expression2)
or      |       (Boolean Expression1) or (Boolean Expression2)
not     |       not(Boolean Expression1)
"""

#Boolean Expression1
# a = 2 > 3
# print(a)

#Boolean Expression2
# a = True
# print(a)

#Practice
a = True
b = False
c = True

#and | or
print(a and b) #Both side should be TRUE
print(a or b)  #Any one side should be TRUE
print(b or b)
print(a and c)

#not
print(not(c)) #It simply reverse the boolean
print(not(b))

print(a and b and c or a)
print(not(not(b)))