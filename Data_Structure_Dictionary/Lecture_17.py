#DICTIONARY Data Structure

'''
dictionary = {key: value}
'''

d1 = {"A":2,"B":3}
print(d1)
print(type(d1))
print(d1["B"])

d2 = {2:"B",55:"C"}
print(d2)
print(d2[55])

#Methods
'''
1) values()
2) keys()
3) items()
4) pop()
5) get()
6) update()
'''
d3 = {2:'c',"A":True,"g":33}
print(d3)
print(d3.values())
print(d3.keys())
print(d3.items())
d3.pop("A")
print(d3)
print(d3.get(2))

# d3.update({"333":333,2:"c"})
d3['333'] = 333
print(d3)

#Keyword

#List
list()
#Tuple
tuple()
#Set
set()
#Dictionary
dict()

l1 = [2,3,4]
t1 = (2,4,5,6)
s1 = {2,3,5,6}
print(list(t1))
print(tuple(l1))
print(set(l1))