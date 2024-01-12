#Special Operators

"""
is
is not
in
not in
"""

"""
Syntax
Expression1 <Special Opreator> Expression2
"""

#IS
a = 2 #IMMUTABLE
b = 2
c = a

print(a is b)
print(a == b)
print(a is not c)
print(b is c)
print(id(a))
print(id(b))

#IN
# We went for swim in the lake

a = "My name is Manzoor Ahmed"
print("Manzoor" in a)
print("manzoor" not in a)