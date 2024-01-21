#Basic IF-ELSE

'''
--------There are 3 modes of Operations--------
1) Sequential (Completed)
2) Conditional (Current)
3) Repetitive (Discuss Later on)
-----------------------------------------------
'''

'''
Syntax:

if Condition1:
    Block of code
else:
    2nd Block of Code
'''

# if 2 < 3:
#     print("Fine")
# else:
#     print("sd")
#
# if 2 < 3 and 2 != 3:
#     print("S")
# else:
#     print("G")

'''
Q1) Write a program to ask a user for his name, if the name length is
greater than 10, print 'FINE' otherwise 'TRY AGAIN'
'''

name = input("Enter the user name: ")

if len(name) > 10:
    print("FINE")
else:
    print("TRY AGAIN")