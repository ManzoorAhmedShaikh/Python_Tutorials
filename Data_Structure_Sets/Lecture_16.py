#SETS Data Structure

'''
Syntax:
s = {a,g,c,d}
'''

s = {2,4,"Gd",False,'%',77,"Gd"}

# print(s)
# print(s[2])

'''
1) add
2) remove
3) discard
4) pop
5) clear
'''
# print(s)
# s.add("Manzoor Ahmed")
# print(s)
# s.remove("Gd")
# print(s)
# s.discard('Gds')
# print(s)
# s.pop()
# print(s)
# s.clear()
# print(s)

'''
6) union
7) intersection
8) difference
'''
s1 = {2,3,'G','s',True,'5',5}
s2 = {2,3,'G',55,"LLS"}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s2.difference(s1))