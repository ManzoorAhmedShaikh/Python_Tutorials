#If Elif Else Conditional Statements

'''
if Condition1:
    Block of Code
elif Condition2:
    Block of Code
.
.
.
else:
    Block of Code
'''

#Part1 (Check one and skip others)
# a = int(input("Enter any number: "))
#
# if a > 2:
#     print("A is Greater")
#
# elif a > 0 and a <= 2:
#     print("A is Stable")
#
# elif a < 0 and a > -2:
#     print("A is negative")
#
# else:
#     print("Something is wrong")

#Part2 (Check each condition)
a = int(input("Enter any number: "))

if a > 2:
    print("A is Greater")

if a > 0 and a <= 3:
    print("A is Stable")

if a < 0 and a > -2:
    print("A is negative")
